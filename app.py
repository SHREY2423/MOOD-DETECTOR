import streamlit as st
from textblob import TextBlob
import random
import time

# Define questions to ask
questions = [
    "How are you feeling right now in one word?",
    "What was the highlight of your day?",
    "Is there anything troubling you today?",
    "Do you feel like talking to someone?",
    "What kind of music do you enjoy lately?",
    "Are you looking forward to something this week?",
]

# Extended motivational quotes
motivational_quotes = [
    "Keep going, you're doing great!",
    "This too shall pass.",
    "You are stronger than you think.",
    "Every day is a second chance.",
    "Difficult roads often lead to beautiful destinations.",
    "Believe in yourself and all that you are.",
    "Your potential is endless.",
    "The comeback is always stronger than the setback.",
    "Don’t give up. Great things take time.",
    "You’re not alone, and you matter.",
    "Choose to be optimistic, it feels better.",
    "Small steps every day lead to big results.",
    "Storms make trees take deeper roots.",
    "The best view comes after the hardest climb.",
    "Pain is temporary. Growth is permanent.",
    "You’ve survived 100% of your worst days.",
    "Rise above the storm and you will find sunshine.",
    "The only way out is through.",
    "Take it day by day, step by step.",
    "Be gentle with yourself, you're doing the best you can.",
    "You’re allowed to rest, not quit.",
    "You are not your thoughts. You are the observer.",
    "Life is tough but so are you.",
    "Progress, not perfection.",
    "It’s okay to not be okay.",
    "You have the power to create change.",
    "You are worthy of love and support.",
    "Don't count the days, make the days count.",
    "Fall seven times, stand up eight.",
    "Your story isn't over yet.",
]

# Jokes by mood
jokes = {
    "happy": [
        "Why don’t scientists trust atoms? Because they make up everything!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "I told my computer I needed a break, and it said 'no problem, I'll go to sleep too.'",
        "How does the ocean say hi? It waves!",
    ],
    "sad": [
        "Why don’t skeletons fight each other? They don’t have the guts.",
        "Why did the math book look sad? Because it had too many problems.",
        "Feeling blue? Here's a smile 🙂",
        "Life may be cloudy now, but the sun always returns. 🌞",
    ],
    "neutral": [
        "Why did the tomato turn red? Because it saw the salad dressing!",
        "Parallel lines have so much in common… it’s a shame they’ll never meet.",
    ],
    "depressed": [
        "You matter. Don’t let your brain convince you otherwise.",
        "Even on your worst days, you are loved and needed.",
    ]
}

# Mood detection keywords
mood_keywords = {
    "depressed": ["depressed", "suicide", "end it", "worthless", "kill myself", "over it", "give up", "nothing left"],
    "sad": ["sad", "unhappy", "cry", "bad mood", "lonely", "broken"],
    "happy": ["happy", "joyful", "excited", "great", "fantastic", "awesome"],
    "neutral": ["okay", "fine", "alright", "meh"]
}

# Gifs by mood
gif_urls = {
    "happy": [
        "https://media.giphy.com/media/yoJC2A59OCZHs1LXvW/giphy.gif",
        "https://media.giphy.com/media/l4FGuhL4U2WyjdkaY/giphy.gif",
    ],
    "sad": [
        "https://media.giphy.com/media/d2lcHJTG5Tscg/giphy.gif",
        "https://media.giphy.com/media/ROF8OQvDmxytW/giphy.gif",
    ],
    "neutral": [
        "https://media.giphy.com/media/3o6ZsX2dNwltku5PZm/giphy.gif",
    ],
    "depressed": [
        "https://media.giphy.com/media/3orieX3dQmr7j3lwTC/giphy.gif",
        "https://media.giphy.com/media/3o6Zt8zb1P4b8QJJgk/giphy.gif",
    ]
}

# Spotify & YouTube suggestions by mood
media_links = {
    "happy": [
        "https://open.spotify.com/playlist/37i9dQZF1DXdPec7aLTmlC",
        "https://www.youtube.com/watch?v=ZbZSe6N_BXs",
    ],
    "sad": [
        "https://open.spotify.com/playlist/37i9dQZF1DX3rxVfibe1L0",
        "https://www.youtube.com/watch?v=hoNb6HuNmU0",
    ],
    "neutral": [
        "https://open.spotify.com/playlist/37i9dQZF1DX4WYpdgoIcn6",
        "https://www.youtube.com/watch?v=RgKAFK5djSk",
    ],
    "depressed": [
        "https://open.spotify.com/playlist/37i9dQZF1DWZqd5JICZI0u",
        "https://www.youtube.com/watch?v=hLQl3WQQoQ0",
    ]
}

st.set_page_config(page_title="Conversational Mood Detector", layout="centered")
st.title("🧠 Conversational Mood Detector")
st.markdown("Let's talk and understand how you're feeling today 😊")

if 'answers' not in st.session_state:
    st.session_state.answers = []
if 'current_question' not in st.session_state:
    st.session_state.current_question = 0
if 'mood' not in st.session_state:
    st.session_state.mood = ""

if st.session_state.current_question < len(questions):
    answer = st.text_input(questions[st.session_state.current_question], key=str(st.session_state.current_question))
    if answer:
        st.session_state.answers.append(answer)
        st.session_state.current_question += 1
        st.experimental_rerun()
else:
    combined_text = " ".join(st.session_state.answers).lower()
    detected_mood = "neutral"

    for mood, keywords in mood_keywords.items():
        if any(word in combined_text for word in keywords):
            detected_mood = mood
            break

    blob = TextBlob(combined_text)
    polarity = blob.sentiment.polarity
    if polarity > 0.2:
        detected_mood = "happy"
    elif polarity < -0.3:
        if detected_mood != "depressed":
            detected_mood = "sad"

    st.session_state.mood = detected_mood

    st.subheader(f"Your Mood: {detected_mood.capitalize()} 💬")
    st.image(random.choice(gif_urls.get(detected_mood, [])), use_column_width=True)

    st.markdown(f"**Quote for You** ✨\n> {random.choice(motivational_quotes)}")

    st.markdown("---")
    st.markdown(f"**Here's something to cheer you up!** 🎵🎬")
    for link in media_links.get(detected_mood, []):
        st.markdown(f"🔗 [Open Link]({link})")

    st.markdown("---")
    st.markdown(f"**Here’s a joke to lighten your mood** 😄\n- {random.choice(jokes.get(detected_mood, []))}")

    if st.button("🔁 Restart"):
        st.session_state.answers = []
        st.session_state.current_question = 0
        st.session_state.mood = ""
        st.experimental_rerun()

# Footer decoration or extra creative UI element
st.markdown("<div style='margin-top: 30px; text-align: center;'>🤖 Made with ❤️ by AI — Your Mood Companion</div>", unsafe_allow_html=True)
