# src/chunker.py
from typing import List

def chunk_text(pages: List[str], chunk_size: int = 300) -> List[str]:
    """Split text into overlapping chunks."""
    chunks = []
    for page in pages:
        words = page.split()
        for i in range(0, len(words), chunk_size):
            chunk = " ".join(words[i:i+chunk_size])
            chunks.append(chunk)
    return chunks
