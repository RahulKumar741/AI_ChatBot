import streamlit as st
import kb_loader
import ui_manager

st.set_page_config(page_title="AI ChatBot", page_icon="🤖", layout="centered")

# Apply UI styles
ui_manager.apply_chat_ui()

# Render header
ui_manager.render_header("Rahul's Smart Assistant")

# Load KB
kb = kb_loader.load_kb()
if kb.empty:
    st.warning("⚠️ Knowledge base empty. Please add files to the Knowledge folder.")

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "bot", "content": "Hi 👋, welcome to Rahul's Smart Assistant! How can I help you today?"}]

# Render chat history
ui_manager.render_messages(st.session_state["messages"])

# Chat input
with st.form(key="chat_form", clear_on_submit=True):
    user_input = st.text_input("Type your message:")
    submit_button = st.form_submit_button("Send")

if submit_button and user_input:
    st.session_state["messages"].append({"role": "user", "content": user_input})
    kb_answer = kb_loader.find_kb_answer(user_input, kb)
    if kb_answer:
        bot_reply = f"📚 {kb_answer}"
    else:
        bot_reply = "🤔 Sorry, I don’t know that yet."
    st.session_state["messages"].append({"role": "bot", "content": bot_reply})
    st.experimental_rerun()

# Optional: Quick reply buttons
choice = ui_manager.render_quick_replies(["Branch Location", "ATM Location", "Contact Support"])
if choice:
    st.session_state["messages"].append({"role": "user", "content": choice})
    st.session_state["messages"].append({"role": "bot", "content": f"You selected: {choice}"})
    st.experimental_rerun()
