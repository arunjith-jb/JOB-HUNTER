import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import pickle
import os


DATA_PATH = "data/resume_training_data.csv"
MODELS_DIR = "models"
CLASSIFIER_PATH = os.path.join(MODELS_DIR, "resume_classifier.pkl")
VECTORIZER_PATH = os.path.join(MODELS_DIR, "resume_vectorizer.pkl")

os.makedirs(MODELS_DIR, exist_ok=True)

df = pd.read_csv(DATA_PATH)

X_text = df["text"].astype(str)
y = df["label"].astype(int)

vectorizer = TfidfVectorizer(stop_words="english", max_features=5000)
X = vectorizer.fit_transform(X_text)

clf = LogisticRegression(max_iter=1000)
clf.fit(X, y)

with open(CLASSIFIER_PATH, "wb") as f:
    pickle.dump(clf, f)

with open(VECTORIZER_PATH, "wb") as f:
    pickle.dump(vectorizer, f)

print("Model and vectorizer saved to 'models/'")
