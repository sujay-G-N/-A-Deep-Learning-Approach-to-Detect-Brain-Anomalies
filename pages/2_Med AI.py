# =====================================================
# Yuva AI – Medical Chat Assistant (FULL CLEAN REFACTOR)
# UI / CSS: UNCHANGED
# Gemini: Official SDK (Direct Model Name, NO REST URLs)
# =====================================================

# ---------------------------
# Core Imports
# ---------------------------
import streamlit as st
import json
import google.genai as genai

# ---------------------------
# Page Config
# ---------------------------
st.set_page_config(
    page_title="Yuva AI",
    page_icon="🧠",
    layout="wide"
)

# ---------------------------
# Configure Gemini (v1 SDK)
# ---------------------------
client = genai.Client(api_key=st.secrets["API_KEY"])

# ---------------------------
# 🌤️ Custom CSS (UNCHANGED)
# ---------------------------
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');

        /* 🌤️ Base Layout */
        html, body, [class*="st-"] {
            font-family: 'Inter', sans-serif;
            background: linear-gradient(135deg, #e0f7fa, #f8fbff, #fefefe);
            color: #1e293b;
            transition: all 0.3s ease-in-out;
        }

        .stApp {
            background: linear-gradient(145deg, #ffffff, #dfe9f3);
        }

        /* 🌈 Header */
        .main-header {
            text-align: center;
            font-weight: 800;
            font-size: 3em;
            background: linear-gradient(90deg, #0077b6, #00b4d8, #90e0ef);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 0.3em;
            letter-spacing: -0.3px;
            text-shadow: 1px 2px 4px rgba(0,0,0,0.15);
            animation: fadeIn 1.2s ease-in-out;
        }

        /* Subheader */
        h3 {
            text-align: center;
            color: #334155;
            font-weight: 500;
            margin-bottom: 1.5em;
            opacity: 0.9;
            animation: fadeIn 1.6s ease-in-out;
        }

        /* Sidebar */
        section[data-testid="stSidebar"] {
            background: rgba(255, 255, 255, 0.45) !important;
            backdrop-filter: blur(10px);
            -webkit-backdrop-filter: blur(10px);
            border-right: 1px solid rgba(255, 255, 255, 0.3);
            box-shadow: 2px 0 15px rgba(0,0,0,0.05);
        }

        /* 🌬️ Chat Bubbles */
        [data-testid="stChatMessageUser"] {
            background: rgba(191, 219, 254, 0.95) !important;
            color: #111827 !important;
            border-radius: 14px !important;
            padding: 12px 18px !important;
            margin: 10px 0;
            border: 1px solid #93c5fd;
            box-shadow: 0 4px 10px rgba(0,0,0,0.08);
            animation: floaty 4s ease-in-out infinite alternate;
        }

        [data-testid="stChatMessageAssistant"] {
            background: rgba(240, 249, 255, 0.95) !important;
            color: #1e3a8a !important;
            border-radius: 14px !important;
            padding: 12px 18px !important;
            margin: 10px 0;
            border: 1px solid #bfdbfe;
            box-shadow: 0 4px 10px rgba(0,0,0,0.08);
            animation: fadeIn 0.6s ease-in-out;
        }

        /* 🖤 Chat Input Box */
        [data-testid="stChatInput"] textarea {
            background-color: #000000 !important;
            color: #000000 !important;
            border: none !important;
            border-radius: 12px !important;
            padding: 14px 18px !important;
            font-size: 1rem !important;
            box-shadow: 0 4px 16px rgba(0, 0, 0, 1) !important;
            transition: all 0.3s ease-in-out;
            resize: none !important;
        }

        [data-testid="stChatInput"] textarea:focus {
            border: 2px solid #60a5fa !important;
            box-shadow: 0 8px 24px rgba(59, 130, 246, 0.4),
                        0 0 10px rgba(96, 165, 250, 0.6) !important;
            transform: translateY(-2px);
            outline: 2px solid #000000 !important; /* bright blue outline */
            outline-offset: 2px;
        }

        [data-testid="stChatInput"] textarea::placeholder {
            color: rgba(0, 0, 0, 1) !important;
        }

        /* ✨ Send Button */
        [data-testid="stChatInput"] button {
            background: linear-gradient(135deg, #3b82f6, #2563eb) !important;
            color: white !important;
            border-radius: 2px !important;
            box-shadow: 0 4px 2px rgba(37, 99, 235, 0.4) !important;
            border: none !important;
            transition: all 0.3s ease-in-out;
        }

        [data-testid="stChatInput"] button:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 18px rgba(30, 58, 138, 0.7) !important; /* darker, deeper blue shadow */
            background: linear-gradient(135deg, #1e3a8a, #1e40af) !important; /* darker gradient blues */
        }


        /* Suggested Questions */
        .stButton>button[data-baseweb="button"] {
            background: rgba(255,255,255,0.85);
            color: #2563eb;
            border: 1px solid #93c5fd;
            border-radius: 8px;
            padding: 8px 18px;
            font-weight: 500;
            box-shadow: 0 2px 6px rgba(37, 99, 235, 0.15);
            transition: 0.3s;
        }

        .stButton>button[data-baseweb="button"]:hover {
            background: rgba(219,234,254,0.8);
            transform: translateY(-2px);
            box-shadow: 0 6px 12px rgba(37, 99, 235, 0.25);
        }

        /* Divider */
        hr {
            border: none;
            height: 1px;
            background: linear-gradient(to right, transparent, rgba(0,0,0,0.1), transparent);
            margin: 40px 0;
        }

        /* Animations */
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(5px); }
            to { opacity: 1; transform: translateY(0); }
        }

        @keyframes floaty {
            0%, 100% { transform: translateY(0px); }
            50% { transform: translateY(-6px); }
        }

        /* Scrollbar */
        ::-webkit-scrollbar {
            width: 8px;
        }
        ::-webkit-scrollbar-thumb {
            background: #93c5fd;
            border-radius: 4px;
        }
        ::-webkit-scrollbar-thumb:hover {
            background: #60a5fa;
        }
    </style>
""", unsafe_allow_html=True)

# ---------------------------
# Gemini Chat Model Helper
# ---------------------------
def get_ai_explanation(query, history):
    """
    google.genai SDK compatible implementation
    """

    # Build plain text context (google.genai does NOT support chat history objects)
    context = (
        "Disclaimer: This is for informational purposes only and not a substitute "
        "for professional medical advice.\n\n"
        "You are a friendly and helpful AI medical assistant. "
        "Provide simple, clear, non-technical medical explanations.\n\n"
    )

    for h in history:
        role = "User" if h["role"] == "user" else "Assistant"
        context += f"{role}: {h['parts'][0]}\n"

    context += f"\nUser: {query}\nAssistant:"

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash-lite",
            contents=context
        )
        return response.text
    except Exception as e:
        st.error(f"AI Error: {e}")
        return "I am unable to provide a response at this time. Please try again later."

# ---------------------------
# App Header
# ---------------------------
st.markdown("<h1 class='main-header'>Yuva AI</h1>", unsafe_allow_html=True)
st.markdown("<h3>Ask the AI about a diagnosis or a general medical question.</h3>", unsafe_allow_html=True)
st.markdown("---")

# ---------------------------
# Session State Initialization
# ---------------------------
# Session State Initialization (REQUIRED)
# ---------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

if "suggested_questions" not in st.session_state:
    st.session_state.suggested_questions = []

if "prompt_from_button" not in st.session_state:
    st.session_state.prompt_from_button = ""
# ---------------------------
# Display Chat History
# ---------------------------
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

## ---------------------------
# Chat Input Handling
# ---------------------------
initial_prompt = st.session_state.pop("prompt_from_button", "")

prompt = st.chat_input("Ask a question about medical assistance or anomalies...")
if initial_prompt:
    prompt = initial_prompt

if prompt:
    # Save user message
    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.spinner("AI is thinking..."):
        # Build SIMPLE history for google.genai
        history = [
            {
                "role": m["role"],
                "parts": [m["content"]]
            }
            for m in st.session_state.messages[:-1]
        ]

        reply = get_ai_explanation(prompt, history)

    # Save assistant response
    st.session_state.messages.append({
        "role": "assistant",
        "content": reply
    })

    st.rerun()

