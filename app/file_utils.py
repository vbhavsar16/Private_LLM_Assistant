# app/file_utils.py
import fitz  # PyMuPDF
from docx import Document
import os
from fastapi import UploadFile

async def process_document(file: UploadFile):
    ext = os.path.splitext(file.filename)[1].lower()
    path = f"/tmp/{file.filename}"

    contents = await file.read()
    with open(path, "wb") as f:
        f.write(contents)

    if ext == ".pdf":
        return extract_text_from_pdf(path)
    elif ext == ".docx":
        return extract_text_from_docx(path)
    elif ext == ".txt":
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    else:
        return "Unsupported file type."

def extract_text_from_pdf(path):
    doc = fitz.open(path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def extract_text_from_docx(path):
    doc = Document(path)
    return "\n".join([p.text for p in doc.paragraphs])