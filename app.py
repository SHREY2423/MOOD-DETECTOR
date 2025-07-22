import streamlit as st
from transformers import pipeline
from textblob import TextBlob
import random
import time

# Initialize model and state
sentiment_pipeline = pipeline("sentiment-analysis")

if "answers" not in st.session_state:
    st.session_state.answers = []
if "question_index" not in st.session_state:
    st.session_state.question_index = 0
if "mood" not in st.session_state:
    st.session_state.mood = ""
if "show_result" not in st.session_state:
    st.session_state.show_result = False

# Questions
questions = [
    "1️⃣ How are you feeling today in one word?",
    "2️⃣ What kind of day did you have?",
    "3️⃣ Have you been social or isolated lately?",
    "4️⃣ What's something on your mind right now?",
    "5️⃣ What motivates or drains you currently?",
    "6️⃣ Any recent moment that made you emotional?"
]

# Mood detection keywords
mood_keywords = {
    "depressed": ["suicide", "kill myself", "die", "ending", "worthless", "over", "useless", "hopeless"],
    "sad": ["sad", "tired", "down", "cry", "lonely", "upset", "hurt"],
    "happy": ["happy", "excited", "grateful", "smile", "joy"],
    "neutral": ["okay", "fine", "normal", "meh", "nothing"],
    "joyful": ["amazing", "great", "awesome", "fantastic", "blessed"]
}

# Quotes
quotes = {
    "depressed": [
        "You have survived 100% of your bad days. Keep going.",
        "This too shall pass. Hold on.",
        "You matter more than you think.",
        "Every day is a second chance.",
        "Let the darkest days teach you the brightest lessons.",
        "Even broken crayons still color.",
        "You are not alone. Talk to someone.",
        "Pain is temporary. Strength is forever.",
        "Your story isn’t over yet.",
        "Bravery is asking for help when you need it."
    ],
    "sad": [
        "Tough times don’t last, but tough people do.",
        "You are stronger than you think.",
        "Healing takes time, and that’s okay.",
        "Let yourself feel, and then let go.",
        "Your current situation is not your final destination.",
        "Sadness is a visitor — not a permanent resident.",
        "It's okay to cry. It’s okay to feel.",
        "You’ve made it through every bad day so far.",
        "One step at a time is still progress.",
        "You will smile again."
    ],
    "happy": [
        "Happiness looks good on you!",
        "Spread your joy like confetti!",
        "Your smile is contagious!",
        "Today is a good day to be happy!",
        "Let your happiness inspire others.",
        "Keep shining!",
        "Live in the moment!",
        "Gratitude fuels happiness.",
        "Celebrate the little victories!",
        "Enjoy the now!"
    ],
    "joyful": [
        "Your vibe is inspiring!",
        "You’re glowing with positivity!",
        "The world needs more of your joy!",
        "Keep laughing, it suits you!",
        "You bring sunshine with you!",
        "This joy is a blessing.",
        "Joy is powerful. Keep it alive!",
        "Ride the wave of this energy!",
        "You’re on fire (in a good way)!",
        "Joy is the ultimate success."
    ],
    "neutral": [
        "Neutral is a safe place to restart.",
        "Sometimes pause is power.",
        "You’re doing okay, and that’s enough.",
        "Balance is a blessing.",
        "Clarity begins in stillness.",
        "Even a flat line is better than burnout.",
        "Breathe. Reflect. Realign.",
        "Today may be neutral, but tomorrow may shine.",
        "Peace is in this moment.",
        "Let today just be."
    ]
}

# Mood-specific jokes
jokes = {
    "sad": [
        "Why don’t skeletons fight each other? They don’t have the guts!",
        "What do you call fake spaghetti? An impasta!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!"
    ],
    "depressed": [
        "Why did the computer go to therapy? It had too many bytes of sadness!",
        "Why did the blanket go to rehab? It was hooked on comfort!",
        "How do cows stay positive? They turn the moooood around!"
    ],
    "happy": [
        "What do you call cheese that isn't yours? Nacho cheese!",
        "Why did the coffee file a police report? It got mugged!"
    ],
    "neutral": [
        "Why don't eggs tell jokes? They’d crack each other up!",
        "Why did the math book look sad? Too many problems."
    ],
    "joyful": [
        "Did you hear about the claustrophobic astronaut? He just needed a little space!",
        "Why did the banana go to the party? Because it was a-peeling!"
    ]
}

# Mood-specific Spotify and YouTube links
recommendations = {
    "depressed": {
        "spotify": ["https://open.spotify.com/playlist/37i9dQZF1DX3rxVfibe1L0"],
        "youtube": ["https://www.youtube.com/watch?v=8ybW48rKBME"]
    },
    "sad": {
        "spotify": ["https://open.spotify.com/playlist/37i9dQZF1DWVrtsSlLKzro"],
        "youtube": ["https://www.youtube.com/watch?v=VYOjWnS4cMY"]
    },
    "happy": {
        "spotify": ["https://open.spotify.com/playlist/37i9dQZF1DXdPec7aLTmlC"],
        "youtube": ["https://www.youtube.com/watch?v=ZbZSe6N_BXs"]
    },
    "neutral": {
        "spotify": ["https://open.spotify.com/playlist/37i9dQZF1DWSqmBTGDYngZ"],
        "youtube": ["https://www.youtube.com/watch?v=QDYfEBY9NM4"]
    },
    "joyful": {
        "spotify": ["https://open.spotify.com/playlist/37i9dQZF1DXdPec7aLTmlC"],
        "youtube": ["https://www.youtube.com/watch?v=OPf0YbXqDm0"]
    }
}

# GIFs
gifs = {
    "depressed": ["https://media.giphy.com/media/xT9IgG50Fb7Mi0prBC/giphy.gif"],
    "sad": ["https://media.giphy.com/media/l0MYRzcWP5V6N4BxG/giphy.gif"],
    "happy": ["https://media.giphy.com/media/1BcfiGlOGXzQk/giphy.gif"],
    "neutral": ["https://media.giphy.com/media/3orieRzZ9h3S9VHzYA/giphy.gif"],
    "joyful": ["https://media.giphy.com/media/111ebonMs90YLu/giphy.gif"]
}

# Detect mood function
def detect_mood(text):
    text = text.lower()
    for mood, keywords in mood_keywords.items():
        if any(word in text for word in keywords):
            return mood
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity
    if polarity < -0.5:
        return "depressed"
    elif polarity < 0:
        return "sad"
    elif polarity == 0:
        return "neutral"
    elif polarity < 0.5:
        return "happy"
    else:
        return "joyful"

# UI Layout
st.title("🧠 Conversational Mood Detector")
st.write("Let's chat and understand your mood today 😊")

if st.session_state.question_index < len(questions):
    current_question = questions[st.session_state.question_index]
    user_input = st.text_input(current_question, key=st.session_state.question_index)

    st.markdown("---")
    st.markdown("🧠 AI Powered • 🌈 Mood Scanner • 💬 Smart Chat")

    if user_input:
        st.session_state.answers.append(user_input)
        st.session_state.question_index += 1
        st.experimental_rerun()

elif not st.session_state.show_result:
    full_text = " ".join(st.session_state.answers)
    detected_mood = detect_mood(full_text)
    st.session_state.mood = detected_mood
    st.session_state.show_result = True
    st.experimental_rerun()

else:
    mood = st.session_state.mood
    st.subheader(f"🎯 Detected Mood: **{mood.upper()}**")
    st.image(random.choice(gifs.get(mood, [])), width=300)
    st.success(random.choice(quotes.get(mood, [])))
    st.info(f"💡 Joke: {random.choice(jokes.get(mood, []))}")

    for link in recommendations[mood]["spotify"]:
        st.markdown(f"🎧 [Listen on Spotify]({link})")
    for yt in recommendations[mood]["youtube"]:
        st.markdown(f"📺 [Watch on YouTube]({yt})")

    st.balloons()
    if st.button("🔁 Try Again"):
        for key in ["answers", "question_index", "mood", "show_result"]:
            st.session_state.pop(key, None)
        st.experimental_rerun()

# Footer Decoration
st.markdown("---")
st.markdown("Made with ❤️ by AI • Powered by 🤖 Transformers • UI Enhanced ✨")
