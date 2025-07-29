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
            "Why did the scarecrow win an award? Because he was outstanding in his field! 🌾"
        ],
        "youtube": [
            "https://www.youtube.com/watch?v=ZbZSe6N_BXs",
            "https://www.youtube.com/watch?v=60ItHLz5WEA"
        ],
        "spotify": [
            "https://open.spotify.com/playlist/37i9dQZF1DXdPec7aLTmlC"
        ],
        "gifs": [
            "https://media.giphy.com/media/l0MYt5jPR6QX5pnqM/giphy.gif",
            "https://media.giphy.com/media/3o6Zt481isNVuQI1l6/giphy.gif",
            "https://media.giphy.com/media/jUwpNzg9IcyrK/giphy.gif",
            "https://media.giphy.com/media/xT5LMHxhOfscxPfIfm/giphy.gif",
            "https://media.giphy.com/media/1BdIPqLDYwL04VtFji/giphy.gif"
        ]
    },
    "happy": {
        "quotes": [
            "Happiness is a warm puppy 🐶",
            "Do more of what makes you happy 🌟"
        ],
        "jokes": [
            "What do you call a happy cowboy? A jolly rancher 🤠",
            "Why did the banana go to the party? Because it was a-peeling! 🍌"
        ],
        "youtube": [
            "https://www.youtube.com/watch?v=CMNry4PE93Y"
        ],
        "spotify": [
            "https://open.spotify.com/playlist/37i9dQZF1DWYBO1MoTDhZI"
        ],
        "gifs": [
            "https://media.giphy.com/media/111ebonMs90YLu/giphy.gif",
            "https://media.giphy.com/media/9Y5BbDSkSTiY8/giphy.gif",
            "https://media.giphy.com/media/5GoVLqeAOo6PK/giphy.gif",
            "https://media.giphy.com/media/yoJC2Olx0ekMy2nX7W/giphy.gif",
            "https://media.giphy.com/media/MDJ9IbxxvDUQM/giphy.gif"
        ]
    },
    "sad": {
        "quotes": [
            "It’s okay to not be okay 💙",
            "Tough times never last, but tough people do 💪"
        ],
        "jokes": [
            "Why did the math book look sad? It had too many problems 📚",
            "Why did the computer visit the therapist? Too many bytes of sadness 💻"
        ],
        "youtube": [
            "https://www.youtube.com/watch?v=2vjPBrBU-TM"
        ],
        "spotify": [
            "https://open.spotify.com/playlist/37i9dQZF1DWVV27DiNWxkR"
        ],
        "gifs": [
            "https://media.giphy.com/media/d2lcHJTG5Tscg/giphy.gif",
            "https://media.giphy.com/media/3oz8xKaR836UJOYeOc/giphy.gif",
            "https://media.giphy.com/media/JYsWwF82EGnpC/giphy.gif",
            "https://media.giphy.com/media/d2lcHJTG5Tscg/giphy.gif",
            "https://media.giphy.com/media/l0MYC0LajbaPoEADu/giphy.gif"
        ]
    },
    "angry": {
        "quotes": [
            "For every minute you are angry, you lose 60 seconds of happiness ⏳",
            "Keep calm, anger is temporary 🧘"
        ],
        "jokes": [
            "Why did the angry Jedi cross the road? To get to the dark side 🌌",
            "What do you call an angry carrot? A steamed veggie 🥕"
        ],
        "youtube": [
            "https://www.youtube.com/watch?v=hLQl3WQQoQ0"
        ],
        "spotify": [
            "https://open.spotify.com/playlist/37i9dQZF1DX6xZZEgC9Ubl"
        ],
        "gifs": [
            "https://media.giphy.com/media/l3q2K5jinAlChoCLS/giphy.gif",
            "https://media.giphy.com/media/3og0IPxMM0erATueVW/giphy.gif",
            "https://media.giphy.com/media/xT0xeJpnrWC4XWblEk/giphy.gif",
            "https://media.giphy.com/media/JQqg4zIGFaWFm/giphy.gif",
            "https://media.giphy.com/media/l2Je66zG6mAAZxgqI/giphy.gif"
        ]
    },
    "neutral": {
        "quotes": [
            "Not every day needs to be amazing. Neutral is okay too 🌥",
            "Stillness speaks louder than noise 🔇"
        ],
        "jokes": [
            "Why did the neutral face go to therapy? To work on its expression 😐",
            "I was going to tell a neutral joke… but it’s neither funny nor sad 😶"
        ],
        "youtube": [
            "https://www.youtube.com/watch?v=V1Pl8CzNzCw"
        ],
        "spotify": [
            "https://open.spotify.com/playlist/37i9dQZF1DWU0ScTcjJBdj"
        ],
        "gifs": [
            "https://media.giphy.com/media/y6cFmbn9X5yis/giphy.gif",
            "https://media.giphy.com/media/3o6Yg4VhjUB2t3sJFe/giphy.gif",
            "https://media.giphy.com/media/OkJat1YNdoD3W/giphy.gif",
            "https://media.giphy.com/media/3ohs4BSacFKI7A717m/giphy.gif",
            "https://media.giphy.com/media/XIqCQx02E1U9W/giphy.gif"
        ]
    },
    "depressed": {
        "quotes": [
            "You’ve survived 100% of your worst days. Keep going 💪",
            "There is hope, even when your brain tells you there isn’t 🧠"
        ],
        "jokes": [
            "Why don’t depressed people like stairs? Because they’re always down 😔",
            "What’s a depressed person’s favorite game? Hide and don’t seek 🫥"
        ],
        "youtube": [
            "https://www.youtube.com/watch?v=ioNng23DkIM"
        ],
        "spotify": [
            "https://open.spotify.com/playlist/37i9dQZF1DX3YSRoSdA634"
        ],
        "gifs": [
            "https://media.giphy.com/media/l2Sq0F6HYKwDi6eek/giphy.gif",
            "https://media.giphy.com/media/26AHONQ79FdWZhAI0/giphy.gif",
            "https://media.giphy.com/media/1BXa2alBjrCXC/giphy.gif",
            "https://media.giphy.com/media/xUPGcguWZHRC2HyBRS/giphy.gif",
            "https://media.giphy.com/media/d3mlE7uhX8KFgEmY/giphy.gif"
        ]
    }
}

# ------------------ Mood Detection Logic ------------------ #
def detect_mood(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    lowered = text.lower()

    if any(word in lowered for word in ["depressed", "suicide", "worthless", "hopeless"]):
        return "depressed"
    elif "angry" in lowered or polarity < -0.3:
        return "angry"
    elif "sad" in lowered or -0.3 <= polarity < -0.1:
        return "sad"
    elif "happy" in lowered or 0.3 < polarity <= 0.6:
        return "happy"
    elif "joy" in lowered or polarity > 0.6:
        return "joyful"
    elif -0.1 <= polarity <= 0.3:
        return "neutral"
    else:
        return "neutral"

# ------------------ App UI ------------------ #
st.set_page_config(page_title="Conversational Mood Detector", layout="centered")
st.title("🧠 DETECT YOUR MOOD")
st.markdown("Answer a few questions below to let us detect your mood and suggest things for you.")

if "conversation" not in st.session_state:
    st.session_state.conversation = []
if "question_index" not in st.session_state:
    st.session_state.question_index = 0

questions = [
    "How are you feeling today?",
    "What’s been on your mind lately?",
    "Describe your day in one sentence.",
    "Is there anything making you feel low or uplifted?",
    "What kind of music are you in the mood for?"
]

if st.session_state.question_index < len(questions):
    question = questions[st.session_state.question_index]
    user_input = st.text_input(f"👉 {question}", key=f"q{st.session_state.question_index}")

    if user_input:
        st.session_state.conversation.append(user_input)
        st.session_state.question_index += 1
        st.experimental_rerun()
else:
    full_text = " ".join(st.session_state.conversation)
    mood = detect_mood(full_text)

    st.subheader(f"🎯 Detected Mood: **{mood.upper()}**")

    try:
        mood_info = mood_data[mood]

        st.markdown(f"💡 **Motivational Quote:** _{random.choice(mood_info['quotes'])}_")
        st.markdown(f"😂 **Mood Joke:** _{random.choice(mood_info['jokes'])}_")
        st.markdown(f"🎵 [Open Spotify Playlist]({random.choice(mood_info['spotify'])})")
        st.markdown(f"📺 [Watch on YouTube]({random.choice(mood_info['youtube'])})")

        # Show GIF
        st.image(random.choice(mood_info['gifs']), use_column_width=True)

    except Exception as e:
        st.error(f"⚠ An error occurred: {e}")

st.markdown("<br><br><p style='text-align: right;'>Made with ❤️ by SHREY<
