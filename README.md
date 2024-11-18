# Heart Disease Prediction and Early Diagnosis Model


## Table of Contents
1. [Introduction](#introduction)
2. [Dataset](#dataset)
3. [Model Development](#model-development)
4. [Features of the application for the model deployment](#features-of-the-application-for-the-model-deployment)
5. [Features of the user interface](#features-of-the-user-interface)
6. [Tech Stack](#tech-stack)
7. [Authors](authors)

---
## Introduction
This project demonstrates the development and deployment of a machine learning model to predict the likelihood of heart disease based on patient data. The application provides insights into feature contributions and suggests actions based on the prediction result.

Heart disease remains one of the leading causes of mortality worldwide. Early detection and intervention significantly improve patient outcomes and reduce healthcare costs. This Heart Disease Prediction and Early Diagnosis Model plays a crucial role in achieving these goals by leveraging machine learning and data analysis to identify individuals at high risk of heart disease.

---

## Dataset
The model was trained on the [Kaggle Heart Disease dataset](https://www.kaggle.com/datasets/arezaei81/heartcsv), containing health records with the following features:
1. age: Age of the patient.
2. sex: Sex (1 = male, 0 = female).
3. cp: Chest pain type (categorical: 0, 1, 2, 3).
4. trestbps: Resting blood pressure (in mm Hg).
5. chol: Serum cholesterol (in mg/dl).
6. fbs: Fasting blood sugar > 120 mg/dl (1 = true; 0 = false).
7. restecg: Resting electrocardiographic results (categorical: 0, 1, 2).
8. thalach: Maximum heart rate achieved.
9. exang: Exercise-induced angina (1 = yes; 0 = no).
10. oldpeak: ST depression induced by exercise relative to rest.
11. slope: Slope of the peak exercise ST segment.
12. ca: Number of major vessels (0-3) colored by fluoroscopy.
13. thal: Thalassemia (categorical: 0, 1, 2, 3).

---

## Model Development
1. **Preprocessing**:
   - Handling missing values.
   - Scaling features using `StandardScaler`.
2. **Training**:
   - Model trained using Logistic Regression for classification.
   - Cross-validation performed to ensure robustness.
3. **Evaluation**:
   - Metrics used: Accuracy, Precision, Recall, F1-Score.
   - Achieved high accuracy (>85%) on test data.

---

## Features of the application for the model deployment
The **Heart Disease Prediction Application** uses a machine learning model to assess patient health parameters and predict the likelihood of heart disease. This Flask-based web application includes:
- An intuitive user interface for entering patient data.
- Detailed predictions with feature contribution analysis using chart.
- Suggested recommendations for consultation or lifestyle improvements.

---

## Features of the user interface
1. **Input Form**: Accepts multiple health parameters, such as age, cholesterol level, and blood pressure.
2. **Prediction Results**:
   - Displays whether heart disease is likely.
   - Shows a chart of feature contributions to the prediction.
3. **Recommendations**: 
   - Provides tailored actions and advice based on the prediction.
4. **Autoplay Video**: Features an engaging animated heartbeat video on the homepage.

---

## Tech Stack
- **Machine Learning**: Scikit-learn
- **Visualization**: Matplotlib
- **Frontend**: HTML5, CSS3, Bootstrap
- **Backend**: Flask (Python)

---


## Authors/Team


