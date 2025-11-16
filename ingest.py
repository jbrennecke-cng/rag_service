from pathlib import Path

from dotenv import load_dotenv
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex


def main() -> None:
    # Load environment variables from .env (including OPENAI_API_KEY)
    load_dotenv()

    base_dir = Path(__file__).parent
    source_dir = base_dir / "app" / "data" / "source_docs"
    storage_dir = base_dir / "storage" / "index"

    print(f"Loading documents from: {source_dir}")
    print(f"Index will be stored in: {storage_dir}")

    # Make sure the storage directory exists
    storage_dir.mkdir(parents=True, exist_ok=True)

    # Load documents
    docs = SimpleDirectoryReader(str(source_dir)).load_data()
    print(f"Loaded {len(docs)} document(s).")

    # Build index in memory (uses OPENAI_API_KEY via env)
    index = VectorStoreIndex.from_documents(docs)

    # Persist index to disk
    index.storage_context.persist(persist_dir=str(storage_dir))

    print("Index build + persist complete.")


if __name__ == "__main__":
    main()
