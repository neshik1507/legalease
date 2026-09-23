# Phase 5 — Project Development

## 5.1 Development Sequence

### Step 1 — Create environment

```bash
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

### Step 2 — Configure environment

Create `.env`:

```env
GEMINI_API_KEY=your_api_key_here
BACKEND_URL=http://127.0.0.1:8000
```

Never commit the real key.

### Step 3 — Start FastAPI

```bash
uvicorn backend.main:app --reload
```

API:

```text
http://127.0.0.1:8000
```

### Step 4 — Start Streamlit

Open another terminal:

```bash
streamlit run frontend/app.py
```

### Step 5 — Test health

Open:

```text
http://127.0.0.1:8000/health
```

Expected:

```json
{"status":"ok"}
```

## 5.2 Development Rules

- Keep API schemas in `backend/schemas.py`.
- Keep routes thin.
- Keep Gemini-specific code in `backend/ai_core/`.
- Keep document formatting in exporter modules.
- Do not place API keys in source code.
- Validate all external input.
- Log useful errors without exposing secrets.

## 5.3 Suggested Module Responsibilities

```text
backend/
├── main.py              # FastAPI app
├── routes.py            # API endpoints
├── schemas.py           # Request/response validation
└── ai_core/
    └── gemini_generator.py

frontend/
├── app.py               # Streamlit UI
└── exporters.py         # TXT/DOCX/PDF generation
```
