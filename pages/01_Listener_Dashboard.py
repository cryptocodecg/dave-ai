import streamlit as st
import requests
import random
import os
from datetime import datetime, timedelta

# ====================================
# TELEGRAM CONFIG
# ====================================

TELEGRAM_BOT_TOKEN = os.getenv(
    "TELEGRAM_BOT_TOKEN",
    ""
)

TELEGRAM_CHAT_ID = os.getenv(
    "TELEGRAM_CHAT_ID",
    ""
)

# ====================================
# MEMORY
# ====================================

if "history" not in st.session_state:
    st.session_state.history = []

# ====================================
# TELEGRAM
# ====================================

def send_telegram(message):

    if not TELEGRAM_BOT_TOKEN:
        return

    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"

    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message
    }

    try:
        requests.post(url, data=payload)
    except:
        pass

# ====================================
# LOCAL FILTER
# ====================================

def local_filter(text):

    keywords = [
        "bandung",
        "kopi",
        "coffee",
        "cafe",
        "buah batu",
        "latte",
        "espresso",
        "barista",
        "nongkrong",
        "wfc"
    ]

    return any(
        k in text.lower()
        for k in keywords
    )

# ====================================
# SCORE
# ====================================

def score_post(text):

    score = 0

    if len(text) > 15:
        score += 2

    if "?" in text:
        score += 2

    if local_filter(text):
        score += 3

    if any(
        word in text.lower()
        for word in [
            "nyari",
            "cari",
            "rekomendasi",
            "mana",
            "dimana"
        ]
    ):
        score += 2

    return min(score, 10)

# ====================================
# REPLY ENGINE
# ====================================

def generate_reply(text):

    text = text.lower()

    if "buah batu" in text:

        replies = [
            "Buah Batu sekarang banyak spot ngopi menarik ☕",
            "Sekitar Buah Batu ada beberapa tempat yang nyaman buat nongkrong ☕",
            "Biasanya cari yang buat kerja atau santai nih? 😄"
        ]

    elif "americano" in text:

        replies = [
            "Tim americano nih ☕",
            "Americano dingin memang cocok buat siang Bandung 😄",
            "Kalau americano biasanya suka karakter kopi yang clean ☕"
        ]

    elif "wifi" in text:

        replies = [
            "Wifi kenceng memang wajib 😄",
            "Apalagi kalau lagi deadline ☕",
            "Cari tempat yang nyaman juga penting 😄"
        ]

    elif "hujan" in text:

        replies = [
            "Bandung + hujan + kopi = combo terbaik ☕",
            "Cuaca begini memang bikin pengen ngopi 😄",
            "Saatnya cari tempat hangat ☕"
        ]

    elif "kopi" in text:

        replies = [
            "Ngomongin kopi memang gak ada habisnya ☕",
            "Tim arabica atau robusta nih? ☕",
            "Kopi favoritmu apa? 😄"
        ]

    else:

        replies = [
            "Menarik juga 😄",
            "Wah seru juga topiknya 😄",
            "Boleh cerita lebih lanjut? ☕"
        ]

    return random.choice(replies)

# ====================================
# DATA
# ====================================

fake_posts = [

    {"username":"@andi_ngopi","text":"lagi nyari kopi enak di buah batu"},
    {"username":"@kopisore","text":"americano dingin enak dimana?"},
    {"username":"@anakbandung","text":"hujan gini pengen ngopi"},
    {"username":"@mahasiswaitb","text":"wifi cafe yang kenceng dimana?"},
    {"username":"@freelancerid","text":"tempat wfc sekitar bandung?"},
    {"username":"@ngopimalam","text":"nongkrong malam enaknya dimana?"}

]

# ====================================
# UI
# ====================================

st.title("🎧 Dave AI Listener Dashboard")

st.write(
    "Social Listening + AI Reply + Telegram Alert"
)

col1,col2,col3,col4 = st.columns(4)

col1.metric(
    "Posts",
    len(fake_posts)
)

col2.metric(
    "Replies",
    len(fake_posts)
)

col3.metric(
    "Potential Leads",
    "4"
)

col4.metric(
    "Alerts",
    "4"
)

if st.button("🚀 Run Dave Listener"):

    now = datetime.now()

    for i,item in enumerate(fake_posts):

        username = item["username"]
        post = item["text"]

        timestamp = now - timedelta(
            minutes=i*5
        )

        score = score_post(post)

        reply = generate_reply(post)

        st.markdown("---")

        st.write(
            f"👤 {username}"
        )

        st.write(
            f"⏰ {timestamp.strftime('%H:%M:%S')}"
        )

        st.write(
            f"📝 {post}"
        )

        st.write(
            f"🤖 {reply}"
        )

        st.write(
            f"📊 Score: {score}"
        )

        if score >= 6:

            send_telegram(
f"""
☕ Dave Alert

User:
{username}

Post:
{post}

Reply:
{reply}

Score:
{score}
"""
            )

            st.success(
                "Telegram Alert Sent"
            )

        st.session_state.history.append({

            "username": username,
            "post": post,
            "reply": reply,
            "score": score

        })

st.markdown("---")

st.subheader(
    "🧠 Recent Activity"
)

for item in reversed(
    st.session_state.history[-10:]
):
    st.write(item)

