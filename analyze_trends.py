from collections import Counter
from datetime import datetime

LOG_FILE = "logs/session_log.txt"


def parse_log():
    states = []
    timestamps = []

    with open(LOG_FILE, "r", encoding="utf-8") as f:
        for line in f:
            try:
                parts = line.strip().split(" | ")
                timestamp = datetime.strptime(parts[0], "%Y-%m-%d %H:%M:%S")
                state = parts[2].split(": ")[1]

                timestamps.append(timestamp)
                states.append(state)
            except Exception:
                continue

    return timestamps, states


def analyze_trends(states):
    counter = Counter(states)

    print("\n🧠 Mental State Summary")
    print("----------------------")
    for state, count in counter.items():
        print(f"{state.upper():10} : {count}")

    most_common = counter.most_common(1)[0]
    print(f"\n📊 Most frequent state: {most_common[0].upper()} ({most_common[1]} times)")


def analyze_recent_trend(timestamps, states):
    if len(states) < 2:
        print("\n⚠️ Not enough data for trend analysis")
        return

    print("\n📈 Recent Trend Analysis")
    print("------------------------")

    recent_states = states[-5:]  # last 5 sessions
    counter = Counter(recent_states)

    for state, count in counter.items():
        print(f"Last sessions → {state.upper()} : {count}")

    dominant = counter.most_common(1)[0][0]
    print(f"\n🔍 Dominant recent state: {dominant.upper()}")


if __name__ == "__main__":
    timestamps, states = parse_log()
    analyze_trends(states)
    analyze_recent_trend(timestamps, states)
