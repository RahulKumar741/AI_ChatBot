import streamlit as st

def apply_chat_ui():
    st.markdown("""
        <style>
        .chat-box {
            width: 380px;
            max-height: 600px;
            margin: auto;
            background: #ffffff;
            border-radius: 12px;
            border: 1px solid #ddd;
            display: flex;
            flex-direction: column;
            box-shadow: 0px 4px 12px rgba(0,0,0,0.1);
        }
        .chat-header {
            background: #004080;
            color: white;
            padding: 12px;
            font-size: 16px;
            font-weight: bold;
            text-align: center;
            border-top-left-radius: 12px;
            border-top-right-radius: 12px;
        }
        .chat-messages {
            flex: 1;
            padding: 10px;
            overflow-y: auto;
            background: #f4f6f9;
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
        .quick-reply {
            display: inline-block;
            margin: 4px;
            padding: 8px 14px;
            border-radius: 20px;
            border: 1px solid #004080;
            color: #004080;
            background: white;
            cursor: pointer;
            font-size: 13px;
        }
        </style>
    """, unsafe_allow_html=True)

def render_header(chat_name="My AI Assistant"):
    st.markdown(f"""
        <div class="chat-header">{chat_name}</div>
    """, unsafe_allow_html=True)

def render_messages(messages):
    st.markdown('<div class="chat-box">', unsafe_allow_html=True)
    st.markdown('<div class="chat-messages">', unsafe_allow_html=True)
    for msg in messages:
        if msg["role"] == "user":
            st.markdown(f'<div class="user-msg">🧑 {msg["content"]}</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="bot-msg">🤖 {msg["content"]}</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)  # close chat-messages

def render_footer():
    st.markdown('<div class="chat-footer">', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

def render_quick_replies(options):
    st.markdown('<div class="chat-footer">', unsafe_allow_html=True)
    for opt in options:
        if st.button(opt, key=opt):
            return opt
    st.markdown('</div>', unsafe_allow_html=True)
    return None
