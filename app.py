import streamlit as st
from textblob import TextBlob
import random

st.set_page_config(page_title="🧠 Conversational Mood Detector", layout="centered")
st.markdown("""
    <style>
        .stApp {
            background: linear-gradient(to bottom, #e0f7fa, #ffffff);
            font-family: 'Segoe UI', sans-serif;
        }
        .question-box {
            background-color: #f1f1f1;
            padding: 20px;
            border-radius: 10px;
            margin-top: 20px;
        }
        .sticker {
            width: 100%;
            text-align: center;
            margin-top: 30px;
        }
    </style>
""", unsafe_allow_html=True)

st.title("🧠 Conversational Mood Detector")
st.subheader("Let's talk and discover how you're truly feeling 😊")

questions = [
    "How are you feeling right now in one word?",
    "What was the highlight of your day?",
    "Anything stressing you out recently?",
    "What's something that made you smile today?",
    "Describe your current mood in a sentence."
]

if 'step' not in st.session_state:
    st.session_state.step = 0
    st.session_state.answers = []

if st.session_state.step < len(questions):
    with st.form(key=f"question_form_{st.session_state.step}"):
        st.markdown(f"**{questions[st.session_state.step]}**")
        user_input = st.text_input("Your answer:")
        submit = st.form_submit_button("Next")

    if submit and user_input:
        st.session_state.answers.append(user_input)
        st.session_state.step += 1
        st.experimental_rerun()
else:
    all_text = " ".join(st.session_state.answers)
    blob = TextBlob(all_text)
    polarity = blob.sentiment.polarity

    # Basic mood detection based on polarity and keywords
    if any(word in all_text.lower() for word in ['depressed', 'suicide', 'hopeless']):
        mood = 'depressed'
    elif polarity > 0.3:
        mood = 'happy'
    elif polarity < -0.3:
        mood = 'sad'
    else:
        mood = 'neutral'

    mood_data = {
        "happy": {
            "quote": [
                "Keep smiling, because life is a beautiful thing!",
                "Happiness is not by chance, but by choice.",
                "Every day is a new beginning, take a deep breath and start again.",
            ],
            "gif": "https://media.giphy.com/media/yoJC2Olx0ekMy2nX7W/giphy.gif",
            "joke": [
                "Why don’t scientists trust atoms? Because they make up everything!",
                "Why did the scarecrow win an award? Because he was outstanding in his field!"
            ],
            "spotify": "https://open.spotify.com/playlist/37i9dQZF1DX3rxVfibe1L0",
            "youtube": "https://www.youtube.com/watch?v=ZbZSe6N_BXs"
        },
        "sad": {
            "quote": [
                "Tough times don’t last, but tough people do.",
                "This too shall pass. Keep going.",
                "Every storm runs out of rain."
            ],
            "gif": "https://media.giphy.com/media/9Y5BbDSkSTiY8/giphy.gif",
            "joke": [
                "Why don’t skeletons fight each other? They don’t have the guts.",
                "I'm reading a book on anti-gravity. It's impossible to put down!"
            ],
            "spotify": "https://open.spotify.com/playlist/1BKTIRsYxVtUgF8RY7F0wI",
            "youtube": "https://www.youtube.com/watch?v=hoNb6HuNmU0"
        },
        "depressed": {
            "quote": [
                "You're stronger than you think.",
                "It's okay to ask for help. You’re not alone.",
                "The darkest nights produce the brightest stars."
            ],
            "gif": "https://media.giphy.com/media/26gsgIkzFv3RVik1i/giphy.gif",
            "joke": [
                "Why did the coffee file a police report? It got mugged!",
                "Parallel lines have so much in common… It’s a shame they’ll never meet."
            ],
            "spotify": "https://open.spotify.com/playlist/4cJcrbiwGr9aZp5N0HEeJ2",
            "youtube": "https://www.youtube.com/watch?v=MejbOFk7H6c"
        },
        "neutral": {
            "quote": [
                "Sometimes, being neutral helps you see things clearly.",
                "Take a moment to breathe. You’re doing fine.",
                "Just keep swimming." 
            ],
            "gif": "https://media.giphy.com/media/QBd2kLB5qDmysEXre9/giphy.gif",
            "joke": [
                "Why can’t your nose be 12 inches long? Because then it would be a foot!",
                "What do you call a fake noodle? An Impasta!",
                "Why don’t skeletons fight each other? They don’t have the guts.",
                "I told my wife she was drawing her eyebrows too high. She looked surprised.",
                "What did one wall say to the other? I’ll meet you at the corner."
            ],
            "spotify": "https://open.spotify.com/playlist/6ftTNMc3VB0pvVSM9fStGA",
            "youtube": "https://www.youtube.com/watch?v=HgzGwKwLmgM"
        }
    }

    data = mood_data.get(mood, mood_data["neutral"])

    st.success(f"Your mood is likely: **{mood.upper()}** 🎯")

    st.image(data["gif"], caption=f"{mood.capitalize()} vibes")
    st.write(f"🎵 [Spotify Playlist]({data['spotify']}) | 📺 [YouTube Video]({data['youtube']})")

    st.markdown(f"**💬 Quote:** {random.choice(data['quote'])}")
    st.markdown(f"**😂 Joke:** {random.choice(data['joke'])}")

    st.markdown("""
        <div class="sticker">
            <img src="https://media.giphy.com/media/l0HlBO7eyXzSZkJri/giphy.gif" width="200" />
            <p><strong>AI Mood Detector powered by ChatGPT</strong></p>
        </div>
    """, unsafe_allow_html=True)

    if st.button("Restart Conversation"):
        st.session_state.step = 0
        st.session_state.answers = []
        st.experimental_rerun()
