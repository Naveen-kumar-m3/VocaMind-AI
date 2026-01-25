\# VocaMind-AI 



VocaMind-AI is a modular, voice-based AI system that converts human speech into intelligent responses and delivers them back as synthesized voice.  

This project is designed as the \*\*foundation for future mental health monitoring and support systems\*\*, combining speech recognition, conversational intelligence, and speech synthesis in a clean, extensible architecture.



---



\## 🚀 Project Overview



VocaMind-AI enables real-time interaction with an AI assistant using voice as the primary interface.



\*\*Core capabilities:\*\*

\- Capture live microphone input

\- Convert speech to text using a local ASR model

\- Generate intelligent responses through a pluggable LLM interface

\- Convert text responses back into speech

\- Modular design to support future ML-based mental state analysis



This repository currently implements \*\*Phase 1: Core Voice Pipeline\*\*.



---



\## 🧩 System Architecture (Phase 1)



User Voice

↓

Speech-to-Text (Whisper)

↓

Text Processing

↓

LLM / Response Engine

↓

Text-to-Speech (gTTS)

↓

AI Voice Output



yaml





The architecture is intentionally modular so that each component can be independently replaced or upgraded in later phases.



---



\## 🛠️ Tech Stack



\- \*\*Language:\*\* Python 3.11

\- \*\*Speech-to-Text:\*\* Faster-Whisper (local inference)

\- \*\*Text-to-Speech:\*\* gTTS

\- \*\*Audio Handling:\*\* sounddevice, scipy

\- \*\*LLM Interface:\*\* OpenAI API (pluggable, with fallback support)

\- \*\*Environment Management:\*\* python-dotenv

\- \*\*Version Control:\*\* Git \& GitHub



---



\## 📁 Project Structure



VocaMind-AI/

│

├── app/

│ ├── init.py

│ ├── main.py

│ └── services/

│ ├── init.py

│ ├── stt.py # Speech-to-Text logic

│ ├── tts.py # Text-to-Speech logic

│ └── llm.py # LLM / response engine

│

├── requirements.txt

├── README.md

└── .gitignore



yaml

Copy code



