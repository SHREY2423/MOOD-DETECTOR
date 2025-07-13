import streamlit as st
from textblob import TextBlob
import random
import time
import base64

# ------------------- Mood Content Data ------------------- #
mood_data = {
    "happy": {
        "quotes": [
            "Keep smiling, because life is a beautiful thing!",
            "Happiness is contagious, spread it everywhere 😄"
        ],
        "jokes": [
            "Why don’t scientists trust atoms? Because they make up everything! 🤣",
            "Why did the scarecrow win an award? Because he was outstanding in his field! 🌾"
        ],
        "youtube": [
            "https://www.youtube.com/watch?v=ZbZSe6N_BXs",  # Happy - Pharrell Williams
            "https://www.youtube.com/watch?v=y6Sxv-sUYtM"   # Uptown Funk
        ],
        "spotify": [
            "https://open.spotify.com/playlist/37i9dQZF1DXdPec7aLTmlC"
        ],
        "gif": "https://media.giphy.com/media/yoJC2A59OCZHs1LXvW/giphy.gif"
    },
    "sad": {
        "quotes": [
            "It’s okay to not be okay 💙",
            "Tough times never last, but tough people do 💪"
        ],
        "jokes": [
            "Why did the computer visit the therapist? It had too many bytes of sadness. 😢",
            "Why did the math book look sad? Because it had too many problems. 📘"
        ],
        "youtube": [
            "https://www.youtube.com/watch?v=RB-RcX5DS5A",  # Fix You - Coldplay
            "https://www.youtube.com/watch?v=uelHwf8o7_U"   # Love the Way You Lie
        ],
        "spotify": [
            "https://open.spotify.com/playlist/37i9dQZF1DX7qK8ma5wgG1"
        ],
        "gif": "https://media.giphy.com/media/3oz8xKaR836UJOYeOc/giphy.gif"
    },
    "angry": {
        "quotes": [
            "Calm is a superpower. 😤🧘‍♂️",
            "Breathe. It's just a bad day, not a bad life. 🌪️"
        ],
        "jokes": [
            "I'm not arguing, I'm just explaining why I'm right! 😡",
            "Why did the skeleton stay calm? Nothing gets under his skin. 🦴"
        ],
        "youtube": [
            "https://www.youtube.com/watch?v=ZtLbnN00ZJI",  # Angry music
            "https://www.youtube.com/watch?v=U9BwWKXjVaI"   # Pump up
        ],
        "spotify": [
            "https://open.spotify.com/playlist/37i9dQZF1DX76Wlfdnj7AP"
        ],
        "gif": "https://media.giphy.com/media/IThjAlJnD9WNO/giphy.gif"
    },
    "neutral": {
        "quotes": [
            "Stay grounded. Everything will fall into place. 🌱",
            "Just breathe, you’ve got this. 🌈"
        ],
        "jokes": [
            "Why can’t your nose be 12 inches long? Because then it would be a foot! 🤓",
            "What do you call cheese that isn't yours? Nacho cheese! 🧀"
        ],
        "youtube": [
            "https://www.youtube.com/watch?v=5qap5aO4i9A",  # Lofi chill
            "https://www.youtube.com/watch?v=hHW1oY26kxQ"   # Relax beats
        ],
        "spotify": [
            "https://open.spotify.com/playlist/37i9dQZF1DX6VdMW310YC7"
        ],
        "gif": "https://media.giphy.com/media/xT1R9ZzU4dU6lV1p7G/giphy.gif"
    }
}

# ------------------- Mood Detection Logic ------------------- #
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

# ------------------- Streamlit UI ------------------- #
st.set_page_config(page_title="Mood Detector", layout="centered")
st.markdown("""
    <style>
    .question-box input {
        font-size: 18px !important;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🎭 Conversational Mood Detector")
st.markdown("Answer these questions and we'll understand your mood better!")

questions = [
    "How are you feeling in one word?",
    "What happened today that impacted your mood?",
    "What’s something currently on your mind?"
]

responses = []
current_question = st.session_state.get("q_index", 0)

if current_question < len(questions):
    st.subheader(f"Question {current_question + 1}:")
    answer = st.text_input(questions[current_question], key=f"q{current_question}")

    if answer:
        responses = st.session_state.get("responses", [])
        responses.append(answer)
        st.session_state.responses = responses
        st.session_state.q_index = current_question + 1
        st.experimental_rerun()

elif "responses" in st.session_state:
    final_mood = detect_mood(st.session_state.responses)
    mood_info = mood_data[final_mood]

    st.balloons()
    st.image(mood_info["gif"], caption=f"Detected mood: {final_mood.capitalize()} 🎭")

    st.success(f"🌟 Your mood is: {final_mood.capitalize()}")

    st.subheader("💡 Quote")
    st.info(random.choice(mood_info["quotes"]))

    st.subheader("🎧 Spotify Playlist")
    for link in mood_info["spotify"]:
        st.markdown(f"[Open Playlist 🎵]({link})")

    st.subheader("📺 YouTube Recommendation")
    yt_link = random.choice(mood_info["youtube"])
    st.video(yt_link)

    st.subheader("😂 Joke to lighten your mood")
    st.write(random.choice(mood_info["jokes"]))

    if st.button("🔄 Restart"):
        st.session_state.q_index = 0
        st.session_state.responses = []
        st.experimental_rerun()
