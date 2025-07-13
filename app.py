import streamlit as st
from textblob import TextBlob
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import random

# ---------------------- Mood Data ---------------------- #
mood_data = {
    "happy": {
        "quotes": [
            "Keep smiling, because life is a beautiful thing! 😊",
            "Happiness is contagious, spread it! 🌞",
            "Every moment is a fresh beginning. ✨",
            "Be so happy that others look at you and feel happy too."
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
            "Tough times never last, but tough people do 💪",
            "Stars can’t shine without darkness. 🌌",
            "You’ve survived 100% of your bad days. Keep going."
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
            "Breathe. It’s just a bad day, not a bad life. 🌪️",
            "Your value doesn’t decrease based on someone’s inability to see your worth. 🛡️",
            "Let your smile change the world, but don’t let the world change your smile."
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
            "Just breathe, you’ve got this. 🌈",
            "Progress is progress, no matter how small. 🚶",
            "In the middle of difficulty lies opportunity."
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
    "What's something on your mind right now?",
    "How do you feel physically and mentally right now?",
    "If you could change one thing about your day, what would it be?"
]

# ---------------------- Session State Setup ---------------------- #
if "q_index" not in st.session_state:
    st.session_state.q_index = 0
if "responses" not in st.session_state:
    st.session_state.responses = []
if "user_input" not in st.session_state:
    st.session_state.user_input = ""

# ---------------------- ML Model Training ---------------------- #
train_texts = [
    "I feel great and energetic today", "What a lovely and beautiful day", "I'm feeling amazing",
    "I just got promoted and I'm so happy", "I'm feeling really down and upset", "I just want to cry and sleep",
    "Life feels meaningless right now", "I'm so mad and frustrated", "Everything is making me angry",
    "People are irritating me a lot today", "Just another normal day", "I feel okay, nothing special"
]
train_labels = [
    "happy", "happy", "happy", "happy",
    "sad", "sad", "sad",
    "angry", "angry", "angry",
    "neutral", "neutral"
]

vectorizer = TfidfVectorizer()
X_train = vectorizer.fit_transform(train_texts)
clf = MultinomialNB()
clf.fit(X_train, train_labels)

# ---------------------- Advance Input ---------------------- #
def advance_question():
    if st.session_state.user_input.strip():
        st.session_state.responses.append(st.session_state.user_input.strip())
        st.session_state.q_index += 1
        st.session_state.user_input = ""

# ---------------------- UI ---------------------- #
st.set_page_config(page_title="Mood Detector", layout="centered")
st.title("🧠 AI Mood Detector")
st.markdown("Answer the following questions honestly. Press **Enter** to go next.")

q_index = st.session_state.q_index

if q_index < len(questions):
    st.subheader(f"Q{q_index + 1}:")
    st.text_input(
        questions[q_index],
        key="user_input",
        on_change=advance_question,
        placeholder="Type here and press Enter..."
    )
else:
    combined_input = " ".join(st.session_state.responses)
    X_input = vectorizer.transform([combined_input])
    mood = clf.predict(X_input)[0]
    info = mood_data[mood]

    st.balloons()
    st.image(info["gif"], caption=f"Detected mood: **{mood.upper()}** 🎯", use_column_width=True)
    st.success(f"🌟 Your mood is: **{mood.capitalize()}**")

    st.subheader("💬 Motivational Quotes")
    for quote in random.sample(info["quotes"], 2):
        st.info(quote)

    st.subheader("🎧 Spotify Playlist")
    for link in info["spotify"]:
        st.markdown(f"[🎵 Open Playlist]({link})")

    st.subheader("📺 YouTube Video Links")
    for link in random.sample(info["youtube"], 2):
        st.markdown(f"[📺 Watch Video]({link})")

    st.subheader("😂 Here's a joke for you:")
    st.write(random.choice(info["jokes"]))

    if st.button("🔁 Start Over"):
        st.session_state.q_index = 0
        st.session_state.responses = []
        st.session_state.user_input = ""
        st.experimental_rerun()

