import streamlit as st

st.set_page_config(
    page_title="Dave AI Social Media Agent",
    page_icon="☕",
    layout="wide"
)

st.title("☕ Dave AI Social Media Agent")

st.markdown("""
### Welcome to Dave AI

Dave AI helps coffee businesses:

✅ Generate content ideas

✅ Simulate social listening

✅ Recommend replies

✅ Score engagement opportunities

✅ Send Telegram notifications

✅ Plan daily posting schedules

---

Use the menu on the left to access:

🎧 Listener Dashboard

📅 Content Scheduler
""")

st.info(
    "Select a module from the sidebar."
)

col1, col2, col3 = st.columns(3)

col1.metric(
    "AI Modules",
    "2"
)

col2.metric(
    "Version",
    "V1 Demo"
)

col3.metric(
    "Status",
    "Running"
)

