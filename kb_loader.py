import os
import pandas as pd
from rapidfuzz import fuzz
from docx import Document
from PyPDF2 import PdfReader

def load_kb():
    kb_data = []

    # 1. Load CSV
    csv_path = "knowledge/data.csv"
    if os.path.exists(csv_path):
        df = pd.read_csv(csv_path)
        for _, row in df.iterrows():
            kb_data.append({
                "Category": row.get("Category", "General"),
                "Question": str(row.get("Question", "")).strip(),
                "Answer": str(row.get("Answer", "")).strip()
            })

    # 2. Load TXT files
    for file in os.listdir("knowledge"):
        if file.endswith(".txt"):
            with open(os.path.join("knowledge", file), "r", encoding="utf-8") as f:
                content = f.read()
                kb_data.append({
                    "Category": "TextDoc",
                    "Question": file,
                    "Answer": content.strip()
                })

    # 3. Load DOCX files
    for file in os.listdir("knowledge"):
        if file.endswith(".docx"):
            doc = Document(os.path.join("knowledge", file))
            content = "\n".join([p.text for p in doc.paragraphs if p.text.strip()])
            kb_data.append({
                "Category": "WordDoc",
                "Question": file,
                "Answer": content.strip()
            })

    # 4. Load PDF files
    for file in os.listdir("knowledge"):
        if file.endswith(".pdf"):
            reader = PdfReader(os.path.join("knowledge", file))
            content = "\n".join([page.extract_text() for page in reader.pages if page.extract_text()])
            kb_data.append({
                "Category": "PDF",
                "Question": file,
                "Answer": content.strip()
            })

    return pd.DataFrame(kb_data)

def find_kb_answer(user_q, kb, threshold=60):
    user_q_lower = user_q.strip().lower()
    best_match = None
    best_score = 0

    for _, row in kb.iterrows():
        question_text = str(row["Question"]).strip().lower()
        score = fuzz.partial_ratio(user_q_lower, question_text)
        if score > best_score:
            best_score = score
            best_match = row

    if best_match is not None and best_score >= threshold:
        return f"[{best_match['Category']}] {best_match['Answer']}"
    return None
