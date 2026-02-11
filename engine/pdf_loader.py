from pathlib import Path

BOOKS_DIR = Path("books")

def list_pdfs():
    """Return a list of PDF filenames in the books/ folder."""
    if not BOOKS_DIR.exists():
        return []
    return sorted([f.name for f in BOOKS_DIR.glob("*.pdf")])

def load_pdf_bytes(filename: str) -> bytes:
    """Load a PDF file from books/ as raw bytes."""
    path = BOOKS_DIR / filename
    if not path.exists():
        raise FileNotFoundError(f"PDF not found: {filename}")
    return path.read_bytes()