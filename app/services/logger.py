from datetime import datetime


def log_session(text, state, confidence):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    log_entry = (
        f"{timestamp} | "
        f"Text: {text} | "
        f"State: {state} | "
        f"Confidence: {confidence:.2f}\n"
    )

    with open("logs/session_log.txt", "a", encoding="utf-8") as f:
        f.write(log_entry)
