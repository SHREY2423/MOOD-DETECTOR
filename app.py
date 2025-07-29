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
            "https://www.youtube.com/watch?v=y6Sxv-sUYtM"
        ],
        "spotify": [
            "https://open.spotify.com/playlist/37i9dQZF1DXdPec7aLTmlC"
        ],
        "gifs": [
            "https://media.giphy.com/media/1BdIPyqzJmS6k/giphy.gif",
            "https://media.giphy.com/media/OkJat1YNdoD3W/giphy.gif",
            "https://media.giphy.com/media/l0MYOUI5XfRkBzP7K/giphy.gif",
            "https://media.giphy.com/media/jUwpNzg9IcyrK/giphy.gif",
            "https://media.giphy.com/media/d31vTpVi1LAcDvdm/giphy.gif"
        ]
    },
    "happy": {
        "quotes": [
            "Happiness is a direction, not a place 😊",
            "Smiles are contagious, spread them generously 😄"
        ],
        "jokes": [
            "What did one wall say to the other? I’ll meet you at the corner! 🧱",
            "Why don’t scientists trust atoms? Because they make up everything! ⚛️"
        ],
        "youtube": [
            "https://www.youtube.com/watch?v=ZbZSe6N_BXs",
            "https://www.youtube.com/watch?v=3GwjfUFyY6M"
        ],
        "spotify": [
            "https://open.spotify.com/playlist/37i9dQZF1DX3rxVfibe1L0"
        ],
        "gifs": [
            "https://media.giphy.com/media/l0MYC0LajbaPoEADu/giphy.gif",
            "https://media.giphy.com/media/5GoVLqeAOo6PK/giphy.gif",
            "https://media.giphy.com/media/xT0xeJpnrWC4XWblEk/giphy.gif",
            "https://media.giphy.com/media/12vJgj7zMN3yhy/giphy.gif",
            "https://media.giphy.com/media/3oriO0OEd9QIDdllqo/giphy.gif"
        ]
    },
    "sad": {
        "quotes": [
            "It’s okay to not be okay 💙",
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
        "spotify": [
            "https://open.spotify.com/playlist/37i9dQZF1DWVrtsSlLKzro"
        ],
        "gifs": [
            "https://media.giphy.com/media/d2lcHJTG5Tscg/giphy.gif",
            "https://media.giphy.com/media/l3vR9O8oGU6bG5FqY/giphy.gif",
            "https://media.giphy.com/media/UoeaPqYrimha6rdTFV/giphy.gif",
            "https://media.giphy.com/media/9Y5BbDSkSTiY8/giphy.gif",
            "https://media.giphy.com/media/ROF8OQvDmxytW/giphy.gif"
        ]
    },
    "angry": {
        "quotes": [
            "Breathe in, breathe out... you got this 🔥",
            "Even the darkest storm passes eventually 🌩️"
        ],
        "jokes": [
            "Why did the angry Jedi cross the road? To get to the Dark Side. 🌌",
            "I’m reading a book on anti-gravity — it’s impossible to put down! 😤"
        ],
        "youtube": [
            "https://www.youtube.com/watch?v=UfcAVejslrU",
            "https://www.youtube.com/watch?v=2vjPBrBU-TM"
        ],
        "spotify": [
            "https://open.spotify.com/playlist/37i9dQZF1DWX83CujKHHOn"
        ],
        "gifs": [
            "https://media.giphy.com/media/JmDpr42aq3K6w/giphy.gif",
            "https://media.giphy.com/media/l0ExncehJzexFpRHq/giphy.gif",
            "https://media.giphy.com/media/TqiwHbFBaZ4ti/giphy.gif",
            "https://media.giphy.com/media/3oz8xPqAvP2wQwJyTS/giphy.gif",
            "https://media.giphy.com/media/NLk1uVJADoEzu/giphy.gif"
        ]
    },
    "neutral": {
        "quotes": [
            "Keep going — sometimes staying still is still progress 🚶",
            "Balance is not something you find, it's something you create ⚖️"
        ],
        "jokes": [
            "What do you call a can opener that doesn’t work? A can’t opener! 🤖",
            "Parallel lines have so much in common. It’s a shame they’ll never meet. 🟰"
        ],
        "youtube": [
            "https://www.youtube.com/watch?v=d-diB65scQU",
            "https://www.youtube.com/watch?v=LHCob76kigA"
        ],
        "spotify": [
            "https://open.spotify.com/playlist/37i9dQZF1DX3Ogo9pFvBkY"
        ],
        "gifs": [
            "https://media.giphy.com/media/13CoXDiaCcCoyk/giphy.gif",
            "https://media.giphy.com/media/3o6Zt8MgUuvSbkZYWc/giphy.gif",
            "https://media.giphy.com/media/10tIjpzIu8fe0/giphy.gif",
            "https://media.giphy.com/media/l2JHRhAtnJSDNJ2py/giphy.gif",
            "https://media.giphy.com/media/l0MYB8Ory7Hqefo9a/giphy.gif"
        ]
    },
    "depressed": {
        "quotes": [
            "You’ve survived 100% of your bad days so far 💪",
            "Sometimes the bravest thing is just getting out of bed 🛏️"
        ],
        "jokes": [
            "Why don't skeletons fight each other? They don't have the guts. ☠️",
            "Why did the cookie go to the doctor? Because it felt crumby. 🍪"
        ],
        "youtube": [
            "https://www.youtube.com/watch?v=ioNng23DkIM",
            "https://www.youtube.com/watch?v=4N3N1MlvVc4"
        ],
        "spotify": [
            "https://open.spotify.com/playlist/37i9dQZF1DWVV27DiNWxkR"
        ],
        "gifs": [
            "https://media.giphy.com/media/3oz8xKaR836UJOYeOc/giphy.gif",
            "https://media.giphy.com/media/l0HlSNOxJB956qwfK/giphy.gif",
            "https://media.giphy.com/media/ZQLwf1DOZfkNa/giphy.gif",
            "https://media.giphy.com/media/4pk6ba2LUEMi4/giphy.gif",
            "https://media.giphy.com/media/26ufdipQqU2lhNA4g/giphy.gif"
        ]
    }
}

# ------------------ Mood Detection ------------------ #
def detect_mood(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    lower_text = text.lower()

    if any(word in lower_text for word in ["depressed", "hopeless", "suicidal"]):
        return "depressed"
    elif any(word in lower_text for word in ["happy", "great", "awesome", "excited", "cheerful", "fun"]):
        return "happy"
    elif any(word in lower_text for word in ["sad", "unhappy", "upset", "cry"]):
        return "sad"
    elif any(word in lower_text for word in ["angry", "mad", "furious", "annoyed"]):
        return "angry"
    elif any(word in lower_text for word in ["joy", "joyful", "delighted", "blessed"]):
        return "joyful"
    elif polarity > 0.5:
        return "joyful"
    elif polarity > 0:
        return "happy"
    elif polarity == 0:
        return "neutral"
    elif polarity > -0.5:
        return "sad"
    else:
        return "depressed"

# ------------------ Streamlit App ------------------ #
st.title("🧠 Conversational Mood Detector")
st.markdown("Answer a few questions below to let us detect your mood and suggest things for you.")

user_input = st.text_input("How are you feeling today?")

if user_input:
    try:
        mood = detect_mood(user_input)
        st.subheader(f"Your mood seems to be: **{mood.upper()}**")

        mood_info = mood_data[mood]
        st.markdown(f"### 🌟 Motivational Quote:\n> {random.choice(mood_info['quotes'])}")
        st.markdown(f"### 🎭 Here's something to make you smile:\n> {random.choice(mood_info['jokes'])}")
        st.markdown(f"### 📺 Watch this:\n[{mood_info['youtube'][0]}]({mood_info['youtube'][0]})")
        st.markdown(f"### 🎵 Music for your mood:\n[{mood_info['spotify'][0]}]({mood_info['spotify'][0]})")

        gif_url = random.choice(mood_info["gifs"])
        st.image(gif_url, caption=f"A visual vibe for your {mood} mood", use_column_width=True)

    except Exception as e:
        st.error(f"⚠ An error occurred: {e}")
