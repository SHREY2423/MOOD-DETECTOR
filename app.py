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
            "What’s a skeleton’s least favorite room in the house? The living room! 💀"
        ],
        "youtube": [
            "https://www.youtube.com/watch?v=d-diB65scQU"
        ],
        "spotify": [
            "https://open.spotify.com/playlist/37i9dQZF1DWYBO1MoTDhZI"
        ],
        "gifs": [
            "https://media.giphy.com/media/l0MYC0LajbaPoEADu/giphy.gif",
            "https://media.giphy.com/media/OkJat1YNdoD3W/giphy.gif",
            "https://media.giphy.com/media/hvRJCLFzcasrR4ia7z/giphy.gif",
            "https://media.giphy.com/media/JltOMwYmi0VrO/giphy.gif",
            "https://media.giphy.com/media/xT0GqF4W9GHZbUpT0I/giphy.gif"
        ]
    },
    "happy": {
        "quotes": [
            "Happiness is a journey, not a destination 😊",
            "Smile, it’s free therapy! 😄"
        ],
        "jokes": [
            "Why don’t eggs tell jokes? Because they’d crack each other up! 🥚😂",
            "Why did the scarecrow win an award? He was outstanding in his field! 🌾"
        ],
        "youtube": [
            "https://www.youtube.com/watch?v=ZbZSe6N_BXs"
        ],
        "spotify": [
            "https://open.spotify.com/playlist/37i9dQZF1DXdPec7aLTmlC"
        ],
        "gifs": [
            "https://media.giphy.com/media/111ebonMs90YLu/giphy.gif",
            "https://media.giphy.com/media/13k4VSc3ngLPUY/giphy.gif",
            "https://media.giphy.com/media/Wq2oPoZGEcRGI/giphy.gif",
            "https://media.giphy.com/media/l3vRn3I4p0Kf6/giphy.gif",
            "https://media.giphy.com/media/kzDA5Hd5Uv5XW/giphy.gif"
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
            "https://www.youtube.com/watch?v=RB-RcX5DS5A"
        ],
        "spotify": [
            "https://open.spotify.com/playlist/37i9dQZF1DX7qK8ma5wgG1"
        ],
        "gifs": [
            "https://media.giphy.com/media/d2lcHJTG5Tscg/giphy.gif",
            "https://media.giphy.com/media/9Y5BbDSkSTiY8/giphy.gif",
            "https://media.giphy.com/media/Y8OcCgwtdj29O/giphy.gif",
            "https://media.giphy.com/media/ROF8OQvDmxytW/giphy.gif",
            "https://media.giphy.com/media/M4DsgnqV63a3WL9KkT/giphy.gif"
        ]
    },
    "angry": {
        "quotes": [
            "Don’t let anger control you. Breathe. 🌬",
            "Speak when you are angry and you will make the best speech you will ever regret. 😠"
        ],
        "jokes": [
            "Why did the angry Jedi cross the road? To get to the dark side! 🌌",
            "I'm not arguing, I'm just explaining why I'm right. 😤"
        ],
        "youtube": [
            "https://www.youtube.com/watch?v=Z3Pu1CIboCw"
        ],
        "spotify": [
            "https://open.spotify.com/playlist/37i9dQZF1DWZQaaqNMbbXa"
        ],
        "gifs": [
            "https://media.giphy.com/media/xT0GqzZ3uVPeXW1JLa/giphy.gif",
            "https://media.giphy.com/media/l0MYEQEzwMWFCg8rm/giphy.gif",
            "https://media.giphy.com/media/3ornka9rAaDRRt9OUE/giphy.gif",
            "https://media.giphy.com/media/iJzz3lvu9twRa/giphy.gif",
            "https://media.giphy.com/media/3o6Zt7tRTa43bWJYl6/giphy.gif"
        ]
    },
    "neutral": {
        "quotes": [
            "Balance is not something you find, it’s something you create ⚖️",
            "Stay calm, stay neutral. 🚶"
        ],
        "jokes": [
            "I told my friend 10 jokes to make him laugh. Sadly, no pun in ten did. 😐",
            "Why don’t scientists trust atoms? Because they make up everything. ⚛️"
        ],
        "youtube": [
            "https://www.youtube.com/watch?v=2Vv-BfVoq4g"
        ],
        "spotify": [
            "https://open.spotify.com/playlist/37i9dQZF1DX6VdMW310YC7"
        ],
        "gifs": [
            "https://media.giphy.com/media/5VKbvrjxpVJCM/giphy.gif",
            "https://media.giphy.com/media/QBd2kLB5qDmysEXre9/giphy.gif",
            "https://media.giphy.com/media/xT0xeJpnrWC4XWblEk/giphy.gif",
            "https://media.giphy.com/media/yFQ0ywscgobJK/giphy.gif",
            "https://media.giphy.com/media/mCRJDo24UvJMA/giphy.gif"
        ]
    },
    "depressed": {
        "quotes": [
            "This too shall pass 🌧️",
            "You’ve survived 100% of your worst days. Keep going 🖤"
        ],
        "jokes": [
            "Why did the chicken join a band? Because it had the drumsticks 🐔🥁",
            "What's orange and sounds like a parrot? A carrot. 🥕"
        ],
        "youtube": [
            "https://www.youtube.com/watch?v=JkK8g6FMEXE"
        ],
        "spotify": [
            "https://open.spotify.com/playlist/37i9dQZF1DWVrtsSlLKzro"
        ],
        "gifs": [
            "https://media.giphy.com/media/SsTcO55LJDBsI/giphy.gif",
            "https://media.giphy.com/media/h4OGa4fK2b3J9fLAdf/giphy.gif",
            "https://media.giphy.com/media/jTnIaJP1ofGxO/giphy.gif",
            "https://media.giphy.com/media/13Z6W7kzQKckGg/giphy.gif",
            "https://media.giphy.com/media/L95W4wv8nnb9K/giphy.gif"
        ]
    }
}

# ------------------ Mood Detection ------------------ #
def detect_mood(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    keywords = text.lower()
    if any(word in keywords for word in ["depressed", "suicide", "worthless", "hopeless"]):
        return "depressed"
    elif any(word in keywords for word in ["angry", "furious", "mad"]):
        return "angry"
    elif any(word in keywords for word in ["happy", "excited", "glad"]):
        return "happy"
    elif any(word in keywords for word in ["sad", "unhappy", "upset"]):
        return "sad"
    elif polarity > 0.5:
        return "joyful"
    elif polarity < -0.3:
        return "depressed"
    elif -0.3 <= polarity <= 0.3:
        return "neutral"
    else:
        return "happy"

# ------------------ Streamlit UI ------------------ #
st.title("🧠 Conversational Mood Detector")
st.markdown("Answer a few questions below to let us detect your mood and suggest things for you.")

user_input = st.text_input("💬 How are you feeling today? (Be honest and expressive)")

if user_input:
    try:
        mood = detect_mood(user_input)
        st.subheader(f"🔍 Detected Mood: {mood.capitalize()}")

        mood_content = mood_data[mood]
        st.markdown("### 💡 Motivational Quote")
        st.info(random.choice(mood_content["quotes"]))

        st.markdown("### 😂 Here's a Joke")
        st.success(random.choice(mood_content["jokes"]))

        st.markdown("### 📺 YouTube Suggestion")
        st.video(random.choice(mood_content["youtube"]))

        st.markdown("### 🎧 Spotify Playlist")
        st.markdown(f"[Listen here]({random.choice(mood_content['spotify'])})")

        st.markdown("### 🖼️ Mood GIF")
        st.image(random.choice(mood_content["gifs"]), use_column_width=True)

    except Exception as e:
        st.error(f"⚠ An error occurred: {e}")
