import streamlit as st

st.set_page_config(
    page_title="A Deep Learning Approach to Brain Anomalies",
    layout="wide",
    initial_sidebar_state="auto",
    page_icon="🧠"
)

# --- Enhanced Light Theme & Animation CSS ---
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&display=swap');

        html, body, [class*="st-"] {
            font-family: 'Poppins', sans-serif;
            background: linear-gradient(135deg, #e0f7fa, #f1f8ff);
            color: #1b1b1b;
            overflow-x: hidden;
        }

        .stApp {
            background: linear-gradient(145deg, #ffffff, #dfe9f3);
        }

        /* Floating animation for sections */
        @keyframes floaty {
            0%, 100% { transform: translateY(0px); }
            50% { transform: translateY(-8px); }
        }

        /* Sidebar glass look */
        section[data-testid="stSidebar"] {
            background: rgba(255, 255, 255, 0.5) !important;
            backdrop-filter: blur(10px);
            -webkit-backdrop-filter: blur(10px);
            border-right: 1px solid rgba(255, 255, 255, 0.3);
            box-shadow: 2px 0 15px rgba(0,0,0,0.05);
        }

        /* Header */
        .main-header {
            text-align: center;
            font-weight: 800;
            font-size: 3.3em;
            background: linear-gradient(90deg, #2193b0, #6dd5ed);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 0.2em;
            letter-spacing: -0.4px;
            text-shadow: 1px 2px 4px rgba(0,0,0,0.1);
        }

        .subheader {
            text-align: center;
            color: #444;
            font-weight: 500;
            font-size: 1.2em;
            margin-bottom: 2.5em;
        }

        /* Feature cards */
        .st-container {
            background: rgba(255, 255, 255, 0.8);
            backdrop-filter: blur(14px);
            border-radius: 20px;
            padding: 28px;
            box-shadow: 0 10px 25px rgba(0,0,0,0.08);
            border: 1px solid rgba(255,255,255,0.5);
            text-align: center;
            transition: all 0.4s ease;
            position: relative;
            animation: floaty 5s ease-in-out infinite;
        }

        .st-container:hover {
            transform: translateY(-10px) scale(1.03);
            box-shadow: 0 15px 35px rgba(0,0,0,0.1);
        }

        .feature-title {
            font-weight: 700;
            color: #0b3954;
            font-size: 1.3em;
            margin-bottom: 12px;
        }

        .feature-description {
            color: #333;
            font-size: 0.95em;
            line-height: 1.5;
            margin-bottom: 20px;
        }

        /* Gradient buttons */
        .stButton>button {
            background: linear-gradient(120deg, #74ebd5, #ACB6E5);
            color: #fff;
            border: none;
            border-radius: 12px;
            font-weight: 600;
            padding: 12px 18px;
            transition: all 0.3s ease;
            width: 100%;
            box-shadow: 0 3px 10px rgba(0,0,0,0.1);
        }

        .stButton>button:hover {
            background: linear-gradient(120deg, #89f7fe, #66a6ff);
            box-shadow: 0 10px 20px rgba(102,166,255,0.3);
            transform: translateY(-4px);
        }

        .stButton>button:active {
            transform: scale(0.98);
        }

        /* Divider */
        hr {
            border: none;
            height: 1px;
            background: linear-gradient(to right, transparent, rgba(0,0,0,0.15), transparent);
            margin: 50px 0;
        }

        /* Subtle glow effect */
        .st-container::after {
            content: "";
            position: absolute;
            inset: 0;
            border-radius: 20px;
            background: radial-gradient(circle at top left, rgba(255,255,255,0.3), transparent 60%);
            opacity: 0;
            transition: opacity 0.3s ease;
        }

        .st-container:hover::after {
            opacity: 1;
        }
    </style>
""", unsafe_allow_html=True)


# --- Homepage Content ---
st.markdown("<h1 class='main-header'>A Deep Learning Approach to Brain Anomalies</h1>", unsafe_allow_html=True)
st.markdown("<h3 class='subheader'>Empowering medical insights through intelligent neural analysis 🧠</h3>", unsafe_allow_html=True)

st.markdown("---")

# Grid layout for features
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("<div class='st-container'>", unsafe_allow_html=True)
    st.markdown("<h4 class='feature-title'>Brain Anomaly Detector</h4>", unsafe_allow_html=True)
    if st.button("🧩 Get Started", key="detector"):
        st.switch_page("pages/1_Brain_Anomaly_Detector.py")
    st.markdown("<p class='feature-description'>Analyze brain MRI images to detect tumors and anomalies with precision. Get AI-driven visual explanations and reports.</p>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.markdown("<div class='st-container'>", unsafe_allow_html=True)
    st.markdown("<h4 class='feature-title'>YuvaAI Assistant</h4>", unsafe_allow_html=True)
    if st.button("💬 Chat with AI", key="yuvaai"):
        st.switch_page("pages/2_Med AI.py")
    st.markdown("<p class='feature-description'>Ask YuvaAI about your reports or symptoms — get natural explanations, advice, and personalized recommendations.</p>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

with col3:
    st.markdown("<div class='st-container'>", unsafe_allow_html=True)
    st.markdown("<h4 class='feature-title'>Medical Knowledge Hub</h4>", unsafe_allow_html=True)
    if st.button("📘 Learn More", key="knowledge"):
        st.switch_page("pages/3_Medical_Knowledge_Library.py")
    st.markdown("<p class='feature-description'>Explore a curated knowledge base of brain tumour details explained in simple language.</p>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)
