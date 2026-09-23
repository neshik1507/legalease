# Phase 8 — Project Demonstration

## 8.1 Demonstration Objective

Demonstrate the complete LegalEase workflow from input to AI generation to document export.

## 8.2 Recommended 7–10 Minute Demo

### Part 1 — Introduction
Explain:
- Project name
- Problem
- Solution
- Target users

### Part 2 — Technology
Show:
- Streamlit
- FastAPI
- Gemini
- Python
- DOCX/PDF/TXT exporters

### Part 3 — Live Input
Enter:
- Document type: Service Agreement
- Party A: Example Company
- Party B: Example Client
- Effective date: current/project date
- Terms: payment, services, responsibilities
- Additional instructions: clear headings

### Part 4 — AI Generation
Click Generate and explain:
1. UI sends data to backend.
2. FastAPI validates the request.
3. AI layer constructs the prompt.
4. Gemini returns the draft.
5. Frontend displays the response.

### Part 5 — Export
Demonstrate:
- TXT
- DOCX
- PDF

Open at least one exported file.

### Part 6 — Testing
Show:
- `/docs`
- `/health`
- Test suite
- One validation failure

### Part 7 — Conclusion
Explain achieved objectives and future improvements.
