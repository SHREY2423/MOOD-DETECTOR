import streamlit as st
from transformers import pipeline
from deepface import DeepFace
from textblob import TextBlob
import random
import webbrowser
import base64

# ------------------ Setup ------------------

# Load HuggingFace GoEmotions model
emotion_classifier = pipeline("text-classification", model="bhadresh-savani/bert-base-go-emotion", return_all_scores=True)

# Jokes and quotes database
mood_data = {
    "joy": {
        "joke": "Why don’t scientists trust atoms? Because they make up everything!",
        "quote": "Happiness is not by chance, but by choice.",
        "gif": "https://media.giphy.com/media/5GoVLqeAOo6PK/giphy.gif",
        "spotify": "https://open.spotify.com/playlist/37i9dQZF1DXdPec7aLTmlC",
        "youtube": "https://www.youtube.com/watch?v=d-diB65scQU"
    },
    "sadness": {
        "joke": "Why did the teddy bear say no to dessert? Because he was already stuffed.",
        "quote": "Tears come from the heart and not from the brain.",
        "gif": "https://media.giphy.com/media/d2lcHJTG5Tscg/giphy.gif",
        "spotify": "https://open.spotify.com/playlist/37i9dQZF1DWVV27DiNWxkR",
        "youtube": "https://www.youtube.com/watch?v=hoNb6HuNmU0"
    },
    "anger": {
        "joke": "Why did the volcano get promoted? Because it was on fire!",
        "quote": "For every minute you remain angry, you give up sixty seconds of peace of mind.",
        "gif": "https://media.giphy.com/media/l3V0j3ytFyGHqiV7W/giphy.gif",
        "spotify": "https://open.spotify.com/playlist/37i9dQZF1DX59NCqCqJtoH",
        "youtube": "https://www.youtube.com/watch?v=QwZT7T-TXT0"
    },
    "neutral": {
        "joke": "I used to play piano by ear, but now I use my hands.",
        "quote": "Life is 10% what happens to us and 90% how we react to it.",
        "gif": "https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif",
        "spotify": "https://open.spotify.com/playlist/37i9dQZF1DWUzFXarNiofw",
        "youtube": "https://www.youtube.com/watch?v=VYOjWnS4cMY"
    },
    "fear": {
        "joke": "Why don’t ghosts like rain? It dampens their spirits.",
        "quote": "Do the thing you fear and the death of fear is certain.",
        "gif": "https://media.giphy.com/media/l1J3preURPiwjRPvG/giphy.gif",
        "spotify": "https://open.spotify.com/playlist/37i9dQZF1DWZqd5JICZI0u",
        "youtube": "https://www.youtube.com/watch?v=wT5Ms3n5RBU"
    }
}

# ------------------ Helper Functions ------------------

def get_goemotions_sentiment(text):
    result = emotion_classifier(text)[0]
    top_emotion = max(result, key=lambda x: x['score'])['label']
    return top_emotion

def get_textblob_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity > 0.2:
        return "joy"
    elif polarity < -0.2:
        return "sadness"
    else:
        return "neutral"

def predict_facial_emotion():
    try:
        analysis = DeepFace.analyze(img_path=0, actions=['emotion'], enforce_detection=False)
        dominant_emotion = analysis[0]['dominant_emotion']
        return dominant_emotion
    except Exception as e:
        return "neutral"

def map_emotion(label):
    label = label.lower()
    if "happy" in label or "joy" in label:
        return "joy"
    elif "sad" in label or "depress" in label:
        return "sadness"
    elif "angry" in label or "anger" in label:
        return "anger"
    elif "fear" in label or "scared" in label:
        return "fear"
    else:
        return "neutral"

# ------------------ Streamlit App ------------------

st.set_page_config(page_title="🧠 Conversational Mood Detector", layout="centered")

st.title("🧠 Conversational Mood Detector")
st.write("Let's talk and understand how you're feeling today 😊")

user_responses = []
questions = [
    "1️⃣ How are you feeling right now in one word?",
    "2️⃣ What’s something that happened today?",
    "3️⃣ What’s on your mind lately?",
    "4️⃣ How was your sleep last night?",
    "5️⃣ What are you looking forward to?"
]

for question in questions:
    answer = st.text_input(question, key=question)
    if answer:
        user_responses.append(answer)

if st.button("🎯 Detect Mood"):
    all_text = " ".join(user_responses)
    go_emotion = map_emotion(get_goemotions_sentiment(all_text))
    blob_emotion = get_textblob_sentiment(all_text)
    face_emotion_raw = predict_facial_emotion()
    face_emotion = map_emotion(face_emotion_raw)

    final_mood = max(
        [go_emotion, blob_emotion, face_emotion],
        key=[go_emotion, blob_emotion, face_emotion].count
    )

    data = mood_data.get(final_mood, mood_data["neutral"])
    
    st.subheader(f"🧠 Detected Mood: `{final_mood.upper()}`")
    st.image(data["gif"], caption="Here's how your mood looks 😄")
    st.write(f"**🎵 Music Suggestion:** [Spotify Playlist]({data['spotify']})")
    st.write(f"**📺 YouTube Video:** [Watch Video]({data['youtube']})")
    st.write(f"**💬 Quote:** _{data['quote']}_")
    st.write(f"**🤣 Joke:** {data['joke']}")
