import streamlit as st
from textblob import TextBlob
import random
import time

# ----------------------------- Data Setup -----------------------------
mood_keywords = {
    "happy": ["happy", "joy", "excited", "awesome", "great"],
    "sad": ["sad", "cry", "tears", "pain", "lonely"],
    "depressed": ["depressed", "suicide", "kill", "worthless", "quit", "over"],
    "neutral": ["ok", "fine", "normal", "nothing"],
    "angry": ["angry", "mad", "frustrated", "irritated"]
}

motivational_quotes = {
    "happy": [
        "Keep spreading the joy!",
        "Happiness is contagious — share it!",
        "Your smile lights up the day!",
        "Stay happy, stay bright!",
        # Add 20-30 more quotes here
    ],
    "sad": [
        "Tough times don’t last, tough people do.",
        "It’s okay to cry. Healing begins when we feel.",
        "Your story isn’t over yet. Keep going.",
        "You’re stronger than you think.",
        # Add 20-30 more quotes here
    ],
    "depressed": [
        "You are not alone. Please talk to someone you trust.",
        "Even the darkest night ends with sunrise.",
        "You're loved more than you know.",
        "Reach out. There’s always help and hope.",
        # Add 20-30 more quotes here
    ],
    "neutral": [
        "Every day is a new chance.",
        "Something amazing might happen today.",
        "Neutral today, shining tomorrow.",
        # Add 20-30 more quotes here
    ],
    "angry": [
        "Take a deep breath, you're in control.",
        "Anger is one letter short of danger. Breathe.",
        # Add 20-30 more quotes here
    ]
}

jokes = {
    "happy": [
        "Why don’t scientists trust atoms? Because they make up everything!",
        # Add 5-10 more jokes
    ],
    "sad": [
        "Why did the computer cry? Because it had a hard drive!",
        # Add 5-10 more jokes
    ],
    "depressed": [
        "What do you call a bear with no teeth? A gummy bear!",
        # Add 5-10 more jokes
    ],
    "neutral": [
        "What do you get when you cross a snowman and a vampire? Frostbite!",
        # Add 5-10 more jokes
    ],
    "angry": [
        "Why did the tomato turn red? Because it saw the salad dressing!",
        # Add 5-10 more jokes
    ]
}

gifs = {
    "happy": ["https://media.giphy.com/media/111ebonMs90YLu/giphy.gif"],
    "sad": ["https://media.giphy.com/media/l2JHRhAtnJSDNJ2py/giphy.gif"],
    "depressed": ["https://media.giphy.com/media/3og0IPxMM0erATueVW/giphy.gif"],
    "neutral": ["https://media.giphy.com/media/26gsjCZpPolPr3sBy/giphy.gif"],
    "angry": ["https://media.giphy.com/media/3ohhwp0HA8HVRc5vIc/giphy.gif"]
    # Add more gifs under each mood
}

youtube_links = {
    "happy": ["https://www.youtube.com/watch?v=ZbZSe6N_BXs"],
    "sad": ["https://www.youtube.com/watch?v=2vjPBrBU-TM"],
    "depressed": ["https://www.youtube.com/watch?v=2c6ZgFiZTnU"],
    "neutral": ["https://www.youtube.com/watch?v=JGwWNGJdvx8"],
    "angry": ["https://www.youtube.com/watch?v=K0ibBPhiaG0"]
}

spotify_links = {
    "happy": ["https://open.spotify.com/playlist/37i9dQZF1DXdPec7aLTmlC"],
    "sad": ["https://open.spotify.com/playlist/37i9dQZF1DX7qK8ma5wgG1"],
    "depressed": ["https://open.spotify.com/playlist/37i9dQZF1DX7gIoKXt0gmx"],
    "neutral": ["https://open.spotify.com/playlist/37i9dQZF1DX3rxVfibe1L0"],
    "angry": ["https://open.spotify.com/playlist/37i9dQZF1DWYQkbn99Zdi2"]
}

questions = [
    "How do you feel right now in one word?",
    "What’s the one thing on your mind today?",
    "What kind of day did you have today?",
    "Describe your mood using any emotion.",
    "What's the biggest feeling you had today?"
]

# ----------------------------- UI Setup -----------------------------
st.set_page_config(page_title="Conversational Mood Detector", layout="centered")
st.title("🧠 Conversational Mood Detector")

responses = []
for question in questions:
    ans = st.text_input(question, key=question)
    if ans:
        responses.append(ans.lower())
    else:
        st.stop()

# ----------------------------- Mood Detection -----------------------------
def detect_mood(texts):
    mood_scores = {mood: 0 for mood in mood_keywords}
    for text in texts:
        blob = TextBlob(text)
        for mood, words in mood_keywords.items():
            if any(word in text for word in words):
                mood_scores[mood] += 1
        if blob.sentiment.polarity > 0.4:
            mood_scores["happy"] += 1
        elif blob.sentiment.polarity < -0.4:
            mood_scores["depressed"] += 1
    return max(mood_scores, key=mood_scores.get)

final_mood = detect_mood(responses)
st.subheader(f"🌟 Detected Mood: `{final_mood.upper()}`")

# ----------------------------- Results -----------------------------
st.image(random.choice(gifs[final_mood]), width=400)
st.markdown(f"**🎧 Spotify Playlist:** [Listen Now]({random.choice(spotify_links[final_mood])})")
st.markdown(f"**📺 YouTube Video:** [Watch Now]({random.choice(youtube_links[final_mood])})")
st.success(random.choice(motivational_quotes[final_mood]))
st.info(random.choice(jokes[final_mood]))
