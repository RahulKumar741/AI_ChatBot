import os
import pandas as pd
from rapidfuzz import fuzz
from docx import Document
from PyPDF2 import PdfReader

def load_kb():
    kb_data = []
    knowledge_path = "knowledge"

    if not os.path.exists(Knowledge_path):
        print("⚠️ knowledge/ folder not found.")
        return pd.DataFrame(columns=["Category", "Question", "Answer"])

    # Load CSV if available
    csv_path = os.path.join(Knowledge_path, "data.csv")
    if os.path.exists(csv_path):
        df = pd.read_csv(csv_path)
        for _, row in df.iterrows():
            kb_data.append({
                "Category": row.get("Category", "General"),
                "Question": str(row.get("Question", "")).strip(),
                "Answer": str(row.get("Answer", "")).strip()
            })
    else:
        print("⚠️ data.csv not found inside knowledge/")

    # Load TXT, DOCX, PDF if folder exists
    for file in os.listdir(Knowledge_path):
        filepath = os.path.join(Knowledge_path, file)

        if file.endswith(".txt"):
            with open(filepath, "r", encoding="utf-8") as f:
                kb_data.append({"Category": "TextDoc", "Question": file, "Answer": f.read().strip()})

        elif file.endswith(".docx"):
            doc = Document(filepath)
            content = "\n".join([p.text for p in doc.paragraphs if p.text.strip()])
            kb_data.append({"Category": "WordDoc", "Question": file, "Answer": content})

        elif file.endswith(".pdf"):
            reader = PdfReader(filepath)
            content = "\n".join([page.extract_text() for page in reader.pages if page.extract_text()])
            kb_data.append({"Category": "PDF", "Question": file, "Answer": content})

    return pd.DataFrame(kb_data)
