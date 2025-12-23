from gtts import gTTS
import os
import winsound

class TextToSpeech:
    def speak(self, text: str):
        filename = "response.wav"

        tts = gTTS(text=text, lang="en")
        tts.save("response.mp3")

        # Convert mp3 to wav (Windows supports wav)
        os.system("ffmpeg -y -i response.mp3 response.wav > nul 2>&1")

        winsound.PlaySound(filename, winsound.SND_FILENAME)

        os.remove("response.mp3")
        os.remove("response.wav")
