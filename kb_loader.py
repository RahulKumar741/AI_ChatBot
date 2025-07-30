import pandas as pd
from rapidfuzz import fuzz

def load_kb():
    try:
        df = pd.read_csv("knowledge/data.csv")
        required_cols = {"Category", "Question", "Answer"}
        if not required_cols.issubset(df.columns):
            print("CSV must have: Category, Question, Answer")
            return pd.DataFrame(columns=["Category", "Question", "Answer"])
        return df
    except Exception as e:
        print(f"Error loading KB: {e}")
        return pd.DataFrame(columns=["Category", "Question", "Answer"])

def find_kb_answer(user_q, kb, threshold=70):
    best_match = None
    best_score = 0
    for _, row in kb.iterrows():
        score = fuzz.partial_ratio(user_q.lower(), row["Question"].lower())
        if score > best_score:
            best_score = score
            best_match = row
    if best_match is not None and best_score >= threshold:
        return f"[{best_match['Category']}] {best_match['Answer']}"
    return None
