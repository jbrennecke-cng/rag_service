# RAG Service Backend

This project is a FastAPI + LlamaIndex RAG backend running inside WSL2 (Ubuntu).
It uses a persisted vector index, a Conda environment, and supports running from WSL, VS Code, or Windows directly.

##Project Structure
rag_notebook/
- app/
- - main.py (FastAPI entrypoint)
- - rag_engine.py (RAG engine)
- - rag_query.py (Query engine wrapper)
- - retriever.py (Document retrieval logic)
- - data/source_docs/ (RAG source documents)
- storage/index/ (Persisted LlamaIndex index)
- notebooks/ (Jupyter notebooks)
- run.sh (WSL helper script)
- run_backend.bat (Windows helper script)
- README.md (this file)



##Requirements
- Windows 11
- WSL2 (Ubuntu)
- Miniconda installed inside Ubuntu
- Conda environment named: ai_env
- Python 3.11
- A local .env file (not committed) containing your OpenAI API key:


OPENAI_API_KEY=your_key_here

##Install Dependencies
Inside Ubuntu:
conda activate ai_env
 cd /mnt/c/dev/ai_projects/rag_notebook
 pip install -r requirements.txt

##Run the Backend (WSL Terminal)
Option 1 — Manual run:
conda activate ai_env
 cd /mnt/c/dev/ai_projects/rag_notebook
 uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
Option 2 — Use the WSL helper script:
cd /mnt/c/dev/ai_projects/rag_notebook
 ./run.sh

##Run the Backend (Windows)
Double-click this file:
C:\dev\ai_projects\rag_notebook\run_backend.bat
This launches FastAPI inside WSL automatically.

##Test Endpoints
Health check:
 http://localhost:8000/health
RAG query:
 http://localhost:8000/ask?q=hello

##Run in VS Code Debugger
1. Open the rag_notebook folder in VS Code (using WSL).
2. Go to “Run & Debug” in the sidebar.
3. Choose the configuration named:
FastAPI (uvicorn)
This will launch the backend with auto-reload and debugging support.

##Notes
- .env is intentionally excluded from Git via .gitignore.
- Never commit secrets.
- Repository history is clean with no credential leaks.