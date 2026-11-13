import streamlit as st
import random
from datetime import datetime

# =====================================
# CONTENT DATABASE
# =====================================

openings = [

    "Bandung dingin gini paling cocok ngopi ☕",
    "Kadang yang dicari dari kopi tuh tenangnya.",
    "Americano sore-sore emang beda vibes.",
    "Ngopi sambil hujan tuh combo terbaik.",
    "Cafe Bandung sekarang makin nyaman buat kerja."

]

topics = [

    "kopi pas hujan",
    "nongkrong malam",
    "cafe buat kerja",
    "weekend coffee vibes",
    "tempat chill Bandung",
    "kopi buat coding"

]

cta = [

    "Tim kopi susu atau americano?",
    "Ada rekomendasi tempat?",
    "Kalian lagi ngopi dimana sekarang?",
    "Siapa yang paling sering nongkrong di cafe?"

]

# =====================================
# POST GENERATOR
# =====================================

def generate_post():

    opening = random.choice(openings)

    topic = random.choice(topics)

    ending = random.choice(cta)

    return f"""
{opening}

{topic} emang cocok banget buat suasana Bandung.

{ending}
"""

# =====================================
# SCHEDULE
# =====================================

def generate_schedule():

    schedule = [
        "09:00",
        "13:00",
        "19:00"
    ]

    posts = []

    for time_slot in schedule:

        posts.append({

            "time": time_slot,

            "content": generate_post(),

            "likes": random.randint(
                10,
                120
            ),

            "comments": random.randint(
                1,
                20
            ),

            "status": random.choice([
                "Posted ✅",
                "Scheduled ⏳"
            ])

        })

    return posts

# =====================================
# UI
# =====================================

st.title(
    "📅 Dave Content Scheduler"
)

st.write(
    "AI-powered content planning simulator"
)

if st.button(
    "Generate Today's Schedule"
):

    schedule = generate_schedule()

    st.subheader(
        "Today's Schedule"
    )

    for item in schedule:

        st.markdown("---")

        st.subheader(
            f"🕒 {item['time']}"
        )

        st.write(
            item["status"]
        )

        st.info(
            item["content"]
        )

        st.write(
            f"❤️ Estimated Likes: {item['likes']}"
        )

        st.write(
            f"💬 Estimated Comments: {item['comments']}"
        )

        st.write(
            f"⏰ Generated: {datetime.now()}"
        )

st.markdown("---")

st.subheader(
    "✍ Generate Single Post"
)

if st.button(
    "Generate Post"
):

    st.success(
        generate_post()
    )

