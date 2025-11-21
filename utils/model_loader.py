import pickle


def load_resume_vectorizer(path: str = "models/resume_vectorizer.pkl"):
    with open(path, "rb") as f:
        return pickle.load(f)


def load_resume_classifier(path: str = "models/resume_classifier.pkl"):
    with open(path, "rb") as f:
        return pickle.load(f)
