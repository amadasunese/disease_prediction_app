from flask import Flask, render_template, request, jsonify
import numpy as np
import pickle

app = Flask(__name__, static_folder="static")

# Load the trained model and scaler
model = pickle.load(open("model/model.pkl", "rb"))
scaler = pickle.load(open("model/scaler.pkl", "rb"))

# Feature labels (corresponding to the input form and feature importance chart)
feature_labels = [
    "Age", "Sex", "Chest Pain Type", "Resting Blood Pressure", "Cholesterol",
    "Fasting Blood Sugar", "Resting ECG", "Max Heart Rate", "Exercise-Induced Angina",
    "ST Depression", "Slope", "Major Vessels", "Thalassemia"
]

# Home route
@app.route("/")
def index():
    return render_template("index.html", prediction_text="Awaiting input...", feature_contributions=[0] * len(feature_labels))


@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Extract input data from the form
        input_data = [
            float(request.form["age"]),
            int(request.form["sex"]),
            int(request.form["cp"]),
            float(request.form["trestbps"]),
            float(request.form["chol"]),
            int(request.form["fbs"]),
            int(request.form["restecg"]),
            float(request.form["thalach"]),
            int(request.form["exang"]),
            float(request.form["oldpeak"]),
            int(request.form["slope"]),
            int(request.form["ca"]),
            int(request.form["thal"])
        ]

        # Scale the input data
        scaled_data = scaler.transform([input_data])

        # Make prediction
        prediction = model.predict(scaled_data)[0]
        prediction_proba = model.predict_proba(scaled_data)[0]

        # Extract feature contributions
        if hasattr(model, "coef_"):
            feature_importance = np.abs(model.coef_).flatten()
        elif hasattr(model, "feature_importances_"):
            feature_importance = model.feature_importances_
        else:
            feature_importance = [0] * len(feature_labels)

        # Normalize feature contributions
        feature_contributions = (feature_importance / np.sum(feature_importance) * 100).round(2).tolist()

        # Create a dynamic explanation
        top_features = sorted(
            zip(feature_labels, feature_contributions), 
            key=lambda x: x[1], 
            reverse=True
        )[:3]  # Top 3 contributing features

        explanation_text = (
            f"The prediction is influenced mainly by {top_features[0][0]} ({top_features[0][1]}%), "
            f"{top_features[1][0]} ({top_features[1][1]}%), and {top_features[2][0]} ({top_features[2][1]}%). "
            "These features significantly contribute to the overall result."
        )

        # Generate recommendations
        if prediction == 1:  # Heart Disease
            recommendation_text = (
                "It is strongly recommended that you consult a cardiologist for further evaluation. "
                "Lifestyle changes, medications, or specific treatments may be required to address the condition."
            )
        else:  # No Heart Disease
            recommendation_text = (
                "The results indicate no signs of heart disease. Maintain a healthy lifestyle with regular exercise, "
                "a balanced diet, and routine check-ups to ensure long-term heart health."
            )

        # Prediction result
        prediction_text = (
            f"The model predicts: {'Heart Disease' if prediction == 1 else 'No Heart Disease'} "
            f"with a confidence of {max(prediction_proba) * 100:.2f}%."
        )

        # Render the template with results
        return render_template(
            "index.html", 
            prediction_text=prediction_text, 
            feature_contributions=feature_contributions, 
            explanation_text=explanation_text, 
            recommendation_text=recommendation_text
        )

    except Exception as e:
        return render_template(
            "index.html", 
            prediction_text="An error occurred during prediction.", 
            feature_contributions=[0] * len(feature_labels), 
            explanation_text="Unable to generate explanation due to an error.", 
            recommendation_text="No recommendations available."
        )



if __name__ == "__main__":
    app.run(debug=True)
