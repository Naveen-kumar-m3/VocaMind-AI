import sounddevice as sd
from scipy.io.wavfile import write

from app.services.stt import SpeechToText
from app.services.tts import TextToSpeech
from app.services.emotion_analysis import MentalStateAnalyzer
from app.services.logger import log_session

SAMPLE_RATE = 44100
DURATION = 5  # seconds


def record_audio(filename="input.wav"):
    print("🎤 Speak now...")
    audio = sd.rec(
        int(DURATION * SAMPLE_RATE),
        samplerate=SAMPLE_RATE,
        channels=1
    )
    sd.wait()
    write(filename, SAMPLE_RATE, audio)
    print("✅ Recording finished")


def main():
    # Initialize services
    stt = SpeechToText()
    tts = TextToSpeech()
    analyzer = MentalStateAnalyzer()

    # Record audio
    record_audio()

    # Speech-to-text
    user_text = stt.transcribe("input.wav")
    print("📝 You said:", user_text)

    # ================================
    # 🔥 PREDICTION + RESPONSE LOGIC
    # ================================
    state, confidence = analyzer.predict_state_with_confidence(user_text)

    print(f"🧠 Detected Mental State: {state.upper()}")
    print(f"📊 Confidence Score: {confidence:.2f}")

    # Log session
    log_session(user_text, state, confidence)

    if state == "stressed":
        response = (
            "It sounds like you are feeling stressed. "
            "Try taking a deep breath and slowing down for a moment. "
            "You are doing your best."
        )

    elif state == "anxious":
        response = (
            "I sense some anxiety in what you said. "
            "Focus on your breathing and remind yourself that this feeling will pass. "
            "You are not alone."
        )

    else:
        response = (
            "I hear you. Would you like to tell me more about "
            "what’s on your mind?"
        )

    print("🤖 AI Response:", response)

    # Text-to-speech
    tts.speak(response)


if __name__ == "__main__":
    main()
