import os
import pandas as pd
from rapidfuzz import fuzz

try:
    from docx import Document
except ImportError:
    Document = None

try:
    from PyPDF2 import PdfReader
except ImportError:
    PdfReader = None

def load_kb():
    kb_data = []
    knowledge_path = "Knowledge"  # capital K

    if not os.path.exists(knowledge_path):
        print("⚠️ Knowledge/ folder not found.")
        return pd.DataFrame(columns=["Category", "Question", "Answer"])

    # Load CSV
    csv_path = os.path.join(knowledge_path, "data.csv")
    if os.path.exists(csv_path):
        df = pd.read_csv(csv_path)
        for _, row in df.iterrows():
            kb_data.append({
                "Category": row.get("Category", "General"),
                "Question": str(row.get("Question", "")).strip(),
                "Answer": str(row.get("Answer", "")).strip()
            })

    # Load TXT
    for file in os.listdir(knowledge_path):
        if file.endswith(".txt"):
            with open(os.path.join(knowledge_path, file), "r", encoding="utf-8") as f:
                kb_data.append({
                    "Category": "TextDoc",
                    "Question": file,
                    "Answer": f.read().strip()
                })

    # Load DOCX
    if Document:
        for file in os.listdir(knowledge_path):
            if file.endswith(".docx"):
                doc = Document(os.path.join(knowledge_path, file))
                content = "\n".join([p.text for p in doc.paragraphs if p.text.strip()])
                kb_data.append({
                    "Category": "WordDoc",
                    "Question": file,
                    "Answer": content
                })

    # Load PDF
    if PdfReader:
        for file in os.listdir(knowledge_path):
            if file.endswith(".pdf"):
                reader = PdfReader(os.path.join(knowledge_path, file))
                content = "\n".join([page.extract_text() for page in reader.pages if page.extract_text()])
                kb_data.append({
                    "Category": "PDF",
                    "Question": file,
                    "Answer": content
                })

    return pd.DataFrame(kb_data, columns=["Category", "Question", "Answer"])

def find_kb_answer(user_q, kb, threshold=60):
    if kb.empty:
        return None

    user_q_lower = user_q.strip().lower()
    best_match, best_score = None, 0

    for _, row in kb.iterrows():
        question_text = str(row["Question"]).strip().lower()
        score = fuzz.partial_ratio(user_q_lower, question_text)
        if score > best_score:
            best_score, best_match = score, row

    if best_match is not None and best_score >= threshold:
        return f"[{best_match['Category']}] {best_match['Answer']}"
    return None
