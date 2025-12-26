import pickle
import re
import numpy as np


class MentalStateAnalyzer:
    def __init__(self):
        with open("models/mental_state_model.pkl", "rb") as f:
            self.vectorizer, self.model = pickle.load(f)

    def preprocess(self, text: str) -> str:
        text = text.lower()
        text = re.sub(r"[^a-z\s]", "", text)
        return text

    def predict_state_with_confidence(self, text: str):
        """
        Returns:
        - predicted_state (str)
        - confidence (float between 0 and 1)
        """
        text = self.preprocess(text)
        vector = self.vectorizer.transform([text])

        probabilities = self.model.predict_proba(vector)[0]
        max_index = int(np.argmax(probabilities))

        predicted_state = self.model.classes_[max_index]
        confidence = probabilities[max_index]

        return predicted_state, confidence
