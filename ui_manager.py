import streamlit as st

def apply_custom_css():
    """Apply custom styles for the chat UI"""
    st.markdown("""
        <style>
        .chat-container {
            max-height: 500px;
            overflow-y: auto;
            padding: 10px;
            background-color: #f0f2f6;
            border-radius: 10px;
            border: 1px solid #ddd;
        }
        .user-bubble {
            background-color: #DCF8C6;
            color: black;
            padding: 10px;
            border-radius: 10px;
            margin: 5px;
            text-align: right;
        }
        .bot-bubble {
            background-color: #E8EAF6;
            color: black;
            padding: 10px;
            border-radius: 10px;
            margin: 5px;
            text-align: left;
        }
        .header-container {
            display: flex;
            align-items: center;
            justify-content: center;
            background-color: #4CAF50;
            padding: 15px;
            border-radius: 8px;
            color: white;
            margin-bottom: 20px;
        }
        .header-icon {
            font-size: 30px;
            margin-right: 10px;
        }
        .header-title {
            font-size: 22px;
            font-weight: bold;
        }
        </style>
    """, unsafe_allow_html=True)

def render_header(chat_name="My AI Assistant", chat_icon="🤖"):
    """Render the chatbot header with a name and icon"""
    st.markdown(f"""
        <div class="header-container">
            <span class="header-icon">{chat_icon}</span>
            <span class="header-title">{chat_name}</span>
        </div>
    """, unsafe_allow_html=True)

def render_chat(messages):
    """Render the chat history as styled bubbles"""
    st.markdown('<div class="chat-container">', unsafe_allow_html=True)
    for msg in messages:
        if msg["role"] == "user":
            st.markdown(f'<div class="user-bubble">🧑 {msg["content"]}</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="bot-bubble">{msg["content"]}</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
