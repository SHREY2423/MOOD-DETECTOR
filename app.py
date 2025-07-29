import streamlit as st
from textblob import TextBlob
import random
import re
from collections import defaultdict

# ------------------ Mood Keywords ------------------ #
mood_keywords = {
    "depressed": [
        "depressed", "hopeless", "suicidal", "empty", "worthless", "pointless", "numb",
        "hate myself", "give up", "kill", "cut", "death", "die", "ending it", "hurting", "done", "useless"
    ],
    "joyful": [
        "joyful", "cheerful", "excited", "grateful", "fantastic", "wonderful", "blessed",
        "great", "amazing", "woohoo", "yaaahoo", "awesome", "yay", "celebrate", "ecstatic"
    ],
    "happy": [
        "happy", "smile", "fun", "sunny", "cool", "loving", "calm", "peaceful", "bright",
        "good", "positive", "content", "satisfied", "relaxed"
    ],
    "sad": [
        "sad", "cry", "tears", "upset", "hurt", "lonely", "bad", "unhappy", "disappointed", "gloomy", "lost", "down"
    ],
    "angry": [
        "angry", "mad", "furious", "pissed", "rage", "hate", "annoyed", "irritated", "frustrated", "yell", "explode", "temper"
    ],
    "neutral": [
        "okay", "normal", "nothing", "meh", "fine", "tired", "bored", "average", "usual", "neutral", "blank"
    ]
}

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
    words = re.findall(r"\b\w+\b", combined_text)

    mood_scores = defaultdict(int)

    # Count keyword matches
    for mood, keywords in mood_keywords.items():
        for keyword in keywords:
            keyword_words = keyword.lower().split()
            if len(keyword_words) == 1:
                mood_scores[mood] += words.count(keyword_words[0])
            else:
                pattern = re.compile(r"\b" + r"\s+".join(keyword_words) + r"\b")
                mood_scores[mood] += len(pattern.findall(combined_text))

    if mood_scores:
        top_mood = max(mood_scores, key=mood_scores.get)
        if mood_scores[top_mood] > 0:
            return top_mood

    # Fallback to sentiment
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
