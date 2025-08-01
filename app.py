import os
import pandas as pd
from rapidfuzz import fuzz

def load_kb():
    kb_data = []
    knowledge_path = "Knowledge"

    if not os.path.exists(knowledge_path):
        return pd.DataFrame(columns=["Category", "Question", "Answer"])

    csv_path = os.path.join(knowledge_path, "data.csv")
    if os.path.exists(csv_path):
        df = pd.read_csv(csv_path)
        for _, row in df.iterrows():
            kb_data.append({
                "Category": row.get("Category", "General"),
                "Question": str(row.get("Question", "")).strip(),
                "Answer": str(row.get("Answer", "")).strip()
            })

    return pd.DataFrame(kb_data, columns=["Category", "Question", "Answer"])

def find_kb_answer(user_q, kb, threshold=80):
    if kb.empty:
        return None

    user_q_lower = user_q.strip().lower()
    if len(user_q_lower) < 3:  # Skip very short inputs like "hi"
        return None

    best_match, best_score = None, 0
    for _, row in kb.iterrows():
        question_text = str(row["Question"]).strip().lower()
        score = fuzz.partial_ratio(user_q_lower, question_text)

        if score > best_score:
            best_score, best_match = score, row
        if score == 100:
            break  # Perfect match found

    if best_match is not None and best_score >= threshold:
        return f"[{best_match['Category']}] {best_match['Answer']}"
    return None
