import streamlit as st

def apply_chat_ui():
    st.markdown("""
        <style>
        .chat-container {
            width: 400px;
            height: 600px;
            margin: auto;
            display: flex;
            flex-direction: column;
            border-radius: 12px;
            border: 2px solid #004080;
            background: url('https://via.placeholder.com/400x600.png?text=Chat+Background') no-repeat center;
            background-size: cover;
            box-shadow: 0px 4px 12px rgba(0,0,0,0.2);
        }
        .chat-header {
            background: #004080;
            color: white;
            padding: 12px;
            font-size: 16px;
            font-weight: bold;
            text-align: left;
            display: flex;
            align-items: center;
            border-top-left-radius: 12px;
            border-top-right-radius: 12px;
        }
        .chat-header img {
            width: 36px;
            height: 36px;
            border-radius: 50%;
            margin-right: 10px;
        }
        .chat-messages {
            flex: 1;
            padding: 10px;
            overflow-y: auto;
            background: rgba(255, 255, 255, 0.9);
        }
        .user-msg {
            background: #DCF8C6;
            padding: 8px 12px;
            border-radius: 12px;
            margin: 6px;
            text-align: right;
            max-width: 75%;
            margin-left: auto;
        }
        .bot-msg {
            background: #E8EAF6;
            padding: 8px 12px;
            border-radius: 12px;
            margin: 6px;
            text-align: left;
            max-width: 75%;
            margin-right: auto;
        }
        .chat-footer {
            padding: 10px;
            border-top: 1px solid #ddd;
            background: #fafafa;
        }
        </style>
    """, unsafe_allow_html=True)

def render_header(chat_name="Rahul's Smart Assistant", icon_url="https://via.placeholder.com/36"):
    st.markdown(f"""
        <div class="chat-header">
            <img src="{icon_url}" alt="Bot Icon">
            <span>{chat_name}</span>
        </div>
    """, unsafe_allow_html=True)

def render_chat(messages):
    st.markdown('<div class="chat-container">', unsafe_allow_html=True)
    st.markdown('<div class="chat-messages">', unsafe_allow_html=True)
    for msg in messages:
        if msg["role"] == "user":
            st.markdown(f'<div class="user-msg">🧑 {msg["content"]}</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="bot-msg">🤖 {msg["content"]}</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)  # close messages
    st.markdown('</div>', unsafe_allow_html=True)  # close container
