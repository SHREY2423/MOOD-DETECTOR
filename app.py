import streamlit as st
import random
from textblob import TextBlob

# --- Mood-based content ---
quotes = {
    "happy": ["Keep smiling, life is beautiful!", "Happiness is a choice."],
    "sad": ["This too shall pass.", "Every storm runs out of rain."],
    "angry": ["Breathe. Let it go.", "Anger doesn’t solve anything."],
    "depressed": ["You're not alone. Please talk to someone.", "Even the darkest night ends with sunrise."],
    "joyful": ["Spread your joy!", "Joy is contagious!"]
}

# --- Background images (URLs or local) ---
backgrounds = [
    "https://images.unsplash.com/photo-1503264116251-35a269479413",
    "https://images.unsplash.com/photo-1522199710521-72d69614c702",
    "https://images.unsplash.com/photo-1506744038136-46273834b3fb",
    "https://images.unsplash.com/photo-1493244040629-496f6d136cc3"
]

# --- Random background ---
bg_url = random.choice(backgrounds)
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url('{bg_url}');
        background-size: cover;
        background-attachment: fixed;
        background-position: center;
    }}
    .main-container {{
        background-color: rgba(255, 255, 255, 0.8);
        padding: 2rem;
        border-radius: 1rem;
        box-shadow: 0 0 10px rgba(0,0,0,0.3);
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# --- Header ---
st.markdown("<div class='main-container'>", unsafe_allow_html=True)
st.title("🧠 Conversational Mood Detector")
st.write("Let's talk and find out how you're feeling today 😊")

# --- Mood detection logic ---
def detect_mood(texts):
    combined_text = " ".join(texts).lower()

    depression_keywords = [
        "depressed", "hopeless", "suicidal", "empty", "worthless", "pointless", "dark",
        "numb", "burned out", "i hate myself", "give up", "i want to die", "kill myself",
        "pain", "unloved", "hate everything", "ending", "can't go on", "overwhelmed", "broken",
        "no one cares", "lost", "why try", "nothing matters", "i'm done", "hurt", "hell", "kill"
    ]
    joyful_keywords = ["joyful", "grateful", "thankful", "blessed", "elated", "euphoric"]
    happy_keywords = ["happy", "smiling", "excited", "good", "content", "satisfied"]
    angry_keywords = ["angry", "mad", "furious", "annoyed", "rage", "frustrated"]
    sad_keywords = ["sad", "down", "blue", "lonely", "crying", "upset", "disappointed"]

    if any(kw in combined_text for kw in depression_keywords):
        return "depressed"
    elif any(kw in combined_text for kw in joyful_keywords):
        return "joyful"
    elif any(kw in combined_text for kw in happy_keywords):
        return "happy"
    elif any(kw in combined_text for kw in angry_keywords):
        return "angry"
    elif any(kw in combined_text for kw in sad_keywords):
        return "sad"

    # Sentiment fallback
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

# --- Conversation input ---
user_inputs = []
st.subheader("🗣️ Talk to me...")

if 'question_num' not in st.session_state:
    st.session_state.question_num = 0
    st.session_state.responses = []

questions = [
    "How are you feeling today?",
    "What’s been on your mind lately?",
    "How was your day?",
    "What do you want to talk about?"
]

if st.session_state.question_num < len(questions):
    with st.form(key=f"form_{st.session_state.question_num}"):
        answer = st.text_input(questions[st.session_state.question_num])
        submit = st.form_submit_button("Next")

        if submit and answer:
            st.session_state.responses.append(answer)
            st.session_state.question_num += 1
else:
    mood = detect_mood(st.session_state.responses)
    st.success(f"🎯 We detected your mood as: **{mood.upper()}**")
    st.markdown(f"💬 *Quote for you:* **{random.choice(quotes.get(mood, ['Stay strong.']))}**")
    st.balloons()
    st.session_state.question_num = 0
    st.session_state.responses = []

st.markdown("</div>", unsafe_allow_html=True)
import streamlit as st
from textblob import TextBlob
import random

# ------------------ Mood Data ------------------ #
mood_data = {
    "joyful": {
        "quotes": [
            "Joy is the simplest form of gratitude 🌈",
            "Live life to the fullest and make every moment count! 🎉"
        ],
        "jokes": [
            "Why do bees have sticky hair? Because they use honeycombs! 🐝",
            "What do you call a singing computer? A Dell! 🎤"
        ],
        "youtube": [
            "https://www.youtube.com/watch?v=3GwjfUFyY6M",
            "https://www.youtube.com/watch?v=ZbZSe6N_BXs"
        ],
        "spotify": ["https://open.spotify.com/playlist/37i9dQZF1DXdPec7aLTmlC"],
        "gifs": [
            "https://media.giphy.com/media/l0MYt5jPR6QX5pnqM/giphy.gif",
            "https://media.giphy.com/media/MDJ9IbxxvDUQM/giphy.gif"
        ]
    },
    "happy": {
        "quotes": [
            "Keep smiling, because life is a beautiful thing! 😊",
            "Happiness is contagious, spread it! 🌞"
        ],
        "jokes": [
            "Why don’t scientists trust atoms? Because they make up everything! 🤣",
            "Why did the scarecrow win an award? Because he was outstanding in his field! 🏆"
        ],
        "youtube": [
            "https://www.youtube.com/watch?v=60ItHLz5WEA",
            "https://www.youtube.com/watch?v=3GwjfUFyY6M"
        ],
        "spotify": ["https://open.spotify.com/playlist/37i9dQZF1DXdPec7aLTmlC"],
        "gifs": [
            "https://media.giphy.com/media/yoJC2A59OCZHs1LXvW/giphy.gif",
            "https://media.giphy.com/media/l0MYt5jPR6QX5pnqM/giphy.gif"
        ]
    },
    "sad": {
        "quotes": [
            "It’s okay to not be okay. 💙",
            "Tough times never last, but tough people do 💪"
        ],
        "jokes": [
            "Why did the math book look sad? Because it had too many problems. 😢",
            "Why did the computer visit the therapist? Too many bytes of sadness. 🖥"
        ],
        "youtube": [
            "https://www.youtube.com/watch?v=RB-RcX5DS5A",
            "https://www.youtube.com/watch?v=2vjPBrBU-TM"
        ],
        "spotify": ["https://open.spotify.com/playlist/37i9dQZF1DX7qK8ma5wgG1"],
        "gifs": [
            "https://media.giphy.com/media/3oz8xKaR836UJOYeOc/giphy.gif",
            "https://media.giphy.com/media/d2lcHJTG5Tscg/giphy.gif"
        ]
    },
    "angry": {
        "quotes": [
            "Calm is a superpower. 🧘",
            "Breathe. It’s just a bad day, not a bad life. 🌪"
        ],
        "jokes": [
            "Why don’t skeletons fight each other? They don’t have the guts. 💀",
            "I'm not arguing, I'm just passionately expressing my rightness 😤"
        ],
        "youtube": [
            "https://www.youtube.com/watch?v=kXYiU_JCYtU"
        ],
        "spotify": ["https://open.spotify.com/playlist/37i9dQZF1DX76Wlfdnj7AP"],
        "gifs": [
            "https://media.giphy.com/media/IThjAlJnD9WNO/giphy.gif"
        ]
    },
    "neutral": {
        "quotes": [
            "Stay grounded. Everything will fall into place. 🌱",
            "Just breathe, you’ve got this. 🌈"
        ],
        "jokes": [
            "Why can’t your nose be 12 inches long? Because then it would be a foot! 👃🤣",
            "What do you call cheese that isn't yours? Nacho cheese! 🧀"
        ],
        "youtube": [
            "https://www.youtube.com/watch?v=hHW1oY26kxQ"
        ],
        "spotify": ["https://open.spotify.com/playlist/37i9dQZF1DX6VdMW310YC7"],
        "gifs": [
            "https://media.giphy.com/media/xT1R9ZzU4dU6lV1p7G/giphy.gif"
        ]
    },
    "depressed": {
        "quotes": [
            "You're not alone. This too shall pass. 🌧",
            "Every storm runs out of rain. 🌦"
        ],
        "jokes": [
            "Why did the chicken go to therapy? To get to the other side of its emotions. 🐔",
            "What’s a depressed person’s favorite food? Anything with serotonin! 😅"
        ],
        "youtube": [
            "https://www.youtube.com/watch?v=w6T02g5hnT4",
            "https://www.youtube.com/watch?v=2vEStDd6HVY"
        ],
        "spotify": ["https://open.spotify.com/playlist/37i9dQZF1DWVrtsSlLKzro"],
        "gifs": [
            "https://media.giphy.com/media/l0HlJzQ9312VRFMBW/giphy.gif"
        ]
    }
}

# ------------------ Questions ------------------ #
questions = [
    "How are you feeling today in one word?",
    "What happened today that affected your mood?",
    "What's something on your mind right now?",
    "How do you feel physically and mentally right now?",
    "If you could change one thing about your day, what would it be?"
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
        "pointless", "dark", "numb", "burned out", "i hate myself", "give up"
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

# ------------------ UI Config ------------------ #
st.set_page_config(page_title="AI Mood Detector 😄", layout="centered")
st.markdown("<h1 style='text-align: center;'>🧠 Conversational Mood Detector</h1>", unsafe_allow_html=True)
st.markdown("Answer a few questions below to let us detect your mood and suggest things for you.")

# ------------------ Q&A or Result ------------------ #
q_index = st.session_state.q_index

if q_index < len(questions):
    st.subheader(f"Q{q_index + 1}: {questions[q_index]}")
    st.text_input(
        label="",
        key="user_input",
        on_change=advance,
        placeholder="Type your response and press Enter..."
    )
else:
    try:
        mood = detect_mood(st.session_state.responses)
        data = mood_data[mood]

        st.balloons()
        st.success(f"🎯 Your mood is: *{mood.capitalize()}*")
        st.image(random.choice(data["gifs"]), use_container_width=True)

        st.subheader("💬 Motivational Quotes")
        for quote in random.sample(data["quotes"], min(2, len(data["quotes"]))):
            st.info(quote)

        st.subheader("🎧 Spotify Playlist")
        for link in data["spotify"]:
            st.markdown(f"[▶ Open Playlist on Spotify]({link})")

        st.subheader("📺 YouTube Videos for You")
        for link in random.sample(data["youtube"], min(2, len(data["youtube"]))):
            st.markdown(f"[🎬 Watch Video]({link})")

        st.subheader("😂 Here's a joke:")
        st.write(random.choice(data["jokes"]))

        if st.button("🔁 Start Again"):
            st.session_state.q_index = 0
            st.session_state.responses = []
            st.session_state.user_input = ""
            st.experimental_rerun()

    except Exception as e:
        st.error(f"⚠ An error occurred: {e}")
