import streamlit as st
from textblob import TextBlob

st.set_page_config(page_title="Conversational Mood Detector", layout="centered")

st.markdown("## 🧠 Conversational Mood Detector")
st.markdown("Hi there! Let's talk and understand how you're feeling today 😊")

# Session state to track question flow
if "step" not in st.session_state:
    st.session_state.step = 1
    st.session_state.answers = []

def analyze_mood(text_list):
    total = 0
    for text in text_list:
        sentiment = TextBlob(text).sentiment.polarity
        total += sentiment
    avg_sentiment = total / len(text_list)
    if avg_sentiment > 0.2:
        return "😊 Positive", ["🎵 Upbeat music", "💪 Motivational quote", "📝 Try journaling"]
    elif avg_sentiment < -0.2:
        return "😟 Negative", ["🎧 Relaxing playlist", "🗣️ Talk to someone", "😂 Watch something funny"]
    else:
        return "😐 Neutral", ["🚶 Go for a walk", "🧘 Meditate", "📖 Read something light"]

# Question loop
questions = [
    "1️⃣ How are you feeling right now in one word?",
    "2️⃣ What kind of day have you had?",
    "3️⃣ What made you smile or annoyed you today?",
    "4️⃣ Would you rather talk to someone or be alone?",
    "5️⃣ Want music, a video, or just rest?"
]

if st.session_state.step <= len(questions):
    with st.form(key=f"form{st.session_state.step}"):
        answer = st.text_input(questions[st.session_state.step - 1])
        submitted = st.form_submit_button("Next")
        if submitted and answer:
            st.session_state.answers.append(answer)
            st.session_state.step += 1
else:
   # Show mood + suggestions + media links
mood, suggestions = analyze_mood(st.session_state.answers)
st.success(f"### Your Mood: {mood}")
st.markdown("#### 💡 Suggestions for you:")
for item in suggestions:
    st.markdown(f"- {item}")

# Show YouTube & Spotify links
if "Positive" in mood:
    st.markdown("🎵 [Listen on Spotify](https://open.spotify.com/playlist/37i9dQZF1DX3rxVfibe1L0)")
    st.markdown("📺 [Watch on YouTube](https://youtu.be/ZXsQAXx_ao0)")
elif "Negative" in mood:
    st.markdown("🎵 [Relax on Spotify](https://open.spotify.com/playlist/37i9dQZF1DWUvHZA1zLcjW)")
    st.markdown("📺 [Calm YouTube Video](https://youtu.be/2OEL4P1Rz04)")
else:
    st.markdown("🎵 [Chill Vibes on Spotify](https://open.spotify.com/playlist/37i9dQZF1DX4WYpdgoIcn6)")
    st.markdown("📺 [Lo-fi YouTube Stream](https://youtu.be/5qap5aO4i9A)")
, suggestions = analyze_mood(st.session_state.answers)
    st.success(f"### Your Mood: {mood}")
    st.markdown("#### 💡 Suggestions for you:")
    for item in suggestions:
        st.markdown(f"- {item}")
    if st.button("🔄 Restart"):
        st.session_state.clear()
