from pathlib import Path

def load_retriever():
    source_path = Path(__file__).parent / "data" / "source_docs"
    files = list(source_path.glob("*.txt"))
    return [str(f.name) for f in files]