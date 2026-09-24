# Use Cases

## UC-01 Generate a document

**Actor:** User

1. User opens LegalEase.
2. User selects document type.
3. User enters party details.
4. User selects effective date.
5. User enters terms.
6. User submits the form.
7. System validates inputs.
8. Backend creates the AI request.
9. Gemini returns a draft.
10. User reviews the result.

## UC-02 Export as DOCX

1. User generates a draft.
2. User selects DOCX.
3. System formats the text.
4. System returns a downloadable Word file.

## UC-03 Export as PDF

1. User generates a draft.
2. User selects PDF.
3. System creates a PDF.
4. System returns the generated file.

## UC-04 Recover from failure

1. User submits a request.
2. API or AI call fails.
3. System catches the exception.
4. System displays a readable error.
5. User can retry.
