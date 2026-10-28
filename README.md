# Agtech_backend

FastAPI backend for the AgTech farmer + buyer app.

## Run locally
```
python -m venv venv
venv\Scripts\activate          # Windows (Mac/Linux: source venv/bin/activate)
pip install -r requirements.txt
copy .env.example .env         # Mac/Linux: cp .env.example .env, then edit .env
uvicorn app.main:app --reload --port 5000
```
Open http://localhost:5000/docs for the interactive API docs.
