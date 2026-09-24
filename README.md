# Phase 2 — Requirement Analysis

## 2.1 Functional Requirements

### FR-01 — Collect document information
The system shall collect document type, parties, effective date, terms, and additional instructions.

### FR-02 — Validate input
The backend shall reject missing or invalid required fields.

### FR-03 — Generate draft
The system shall construct a controlled prompt and request a document draft from Gemini.

### FR-04 — Preview
The frontend shall display generated content before export.

### FR-05 — TXT export
The system shall export the draft as plain text.

### FR-06 — DOCX export
The system shall create a Microsoft Word document.

### FR-07 — PDF export
The system shall create a PDF document.

### FR-08 — Error handling
The application shall show useful messages when the API, validation, or export process fails.

### FR-09 — Environment configuration
Secrets such as API keys shall be loaded from environment variables.

## 2.2 Non-Functional Requirements

- Usability: simple form-driven interface
- Performance: avoid unnecessary API calls
- Security: never hard-code API keys
- Maintainability: separate frontend, backend, AI, and export logic
- Reliability: handle invalid requests and AI failures
- Portability: support local development and Docker deployment

## 2.3 Inputs

- Document type
- First party
- Second party
- Effective date
- Terms and conditions
- Additional instructions
- Optional logo

## 2.4 Outputs

- Structured legal-document draft
- TXT file
- DOCX file
- PDF file

## 2.5 Assumptions

- User has a valid Gemini API key.
- Python dependencies can be installed.
- Internet access is available when Gemini is called.
- User reviews generated content.

## 2.6 Out of Scope

- Legal representation
- Court filing
- Electronic signatures
- Automated legal compliance certification
- Guaranteed jurisdiction-specific legal validity
- Autonomous legal advice
