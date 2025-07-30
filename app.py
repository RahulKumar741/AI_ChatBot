import streamlit as st
import kb_loader
import ui_manager

st.set_page_config(page_title="AI ChatBot", page_icon="🤖", layout="centered")

ui_manager.apply_chat_ui()

kb = kb_loader.load_kb()
if kb.empty:
    st.warning("⚠️ Knowledge base empty. Please add files to the Knowledge/ folder.")

if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "bot", "content": "Hi 👋, welcome to Rahul's Smart Assistant! How can I help you today?"}
    ]

# Render chat UI (header + messages + footer input)
user_input = ui_manager.render_chat_ui(st.session_state["messages"])

if user_input:
    st.session_state["messages"].append({"role": "user", "content": user_input})
    kb_answer = kb_loader.find_kb_answer(user_input, kb)
    if kb_answer:
        bot_reply = f"📚 {kb_answer}"
    else:
        bot_reply = "🤔 Sorry, I don’t know that yet."
    st.session_state["messages"].append({"role": "bot", "content": bot_reply})
    st.experimental_rerun()
