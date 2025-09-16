import streamlit as st
from document_processor import process_excel, process_pdf
from qa_engine import ask_ollama

st.title("📊 Financial Document Q&A Assistant")

uploaded_file = st.file_uploader("Upload a financial document (PDF/Excel)", type=["pdf", "xlsx"])

if uploaded_file:
    if uploaded_file.type == "application/pdf":
        content = process_pdf(uploaded_file)
    else:
        df = process_excel(uploaded_file)
        content = df.to_string()

    st.success("✅ Document processed successfully!")
    st.text_area("Extracted Content (preview)", content[:1000])

    question = st.text_input("Ask a question about the financial data:")
    if st.button("Get Answer"):
        answer = ask_ollama(question, content)
        st.write("💡 Answer:", answer)
