import pandas as pd
import pickle
import re

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression


def preprocess(text):
    text = text.lower()
    text = re.sub(r"[^a-z\s]", "", text)
    return text


# Load dataset
data = pd.read_csv("data/mental_state_data.csv")
data["text"] = data["text"].apply(preprocess)

X = data["text"]
y = data["label"]

# Vectorization
vectorizer = TfidfVectorizer()
X_vec = vectorizer.fit_transform(X)

# Train model
model = LogisticRegression()
model.fit(X_vec, y)

# Save model
with open("models/mental_state_model.pkl", "wb") as f:
    pickle.dump((vectorizer, model), f)

print("✅ Mental state ML model trained and saved successfully")
