import streamlit as st
import kb_loader
import ui_manager

st.set_page_config(page_title="AI ChatBot", page_icon="🤖", layout="centered")

# Apply CSS
ui_manager.apply_chat_ui()

# Load knowledge base
kb = kb_loader.load_kb()
if kb.empty:
    st.warning("⚠️ Knowledge base empty. Please add files to the Knowledge/ folder.")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "bot", "content": "Hi 👋, welcome to Rahul's Smart Assistant! How can I help you today?"}]

# Render the chat UI (header + messages inside one container)
ui_manager.render_chat_ui(st.session_state["messages"])

# Chat input INSIDE the container footer
with st.container():
    st.markdown('<div class="chat-footer">', unsafe_allow_html=True)
    with st.form(key="chat_form", clear_on_submit=True):
        user_input = st.text_input("💬 Type your message:")
        submit_button = st.form_submit_button("Send")
    st.markdown('</div>', unsafe_allow_html=True)

if submit_button and user_input:
    st.session_state["messages"].append({"role": "user", "content": user_input})
    kb_answer = kb_loader.find_kb_answer(user_input, kb)
    if kb_answer:
        bot_reply = f"📚 {kb_answer}"
    else:
        bot_reply = "🤔 Sorry, I don’t know that yet."
    st.session_state["messages"].append({"role": "bot", "content": bot_reply})
    st.experimental_rerun()
