import streamlit as st
import kb_loader
import ui_manager

st.set_page_config(page_title="AI ChatBot", page_icon="🤖", layout="centered")

# Apply custom styles
ui_manager.apply_chat_ui()

# Render header with profile photo
ui_manager.render_header(
    chat_name="Rahul's Smart Assistant",
    icon_url="https://cdn-icons-png.flaticon.com/512/4712/4712109.png"  # sample bot icon
)

# Load KB
kb = kb_loader.load_kb()
if kb.empty:
    st.warning("⚠️ No knowledge base loaded. Please add files to the Knowledge/ folder.")

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "bot", "content": "Hi 👋, welcome to Rahul's Smart Assistant! How can I help you today?"}]

# Render chat history
ui_manager.render_chat(st.session_state["messages"])

# Chat input
with st.form(key="chat_form", clear_on_submit=True):
    user_input = st.text_input("💬 Type your message:")
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
