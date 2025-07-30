import streamlit as st
import kb_loader
import ui_manager

st.set_page_config(page_title="AI ChatBot", page_icon="🤖", layout="wide")

# Apply custom styling
ui_manager.apply_custom_css()

# Render personalized header
ui_manager.render_header(chat_name="Rahul's Smart Assistant", chat_icon="🤖")

# Load KB
kb = kb_loader.load_kb()
if kb.empty:
    st.warning("⚠️ No knowledge base loaded. Add files to the Knowledge/ folder.")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Greetings dictionary
greetings = {
    "hi": "🤖 Hello! How can I assist you today?",
    "hello": "🤖 Hi there! Good to see you 😊",
    "hey": "🤖 Hey! What would you like to know?",
    "good morning": "🤖 Good morning! Hope you have a great day 🌞",
    "good evening": "🤖 Good evening! How can I help you tonight?",
}

# Chat input form
with st.form(key="chat_form", clear_on_submit=True):
    user_input = st.text_input("💬 Type your message:")
    submit_button = st.form_submit_button("Send")

if submit_button and user_input:
    st.session_state["messages"].append({"role": "user", "content": user_input})

    user_text = user_input.lower().strip()
    if user_text in greetings:
        bot_reply = greetings[user_text]
    else:
        kb_answer = kb_loader.find_kb_answer(user_input, kb)
        if kb_answer:
            bot_reply = f"📚 {kb_answer}"
        else:
            bot_reply = "🤔 Sorry, I don’t know that yet. (AI fallback disabled)"
    
    st.session_state["messages"].append({"role": "bot", "content": bot_reply})

# Render chat history
ui_manager.render_chat(st.session_state["messages"])
