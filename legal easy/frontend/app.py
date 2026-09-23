import os
import requests
import streamlit as st
from dotenv import load_dotenv

from generators.txt_generator import format_txt
from generators.docx_generator import format_docx
from generators.pdf_generator import format_pdf
from generators.html_generator import format_html_preview

load_dotenv()
BACKEND_URL = os.getenv("BACKEND_URL", "http://127.0.0.1:8000").rstrip("/")

st.set_page_config(page_title="LegalEase", page_icon="⚖️", layout="wide")

st.markdown("""
<style>
.main { background: #0b1020; }
.block-container { max-width: 1200px; padding-top: 2rem; }
.hero {
    padding: 28px;
    border-radius: 20px;
    background: linear-gradient(135deg, #111827, #172554);
    border: 1px solid #334155;
    margin-bottom: 24px;
}
.hero h1 { margin: 0; color: white; }
.hero p { color: #cbd5e1; }
.preview {
    background: #0b1220;
    color: #e5e7eb;
    border: 1px solid #334155;
    border-radius: 14px;
    padding: 24px;
    max-height: 620px;
    overflow-y: auto;
    line-height: 1.65;
}
.preview h3 { color: #93c5fd; }
.disclaimer {
    padding: 12px 16px;
    border-left: 4px solid #f59e0b;
    background: #1f2937;
    color: #f8fafc;
    border-radius: 8px;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
<h1>⚖️ LegalEase</h1>
<p>AI-Powered Legal Document Generator — create editable first drafts and export them professionally.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="disclaimer">
<strong>Important:</strong> LegalEase creates AI-assisted drafts, not legal advice.
Verify the information and have important documents reviewed by a qualified legal professional.
</div>
""", unsafe_allow_html=True)

if "document" not in st.session_state:
    st.session_state.document = ""
if "terms" not in st.session_state:
    st.session_state.terms = ""

col1, col2 = st.columns(2)

with col1:
    document_type = st.selectbox(
        "Document Type",
        [
            "Employment Contract",
            "Non-Disclosure Agreement (NDA)",
            "Lease Agreement",
            "Freelance Work Contract",
            "Service Agreement",
            "Employment Offer Letter",
            "General Agreement",
            "Custom Legal Document",
        ],
    )
    if document_type == "Custom Legal Document":
        document_type = st.text_input("Custom document type")
    parties = st.text_area(
        "Parties Involved",
        placeholder="Jane Doe (Service Provider), TechNova Inc. (Client)",
        height=130,
    )

with col2:
    dates = st.text_input("Effective Date", placeholder="April 10, 2026")
    terms = st.text_area(
        "Terms & Conditions",
        placeholder="Payment within 30 days; Confidentiality must be maintained; Either party may terminate with 15 days notice",
        height=130,
        help="Separate individual terms with semicolons.",
    )

logo_file = st.file_uploader("Optional company logo", type=["png", "jpg", "jpeg"])

if st.button("✨ Generate Document", type="primary", use_container_width=True):
    if not document_type or not parties or not terms or not dates:
        st.error("Please complete document type, parties, terms and effective date.")
    else:
        try:
            with st.spinner("Generating your legal draft with Gemini..."):
                response = requests.post(
                    f"{BACKEND_URL}/generate",
                    json={
                        "document_type": document_type,
                        "parties": parties,
                        "terms": terms,
                        "dates": dates,
                    },
                    timeout=120,
                )
            if response.ok:
                st.session_state.document = response.json()["text"]
                st.session_state.terms = terms
                st.success("Document generated successfully.")
            else:
                try:
                    detail = response.json().get("detail", response.text)
                except Exception:
                    detail = response.text
                st.error(f"Backend error: {detail}")
        except requests.RequestException as exc:
            st.error(f"Could not connect to FastAPI at {BACKEND_URL}. Start the backend first. Details: {exc}")

if st.session_state.document:
    st.divider()
    st.subheader("Document Preview")
    document = st.session_state.document or ""
    preview = format_html_preview(document)
    st.markdown(f'<div class="preview">{preview}</div>', unsafe_allow_html=True)

    st.subheader("Edit Document")
    edited = st.text_area(
        "Edit the generated text before exporting",
        value=document,
        height=500,
        label_visibility="collapsed",
    )
    st.session_state.document = edited

    st.subheader("Download")
    d1, d2, d3 = st.columns(3)
    txt_data = format_txt(document)
    docx_data = format_docx(document, document_type, st.session_state.terms, logo_file)
    pdf_data = format_pdf(document, document_type, logo_file)

    safe_name = "".join(
        c if c.isalnum() or c in "-_" else "_"
        for c in document_type.lower()
    ).strip("_") or "legalease_document"

    with d1:
        st.download_button("⬇️ Download TXT", data=txt_data,
                           file_name=f"{safe_name}.txt", mime="text/plain",
                           use_container_width=True)
    with d2:
        st.download_button("⬇️ Download DOCX", data=docx_data,
                           file_name=f"{safe_name}.docx",
                           mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                           use_container_width=True)
    with d3:
        st.download_button("⬇️ Download PDF", data=pdf_data,
                           file_name=f"{safe_name}.pdf", mime="application/pdf",
                           use_container_width=True)

st.caption("LegalEase — AI-assisted drafting prototype")
