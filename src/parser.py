# src/parser.py
import fitz  # PyMuPDF
from typing import List

def parse_pdf(path: str) -> List[str]:
    """Extract text from each page of a PDF."""
    doc = fitz.open(path)
    pages = []
    for page in doc:
        text = page.get_text()
        if text.strip():
            pages.append(text.strip())
    return pages
