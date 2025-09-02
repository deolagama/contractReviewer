import sys, os 
from .config import MODEL_NAME, CHROMA_DB_DIR, REPORT_PATH
from .parser import parse_pdf
from .chunker import chunk_text
from .embeddings import Embedder
from .rag import RAGStore
from .extract import detect_clauses
from .report import build_report, save_report

def main(pdf_path: str):
    print(f"📄 Processing: {pdf_path}")
    pages = parse_pdf(pdf_path)
    chunks = chunk_text(pages)
    print(f"🔍 Parsed {len(chunks)} chunks")

    # Embeddings & RAG store
    embedder = Embedder(MODEL_NAME)
    vecs = embedder.encode(chunks)
    rag = RAGStore(CHROMA_DB_DIR)
    rag.add(ids=[f"chunk_{i}" for i in range(len(chunks))], texts=chunks, embeddings=vecs)

    # Detect clauses
    items = detect_clauses(chunks)
    print(f"✅ Found {len(items)} clauses")

    # Report
    report = build_report(items)
    save_report(report, REPORT_PATH)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python -m src.app <PDF_PATH>")
        sys.exit(1)
    pdf_path = sys.argv[1]
    os.makedirs("outputs", exist_ok=True)
    main(pdf_path)
