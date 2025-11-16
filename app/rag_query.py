from pathlib import Path

from dotenv import load_dotenv
from llama_index.core import StorageContext, load_index_from_storage


def get_query_engine():
    # Load environment variables (OPENAI_API_KEY)
    load_dotenv()

    base_dir = Path(__file__).resolve().parent.parent
    storage_dir = base_dir / "storage" / "index"

    storage_context = StorageContext.from_defaults(persist_dir=str(storage_dir))
    index = load_index_from_storage(storage_context)

    return index.as_query_engine()
