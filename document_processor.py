import pandas as pd
import PyPDF2

def process_excel(file):
    return pd.read_excel(file)

def process_pdf(file):
    reader = PyPDF2.PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    return text
