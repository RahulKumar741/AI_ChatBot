import streamlit as st

def apply_chat_ui():
    st.markdown("""
        <style>
        .chat-container {
            width: 600px;
            height: 700px;
            margin: auto;
            display: flex;
            flex-direction: column;
            border-radius: 12px;
            border: 2px solid #004080;
            background: #ffffff;
            box-shadow: 0px 4px 12px rgba(0,0,0,0.2);
        }
        .chat-header {
            background: #004080;
            color: white;
            padding: 12px;
            font-size: 18px;
            font-weight: bold;
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
            background: #f4f6f9;
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
            border-top: 1px solid #ddd;
            background: #fafafa;
        }
        /* Mobile responsive */
        @media (max-width: 768px) {
            .chat-container {
                width: 95% !important;
                height: 80vh !important;
            }
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

def auto_scroll():
    st.markdown(
        "<script>window.scrollTo(0, document.body.scrollHeight);</script>",
        unsafe_allow_html=True
    )
