from app.rag_query import get_query_engine


def answer_question(query: str) -> str:
    """
    Answer a question using the persisted LlamaIndex index.
    """
    query_engine = get_query_engine()
    response = query_engine.query(query)
    # Add a clear marker so we KNOW this code path is active
    return f"[RAG INDEX ACTIVE] {str(response)}"
