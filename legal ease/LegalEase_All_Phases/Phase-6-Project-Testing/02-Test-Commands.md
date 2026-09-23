# Test Commands

Install test dependencies if required:

```bash
pip install pytest httpx
```

Run all tests:

```bash
pytest -v
```

Run API tests:

```bash
pytest tests/test_api.py -v
```

Run exporter tests:

```bash
pytest tests/test_exporters.py -v
```

Manual API documentation:

```text
http://127.0.0.1:8000/docs
```

## Example smoke-test flow

1. Start backend.
2. Open `/docs`.
3. Call `/health`.
4. Send one valid `/generate` request.
5. Verify response contains document text.
6. Open Streamlit.
7. Generate the same document from the UI.
8. Test TXT.
9. Test DOCX.
10. Test PDF.
