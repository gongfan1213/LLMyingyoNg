import fitz  # PyMuPDF

doc = fitz.open("input.pdf")
with open("output.md", "w", encoding="utf-8") as f:
    for page in doc:
        text = page.get_text()
        f.write(text + "\n\n")
