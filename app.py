import streamlit as st
import kb_loader
import ui_manager

st.set_page_config(page_title="AI ChatBot", page_icon="🤖", layout="centered")

ui_manager.apply_chat_ui()

kb = kb_loader.load_kb()
if kb.empty:
    st.warning("⚠️ Knowledge base empty. Please add files to the Knowledge/ folder.")

# Keep chat history alive
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "bot", "content": "Hi 👋, welcome to Rahul's Smart Assistant! How can I help you today?"}
    ]

# Header
ui_manager.render_header(chat_name="Rahul's Smart Assistant", 
                         icon_url="https://cdn-icons-png.flaticon.com/512/4712/4712109.png")

# Messages
st.markdown('<div class="chat-messages">', unsafe_allow_html=True)
for msg in st.session_state["messages"]:
    if msg["role"] == "user":
        st.markdown(f'<div class="user-msg">🧑 {msg["content"]}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="bot-msg">🤖 {msg["content"]}</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Footer input
st.markdown('<div class="chat-footer">', unsafe_allow_html=True)
col1, col2 = st.columns([8, 2])
with col1:
    user_input = st.text_input("💬 Type your message:", key="chat_input", label_visibility="collapsed")
with col2:
    send = st.button("Send", key="send_btn")
st.markdown('</div>', unsafe_allow_html=True)

# Process input (without clearing)
if send and user_input.strip():
    st.session_state["messages"].append({"role": "user", "content": user_input})

    kb_answer = kb_loader.find_kb_answer(user_input, kb)
    if kb_answer:
        bot_reply = f"📚 {kb_answer}"
    else:
        bot_reply = "🤔 Sorry, I don’t know that yet."

    st.session_state["messages"].append({"role": "bot", "content": bot_reply})
