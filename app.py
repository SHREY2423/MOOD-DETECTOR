import streamlit as st
from textblob import TextBlob
import random

# ------------------ Mood Data ------------------ #
mood_data = {
    "joyful": {
        "quotes": [
            "Joy is the simplest form of gratitude 🌈",
            "Live life to the fullest and make every moment count! 🎉",
            "Let your joy be in your journey, not in some distant goal. 🚀",
            "The most wasted of all days is one without laughter. 😂",
            "Be happy for this moment. This moment is your life. 💫",
            "Today is a perfect day to be joyful. ✨",
            "Joy multiplies when it is shared. 🤗",
            "Surround yourself with those who make you smile. 😊",
            "The best way to cheer yourself is to try to cheer someone else up. 💖",
            "Joy is power. Shine your light. 💡",
            "Smile more. Laugh louder. Live longer. 🥰",
            "Every day brings new opportunities for joy. 🌞",
            "A joyful heart is the inevitable result of a heart burning with love. ❤️",
            "Joy is not in things; it is in us. 🌺",
            "Happiness held is the seed; happiness shared is the flower. 🌸",
            "Dance like no one is watching. 💃",
            "Keep looking up… that's the secret of life. 🌤",
            "Let joy be your compass. 🧭",
            "There is always something to be joyful about. 🌈",
            "Joy is a net of love by which you can catch souls. 🎣"
        ],
        "jokes": [
            "Why do bees have sticky hair? Because they use honeycombs! 🐝",
            "What do you call a singing computer? A Dell! 🎤",
            "Why don’t eggs tell jokes? They’d crack each other up! 🥚",
            "How do you organize a space party? You planet. 🌌",
            "Why did the golfer bring two pairs of pants? In case he got a hole in one! ⛳",
            "Why did the bicycle fall over? It was two-tired! 🚲",
            "Why don’t skeletons fight each other? They don’t have the guts. 💀",
            "I used to play piano by ear, now I use my hands. 🎹",
            "What lights up a soccer stadium? A soccer match! ⚽",
            "How does a penguin build its house? Igloos it together! 🐧"
        ],
        "youtube": [
            "https://www.youtube.com/watch?v=3GwjfUFyY6M",
            "https://www.youtube.com/watch?v=ZbZSe6N_BXs",
            "https://www.youtube.com/watch?v=UtF6Jej8yb4"
        ],
        "spotify": [
            "https://open.spotify.com/playlist/37i9dQZF1DXdPec7aLTmlC",
            "https://open.spotify.com/playlist/1k0FIJ5x6HOXIXnpLMOfjq"
        ],
        "gifs": [
            "https://media.giphy.com/media/l0MYt5jPR6QX5pnqM/giphy.gif",
            "https://media.giphy.com/media/MDJ9IbxxvDUQM/giphy.gif",
            "https://media.giphy.com/media/fxsqOYnIMEefC/giphy.gif",
            "https://media.giphy.com/media/26xBMuLMjJnwz5sve/giphy.gif",
            "https://media.giphy.com/media/3oKIPtjElfqwMOTbH2/giphy.gif"
        ]
    },
    # More mood types like "happy", "sad", "neutral", etc., will follow same structure
}

# ------------------ Questions ------------------ #
questions = [
    "How are you feeling right now, in one word?",
    "Can you share what made you feel this way today?",
    "What’s on your mind right now?",
    "Describe your mental and physical energy levels today.",
    "If one thing could go differently today, what would it be?"
]

# ------------------ Session State ------------------ #
if "q_index" not in st.session_state:
    st.session_state.q_index = 0
if "responses" not in st.session_state:
    st.session_state.responses = []
if "user_input" not in st.session_state:
    st.session_state.user_input = ""

# ------------------ Functions ------------------ #
def advance():
    if st.session_state.user_input.strip():
        st.session_state.responses.append(st.session_state.user_input.strip())
        st.session_state.q_index += 1
        st.session_state.user_input = ""

def detect_mood(texts):
    combined_text = " ".join(texts).lower()
    depression_keywords = [
        "depressed", "hopeless", "suicidal", "empty", "worthless",
        "pointless", "dark", "numb", "burned out", "i hate myself", "give up",
        "kill me", "over", "quit"
    ]
    if any(kw in combined_text for kw in depression_keywords):
        return "depressed"

    polarity = sum(TextBlob(t).sentiment.polarity for t in texts) / len(texts)

    if polarity >= 0.5:
        return "joyful"
    elif 0.2 <= polarity < 0.5:
        return "happy"
    elif -0.2 < polarity < 0.2:
        return "neutral"
    elif -0.6 < polarity <= -0.2:
        return "sad"
    else:
        return "depressed"

# ------------------ UI ------------------ #
st.set_page_config(page_title="AI Mood Detector 😄", layout="centered")
st.markdown("""
    <div style='text-align: center;'>
        <h1>🧠 Conversational Mood Detector</h1>
        <img src='https://media.giphy.com/media/3o6gE5aYpGk2kNI5Ww/giphy.gif' width='200'>
        <p style='font-size:18px;'>Let's talk and discover how you're truly feeling 😊</p>
    </div>
""", unsafe_allow_html=True)

q_index = st.session_state.q_index
if q_index < len(questions):
    st.subheader(f"Q{q_index + 1}: {questions[q_index]}")
    st.text_input("", key="user_input", on_change=advance, placeholder="Type and press Enter...")
    st.markdown("<hr><div style='text-align:center;'>🤖 Mood Detector is listening...</div>", unsafe_allow_html=True)
else:
    mood = detect_mood(st.session_state.responses)
    data = mood_data.get(mood, mood_data["neutral"])

    st.balloons()
    st.success(f"🎯 Your mood is: *{mood.upper()}*")
    st.image(random.choice(data["gifs"]), use_container_width=True)

    st.subheader("💬 Motivational Quotes")
    for quote in random.sample(data["quotes"], min(3, len(data["quotes"]))):
        st.info(quote)

    st.subheader("🎧 Spotify Playlist")
    for link in data["spotify"]:
        st.markdown(f"[▶ Play on Spotify]({link})")

    st.subheader("📺 YouTube Videos")
    for link in data["youtube"]:
        st.markdown(f"[🎬 Watch Now]({link})")

    st.subheader("😂 A joke to lighten the mood")
    st.write(random.choice(data["jokes"]))

    if st.button("🔁 Start Over"):
        st.session_state.q_index = 0
        st.session_state.responses = []
        st.session_state.user_input = ""
        st.experimental_rerun()
