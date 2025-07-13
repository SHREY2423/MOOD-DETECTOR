import streamlit as st
from textblob import TextBlob
import random
import json

# ----------------- App Config -----------------
st.set_page_config(page_title="How Are You — Really?", layout="centered")
st.title("🧠 How Are You — Really?")
st.markdown("Let’s take a few moments to check in with your emotions.")

# ----------------- Load Joke & Quote Dataset -----------------
@st.cache_data
def load_jokes_quotes():
    with open("mood_jokes_quotes.json", "r") as f:
        data = json.load(f)
    return data

data = load_jokes_quotes()

# ----------------- Mood Analysis Function -----------------
def analyze_mood(text_list):
    total = 0
    for text in text_list:
        total += TextBlob(text).sentiment.polarity
    avg_sentiment = total / len(text_list)
    if avg_sentiment > 0.2:
        return "😊 Positive", "Positive"
    elif avg_sentiment < -0.2:
        return "😟 Negative", "Negative"
    else:
        return "😐 Neutral", "Neutral"

# ----------------- Session Setup -----------------
if "step" not in st.session_state:
    st.session_state.step = 1
    st.session_state.answers = []

# ----------------- Refined Questions -----------------
questions = [
    "1️⃣ How are you genuinely feeling today?",
    "2️⃣ Can you describe your current state of mind?",
    "3️⃣ What stood out most in your day?",
    "4️⃣ Is there something bothering or uplifting you recently?",
    "5️⃣ What would bring you peace or joy right now?"
]

# ----------------- Question & Answer Flow -----------------
if st.session_state.step <= len(questions):
    with st.form(key=f"form{st.session_state.step}"):
        answer = st.text_input(questions[st.session_state.step - 1])
        submitted = st.form_submit_button("Next")
        if submitted and answer:
            st.session_state.answers.append(answer)
            st.session_state.step += 1
else:
    # ------------- Mood Detection -------------
    mood_emoji, mood_label = analyze_mood(st.session_state.answers)
    st.success(f"### Your Mood: {mood_emoji} ({mood_label})")

    # ------------- Motivational Quote -------------
    quote = random.choice(data["quotes"][mood_label])
    st.markdown(f"#### 💬 Motivation for You:")
    st.info(f"“{quote}”")

    # ------------- Joke -------------
    joke = random.choice(data["jokes"][mood_label])
    st.markdown("#### 😂 Lighten Up With a Joke:")
    st.warning(joke)

    # ------------- Suggestions -------------
    st.markdown("#### 💡 What You Can Try:")
    suggestions = {
        "Positive": [
            "🎵 Listen to some feel-good music",
            "💪 Share your energy with others",
            "📝 Capture your thoughts in a journal"
        ],
        "Negative": [
            "🧘 Try 5 mins of deep breathing",
            "🎧 Listen to relaxing music",
            "🗣️ Talk to someone you trust"
        ],
        "Neutral": [
            "🚶 Take a short mindful walk",
            "📺 Watch a feel-good video",
            "☕ Take a mindful break"
        ]
    }
    for suggestion in suggestions[mood_label]:
        st.markdown(f"- {suggestion}")

    # ------------- Media Links -------------
    st.markdown("#### 🎶 Your Personalized Content:")
    if mood_label == "Positive":
        st.markdown("🎵 [Spotify – Feel Good Playlist](https://open.spotify.com/playlist/37i9dQZF1DX3rxVfibe1L0)")
        st.markdown("📺 [YouTube – Motivational Video](https://youtu.be/ZXsQAXx_ao0)")
    elif mood_label == "Negative":
        st.markdown("🎵 [Spotify – Calm Down Playlist](https://open.spotify.com/playlist/37i9dQZF1DWUvHZA1zLcjW)")
        st.markdown("📺 [YouTube – Relaxing Music](https://youtu.be/2OEL4P1Rz04)")
    else:
        st.markdown("🎵 [Spotify – Chill Vibes](https://open.spotify.com/playlist/37i9dQZF1DX4WYpdgoIcn6)")
        st.markdown("📺 [YouTube – Lo-fi Live](https://youtu.be/5qap5aO4i9A)")

    # ------------- Restart Button -------------
    if st.button("🔄 Start Over"):
        st.session_state.clear()

