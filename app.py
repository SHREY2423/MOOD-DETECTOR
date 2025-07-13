import streamlit as st
from textblob import TextBlob
import random

# -------------------- Mood Data -------------------- #
mood_data = {
    "happy": {
        "quotes": [
            "Keep smiling, because life is a beautiful thing! 😊",
            "Happiness is contagious, spread it! 🌞",
            "Every moment is a fresh beginning. ✨",
        ],
        "jokes": [
            "Why don’t scientists trust atoms? Because they make up everything! 🤣",
            "Why did the scarecrow win an award? Because he was outstanding in his field! 🏆"
        ],
        "youtube": [
            "https://www.youtube.com/watch?v=ZbZSe6N_BXs",
            "https://www.youtube.com/watch?v=60ItHLz5WEA",
            "https://www.youtube.com/watch?v=3GwjfUFyY6M"
        ],
        "spotify": ["https://open.spotify.com/playlist/37i9dQZF1DXdPec7aLTmlC"],
        "gif": "https://media.giphy.com/media/yoJC2A59OCZHs1LXvW/giphy.gif"
    },
    "sad": {
        "quotes": [
            "It’s okay to not be okay. 💙",
            "Tough times never last, but tough people do 💪",
            "Stars can’t shine without darkness. 🌌",
        ],
        "jokes": [
            "Why did the math book look sad? Because it had too many problems. 😢",
            "Why did the computer visit the therapist? Too many bytes of sadness. 🖥️"
        ],
        "youtube": [
            "https://www.youtube.com/watch?v=uelHwf8o7_U",
            "https://www.youtube.com/watch?v=RB-RcX5DS5A",
            "https://www.youtube.com/watch?v=2vjPBrBU-TM"
        ],
        "spotify": ["https://open.spotify.com/playlist/37i9dQZF1DX7qK8ma5wgG1"],
        "gif": "https://media.giphy.com/media/3oz8xKaR836UJOYeOc/giphy.gif"
    },
    "angry": {
        "quotes": [
            "Calm is a superpower. 🧘",
            "Breathe. It’s just a bad day, not a bad life. 🌪️",
            "Let your smile change the world. 😤"
        ],
        "jokes": [
            "Why don’t skeletons fight each other? They don’t have the guts. 💀",
            "I'm not arguing, I'm just passionately expressing my rightness 😤"
        ],
        "youtube": [
            "https://www.youtube.com/watch?v=ZtLbnN00ZJI",
            "https://www.youtube.com/watch?v=U9BwWKXjVaI",
            "https://www.youtube.com/watch?v=kXYiU_JCYtU"
        ],
        "spotify": ["https://open.spotify.com/playlist/37i9dQZF1DX76Wlfdnj7AP"],
        "gif": "https://media.giphy.com/media/IThjAlJnD9WNO/giphy.gif"
    },
    "neutral": {
        "quotes": [
            "Stay grounded. Everything will fall into place. 🌱",
            "Just breathe, you’ve got this. 🌈",
            "Progress is progress, no matter how small. 🚶"
        ],
        "jokes": [
            "Why can’t your nose be 12 inches long? Because then it would be a foot! 👃🤣",
            "What do you call cheese that isn't yours? Nacho cheese! 🧀"
        ],
        "youtube": [
            "https://www.youtube.com/watch?v=hHW1oY26kxQ",
            "https://www.youtube.com/watch?v=5qap5aO4i9A",
            "https://www.youtube.com/watch?v=V1Pl8CzNzCw"
        ],
        "spotify": ["https://open.spotify.com/playlist/37i9dQZF1DX6VdMW310YC7"],
        "gif": "https://media.giphy.com/media/xT1R9ZzU4dU6lV1p7G/giphy.gif"
    }
}

questions = [
    "How are you feeling today in one word?",
    "What happened today that affected your mood?",
    "What's something on your mind right now?",
    "How do you feel physically and mentally right now?",
    "If you could change one thing about your day, what would it be?"
]

# ------------------ Setup Session ------------------ #
if "q_index" not in st.session_state:
    st.session_state.q_index = 0
if "responses" not in st.session_state:
    st.session_state.responses = []
if "user_input" not in st.session_state:
    st.session_state.user_input = ""

# ------------------ Advance Question ------------------ #
def advance():
    if st.session_state.user_input.strip():
        st.session_state.responses.append(st.session_state.user_input.strip())
        st.session_state.q_index += 1
        st.session_state.user_input = ""

# ------------------ Mood Detection (Improved) ------------------ #
def detect_mood(texts):
    polarity = sum(TextBlob(t).sentiment.polarity for t in texts) / len(texts)
    if polarity >= 0.2:
        return "happy"
    elif polarity <= -0.2:
        return "sad"
    elif -0.2 < polarity < 0.2:
        return "neutral"
    else:
        return "angry"

# ------------------ UI Setup ------------------ #
st.set_page_config(page_title="AI Mood Detector 😄", layout="centered")
st.markdown("<h1 style='text-align: center;'>🧠 Conversational Mood Detector</h1>", unsafe_allow_html=True)
st.markdown("Answer a few questions below to let us detect your mood and suggest things for you.")

# ------------------ Q&A Section ------------------ #
q_index = st.session_state.q_index

if q_index < len(questions):
    st.subheader(f"Q{q_index + 1}: {questions[q_index]}")
    st.text_input(
        label="",
        key="user_input",
        on_change=advance,
        placeholder="Type your response and hit Enter..."
    )
else:
    mood = detect_mood(st.session_state.responses)
    data = mood_data[mood]

    # ------------------ Final Result ------------------ #
    st.balloons()
    st.success(f"🎯 Your mood is: **{mood.capitalize()}**")
    st.image(data["gif"], use_container_width=True)

    st.subheader("💬 Motivational Quotes")
    for quote in random.sample(data["quotes"], 2):
        st.info(quote)

    st.subheader("🎧 Spotify Playlist")
    for link in data["spotify"]:
        st.markdown(f"[▶️ Open Playlist on Spotify]({link})")

    st.subheader("📺 YouTube Videos for You")
    for link in random.sample(data["youtube"], 2):
        st.markdown(f"[🎬 Watch Video]({link})")

    st.subheader("😂 Here's a joke:")
    st.write(random.choice(data["jokes"]))

    if st.button("🔁 Start Again"):
        st.session_state.q_index = 0
        st.session_state.responses = []
        st.session_state.user_input = ""
        st.experimental_rerun()

