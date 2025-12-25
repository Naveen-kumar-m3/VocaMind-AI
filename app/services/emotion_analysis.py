import pickle
import re


class MentalStateAnalyzer:
    def __init__(self):
        with open("models/mental_state_model.pkl", "rb") as f:
            self.vectorizer, self.model = pickle.load(f)

    def preprocess(self, text):
        text = text.lower()
        text = re.sub(r"[^a-z\s]", "", text)
        return text

    def predict_state(self, text):
        text = self.preprocess(text)
        vector = self.vectorizer.transform([text])
        prediction = self.model.predict(vector)[0]
        return prediction
