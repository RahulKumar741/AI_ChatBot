import streamlit as st

def apply_chat_ui():
    st.markdown("""
        <style>
        .chat-header img {
            width: 36px;
            height: 36px;
            border-radius: 50%;
            margin-right: 10px;
        }
        .chat-messages {
            padding: 10px;
            overflow-y: auto;
            background: #f4f6f9;
            border-radius: 8px;
            margin-bottom: 10px;
        }
        .user-msg {
            background: #DCF8C6;
            padding: 10px 14px;
            border-radius: 12px;
            margin: 6px;
            text-align: right;
            max-width: 80%;
            margin-left: auto;
        }
        .bot-msg {
            background: #E8EAF6;
            padding: 10px 14px;
            border-radius: 12px;
            margin: 6px;
            text-align: left;
            max-width: 80%;
            margin-right: auto;
        }
        .chat-footer {
            padding: 10px;
            background: #fafafa;
            border-radius: 8px;
        }
        </style>
    """, unsafe_allow_html=True)

def render_header(chat_name="Rahul's Smart Assistant", icon_url="https://cdn-icons-png.flaticon.com/512/4712/4712109.png"):
    st.markdown(f"""
        <div class="chat-header">
            <img src="{icon_url}" alt="Bot Icon">
            <span>{chat_name}</span>
        </div>
    """, unsafe_allow_html=True)
