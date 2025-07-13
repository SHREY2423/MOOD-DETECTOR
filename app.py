import streamlit as st
from textblob import TextBlob
import random

# --------- Mood Data --------- #
mood_data = {
    "happy": {
        "quotes": [
            "Keep smiling, because life is a beautiful thing! 😊",
            "Happiness is contagious, spread it! 🌞"
        ],
        "jokes": [
            "Why don’t scientists trust atoms? Because they make up everything! 🤣",
            "Why did the scarecrow win an award? Because he was outstanding in his field! 🏆"
        ],
        "youtube": [
            "https://www.youtube.com/watch?v=ZbZSe6N_BXs",
            "https://www.youtube.com/watch?v=y6Sxv-sUYtM"
        ],
        "spotify": ["https://open.spotify.com/playlist/37i9dQZF1DXdPec7aLTmlC"],
        "gif": "https://media.giphy.com/media/yoJC2A59OCZHs1LXvW/giphy.gif"
    },
    "sad": {
        "quotes": [
            "It’s okay to not be okay. 💙",
            "Tough times never last, but tough people do 💪"
        ],
        "jokes": [
            "Why did the math book look sad? Because it had too many problems. 😢",
            "Why did the computer visit the therapist? Too many bytes of sadness. 🖥️"
        ],
        "youtube": [
            "https://www.youtube.com/watch?v=RB-RcX5DS5A",
            "https://www.youtube.com/watch?v=uelHwf8o7_U"
        ],
        "spotify": ["https://open.spotify.com/playlist/37i9dQZF1DX7qK8ma5wgG1"],
        "gif": "https://media.giphy.com/media/3oz8xKaR836UJOYeOc/giphy.gif"
    },
    "angry": {
        "quotes": [
            "Calm is a superpower. 🧘",
            "Breathe. It’s just a bad day, not a bad life. 🌪️"
        ],
        "jokes": [
            "I'm not arguing. I'm just explaining why I’m right! 😠",
            "Why don’t skeletons fight each other? They don’t have the guts. 💀"
        ],
        "youtube": [
            "https://www.youtube.com/watch?v=ZtLbnN00ZJI",
            "https://www.youtube.com/watch?v=U9BwWKXjVaI"
        ],
        "spotify": ["https://open.spotify.com/playlist/37i9dQZF1DX76Wlfdnj7AP"],
        "gif": "https://media.giphy.com/media/IThjAlJnD9WNO/giphy.gif"
    },
    "neutral": {
        "quotes": [
            "Stay grounded. Everything will fall into place. 🌱",
            "Just breathe, you’ve got this. 🌈"
        ],
        "jokes": [
            "Why can’t your nose be 12 inches long? Because then it would be a foot! 👃🤣",
            "What do you call cheese that isn't yours? Nacho cheese! 🧀"
        ],
        "youtube": [
            "https://www.youtube.com/watch?v=5qap5aO4i9A",
            "https://www.youtube.com/watch?v=hHW1oY26kxQ"
        ],
        "spotify": ["https://open.spotify.com/playlist/37i9dQZF1DX6VdMW310YC7"],
        "gif": "https://media.giphy.com/media/xT1R9ZzU4dU6lV1p7G/giphy.gif"
    }
}

questions = [
    "How are you feeling today in one word?",
    "What happened today that affected your mood?",
    "What's something on your mind right now?"
]

# --------- Initialize Session State Safely --------- #
if "q_index" not in st.session_state:
    st.session_state.q_index = 0

if "responses" not in st.session_state:
    st.session_state.responses = []

# --------- Mood Detection Function --------- #
def detect_mood(responses):
    total_polarity = sum(TextBlob(r).sentiment.polarity for r in responses)
    avg = total_polarity / len(responses)
    if avg > 0.2:
        return "happy"
    elif avg < -0.2:
        return "sad"
    elif -0.1 < avg < 0.1:
        return "neutral"
    else:
        return "angry"

# --------- UI --------- #
st.set_page_config(page_title="Mood Detector", layout="centered")
st.title("🎭 Conversational Mood Detector")
st.markdown("Answer these quick questions and I’ll detect your mood 🔍")

q_index = st.session_state.q_index

if q_index < len(questions):
    with st.form(key="mood_form"):
        response = st.text_input(questions[q_index], key=f"q{q_index}")
        submitted = st.form_submit_button("Next")
        if submitted and response.strip():
            st.session_state.responses.append(response)
            st.session_state.q_index += 1
            st.experimental_rerun()
else:
    mood = detect_mood(st.session_state.responses)
    info = mood_data[mood]

    st.balloons()
    st.image(info["gif"], caption=f"Detected mood: **{mood.upper()}** 🎯", use_column_width=True)
    st.success(f"🌟 Your mood is: **{mood.capitalize()}**")

    st.subheader("💬 Inspirational Quote")
    st.info(random.choice(info["quotes"]))

    st.subheader("🎧 Spotify Playlist")
    for link in info["spotify"]:
        st.markdown(f"[🎵 Open Playlist]({link})")

    st.subheader("📺 YouTube Video")
    st.video(random.choice(info["youtube"]))

    st.subheader("😂 Here's a joke for you:")
    st.write(random.choice(info["jokes"]))

    if st.button("🔁 Try Again"):
        st.session_state.q_index = 0
        st.session_state.responses = []
        st.experimental_rerun()
