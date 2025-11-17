# RAG Service Backend

FastAPI + LlamaIndex backend running in WSL2 (Ubuntu) with a persisted vector index.

## Requirements

- Windows 11 with WSL2 (Ubuntu)
- Conda environment: `ai_env`
- Python 3.11
- OpenAI API key in a local `.env` file (NOT committed)

## How to run

```bash
conda activate ai_env
cd /mnt/c/dev/ai_projects/rag_notebook
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
