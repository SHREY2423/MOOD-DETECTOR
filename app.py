import streamlit as st
from textblob import TextBlob
import random
from PIL import Image

st.set_page_config(page_title="🧠 Conversational Mood Detector", layout="centered")
st.markdown("""
    <style>
        body {
            background: linear-gradient(to bottom, #eafcff, #f0f8ff);
            font-family: 'Segoe UI', sans-serif;
        }
        .question-box {
            background-color: #ffffffcc;
            padding: 1.5rem;
            border-radius: 15px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.05);
            margin-bottom: 2rem;
        }
        .gif-container img {
            max-width: 100%;
            border-radius: 12px;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
# 🧠 <span style='color: #4a90e2;'>Conversational Mood Detector</span>  
### <span style='color: #444;'>Let's talk and discover how you're truly feeling 😊</span>
""", unsafe_allow_html=True)

questions = [
    "How are you feeling right now in one word?",
    "What’s one thing on your mind today?",
    "Describe your current energy level (1-10)?",
    "Have you smiled genuinely today?",
    "Is there anything you’re looking forward to?",
    "Choose a word that sums up your day so far."
]

if 'step' not in st.session_state:
    st.session_state.step = 0
    st.session_state.responses = []

with st.form(key='mood_form'):
    st.markdown(f"**{questions[st.session_state.step]}**")
    user_input = st.text_input("Your answer:", key=f"input_{st.session_state.step}")
    submitted = st.form_submit_button("Next")

if submitted and user_input.strip():
    st.session_state.responses.append(user_input.strip())
    st.session_state.step += 1

if st.session_state.step >= len(questions):
    full_response = " ".join(st.session_state.responses)
    blob = TextBlob(full_response)
    sentiment = blob.sentiment.polarity

    keywords = {
        "happy": ["happy", "joyful", "great", "excited", "grateful"],
        "sad": ["sad", "down", "blue", "cry"],
        "depressed": ["depressed", "worthless", "hopeless", "suicidal", "overwhelmed", "dark", "lost", "pointless"],
        "neutral": ["okay", "fine", "meh", "normal"]
    }

    def detect_mood(text):
        text = text.lower()
        for mood, keys in keywords.items():
            if any(k in text for k in keys):
                return mood
        if sentiment > 0.3:
            return "happy"
        elif sentiment < -0.3:
            return "sad"
        else:
            return "neutral"

    mood = detect_mood(full_response)

    # Content by mood
    mood_data = {
        "happy": {
            "quote": ["Keep smiling, life is beautiful! 🌈", "Your joy is contagious, keep spreading it! 🌟"],
            "gif": ["https://media.giphy.com/media/l0MYt5jPR6QX5pnqM/giphy.gif"],
            "music": ["https://open.spotify.com/playlist/37i9dQZF1DXdPec7aLTmlC"],
            "youtube": ["https://www.youtube.com/watch?v=ZbZSe6N_BXs"],
            "jokes": ["Why don’t scientists trust atoms? Because they make up everything!"]
        },
        "sad": {
            "quote": ["Tough times never last, but tough people do. 💪", "It’s okay to not be okay. Tomorrow is a new day. 🌤️"],
            "gif": ["https://media.giphy.com/media/l0MYEqEzwMWFCg8rm/giphy.gif"],
            "music": ["https://open.spotify.com/playlist/37i9dQZF1DX3rxVfibe1L0"],
            "youtube": ["https://www.youtube.com/watch?v=hoNb6HuNmU0"],
            "jokes": ["Why did the scarecrow win an award? Because he was outstanding in his field!"]
        },
        "depressed": {
            "quote": ["You are not alone. Help is always closer than you think. 💖", "Even the darkest night will end and the sun will rise. 🌅"],
            "gif": ["https://media.giphy.com/media/3og0IPxMM0erATueVW/giphy.gif"],
            "music": ["https://open.spotify.com/playlist/5F0M3IFKM4zquT1HdJv2FP"],
            "youtube": ["https://www.youtube.com/watch?v=rlZ0wjj_4xQ"],
            "jokes": ["Why can’t your nose be 12 inches long? Because then it would be a foot!"]
        },
        "neutral": {
            "quote": ["Every day is a second chance. ✨", "Stay balanced, stay calm. 🧘‍♂️"],
            "gif": ["https://media.giphy.com/media/3o7qE1YN7aBOFPRw8E/giphy.gif"],
            "music": ["https://open.spotify.com/playlist/37i9dQZF1DWYBO1MoTDhZI"],
            "youtube": ["https://www.youtube.com/watch?v=2vjPBrBU-TM"],
            "jokes": ["What do you call a fake noodle? An impasta!"]
        }
    }

    data = mood_data.get(mood, mood_data["neutral"])

    st.success(f"### Your detected mood is: `{mood.capitalize()}`")
    st.markdown(f"#### 🧘 Quote of the Day: *{random.choice(data['quote'])}*")

    st.markdown("""
    <div class='gif-container'>
        <img src='""" + random.choice(data['gif']) + """' alt='gif' />
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"🎵 [Listen on Spotify]({data['music'][0]})")
    st.markdown(f"📺 [Watch on YouTube]({data['youtube'][0]})")

    st.info(f"🃏 Joke: {random.choice(data['jokes'])}")

    st.markdown("""
    ---
    <p style='font-size:13px; color:gray;'>Made with ❤️ to help you feel better, one question at a time.</p>
    """, unsafe_allow_html=True)

    st.stop()

# Footer when app starts
st.markdown("""
    <footer style='text-align:center; color:#bbb; font-size:12px;'>
        🌱 Calm UI | Powered by Streamlit | MoodSense 2025
    </footer>
""", unsafe_allow_html=True)

