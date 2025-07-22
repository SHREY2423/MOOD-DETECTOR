import streamlit as st
from textblob import TextBlob
from transformers import pipeline
import random
import time

# Sentiment pipeline
classifier = pipeline("sentiment-analysis")

# Mood-specific data
motivational_quotes = {
    "happy": [
        "Happiness is not something ready made. It comes from your own actions. – Dalai Lama",
        "The purpose of our lives is to be happy. – Dalai Lama",
        "Happiness depends upon ourselves. – Aristotle",
        "Smile, and let the world wonder why.",
        "Choose happiness daily and you’ll find joy in every moment.",
        "Enjoy the little things in life.",
        "Happiness is the highest level of success.",
        "Good vibes only.",
        "Be the reason someone smiles today.",
        "Joy is a decision, not a condition.",
        "Happiness is contagious, spread it.",
        "Focus on what makes you feel alive.",
        "Happiness is homemade.",
        "You deserve happiness.",
        "Think happy. Be happy.",
        "Celebrate every tiny victory.",
        "Gratitude unlocks joy.",
        "Life is beautiful, notice it.",
        "You glow differently when you're happy.",
        "Stay close to what feels like sunshine.",
        "Live life in full bloom.",
        "Create your own sunshine.",
        "You attract what you radiate.",
        "Your vibe attracts your tribe.",
        "Smiles are free but priceless.",
        "Positive mind, positive life.",
        "Be happy—it drives people crazy!",
        "Laughter is timeless, imagination has no age.",
        "Collect moments, not things.",
        "Shine bright, always."
    ],
    "sad": [
        "This too shall pass.",
        "Every storm runs out of rain. — Maya Angelou",
        "Sadness flies away on the wings of time. — Jean de La Fontaine",
        "Healing takes time, and that's okay.",
        "It’s okay not to be okay.",
        "The sun will rise and we will try again.",
        "Tears are words the heart can't say.",
        "Sometimes you have to know sadness to appreciate happiness.",
        "Be gentle with yourself. You're doing the best you can.",
        "Even the darkest night will end and the sun will rise.",
        "You’re stronger than you think.",
        "Crying isn’t a weakness.",
        "It's okay to rest.",
        "Healing begins with acceptance.",
        "Let it hurt, then let it go.",
        "You are not alone.",
        "Take your time, one day at a time.",
        "Everything you feel is valid.",
        "It’s brave to ask for help.",
        "Hope is real.",
        "It’s okay to feel lost.",
        "Your feelings matter.",
        "Storms don’t last forever.",
        "Be proud of how far you’ve come.",
        "Small steps still move you forward.",
        "You're allowed to feel everything.",
        "Time heals. Be patient.",
        "Even broken crayons still color.",
        "Pain is temporary.",
        "Stay. You’re not alone."
    ],
    "depressed": [
        "You are not alone. Talk to someone you trust.",
        "The darkest hour has only sixty minutes.",
        "You’ve made it through 100% of your worst days. Keep going.",
        "Your presence matters. You matter.",
        "Reach out — someone cares.",
        "One small step is still progress.",
        "It’s okay to ask for help. That’s strength, not weakness.",
        "Don’t give up now, your future self is waiting.",
        "You are needed. You are loved.",
        "Even the strongest feel weak sometimes. Rest, then rise.",
        "You can start over each day.",
        "Mental pain is real. Healing is too.",
        "You are stronger than your thoughts.",
        "Never be ashamed of your story.",
        "Depression lies — don’t listen.",
        "There’s hope, even when your brain tells you there isn’t.",
        "Don’t suffer in silence. Talk to a friend or professional.",
        "Suicidal thoughts do not define you.",
        "Stay. There’s more life for you to live.",
        "Healing is not linear, but you’re healing."
    ]
}

spotify_links = {
    "happy": [
        "https://open.spotify.com/playlist/37i9dQZF1DXdPec7aLTmlC",
        "https://open.spotify.com/playlist/37i9dQZF1DWYBO1MoTDhZI",
        "https://open.spotify.com/playlist/37i9dQZF1DX3rxVfibe1L0"
    ],
    "sad": [
        "https://open.spotify.com/playlist/37i9dQZF1DWVrtsSlLKzro",
        "https://open.spotify.com/playlist/37i9dQZF1DX7qK8ma5wgG1",
        "https://open.spotify.com/playlist/37i9dQZF1DX3YSRoSdA634"
    ],
    "depressed": [
        "https://open.spotify.com/playlist/37i9dQZF1DX7gIoKXt0gmx",
        "https://open.spotify.com/playlist/37i9dQZF1DX3YSRoSdA634"
    ]
}

youtube_links = {
    "happy": [
        "https://youtu.be/ZbZSe6N_BXs",  # Happy - Pharrell Williams
        "https://youtu.be/y6Sxv-sUYtM"
    ],
    "sad": [
        "https://youtu.be/7qEHsqek33s",  # Lewis Capaldi - Someone You Loved
        "https://youtu.be/Jk1nw4Uoxig"
    ],
    "depressed": [
        "https://youtu.be/2vjPBrBU-TM",  # Sia - Chandelier
        "https://youtu.be/M6sSOhLftK4"
    ]
}

# Suicide/depression keywords
depression_keywords = ["depressed", "suicide", "kill myself", "no one cares", "worthless", "hopeless"]

# Streamlit UI
st.set_page_config(page_title="Conversational Mood Detector", layout="centered")
st.title("🧠 Conversational Mood Detector")
st.write("Hi! Let's understand how you're feeling today. Please answer the following questions.")

questions = [
    "1️⃣ How are you feeling right now (in one word)?",
    "2️⃣ What kind of day did you have?",
    "3️⃣ Describe your mood using a short sentence.",
    "4️⃣ Are you feeling motivated or tired?",
    "5️⃣ Do you feel like talking to someone?"
]

responses = []

for q in questions:
    response = st.text_input(q, key=q)
    if response:
        responses.append(response)
        time.sleep(0.5)

if len(responses) == len(questions):
    full_text = " ".join(responses).lower()

    # Check for depression keywords
    if any(word in full_text for word in depression_keywords):
        mood = "depressed"
    else:
        sentiment = classifier(full_text)[0]
        polarity = TextBlob(full_text).sentiment.polarity

        if sentiment['label'] == "POSITIVE" and polarity > 0.2:
            mood = "happy"
        elif sentiment['label'] == "NEGATIVE" and polarity < -0.2:
            mood = "sad"
        else:
            mood = "neutral"

    st.subheader(f"🧠 Predicted Mood: **{mood.upper()}**")

    # Show motivational quote
    if mood in motivational_quotes:
        st.info(f"💡 {random.choice(motivational_quotes[mood])}")

    # Show Spotify links
    if mood in spotify_links:
        st.markdown("🎧 **Spotify Playlist:**")
        for link in spotify_links[mood]:
            st.markdown(f"- [Open Playlist]({link})")

    # Show YouTube videos
    if mood in youtube_links:
        st.markdown("📺 **YouTube Videos:**")
        for link in youtube_links[mood]:
            st.markdown(f"- [Watch Video]({link})")
else:
    st.warning("👉 Please answer all the questions above.")

