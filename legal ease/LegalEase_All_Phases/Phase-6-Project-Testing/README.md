# Phase 6 — Project Testing

## 6.1 Testing Strategy

Testing is divided into:

1. Unit testing
2. API testing
3. Export testing
4. Validation testing
5. Error-handling testing
6. Manual UI testing

## 6.2 Test Cases

| ID | Test | Input | Expected |
|---|---|---|---|
| TC-01 | Health check | GET `/health` | 200 + status ok |
| TC-02 | Valid request | All required fields | Draft generated |
| TC-03 | Missing party | Empty party | Validation error |
| TC-04 | Missing terms | Empty terms | Validation error |
| TC-05 | Invalid date | Bad date | Validation error |
| TC-06 | Gemini failure | Simulated API error | Friendly error |
| TC-07 | TXT export | Generated draft | `.txt` created |
| TC-08 | DOCX export | Generated draft | Valid `.docx` |
| TC-09 | PDF export | Generated draft | Valid `.pdf` |
| TC-10 | Special characters | Unicode text | Output preserved |
| TC-11 | Long input | Large terms | Controlled handling |
| TC-12 | Empty AI output | Mock empty response | Error/retry message |

## 6.3 Security Tests

- API key is absent from source code.
- `.env` is ignored by Git.
- User input is not executed as code.
- Error messages do not reveal secrets.
- Uploaded files are handled safely.

## 6.4 Acceptance Criteria

The application passes acceptance when:
- API starts successfully.
- Frontend starts successfully.
- Valid requests generate drafts.
- Invalid requests are rejected.
- All three export formats work.
- AI failures are handled.
- No secret is committed.
