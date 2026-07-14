import fitz

def extract_text_from_pdf(pdf_path):
    file = fitz.open(pdf_path)
    text = ""
    for page in file:
        text += page.get_text()
    return text