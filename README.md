# 📧 Spam Classifier App

A machine learning-powered web app that detects whether an email message is **Spam** or **Not Spam** using **Natural Language Processing (NLP)** and a **Naïve Bayes classifier**.

Built with:
- Python 🐍
- scikit-learn 🔍
- NLTK 🧠
- Streamlit 🌐
- Google Drive (for model storage via `gdown`)

---

## ✨ Features

- 📥 Classify raw email text as spam or ham (not spam)
- 🔠 Text preprocessing using stemming, stopwords removal, and TF-IDF
- 🤖 Trained using a Multinomial Naïve Bayes classifier
- ☁️ Loads model and vectorizer from Google Drive
- 📊 Visualizes performance metrics (accuracy, confusion matrix, etc.)

---

## 🚀 How to Run the App

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/spam-classifier.git
cd spam-classifier
