# Main Streamlit App
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
        return "😊 Positive", ["Upbeat music", "Motivational quote", "Try journaling"]
    elif avg_sentiment < -0.2:
        return "😟 Negative", ["Relaxing playlist", "Talk to someone", "Watch something funny"]
    else:
        return "😐 Neutral", ["Go for a walk", "Meditate", "Read something light"]

# Question loop
questions = [
    "1️⃣ How are you feeling right now in one word?",
    "2️⃣ What kind of day have you had?",
    "3️⃣ What made you smile or annoyed you today?",
    "4️⃣ Would you rather talk to someone or be alone?",
    "5️⃣ Want music, a video, or just rest?"
]

if st.session_state.step <= len(questions):
    answer = st.text_input(questions[st.session_state.step - 1], key=f"q{st.session_state.step}")
    if answer:
        st.session_state.answers.append(answer)
        st.session_state.step += 1
        st.experimental_rerun()
else:
    mood, suggestions = analyze_mood(st.session_state.answers)
    st.success(f"### Your Mood: {mood}")
    st.markdown("#### 💡 Suggestions for you:")
    for item in suggestions:
        st.markdown(f"- {item}")
    st.button("🔄 Restart", on_click=lambda: st.session_state.clear())
