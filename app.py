import streamlit as st
from search import search_web
from synthesizer import synthesize_report
import os

st.set_page_config(page_title="Beacon", page_icon="🔦", layout="centered")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;600;700&display=swap');

* { font-family: 'Space Grotesk', sans-serif; }

body, .stApp {
    background-color: #0a0f1e;
    color: #e2e8f0;
}

.title {
    font-size: 3rem;
    font-weight: 700;
    color: #3b82f6;
    letter-spacing: -1px;
}

.subtitle {
    color: #64748b;
    font-size: 1rem;
    margin-bottom: 2rem;
}

.stTextInput > div > div > input {
    background: #111827;
    border: 1px solid #1e3a5f;
    border-radius: 8px;
    color: #e2e8f0;
    font-size: 1rem;
    padding: 0.75rem;
}

.stButton > button {
    background: #3b82f6;
    color: white;
    border: none;
    border-radius: 8px;
    padding: 0.6rem 2rem;
    font-weight: 600;
    font-size: 1rem;
    width: 100%;
    transition: background 0.2s;
}

.stButton > button:hover {
    background: #2563eb;
}

.report-box {
    background: #111827;
    border: 1px solid #1e3a5f;
    border-radius: 12px;
    padding: 2rem;
    margin-top: 1.5rem;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">🔦 Beacon</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Enter a topic. Get a research report in seconds.</div>', unsafe_allow_html=True)

topic = st.text_input("", placeholder="e.g. What is Retrieval Augmented Generation?")

if st.button("Run Research"):
    if topic.strip():
        with st.status("Running Beacon...", expanded=True) as status:
            st.write("🔍 Searching the web...")
            results = search_web(topic)
            pages = [r["content"] for r in results]

            st.write("🧠 Synthesizing report...")
            report = synthesize_report(topic, pages)

            os.makedirs("outputs", exist_ok=True)
            safe_topic = topic.replace(' ', '_').replace('?', '').replace('/', '').replace('\\', '')
            filename = f"outputs/{safe_topic}_report.md"
            with open(filename, "w") as f:
                f.write(report)

            status.update(label="Research complete!", state="complete")

        st.markdown('<div class="report-box">', unsafe_allow_html=True)
        st.markdown(report)
        st.markdown('</div>', unsafe_allow_html=True)

        with open(filename, "rb") as f:
            st.download_button("Download Report", f, file_name=f"{topic}_report.md")
    else:
        st.warning("Please enter a topic.")