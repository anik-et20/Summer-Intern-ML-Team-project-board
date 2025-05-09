import PyPDF2

def extract_text_pypdf2(pdf_path):
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            content = page.extract_text()
            if content:
                text += content + "\n"
    return text.strip()

# Example usage
pdf_path = "dummy_resume.pdf"
resume_text = extract_text_pypdf2(pdf_path)
print(resume_text)
