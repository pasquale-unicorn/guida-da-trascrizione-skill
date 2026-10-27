#!/usr/bin/env python3
"""Estrazione meccanica di un .pptx: testo, note relatore e immagini di ogni slide.

Uso: estrai-pptx.py <file.pptx> <cartella-uscita>

Produce in <cartella-uscita>:
  img/sNNN-K.ext       ogni immagine usata dalle slide (NNN = numero slide in ordine di presentazione)
  img/sNNN-K-web.jpg   copia ridotta (lato lungo 1600 px) delle immagini oltre 3 MB
  indice-slide.md      per slide: titolo, testo, note relatore, immagini, presenza di video
  immagini.txt         elenco delle immagini, per foglio-immagini.py

Solo libreria standard di Python + sips (macOS). Il .pptx è uno zip: non serve LibreOffice.
I video non si estraggono: si segnalano soltanto.
"""

from __future__ import annotations

import posixpath
import subprocess
import sys
import xml.etree.ElementTree as ET
import zipfile
from pathlib import Path

REL_NS = "http://schemas.openxmlformats.org/package/2006/relationships"
P = "http://schemas.openxmlformats.org/presentationml/2006/main"
A = "http://schemas.openxmlformats.org/drawingml/2006/main"
R = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
LIMITE_WEB = 3 * 1024 * 1024
ESTENSIONI_VIDEO = (".mov", ".mp4", ".avi", ".m4v", ".wmv")


def rels_path(part: str) -> str:
    folder, filename = posixpath.split(part)
    return posixpath.join(folder, "_rels", filename + ".rels")


def relationships(z: zipfile.ZipFile, part: str) -> list[dict[str, str]]:
    path = rels_path(part)
    if path not in z.namelist():
        return []
    root = ET.fromstring(z.read(path))
    return [dict(el.attrib) for el in root.findall(f"{{{REL_NS}}}Relationship")]


def target(part: str, relation: dict[str, str]) -> str:
    if relation.get("TargetMode") == "External":
        return relation["Target"]
    return posixpath.normpath(posixpath.join(posixpath.dirname(part), relation["Target"].lstrip("/")))


def paragraphs(node: ET.Element) -> list[str]:
    return ["".join((t.text or "") for t in para.iter(f"{{{A}}}t"))
            for para in node.iter(f"{{{A}}}p")]


def slide_title(root: ET.Element, text: list[str]) -> str:
    for shape in root.iter(f"{{{P}}}sp"):
        ph = shape.find(f"./{{{P}}}nvSpPr/{{{P}}}nvPr/{{{P}}}ph")
        if ph is not None and ph.get("type") in ("title", "ctrTitle"):
            name = " ".join(x for x in paragraphs(shape) if x.strip()).strip()
            if name:
                return name
    return next((x.strip() for x in text if x.strip()), "(senza titolo)")


def notes_text(z: zipfile.ZipFile, part: str) -> list[str]:
    root = ET.fromstring(z.read(part))
    result = []
    for shape in root.iter(f"{{{P}}}sp"):
        ph = shape.find(f"./{{{P}}}nvSpPr/{{{P}}}nvPr/{{{P}}}ph")
        if ph is not None and ph.get("type") == "body":
            result.extend(paragraphs(shape))
    return result


def clean(s: str) -> str:
    return s.replace("\r", " ").replace("\n", " ").strip()


def copia_immagine(z: zipfile.ZipFile, source_part: str, destinazione: Path) -> int:
    info = z.getinfo(source_part)
    with z.open(info) as incoming, destinazione.open("wb") as outgoing:
        while chunk := incoming.read(1024 * 1024):
            outgoing.write(chunk)
    return info.file_size


def versione_web(path: Path) -> None:
    web = path.with_name(path.stem + "-web.jpg")
    subprocess.run(["sips", "-s", "format", "jpeg", "-s", "formatOptions", "85",
                    "--resampleHeightWidthMax", "1600", str(path), "--out", str(web)],
                   check=True, stdout=subprocess.DEVNULL)


def estrai(sorgente: Path, uscita: Path) -> None:
    img = uscita / "img"
    img.mkdir(parents=True, exist_ok=True)
    entries, image_names = [], []
    with zipfile.ZipFile(sorgente) as z:
        presentation = "ppt/presentation.xml"
        root = ET.fromstring(z.read(presentation))
        presentation_rels = {x["Id"]: x for x in relationships(z, presentation)}
        ids = root.find(f"{{{P}}}sldIdLst")
        if ids is None:
            sys.exit("presentation.xml senza elenco slide: file .pptx non valido?")
        slide_parts = [target(presentation, presentation_rels[x.attrib[f"{{{R}}}id"]])
                       for x in ids.findall(f"{{{P}}}sldId")]

        for number, slide_part in enumerate(slide_parts, 1):
            slide_root = ET.fromstring(z.read(slide_part))
            text = paragraphs(slide_root)
            rels = relationships(z, slide_part)
            images = [x for x in rels if x["Type"].endswith("/image")]
            note_rels = [x for x in rels if x["Type"].endswith("/notesSlide")]
            has_video = any("video" in x["Type"].lower()
                            or target(slide_part, x).lower().endswith(ESTENSIONI_VIDEO) for x in rels)
            names = []
            for k, relation in enumerate(images, 1):
                if relation.get("TargetMode") == "External":
                    continue
                source_part = target(slide_part, relation)
                filename = f"s{number:03d}-{k}{Path(source_part).suffix.lower()}"
                if copia_immagine(z, source_part, img / filename) > LIMITE_WEB:
                    versione_web(img / filename)
                names.append(filename)
            image_names.extend(names)
            notes = []
            for relation in note_rels:
                notes.extend(notes_text(z, target(slide_part, relation)))
            entries.append((number, slide_title(slide_root, text), text, notes, names, has_video))

    lines = [f"# Indice delle slide — {sorgente.name}", "",
             "Ordine da `ppt/presentation.xml`; testo e note estratti dagli XML senza interpretazione.", "",
             f"Slide: {len(entries)} · Immagini referenziate ed estratte: {len(image_names)}", ""]
    for number, title, body, notes, images, has_video in entries:
        lines += [f"## Slide {number:03d} — {clean(title)}", "", "### Testo", ""]
        lines += [f"- {clean(line)}" for line in body if clean(line)] or ["(nessun testo)"]
        lines += ["", "### Note relatore", ""]
        lines += [f"- {clean(line)}" for line in notes if clean(line)] or ["(nessuna nota)"]
        lines += ["", "### Immagini", ""]
        lines += [f"- `img/{name}`" for name in images] or ["(nessuna immagine)"]
        lines += ["", f"Video: {'sì' if has_video else 'no'}", ""]
    (uscita / "indice-slide.md").write_text("\n".join(lines), encoding="utf-8")
    (uscita / "immagini.txt").write_text("\n".join(image_names) + "\n", encoding="utf-8")
    print(f"{len(entries)} slide, {len(image_names)} immagini estratte, "
          f"{sum(x[5] for x in entries)} slide con video (non estratti)")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    sorgente_pptx = Path(sys.argv[1])
    if not sorgente_pptx.is_file():
        sys.exit(f"file non trovato: {sorgente_pptx}")
    estrai(sorgente_pptx, Path(sys.argv[2]))
