import streamlit as st
from textblob import TextBlob

# App Config
st.set_page_config(page_title="Conversational Mood Detector", layout="centered")
st.title("🧠 Conversational Mood Detector")
st.markdown("Let’s talk and figure out how you’re really feeling today.")

# Setup session state
if "step" not in st.session_state:
    st.session_state.step = 1
    st.session_state.answers = []

# Mood Analysis Function
def analyze_mood(text_list):
    total = 0
    for text in text_list:
        sentiment = TextBlob(text).sentiment.polarity
        total += sentiment
    avg_sentiment = total / len(text_list)
    if avg_sentiment > 0.2:
        return "😊 Positive", [
            "🎵 Listen to upbeat music",
            "💪 Read a motivational quote",
            "📝 Try journaling your goals"
        ]
    elif avg_sentiment < -0.2:
        return "😟 Negative", [
            "🎧 Listen to calming sounds",
            "🗣️ Talk to someone close",
            "😂 Watch something light and funny"
        ]
    else:
        return "😐 Neutral", [
            "🚶 Take a short walk",
            "🧘 Meditate for 5 mins",
            "📖 Read a light story"
        ]

# Questions
questions = [
    "1️⃣ How are you feeling right now in one word?",
    "2️⃣ What kind of day have you had?",
    "3️⃣ What made you smile or annoyed you today?",
    "4️⃣ Would you rather talk to someone or be alone?",
    "5️⃣ Want music, a video, or just rest?"
]

# Form-based input for each question
if st.session_state.step <= len(questions):
    with st.form(key=f"form{st.session_state.step}"):
        answer = st.text_input(questions[st.session_state.step - 1])
        submitted = st.form_submit_button("Next")
        if submitted and answer:
            st.session_state.answers.append(answer)
            st.session_state.step += 1
else:
    # Final Mood Detection and Suggestions
    mood, suggestions = analyze_mood(st.session_state.answers)
    st.success(f"### Your Mood: {mood}")
    st.markdown("#### 💡 Suggestions for you:")
    for item in suggestions:
        st.markdown(f"- {item}")

    # Spotify + YouTube Links
    st.markdown("#### 🎶 Recommended Content:")
    if "Positive" in mood:
        st.markdown("🎵 [Feel Good Spotify Playlist](https://open.spotify.com/playlist/37i9dQZF1DX3rxVfibe1L0)")
        st.markdown("📺 [Motivational YouTube Video](https://youtu.be/ZXsQAXx_ao0)")
    elif "Negative" in mood:
        st.markdown("🎵 [Calm Down Spotify Playlist](https://open.spotify.com/playlist/37i9dQZF1DWUvHZA1zLcjW)")
        st.markdown("📺 [Relaxing YouTube Music](https://youtu.be/2OEL4P1Rz04)")
    else:
        st.markdown("🎵 [Chill Vibes Spotify Playlist](https://open.spotify.com/playlist/37i9dQZF1DX4WYpdgoIcn6)")
        st.markdown("📺 [Lo-fi YouTube Live Stream](https://youtu.be/5qap5aO4i9A)")

    # Restart Option
    if st.button("🔄 Restart"):
        st.session_state.clear()

