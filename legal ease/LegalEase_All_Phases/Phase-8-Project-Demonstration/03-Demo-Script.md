# Ready-to-Speak Demo Script

Good morning everyone. Our project is **LegalEase**, an AI-powered legal document drafting and export platform.

The main idea is to help users create a structured first draft from simple information such as document type, parties, effective date, and terms.

The frontend is developed using Streamlit. The backend uses FastAPI. Google Gemini is used for generative AI, while Python libraries generate TXT, DOCX, and PDF files.

First, I enter the document information. When I click Generate, the request is validated by the FastAPI backend. The AI module then builds a controlled prompt and sends it to Gemini. The generated draft is returned to the application and displayed for review.

Now I can export the result as TXT, DOCX, or PDF.

We also test invalid inputs and API failures so that the application does not simply crash.

LegalEase is intended as an AI-assisted drafting tool. Generated documents should be reviewed appropriately before real-world legal use.

Thank you.
