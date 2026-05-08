import streamlit as st
import json

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Medical Knowledge Library",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --- CUSTOM CSS ---
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');

        /* 🌤️ Global Style */
        html, body, [class*="st-"] {
            font-family: 'Inter', sans-serif;
            background: linear-gradient(135deg, #f0f9ff, #e0f7fa, #fefefe);
            color: #1a1a1a;
            overflow-x: hidden;
            transition: all 0.3s ease-in-out;
        }

        /* Main App Container */
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
            margin-bottom: 0.2em;
            letter-spacing: -0.3px;
            text-shadow: 1px 2px 4px rgba(0,0,0,0.15);
            animation: fadeIn 1.2s ease-in-out;
        }

        .subheader {
            text-align: center;
            color: #333;
            font-weight: 500;
            font-size: 1.15em;
            margin-bottom: 2.5em;
            opacity: 0.9;
            animation: fadeIn 1.8s ease-in-out;
        }

        /* 🌬️ Smooth fade animation */
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0); }
        }

        /* Sidebar (Glass look) */
        section[data-testid="stSidebar"] {
            background: rgba(255, 255, 255, 0.5) !important;
            backdrop-filter: blur(10px);
            -webkit-backdrop-filter: blur(10px);
            border-right: 1px solid rgba(255, 255, 255, 0.3);
            box-shadow: 2px 0 15px rgba(0,0,0,0.05);
        }

        /* Floating cards */
        .st-container {
            background: rgba(255, 255, 255, 0.9);
            backdrop-filter: blur(12px);
            border-radius: 18px;
            padding: 25px;
            margin-bottom: 24px;
            box-shadow: 0 8px 24px rgba(0,0,0,0.1);
            transition: all 0.3s ease-in-out;
            animation: floaty 6s ease-in-out infinite;
        }

        .st-container:hover {
            transform: translateY(-8px) scale(1.02);
            box-shadow: 0 12px 30px rgba(0,0,0,0.15);
        }

        /* Gentle floating animation */
        @keyframes floaty {
            0%, 100% { transform: translateY(0); }
            50% { transform: translateY(-6px); }
        }

        /* Titles inside container */
        .condition-title {
            color: #0b3954;
            font-weight: 700;
            font-size: 1.25em;
            margin-bottom: 10px;
        }

        /* Descriptions */
        .condition-description {
            color: #1f2937;
            font-size: 1em;
            line-height: 1.55;
        }

        /* Input box with shadow */
        .stTextInput input {
            border-radius: 10px !important;
            border: 1.8px solid #60a5fa !important;
            background-color: #f9fafb !important;
            padding: 12px 18px !important;
            font-size: 1rem;
            color: #111827 !important;
            box-shadow: 0 4px 14px rgba(0, 0, 0, 0.15);
            transition: all 0.3s ease;
        }

        .stTextInput input:focus {
            border-color: #3b82f6 !important;
            box-shadow: 0 6px 20px rgba(59, 130, 246, 0.25);
            transform: translateY(-2px);
            outline: none !important;
        }

        /* Divider */
        hr {
            border: none;
            height: 1px;
            background: linear-gradient(to right, transparent, rgba(0,0,0,0.1), transparent);
            margin: 40px 0;
        }
    </style>

""", unsafe_allow_html=True)


# --- PAGE HEADER ---
st.markdown("<h1 class='main-header'>Medical Knowledge Library</h1>", unsafe_allow_html=True)
st.markdown("<h3 class='subheader'>Browse through key brain-related conditions and get simple, clear explanations.</h3>", unsafe_allow_html=True)

st.markdown("---")

# --- SAMPLE MEDICAL CONDITIONS (You can expand this list later) ---
conditions = [
    {
        "name": "Brain Tumor",
        "description": "An abnormal growth of cells inside the brain. Symptoms include headaches, vision problems, seizures, and nausea. Treatment can involve surgery, radiation, or chemotherapy depending on the type and size."
    },
    {
        "name": "pituitary",
        "description": "pituitary tumours, which are abnormal growths in the pituitary gland—a pea-sized gland located at the base of the brain. These tumours can affect hormone production and cause a wide range of symptoms depending on their type and size."
    },
    {
        "name": "meningioma",
        "description": "meningiomas, which are tumors that arise from the meninges, the protective layers surrounding the brain and spinal cord. These tumors are usually slow-growing and often benign, but their location can lead to serious symptoms depending on what they press against."
    },
    {
        "name": "glioma",
        "description": "gliomas, which are tumors that originate from glial cells in the brain or spinal cord. These cells normally support and protect neurons, but when they grow uncontrollably, they can form tumors that vary in aggressiveness."
    }
]

# --- SEARCH FEATURE ---
search_query = st.text_input("🔎 Search for a condition...", placeholder="Type a condition name...")

filtered_conditions = [c for c in conditions if search_query.lower() in c["name"].lower()] if search_query else conditions

# --- DISPLAY RESULTS ---
if filtered_conditions:
    for condition in filtered_conditions:
        st.markdown("<div class='st-container'>", unsafe_allow_html=True)
        st.markdown(f"<p class='condition-title'>{condition['name']}</p>", unsafe_allow_html=True)
        st.markdown(f"<p class='condition-description'>{condition['description']}</p>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
else:
    st.info("No matching conditions found. Try a different search term.")
