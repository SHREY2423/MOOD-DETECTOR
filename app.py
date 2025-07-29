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
            "What do you call a singing computer? A Dell! 🎤"
        ],
        "youtube": [
            "https://www.youtube.com/watch?v=3GwjfUFyY6M",
            "https://www.youtube.com/watch?v=ZbZSe6N_BXs"
        ],
        "spotify": ["https://open.spotify.com/playlist/37i9dQZF1DXdPec7aLTmlC"],
        "gifs": [
            "https://media.giphy.com/media/l0MYt5jPR6QX5pnqM/giphy.gif",
            "https://media.giphy.com/media/MDJ9IbxxvDUQM/giphy.gif",
            "https://media.giphy.com/media/5GoVLqeAOo6PK/giphy.gif",
            "https://media.giphy.com/media/1BcfiGlOGXzQf/giphy.gif"
        ]
    },
    "happy": {
        "quotes": [
            "Keep smiling, because life is a beautiful thing! 😊",
            "Happiness is contagious, spread it! 🌞"
        ],
        "jokes": [
            "Why don’t scientists trust atoms? Because they make up everything! 🤣",
            "Why did the scarecrow win an award? Because he was outstanding in his field! 🏆"
        ],
        "youtube": [
            "https://www.youtube.com/watch?v=60ItHLz5WEA",
            "https://www.youtube.com/watch?v=3GwjfUFyY6M"
        ],
        "spotify": ["https://open.spotify.com/playlist/37i9dQZF1DXdPec7aLTmlC"],
        "gifs": [
            "https://media.giphy.com/media/yoJC2A59OCZHs1LXvW/giphy.gif",
            "https://media.giphy.com/media/l0MYt5jPR6QX5pnqM/giphy.gif",
            "https://media.giphy.com/media/l0Exk8EUzSLsrErEQ/giphy.gif",
            "https://media.giphy.com/media/1xVhmN8RxFzvO/giphy.gif"
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
            "https://www.youtube.com/watch?v=RB-RcX5DS5A",
            "https://www.youtube.com/watch?v=2vjPBrBU-TM"
        ],
        "spotify": ["https://open.spotify.com/playlist/37i9dQZF1DX7qK8ma5wgG1"],
        "gifs": [
            "https://media.giphy.com/media/3oz8xKaR836UJOYeOc/giphy.gif",
            "https://media.giphy.com/media/d2lcHJTG5Tscg/giphy.gif",
            "https://media.giphy.com/media/d9C1LdY7y3M7a/giphy.gif",
            "https://media.giphy.com/media/ROF8OQvDmxytW/giphy.gif"
        ]
    },
    "angry": {
        "quotes": [
            "Calm is a superpower. 🧘",
            "Breathe. It’s just a bad day, not a bad life. 🌪"
        ],
        "jokes": [
            "Why don’t skeletons fight each other? They don’t have the guts. 💀",
            "I'm not arguing, I'm just passionately expressing my rightness 😤"
        ],
        "youtube": [
            "https://www.youtube.com/watch?v=kXYiU_JCYtU"
        ],
        "spotify": ["https://open.spotify.com/playlist/37i9dQZF1DX76Wlfdnj7AP"],
        "gifs": [
            "https://media.giphy.com/media/IThjAlJnD9WNO/giphy.gif",
            "https://media.giphy.com/media/xUOwFUXF1GG2cZs3ok/giphy.gif",
            "https://media.giphy.com/media/8YutMatqkTfSE/giphy.gif",
            "https://media.giphy.com/media/hPPx8yk3Bmqys/giphy.gif"
        ]
    },
    "neutral": {
        "quotes": [
            "Stay grounded. Everything will fall into place. 🌱",
            "Just breathe, you’ve got this. 🌈"
        ],
        "jokes": [
            "Why can’t your nose be 12 inches long? Because then it would be a foot! 👃🤣",
            "What do you call cheese that isn't yours? Nacho cheese! 🧀"
        ],
        "youtube": [
            "https://www.youtube.com/watch?v=hHW1oY26kxQ"
        ],
        "spotify": ["https://open.spotify.com/playlist/37i9dQZF1DX6VdMW310YC7"],
        "gifs": [
            "https://media.giphy.com/media/xT1R9ZzU4dU6lV1p7G/giphy.gif",
            "https://media.giphy.com/media/3oEjHKP0D0V4DjdQU8/giphy.gif",
            "https://media.giphy.com/media/l1J3preURPiwjRPvG/giphy.gif",
            "https://media.giphy.com/media/3o7TKP9ln8y7B5U0K0/giphy.gif"
        ]
    },
    "depressed": {
        "quotes": [
            "You're not alone. This too shall pass. 🌧",
            "Every storm runs out of rain. 🌦"
        ],
        "jokes": [
            "Why did the chicken go to therapy? To get to the other side of its emotions. 🐔",
            "What’s a depressed person’s favorite food? Anything with serotonin! 😅"
        ],
        "youtube": [
            "https://www.youtube.com/watch?v=w6T02g5hnT4",
            "https://www.youtube.com/watch?v=2vEStDd6HVY"
        ],
        "spotify": ["https://open.spotify.com/playlist/37i9dQZF1DWVrtsSlLKzro"],
        "gifs": [
            "https://media.giphy.com/media/l0HlJzQ9312VRFMBW/giphy.gif",
            "https://media.giphy.com/media/Z5zuypbEO1FqM/giphy.gif",
            "https://media.giphy.com/media/3ohjUWSQF9MLFzrQn6/giphy.gif",
            "https://media.giphy.com/media/TgmiJ4AZ3HSiIqpOj6/giphy.gif"
        ]
    }
}
