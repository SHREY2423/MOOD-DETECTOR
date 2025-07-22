import streamlit as st
from textblob import TextBlob
import random
import base64

# ------------------------- App Config ---------------------------
st.set_page_config(page_title="Conversational Mood Detector 😊", layout="centered")

# ------------------------- Styling ---------------------------
st.markdown("""
    <style>
        body {
            background: linear-gradient(to right, #e0f7fa, #ffffff);
            font-family: 'Segoe UI', sans-serif;
        }
        .title {
            font-size: 3em;
            font-weight: bold;
            color: #4a90e2;
            text-align: center;
        }
        .subtitle {
            font-size: 1.5em;
            text-align: center;
            margin-top: -15px;
            color: #00796b;
        }
        .box {
            background-color: #ffffffaa;
            padding: 2em;
            border-radius: 20px;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
            margin-top: 2em;
        }
        .gif-bg {
            background-image: url('https://media.giphy.com/media/3oEduSbSGpGaRX2Vri/giphy.gif');
            background-size: 150px;
            background-repeat: no-repeat;
            background-position: right bottom;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
    <div class='title'>🧠 Conversational Mood Detector</div>
    <div class='subtitle'>Let's talk and discover how you're truly feeling 😊</div>
""", unsafe_allow_html=True)

# ---------------------- Mood Data ---------------------------
questions = [
    "How are you feeling right now in one word?",
    "What kind of day are you having?",
    "Do you want to talk to someone today?",
    "What’s one thing on your mind?",
    "Are you feeling more positive or negative lately?"
]

keywords = {
    "depressed": ["depressed", "hopeless", "worthless", "suicidal"],
    "sad": ["sad", "down", "unhappy", "lonely"],
    "happy": ["happy", "great", "awesome", "fantastic", "joyful", "good"],
    "neutral": ["fine", "okay", "normal", "meh", "neutral"]
}

quotes = {
    "depressed": [
        "This too shall pass. Keep going. 💪",
        "You’re not alone, and your feelings are valid. ❤️",
        "Sometimes just holding on is the bravest thing."
    ],
    "sad": [
        "Crying isn’t a sign of weakness. It’s a sign of being human.",
        "Pain is temporary. Better days are coming. 🌈",
        "It’s okay to not be okay."
    ],
    "happy": [
        "Happiness looks good on you! 😄",
        "Spread the joy. The world needs it. 🌍",
        "Keep smiling — it suits you!"
    ],
    "neutral": [
        "Sometimes, neutral is peaceful. ☁️",
        "Every day doesn’t need to be exciting to be meaningful.",
        "Peace of mind is priceless."
    ]
}

gifs = {
    "happy": ["https://media.giphy.com/media/111ebonMs90YLu/giphy.gif"],
    "sad": ["https://media.giphy.com/media/d2lcHJTG5Tscg/giphy.gif"],
    "depressed": ["https://media.giphy.com/media/YUg5jjO2TmnOE/giphy.gif"],
    "neutral": ["https://media.giphy.com/media/l0MYEqEzwMWFCg8rm/giphy.gif"]
}

jokes = {
    "happy": ["Why don’t scientists trust atoms? Because they make up everything!"],
    "sad": ["Why did the scarecrow win an award? Because he was outstanding in his field!"],
    "depressed": ["Why don’t skeletons fight each other? They don’t have the guts."],
    "neutral": ["Why can’t your nose be 12 inches long? Because then it would be a foot!"]
}

# ----------------------- State ----------------------------
if "step" not in st.session_state:
    st.session_state.step = 0
if "answers" not in st.session_state:
    st.session_state.answers = []

# ----------------------- Interaction ----------------------------
st.markdown("<div class='box gif-bg'>", unsafe_allow_html=True)
st.markdown(f"**{questions[st.session_state.step]}**")
answer = st.text_input("Your answer:", key=f"input_{st.session_state.step}")
submit = st.button("Next")

if submit and answer:
    st.session_state.answers.append(answer)
    st.session_state.step += 1
    st.experimental_rerun()

st.markdown("</div>", unsafe_allow_html=True)

# ------------------- Mood Detection -------------------------
def detect_mood(answers):
    mood_score = {"happy": 0, "sad": 0, "depressed": 0, "neutral": 0}
    for text in answers:
        blob = TextBlob(text)
        polarity = blob.sentiment.polarity
        if polarity >= 0.4:
            mood_score["happy"] += 1
        elif polarity <= -0.4:
            mood_score["depressed"] += 1
        elif polarity < 0:
            mood_score["sad"] += 1
        else:
            mood_score["neutral"] += 1

        for mood, words in keywords.items():
            if any(word in text.lower() for word in words):
                mood_score[mood] += 2
    return max(mood_score, key=mood_score.get)

# ---------------------- Final Output --------------------------
if st.session_state.step >= len(questions):
    mood = detect_mood(st.session_state.answers)
    st.balloons()
    st.image(random.choice(gifs[mood]), use_column_width=True)
    st.markdown(f"### 😄 Your mood seems to be: **{mood.upper()}**")
    st.markdown(f"> _{random.choice(quotes[mood])}_")
    st.success(random.choice(jokes[mood]))
    st.stop()

