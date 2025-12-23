import sounddevice as sd
from scipy.io.wavfile import write

from app.services.stt import SpeechToText
from app.services.tts import TextToSpeech
from app.services.llm import LLMService


SAMPLE_RATE = 44100
DURATION = 5  # seconds

def record_audio(filename="input.wav"):
    print("🎤 Speak now...")
    audio = sd.rec(int(DURATION * SAMPLE_RATE),
                   samplerate=SAMPLE_RATE,
                   channels=1)
    sd.wait()
    write(filename, SAMPLE_RATE, audio)
    print("✅ Recording finished")

def main():
    record_audio()

    stt = SpeechToText()
    tts = TextToSpeech()
    llm = LLMService()

    user_text = stt.transcribe("input.wav")
    print("📝 You said:", user_text)

    response = llm.generate_response(user_text)
    print("🤖 AI:", response)

    tts.speak(response)

if __name__ == "__main__":
    main()
