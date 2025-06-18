import streamlit as st
from model import load_model_and_vectorizer

# Load model/vectorizer
model, vectorizer = load_model_and_vectorizer()

# Streamlit UI
st.title("📧 Spam Email Classifier")
input_text = st.text_area("Enter your email text")

if st.button("Classify"):
    if input_text.strip() == "":
        st.warning("Please enter a message.")
    else:
        transformed = vectorizer.transform([input_text])
        prediction = model.predict(transformed)[0]
        label = "🚫 Spam" if prediction == 1 else "✅ Not Spam"
        st.success(f"Prediction: {label}")
