from pathlib import Path
from llama_index.core import SimpleDirectoryReader

def main() -> None:
    source_dir = Path(__file__).parent / "app" / "data" / "source_docs"
    print(f"Looking for documents in: {source_dir}")

    if not source_dir.exists():
        print("source_docs folder does not exist.")
        return

    docs = SimpleDirectoryReader(str(source_dir)).load_data()
    print(f"Loaded {len(docs)} document(s).")

    for i, doc in enumerate(docs, start=1):
        # Print the first 100 characters so we know it worked
        snippet = doc.text[:100].replace("\n", " ")
        print(f"[{i}] {snippet}...")

if __name__ == "__main__":
    main()
