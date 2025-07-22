import streamlit as st
from textblob import TextBlob
import random
import time

st.set_page_config(page_title="🧠 Conversational Mood Detector", layout="centered")
st.markdown("""
    <style>
    .big-font {font-size:30px !important; text-align: center;}
    .stTextInput>div>div>input {text-align: center; font-size: 20px;}
    .stButton>button {width: 100%;}
    </style>
""", unsafe_allow_html=True)

st.title("🧠 Conversational Mood Detector")
st.markdown("## Let's talk and discover how you're truly feeling 😊")

# Mood keywords for training-like matching (instead of full ML training)
mood_keywords = {
    "happy": ["happy", "good", "awesome", "excited", "great"],
    "sad": ["sad", "unhappy", "down", "gloomy", "cry"],
    "depressed": ["depressed", "suicide", "kill me", "worthless", "over", "done", "hopeless", "lonely", "quit"],
    "neutral": ["okay", "fine", "normal", "meh", "alright"],
    "angry": ["angry", "mad", "furious", "annoyed", "pissed"]
}

# Motivational quotes
quotes = {
    "happy": ["Keep smiling, it makes people wonder what you're up to!", "Happiness is contagious. Share it!", "Joy is the simplest form of gratitude."] * 10,
    "sad": ["This too shall pass.", "Tough times never last, but tough people do.", "You're stronger than you think."] * 10,
    "depressed": ["You matter. Don’t give up.", "Talk to someone. You are not alone.", "Even the darkest night ends with dawn."] * 10,
    "neutral": ["Balance is beautiful.", "Sometimes doing nothing is doing something.", "Embrace the pause."] * 10,
    "angry": ["Take a deep breath. You’re in control.", "Anger is just one letter away from danger.", "Walk away. Clear your head."] * 10
}

# Jokes
jokes = {
    "happy": ["Why don’t scientists trust atoms? Because they make up everything!", "I told my computer I needed a break, and it said: 'No problem, I’ll go to sleep.'"] * 5,
    "sad": ["Why don’t skeletons fight each other? They don’t have the guts.", "What did one wall say to the other? I’ll meet you at the corner."] * 5,
    "depressed": ["Why did the scarecrow win an award? Because he was outstanding in his field.", "I tried to catch some fog earlier. I mist."] * 5,
    "neutral": ["Why can’t your nose be 12 inches long? Because then it would be a foot!", "What do you call a fake noodle? A
