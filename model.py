import gdown
import joblib
import os

# ✅ Google Drive File IDs
MODEL_ID = '1p0gcDsDnr6RtZoSdgL53l-Q1Wd4upFTq'
VECTORIZER_ID = '137JCsbcrylRvwDXc6MJ-YSFdiZnSxqcM'

# Local file names
MODEL_PATH = 'spam_model.pkl'
VECTORIZER_PATH = 'vectorizer.pkl'

def download_file(file_id, output_path):
    if not os.path.exists(output_path):
        url = f'https://drive.google.com/uc?id={file_id}'
        print(f"Downloading {output_path}...")
        gdown.download(url, output_path, quiet=False)
    else:
        print(f"{output_path} already exists. Skipping download.")

def load_model_and_vectorizer():
    # Download files if not already present
    download_file(MODEL_ID, MODEL_PATH)
    download_file(VECTORIZER_ID, VECTORIZER_PATH)

    # Load with joblib
    model = joblib.load(MODEL_PATH)
    vectorizer = joblib.load(VECTORIZER_PATH)

    return model, vectorizer

