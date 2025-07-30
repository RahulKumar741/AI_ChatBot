import streamlit as st
import kb_loader

st.set_page_config(page_title="AI ChatBot", page_icon="🤖", layout="wide")

st.title("🤖 Knowledge-Based AI ChatBot")
st.write("✅ Answers come from the Knowledge folder. (AI fallback disabled)")

# Load knowledge base
kb = kb_loader.load_kb()

if kb.empty:
    st.warning("⚠️ No knowledge base loaded. Please add a CSV/TXT/DOCX/PDF file in the Knowledge/ folder.")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Chat input form
with st.form(key="chat_form", clear_on_submit=True):
    user_input = st.text_input("💬 Ask your question:")
    submit_button = st.form_submit_button("Send")

if submit_button and user_input:
    st.session_state["messages"].append({"role": "user", "content": user_input})

    kb_answer = kb_loader.find_kb_answer(user_input, kb)
    if kb_answer:
        bot_reply = f"📚 {kb_answer}"
    else:
        bot_reply = "🤔 Sorry, I don’t know that yet. (AI fallback disabled)"
    
    st.session_state["messages"].append({"role": "bot", "content": bot_reply})

# Display chat history
for msg in st.session_state["messages"]:
    if msg["role"] == "user":
        st.markdown(f"🧑 **You:** {msg['content']}")
    else:
        st.markdown(f"🤖 **Bot:** {msg['content']}")
