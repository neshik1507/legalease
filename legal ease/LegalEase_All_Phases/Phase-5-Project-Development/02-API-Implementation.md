# API Implementation Specification

## Health Endpoint

```python
@app.get("/health")
def health():
    return {"status": "ok"}
```

## Generation Endpoint

```python
@app.post("/generate")
def generate(request: DocumentRequest):
    document = generate_document(request)
    return {
        "success": True,
        "document": document
    }
```

## Validation Model

```python
class DocumentRequest(BaseModel):
    document_type: str
    party_a: str
    party_b: str
    effective_date: date
    terms: str
    additional_instructions: str = ""
```

## Error Response

Use a consistent structure:

```json
{
  "success": false,
  "error": "Readable error message"
}
```

Do not expose API keys, stack traces, or internal secrets to users.
