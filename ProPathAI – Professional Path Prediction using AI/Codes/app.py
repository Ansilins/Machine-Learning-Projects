import streamlit as st
import pandas as pd
import joblib

# Load the trained model and feature columns
model = joblib.load("/Users/ansilin/Documents/my_works/edu_project_taiwan/model/career_predictor_model1.pkl")
feature_columns = joblib.load("/Users/ansilin/Documents/my_works/edu_project_taiwan/model/feature_columns1.pkl")

# Custom slider ranges
slider_ranges = {
    "Computer Architecture": (0.0, 6.0, 0),
    "Programming Skills": (0.0, 6.0, 0),
    "Project Management": (0.0, 6.0, 0),
    "Communication skills": (0.0, 6.0, 0),
    "Openness": (0.49, 1.0, 0),
    "Conscientousness": (0.0, 1.0, 0),
    "Extraversion": (0.0, 1.0, 0),
    "Agreeableness": (0.0, 1.0, 0),
    "Emotional_Range": (0.34, 1.0, 0),
    "Conversation": (0.0, 1.0, 0),
    "Openness to Change": (0.19, 1.0, 0),
    "Hedonism": (0.0, 1.0, 0),
    "Self-enhancement": (0.14, 1.0, 0),
    "Self-transcendence": (0.09, 1.0, 0)
}

# Page config
st.set_page_config(page_title="Career Path Predictor", layout="wide")

# Inject dark theme CSS
st.markdown("""
    <style>
        html, body, [class*="css"] {
            background-color: #1e1e1e !important;
            color: #f0f0f0 !important;
            font-family: 'Segoe UI', sans-serif;
        }
        .stSlider label, .stSidebar h2, .stSidebar h1 {
            color: #ffffff !important;
        }
        .stSidebar {
            background-color: #2c2c2c !important;
        }
        .stButton > button {
            background-color: #007acc;
            color: white;
            font-size: 18px;
            padding: 10px 24px;
            border-radius: 10px;
            border: none;
        }
        .stButton > button:hover {
            background-color: #005f99;
            color: #ffffff;
        }
        .stExpanderHeader {
            color: #ffffff !important;
        }
        .stDataFrame, .stTable {
            background-color: #2c2c2c !important;
        }
    </style>
""", unsafe_allow_html=True)

# App title
st.title("🌙 Career Path Predictor (Dark Mode)")
st.markdown("Input your profile through the sliders on the left to receive a career suggestion powered by machine learning.")

# Sidebar input
st.sidebar.header("📋 Your Profile")
user_input = {}
for feature in feature_columns:
    min_val, max_val, mean_val = slider_ranges.get(feature, (0, 10, 5))
    user_input[feature] = st.sidebar.slider(
        label=feature,
        min_value=float(min_val),
        max_value=float(max_val),
        value=float(mean_val),
        step=0.01
    )

# DataFrame for prediction
input_df = pd.DataFrame([user_input])
input_df = input_df.reindex(columns=feature_columns, fill_value=0)

# Prediction
if st.button("🔮 Predict Career Path"):
    prediction = model.predict(input_df)[0]
    st.success(f"✨ Suggested Career Path: **{prediction}**")

    with st.expander("📊 See Input Summary"):
        st.dataframe(input_df.style.format(precision=2))

# Footer
st.markdown("""
---
🧠 *This AI-based app analyzes your traits and academic background to predict your optimal career path.*
""")