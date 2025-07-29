import streamlit as st
from textblob import TextBlob
import random

# ------------------ Mood Data ------------------ #
mood_data = {
    "joyful": {
        "label": "😊 Joyful",
        "color": "#FFE066",
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
        "label": "🙂 Happy",
        "color": "#FFB347",
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
        "label": "☹️ Sad",
        "color": "#AEC6CF",
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
        "label": "😠 Angry",
        "color": "#FF6961",
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
        "label": "😐 Neutral",
        "color": "#D3D3D3",
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
        "label": "😔 Depressed",
        "color": "#A9A9A9",
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
st.set_page_config(page_title="Detect Your Mood", layout="centered")
st.markdown("<h1 style='text-align: center; color:#fff;'>🧠 Detect Your Mood</h1>", unsafe_allow_html=True)

st.markdown("""
    <style>
    body {
        background-color: #311956;
    }
    .block-container {
        background-color: #311956;
    }
    </style>
""", unsafe_allow_html=True)

# ------------------ App Flow ------------------ #
q_index = st.session_state.q_index

if q_index < len(questions):
    st.markdown(f"<h3 style='color:white;'>Q{q_index+1}: {questions[q_index]}</h3>", unsafe_allow_html=True)
    st.text_input("", key="user_input", on_change=advance, placeholder="Type your response and press Enter...")
else:
    mood = detect_mood(st.session_state.responses)
    data = mood_data[mood]

    st.success(f"🎯 Your mood is: {data['label']}")
    st.image(random.choice(data["gifs"]), use_container_width=True)

    st.markdown(f"<div style='background-color:{data['color']};padding:20px;border-radius:15px;'>", unsafe_allow_html=True)

    st.subheader("💬 Motivational Quotes")
    for q in random.sample(data["quotes"], min(2, len(data["quotes"]))):
        st.info(q)

    st.subheader("🎧 Spotify Playlist")
    for s in data["spotify"]:
        st.markdown(f"[▶ Listen on Spotify]({s})")

    st.subheader("📺 YouTube Recommendations")
    for y in random.sample(data["youtube"], min(2, len(data["youtube"]))):
        st.markdown(f"[🎬 Watch]({y})")

    st.subheader("😂 Joke")
    st.write(random.choice(data["jokes"]))

    st.markdown("</div>", unsafe_allow_html=True)

    if st.button("🔁 Start Again"):
        st.session_state.q_index = 0
        st.session_state.responses = []
        st.session_state.user_input = ""
        st.experimental_rerun()
