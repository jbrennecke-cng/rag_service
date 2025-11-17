#!/bin/bash

# Initialize conda for non-interactive shells
source /home/joelb/miniconda3/etc/profile.d/conda.sh

conda activate ai_env
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

