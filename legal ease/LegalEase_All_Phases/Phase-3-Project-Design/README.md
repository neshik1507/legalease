# Phase 3 — Project Design

## 3.1 High-Level Architecture

```text
┌───────────────────────────────┐
│        Streamlit UI           │
│ Form / Preview / Downloads    │
└───────────────┬───────────────┘
                │ HTTP
                ▼
┌───────────────────────────────┐
│          FastAPI              │
│ Routes / Validation / Errors  │
└───────────────┬───────────────┘
                │
                ▼
┌───────────────────────────────┐
│       AI Core / Gemini        │
│ Prompt construction + model   │
└───────────────┬───────────────┘
                │
                ▼
         Generated Draft
                │
       ┌────────┼────────┐
       ▼        ▼        ▼
      TXT      DOCX      PDF
```

## 3.2 Component Responsibilities

### Frontend
- Render input form
- Send request
- Display generated text
- Provide export controls
- Show errors

### Backend
- Define API routes
- Validate schemas
- Coordinate generation
- Return structured responses

### AI Core
- Build controlled prompt
- Call Gemini
- Normalize model output
- Handle model errors

### Export Layer
- Convert generated text to TXT/DOCX/PDF
- Return file bytes or file response

## 3.3 API Contract

### POST `/generate`

Request:

```json
{
  "document_type": "Service Agreement",
  "party_a": "Company A",
  "party_b": "Person B",
  "effective_date": "2026-09-24",
  "terms": "Payment is due within 30 days.",
  "additional_instructions": "Use clear section headings."
}
```

Response:

```json
{
  "success": true,
  "document": "GENERATED DOCUMENT TEXT"
}
```

### GET `/health`

Response:

```json
{
  "status": "ok"
}
```

## 3.4 Data Flow

1. Form input
2. Client validation
3. HTTP request
4. Pydantic validation
5. Prompt construction
6. Gemini request
7. Generated content
8. API response
9. UI preview
10. Export
