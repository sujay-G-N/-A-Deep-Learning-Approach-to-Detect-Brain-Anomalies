# ===============================
# Brain Anomaly Detector – Clean Refactor
# UI / THEME: UNCHANGED
# Gemini Integration: NEW SDK (google-genai)
# ===============================

# ---------- Core Imports ----------
import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
from io import BytesIO
import pandas as pd
import plotly.express as px
import tempfile
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import google.generativeai as genai


# ---------- NEW Gemini SDK ----------
from google import genai

# ---------- Page Config ----------
st.set_page_config(
    page_title="Brain Anomaly Detector",
    layout="wide",
    initial_sidebar_state="expanded",
    page_icon="🧠"
)

# ---------- Configure Gemini (v1 SDK) ----------
client = genai.Client(api_key=st.secrets["API_KEY"])

# ---------- Custom CSS (UNCHANGED) ----------
st.markdown(""" 
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&display=swap');

html, body, [class*="st-"] {
    font-family: 'Poppins', sans-serif;
    background: linear-gradient(125deg, #f7fbff, #eef5ff, #e0f7fa, #f1f8ff);
    background-size: 400% 400%;
    animation: flow 15s ease infinite;
    color: #1e293b;
}

/* animated gradient background */
@keyframes flow {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

/* Sidebar - floating glass look */
section[data-testid="stSidebar"] {
    background: rgba(255, 255, 255, 0.55);
    border-right: 1px solid rgba(180,200,255,0.35);
    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);
    box-shadow: 6px 0 25px rgba(173, 216, 230, 0.35);
}

/* Glowing main header */
.main-header {
    text-align: center;
    font-weight: 700;
    font-size: 3em;
    letter-spacing: 0.6px;
    background: linear-gradient(90deg, #007BFF, #00B7FF, #00E5FF);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    animation: glowPulse 3.5s ease-in-out infinite alternate;
    text-shadow: 0 0 20px rgba(0, 183, 255, 0.4);
}
@keyframes glowPulse {
    0% { text-shadow: 0 0 10px rgba(0,183,255,0.3); }
    50% { text-shadow: 0 0 25px rgba(0,183,255,0.8); }
    100% { text-shadow: 0 0 10px rgba(0,183,255,0.3); }
}

.subheader {
    color: #334155;
    text-align: center;
    font-size: 1.25em;
    font-weight: 500;
    margin-top: -10px;
    margin-bottom: 1.5em;
}

/* Content container – breathing card */
.st-emotion-cache-1cypcdb {
    background: rgba(255,255,255,0.75);
    backdrop-filter: blur(18px);
    border-radius: 20px;
    box-shadow: 0 4px 25px rgba(0,150,255,0.15);
    padding: 30px;
    animation: breathe 6s ease-in-out infinite;
    border: 1px solid rgba(180,200,255,0.4);
}
@keyframes breathe {
    0%, 100% { transform: scale(1); box-shadow: 0 4px 25px rgba(0,150,255,0.15); }
    50% { transform: scale(1.02); box-shadow: 0 8px 40px rgba(0,150,255,0.3); }
}

/* Upload container */
.upload-container {
    border: 2px dashed rgba(0,150,255,0.4);
    border-radius: 18px;
    padding: 2em;
    background: rgba(240, 248, 255, 0.5);
    transition: all 0.4s ease;
    text-align: center;
}
.upload-container:hover {
    border-color: rgba(0,150,255,0.8);
    box-shadow: 0 0 25px rgba(0,150,255,0.3);
    transform: scale(1.03);
}

/* Buttons - interactive pulse */
.stButton>button {
    background: linear-gradient(135deg, #00B4D8, #48CAE4);
    color: white;
    border-radius: 12px;
    padding: 12px 28px;
    font-weight: 600;
    font-size: 1.05em;
    border: none;
    box-shadow: 0 0 15px rgba(0,180,255,0.4);
    transition: all 0.35s ease;
    animation: softPulse 4s infinite ease-in-out;
}
@keyframes softPulse {
    0%, 100% { box-shadow: 0 0 15px rgba(0,180,255,0.4); }
    50% { box-shadow: 0 0 35px rgba(0,180,255,0.7); }
}
.stButton>button:hover {
    transform: translateY(-3px) scale(1.03);
    background: linear-gradient(135deg, #0096c7, #48cae4);
    box-shadow: 0 0 40px rgba(0,180,255,0.8);
}
.stButton>button:active {
    transform: scale(0.98);
}

/* Info and result boxes */
.success-box, .warning-box, .info-box {
    border-radius: 14px;
    padding: 16px;
    font-weight: 500;
    text-align: center;
    box-shadow: 0 0 20px rgba(0,150,255,0.15);
    margin-bottom: 12px;
    animation: floatUp 6s ease-in-out infinite;
}
@keyframes floatUp {
    0%,100% { transform: translateY(0px); }
    50% { transform: translateY(-4px); }
}

.success-box {
    background: linear-gradient(135deg, #d1f7d6, #a7f3d0);
    color: #065f46;
}
.warning-box {
    background: linear-gradient(135deg, #fff5d6, #fde68a);
    color: #92400e;
}
.info-box {
    background: linear-gradient(135deg, #e0f2fe, #bfdbfe);
    color: #1e3a8a;
}

/* Charts glow */
.js-plotly-plot .plotly .modebar {
    background: transparent !important;
}
svg.main-svg {
    filter: drop-shadow(0 0 8px rgba(0,150,255,0.3));
}

/* Divider */
hr {
    border: none;
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(0,150,255,0.4), transparent);
    margin: 2em 0;
}

/* Smooth transitions globally */
* {
    transition: all 0.25s ease-in-out;
}
</style>
""", unsafe_allow_html=True)

# ---------- Session State ----------
if "page" not in st.session_state:
    st.session_state.page = "home"

# ---------- Load Model ----------
@st.cache_resource
def load_model():
    try:
        return tf.keras.models.load_model("brain_model.keras")
    except Exception:
        st.error("brain_model.keras not found")
        return None

# ---------- Image Preprocessing ----------
def preprocess_image(image_bytes):
    img = Image.open(BytesIO(image_bytes)).convert("RGB").resize((128, 128))
    return np.expand_dims(np.array(img), axis=0) / 255.0

# ---------- Gemini Vision Validation (FIXED) ----------
def is_mri_brain_image_gemini(image_bytes):
    image = Image.open(BytesIO(image_bytes))

    response = client.models.generate_content(
        model="gemini-2.5-flash-lite",
        contents=[
            image,
            "Is this a brain MRI scan image? Answer only yes or no."
        ]
    )

    return response.text.strip().lower().startswith("y")

# ---------- Gemini Medical Explanation (FIXED) ----------
def get_ai_explanation(query):
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=query,
            config={
                "system_instruction": (
                    "You are a medical assistant. Provide clear, non-technical explanations. "
                    "Always include this disclaimer: "
                    "'Disclaimer: This is for informational purposes only and not a substitute for professional medical advice.'"
                )
            }
        )
        return response.text
    except Exception:
        return "AI explanation unavailable at the moment."

# ---------- UI Page ----------
def home_page():
    st.markdown("<h1 class='main-header'>Brain Anomaly Detector</h1>", unsafe_allow_html=True)
    st.markdown("<h3 class='subheader'>Upload a brain MRI image</h3>", unsafe_allow_html=True)

    col1, col2 = st.columns([1, 2])

    with col1:
        uploaded_file = st.file_uploader("Upload Image", type=["png", "jpg", "jpeg"])

        if uploaded_file:
            image_bytes = uploaded_file.read()
            st.image(image_bytes, use_container_width=True)

            st.info("Validating image using AI...")
            if not is_mri_brain_image_gemini(image_bytes):
                st.error("Not a valid brain MRI")
                return
            st.success("Valid brain MRI detected")

    with col2:
        if uploaded_file:
            model = load_model()
            if model:
                img = preprocess_image(image_bytes)
                preds = model.predict(img)[0]

                labels = ["Glioma", "Meningioma", "Normal", "Pituitary"]
                idx = np.argmax(preds)
                label = labels[idx]

                if label == "Normal":
                    st.markdown("<div class='success-box'>No Tumor Detected</div>", unsafe_allow_html=True)
                else:
                    st.markdown(f"<div class='warning-box'>{label} Tumor Detected</div>", unsafe_allow_html=True)

                df = pd.DataFrame({"Category": labels, "Confidence": preds})
                fig = px.pie(df, values="Confidence", names="Category", hole=0.4)
                st.plotly_chart(fig, use_container_width=True)

                st.markdown("---")
                st.header("Yuva AI Report")

                query = f"Explain {label} tumor, medication, next steps, and consultant type"
                explanation = get_ai_explanation(query)
                st.markdown(explanation)

                st.markdown("---")
                st.header("Generate Patient Report")

                with st.form("report_form"):
                    name = st.text_input("Patient Name")
                    age = st.number_input("Age", 1, 120)
                    gender = st.selectbox("Gender", ["Male", "Female", "Other"])
                    submitted = st.form_submit_button("Generate PDF")

                if submitted and name:
                    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as f:
                        pdf_path = f.name

                    c = canvas.Canvas(pdf_path, pagesize=A4)
                    c.setFont("Helvetica-Bold", 18)
                    c.drawString(50, 800, "AI Brain Anomaly Report")
                    c.setFont("Helvetica", 12)
                    c.drawString(50, 770, f"Patient: {name}, Age: {age}, Gender: {gender}")
                    c.drawString(50, 740, f"Prediction: {label}")

                    text = c.beginText(50, 710)
                    for line in explanation.split("\n"):
                        text.textLine(line)
                    c.drawText(text)
                    c.save()

                    with open(pdf_path, "rb") as f:
                        st.download_button(
                            "Download PDF",
                            f,
                            file_name=f"{name}_report.pdf"
                        )

# ---------- Run ----------
if st.session_state.page == "home":
    home_page()
