# app.py

import streamlit as st
from textblob import TextBlob
import random
import time

st.set_page_config(page_title="🧠 Conversational Mood Detector", layout="centered")

# ------------------ Data Setup ------------------ #

mood_keywords = {
    "joyful": ["happy", "joyful", "excited", "great", "amazing", "fantastic"],
    "sad": ["sad", "unhappy", "crying", "lonely", "upset"],
    "depressed": ["depressed", "suicidal", "kill myself", "end it", "tired of life", "hopeless", "give up", "quit", "over"],
    "neutral": ["okay", "fine", "neutral", "meh", "normal"]
}

def detect_mood(text):
    text = text.lower()
    for mood, keywords in mood_keywords.items():
        for keyword in keywords:
            if keyword in text:
                return mood
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity > 0.3:
        return "joyful"
    elif polarity < -0.3:
        return "sad"
    else:
        return "neutral"

mood_data = {
    "joyful": {
        "quotes": [
            "Happiness is not by chance, but by choice.",
            "The best way to cheer yourself is to try to cheer someone else up.",
            "Joy is the simplest form of gratitude.",
            "Happiness is only real when shared.",
            "Do more of what makes you happy!",
            "Be happy for this moment. This moment is your life.",
            "Stay close to anything that makes you glad you are alive.",
            "Let your smile change the world.",
            "The purpose of our lives is to be happy.",
            "Choose happiness every day.",
            "Smile – it increases your face value!",
            "A joyful heart is the inevitable result of a heart burning with love.",
            "Joy is a net of love by which you can catch souls.",
            "Joy does not simply happen to us. We have to choose joy.",
            "Happiness radiates like the fragrance from a flower.",
            "Joy multiplies when it is shared among friends.",
            "Find joy in the journey.",
            "Your joy can be the source of your smile.",
            "Happiness is contagious. Be a carrier!",
            "Laugh loud. Smile big. Love much.",
        ],
        "jokes": [
            "Why don’t scientists trust atoms? Because they make up everything!",
            "Why did the scarecrow win an award? Because he was outstanding in his field!",
            "Why don't skeletons fight each other? They don't have the guts.",
            "What do you call fake spaghetti? An impasta!",
            "Why did the bicycle fall over? It was two-tired!",
            "Parallel lines have so much in common. It’s a shame they’ll never meet.",
            "What do you get when you cross a snowman and a vampire? Frostbite.",
            "Why don’t oysters share their pearls? Because they’re shellfish!",
            "Why couldn’t the leopard play hide and seek? Because he was always spotted.",
            "What did one wall say to the other wall? I'll meet you at the corner!"
        ],
        "gifs": [
            "https://media.giphy.com/media/l0HlBO7eyXzSZkJri/giphy.gif",
            "https://media.giphy.com/media/xUPGcuOMYwAFYhLZgk/giphy.gif",
            "https://media.giphy.com/media/3o7abB06u9bNzA8lu8/giphy.gif",
            "https://media.giphy.com/media/l0MYt5jPR6QX5pnqM/giphy.gif",
            "https://media.giphy.com/media/26n6WywJyh39n1pBu/giphy.gif"
        ],
        "spotify": [
            "https://open.spotify.com/playlist/37i9dQZF1DX3rxVfibe1L0",
            "https://open.spotify.com/playlist/37i9dQZF1DXdPec7aLTmlC",
        ],
        "youtube": [
            "https://www.youtube.com/watch?v=ZbZSe6N_BXs",
            "https://www.youtube.com/watch?v=y6Sxv-sUYtM",
        ]
    },
    "sad": {
        "quotes": ["This too shall pass.", "Sadness flies away on the wings of time."]
    },
    "depressed": {
        "quotes": ["You’re not alone. Things will get better.", "Even the darkest night will end and the sun will rise."]
    },
    "neutral": {
        "quotes": ["Every day is a fresh start.", "Stay present and stay grounded."]
    }
}

# ------------------ App UI ------------------ #

st.title("🧠 Conversational Mood Detector")
st.markdown("Let's talk and discover how you're truly feeling 😊")

if "question_index" not in st.session_state:
    st.session_state.question_index = 0
    st.session_state.answers = []
    st.session_state.questions = [
        "How are you feeling right now in one word?",
        "What made you feel that way today?",
        "How would you describe your day in 3 words?",
        "Do you feel like talking to someone today?",
        "What’s one thing you’re grateful for?"
    ]

def display_question():
    q = st.session_state.questions[st.session_state.question_index]
    answer = st.text_input(q, key=f"q_{st.session_state.question_index}")
    if answer:
        st.session_state.answers.append(answer)
        st.session_state.question_index += 1
        time.sleep(0.3)
        st.experimental_rerun()

if st.session_state.question_index < len(st.session_state.questions):
    display_question()
    st.markdown("""
        <div style='margin-top:30px;'>
            <img src='https://media.giphy.com/media/dzaUX7CAG0Ihi/giphy.gif' width='80'/>
            <p style='font-style:italic;'>Powered by your friendly AI 🤖</p>
        </div>
    """, unsafe_allow_html=True)
else:
    combined_text = " ".join(st.session_state.answers)
    mood = detect_mood(combined_text)
    st.subheader(f"🔍 Detected Mood: {mood.capitalize()}")

    data = mood_data.get(mood, mood_data["neutral"])
    quote = random.choice(data["quotes"])
    st.success(f"💡 Quote: {quote}")

    if "jokes" in data:
        joke = random.choice(data["jokes"])
        st.info(f"🤣 Joke: {joke}")

    if "gifs" in data:
        gif = random.choice(data["gifs"])
        st.image(gif)

    if "spotify" in data:
        for link in data["spotify"]:
            st.markdown(f"🎵 [Spotify Playlist]({link})")

    if "youtube" in data:
        for link in data["youtube"]:
            st.markdown(f"▶️ [YouTube Video]({link})")

    st.markdown("""
        <div style='margin-top:30px;'>
            <h4>🌈 Thank you for sharing. Stay awesome!</h4>
        </div>
    """, unsafe_allow_html=True)

    st.button("🔁 Start Over", on_click=lambda: st.session_state.update(question_index=0, answers=[]))
    
