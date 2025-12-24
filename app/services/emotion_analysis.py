import re

class MentalStateAnalyzer:
    """
    Simple rule-based + ML-ready mental state analyzer.
    This acts as Phase-2 intelligence layer.
    """

    def preprocess(self, text: str) -> str:
        text = text.lower()
        text = re.sub(r"[^a-z\s]", "", text)
        return text

    def predict_state(self, text: str) -> str:
        """
        Returns one of:
        - 'neutral'
        - 'stressed'
        - 'anxious'
        """

        text = self.preprocess(text)

        stress_keywords = [
            "tired", "pressure", "overwhelmed", "stress", "busy", "burnout"
        ]

        anxiety_keywords = [
            "worried", "anxious", "fear", "panic", "nervous", "scared"
        ]

        for word in anxiety_keywords:
            if word in text:
                return "anxious"

        for word in stress_keywords:
            if word in text:
                return "stressed"

        return "neutral"
