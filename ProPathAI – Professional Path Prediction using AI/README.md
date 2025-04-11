# 🎓 Career Path Prediction App

## Web Application

This project is a **web application** designed to help individuals predict their most suitable career path based on their academic performance, technical skills, and personality traits. The application utilizes a machine learning model to suggest career paths based on a user’s profile. Built using **Streamlit**, this interactive app provides an engaging user interface where users can enter their data and get predictions instantly.

---

## Project Overview

The **Career Path Prediction App** predicts the most suitable career path for individuals by analyzing multiple factors such as **academic performance**, **technical skills**, and **personality traits**. The app uses a **Random Forest** model trained on a dataset containing these attributes. Users provide inputs through interactive sliders, and the app generates career path suggestions accordingly.

### Features:
- **Input Data**: Users can input academic scores, coding skills, communication skills, personality traits, and more using sliders.
- **Prediction Model**: The app uses a **Random Forest Classifier** model for predicting career paths based on user input.
- **Interactive Interface**: The interface is intuitive, with sliders and buttons that make the app user-friendly.

---

## Project Description

The **Career Path Prediction App** helps individuals make informed decisions regarding their career choices. By analyzing various features such as GPA, coding skills, personality traits, and more, the app suggests the most suitable career options. It can be particularly useful for students, professionals, and career counselors to explore career paths based on measurable personal data.

The app’s user-friendly interface allows users to enter their data and receive career path recommendations, all in real-time. By leveraging machine learning, it provides a tailored approach to career advice.

---

## Motivation

The motivation behind this project is to provide a **data-driven, personalized career recommendation system**. Choosing the right career path can be overwhelming, and this app simplifies that decision-making process by relying on machine learning techniques. It enables users to explore various career options based on their unique profiles and characteristics, making career guidance more accessible and accurate.

---

## Machine Learning Methods Used

The project uses the **Random Forest Classifier**, a robust ensemble learning algorithm, to predict the best career path for the user based on input features. The model works well for multiclass classification tasks and handles both categorical and continuous data efficiently.

Key components of the machine learning pipeline:
1. **Random Forest Classifier**: Trained on historical data, it learns patterns in the relationships between academic performance, skills, and career outcomes.
2. **Model Evaluation**: The model's performance is evaluated using accuracy and classification metrics like precision, recall, and F1-score.

---

## Data Preprocessing

Before training the model, the dataset was preprocessed to ensure that the data is clean, standardized, and ready for modeling.

Key preprocessing steps:
1. **Data Cleaning**: Missing values were handled by imputation or removal, ensuring that the data fed to the model is complete and accurate.
2. **Normalization/Standardization**: Features like GPA, coding skills, and personality traits were normalized to bring them to a comparable scale, enhancing model performance.
3. **Feature Engineering**: New features were created based on domain knowledge, which helped in improving the predictive power of the model.

---

## Model Training

The **Random Forest Classifier** was trained using a diverse set of features like GPA, coding skills, personality traits, and soft skills. The dataset was split into training and test sets to evaluate the model's performance.

Key steps in model training:
1. **Splitting the Dataset**: The data was split into training and testing subsets to evaluate the model’s ability to generalize to unseen data.
2. **Model Tuning**: Hyperparameters such as the number of trees (`n_estimators`) and random state were tuned to optimize model performance.
3. **Model Evaluation**: Accuracy, precision, recall, and F1-score were calculated to assess model performance on both the training and testing sets.

---

## Conclusion

The **Career Path Prediction App** provides a simple yet powerful tool for predicting career paths based on personal data. By leveraging machine learning, it offers users personalized career suggestions and helps them make data-informed decisions. The app is built using **Streamlit** for the frontend and **scikit-learn** for machine learning, making it easy to deploy and interact with.

Moving forward, the app can be improved by expanding the dataset, exploring more sophisticated models, and adding features like saving and tracking predictions over time.

---

## Contact

If you have any questions, suggestions, or feedback regarding this project, feel free to reach out to me:

- **Email**: [ansilinkumarai@gmail.com](mailto:ansilinkumarai.com)
- **GitHub**: [ansilins]([https://github.com/your-username](https://github.com/Ansilins))
- **LinkedIn**: [Ansilin Kumar](https://www.linkedin.com/in/ansilin-kumar/)

---

Feel free to contribute to this project or report issues via the GitHub issues section. I appreciate your interest in the **Career Path Prediction App**!
