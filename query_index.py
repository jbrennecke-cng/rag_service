from pathlib import Path

from dotenv import load_dotenv
from llama_index.core import StorageContext, load_index_from_storage


def main() -> None:
    # Load OPENAI_API_KEY from .env
    load_dotenv()

    base_dir = Path(__file__).parent
    storage_dir = base_dir / "storage" / "index"

    print(f"Loading index from: {storage_dir}")

    storage_context = StorageContext.from_defaults(persist_dir=str(storage_dir))
    index = load_index_from_storage(storage_context)

    query_engine = index.as_query_engine()
    response = query_engine.query("What is inside my documents?")
    print("Response:")
    print(response)


if __name__ == "__main__":
    main()
