## 🧠 Code Overview

This project includes three core Python scripts:

### 📊 `EDA.py`
- Performs **Exploratory Data Analysis** on the input dataset.
- Analyzes distribution, correlations, and outliers among the features.
- Useful for understanding feature importance and overall data quality before training.

### 🌲 `RandomForest.py`
- Trains a **Random Forest Classifier** using the processed dataset.
- Saves the trained model (`career_predictor_model1.pkl`) and the list of feature columns (`feature_columns1.pkl`) using `joblib`.
- Includes performance metrics like training/test accuracy and classification reports.

### 🌐 `app.py`
- The **Streamlit web application** for predicting career paths.
- Loads the saved model and feature columns.
- Collects user inputs via sliders and predicts the most suitable career path.
- Offers an interactive and user-friendly interface.
