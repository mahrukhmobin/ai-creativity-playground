# app.py
import streamlit as st
import requests
from dotenv import load_dotenv
import os
from streamlit_lottie import st_lottie
import fitz  # PyMuPDF
from docx import Document
import io

# Load environment variables
load_dotenv()
API_KEY = os.getenv("GROQ_API_KEY")

st.set_page_config(
    page_title="AI Creativity Playground 🎨",
    layout="centered",
    page_icon="🎨"
)

def load_lottie_url(url):
    try:
        r = requests.get(url)
        if r.status_code == 200:
            return r.json()
    except:
        return None

ai_animation = load_lottie_url("https://lottie.host/67f1d10d-4d0d-4c99-a889-55b37e993b76/RSTX8aZ5u2.json")

st.markdown("<h1 style='text-align: center; color: #d63384;'>🌈 AI Creativity Playground</h1>", unsafe_allow_html=True)
if ai_animation:
    st_lottie(ai_animation, height=250, speed=1)

def word_count_slider(label):
    return st.slider(label, 50, 500, step=50, value=150)

def generate_text(prompt, word_limit):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    body = {
        "model": "llama-3.3-70b-versatile",
        "messages": [
            {"role": "system", "content": "You are a creative assistant."},
            {"role": "user", "content": f"{prompt}. Limit around {word_limit} words. End with a complete sentence."}
        ],
        "temperature": 0.9
    }
    try:
        res = requests.post("https://api.groq.com/openai/v1/chat/completions", headers=headers, json=body)
        res.raise_for_status()
        return res.json()["choices"][0]["message"]["content"].strip()
    except Exception as e:
        return f"⚠ Error: {e}"

languages = ["English", "Urdu", "Spanish", "French", "Arabic", "Chinese", "German", "Hindi", "Turkish", "Japanese", "Russian", "Portuguese"]

tabs = st.tabs(["📖 Story Generator", "📝 Poem Creator", "😂 Emoji Story", "🎯 Slogan Generator", "📘 Study Notes Generator", "🧹 Essay Improver"])

# --- STORY ---
with tabs[0]:
    st.subheader("📖 Create a Magical Story")
    st.session_state.story_input = st.text_input("💡 What's your story idea?", st.session_state.get("story_input", ""))
    lang = st.selectbox("🌐 Select story language", languages, key="story_lang")
    word_limit = word_count_slider("🔢 Select word limit for story")
    out = st.empty()
    if st.button("✨ Generate Story", key="story_btn"):
        if st.session_state.story_input:
            result = generate_text(f"Write a creative story about: {st.session_state.story_input}. Write it in {lang}.", word_limit)
            out.success("✅ Story Generated:")
            out.markdown(result.replace("\n", "  \n"))
        else:
            out.warning("🚨 Please enter a story idea.")
    if st.button("🧹 Clear Chat", key="clear_story"):
        st.session_state.story_input = ""
        out.empty()
        st.rerun()

# --- POEM ---
with tabs[1]:
    st.subheader("📝 Compose a Beautiful Poem")
    st.session_state.poem_input = st.text_input("🌸 Poem topic", st.session_state.get("poem_input", ""))
    lang = st.selectbox("🌐 Select poem language", languages, key="poem_lang")
    word_limit = word_count_slider("🔢 Select word limit for poem")
    out = st.empty()
    if st.button("🧠 Generate Poem", key="poem_btn"):
        if st.session_state.poem_input:
            prompt = f"Write a poem on: {st.session_state.poem_input}. Format it in poetic verse — each line on a new line. Use 2–4 lines per stanza and separate stanzas with blank lines. Avoid writing it as a paragraph. Write it in {lang}."
            result = generate_text(prompt, word_limit)
            out.success("✅ Poem Generated:")
            out.markdown(result.replace("\n", "  \n"))
        else:
            out.warning("🚨 Please enter a poem topic.")
    if st.button("🧹 Clear Chat", key="clear_poem"):
        st.session_state.poem_input = ""
        out.empty()
        st.rerun()

# --- EMOJI STORY ---
with tabs[2]:
    st.subheader("😂 Tell a Story with Emojis")
    st.session_state.emoji_input = st.text_input("🎭 Fun theme or scenario", st.session_state.get("emoji_input", ""))
    lang = st.selectbox("🌐 Select emoji story language", languages, key="emoji_lang")
    word_limit = word_count_slider("🔢 Select word limit for emoji story")
    out = st.empty()
    if st.button("😄 Generate Emoji Story", key="emoji_btn"):
        if st.session_state.emoji_input:
            result = generate_text(f"Write a funny and creative emoji story about: {st.session_state.emoji_input}. Write it in {lang}.", word_limit)
            out.success("✅ Emoji Story Generated:")
            out.markdown(result.replace("\n", "  \n"))
        else:
            out.warning("🚨 Please enter a fun theme.")
    if st.button("🧹 Clear Chat", key="clear_emoji"):
        st.session_state.emoji_input = ""
        out.empty()
        st.rerun()

# --- SLOGAN GENERATOR ---
with tabs[3]:
    st.subheader("🎯 Generate a Catchy Slogan")
    st.session_state.slogan_input = st.text_input("💬 What's the product, brand, or concept?", st.session_state.get("slogan_input", ""))
    lang = st.selectbox("🌐 Select slogan language", languages, key="slogan_lang")
    word_limit = word_count_slider("🔢 Select word limit for slogan")
    out = st.empty()
    if st.button("🚀 Generate Slogan", key="slogan_btn"):
        if st.session_state.slogan_input:
            result = generate_text(f"Create a creative and impactful slogan for: {st.session_state.slogan_input}. Write it in {lang}.", word_limit)
            out.success("✅ Slogan Generated:")
            out.markdown(result.replace("\n", "  \n"))
        else:
            out.warning("🚨 Please enter a slogan idea.")
    if st.button("🧹 Clear Chat", key="clear_slogan"):
        st.session_state.slogan_input = ""
        out.empty()
        st.rerun()

# --- STUDY NOTES GENERATOR ---
with tabs[4]:
    st.subheader("📘 Study Notes Generator")

    input_mode = st.radio("📥 Input Method", ["✍ Paste Text", "📂 Upload File"], horizontal=True)
    text_input = ""

    if input_mode == "✍ Paste Text":
        st.session_state.notes_input = st.text_area("📖 Paste your study material", st.session_state.get("notes_input", ""))
        text_input = st.session_state.notes_input
    else:
        uploaded_file = st.file_uploader("📂 Upload a file (.txt, .pdf, .docx)", type=["txt", "pdf", "docx"])
        if uploaded_file is not None:
            if uploaded_file.name.endswith(".txt"):
                text_input = uploaded_file.read().decode("utf-8")
            elif uploaded_file.name.endswith(".pdf"):
                with fitz.open(stream=uploaded_file.read(), filetype="pdf") as doc:
                    text_input = ""
                    for page in doc:
                        text_input += page.get_text()
            elif uploaded_file.name.endswith(".docx"):
                doc = Document(io.BytesIO(uploaded_file.read()))
                text_input = "\n".join([para.text for para in doc.paragraphs])
            else:
                text_input = ""
                st.warning("Unsupported file format.")
            st.text_area("📖 File Content", text_input, height=200, disabled=True)

    mode = st.radio("✨ Choose mode", ["Simple", "Detailed", "Flashcards"], horizontal=True)
    lang = st.selectbox("🌐 Select language", languages, key="notes_lang")
    out = st.empty()

    if st.button("🧠 Generate Notes", key="notes_btn"):
        if text_input.strip():
            prompt = f"Summarize this content in {mode.lower()} bullet points. Write in {lang}: {text_input}"
            result = generate_text(prompt, 300)
            out.success("✅ Notes Generated:")
            out.markdown(result.replace("\n", "  \n"))
        else:
            out.warning("🚨 Please provide text input or upload a file.")

    if st.button("🧹 Clear Chat", key="clear_notes"):
        st.session_state.notes_input = ""
        out.empty()
        st.rerun()

# --- ESSAY IMPROVER ---
with tabs[5]:
    st.subheader("🧹 Essay Improver")
    st.session_state.essay_input = st.text_area("📝 Paste your essay", st.session_state.get("essay_input", ""))
    lang = st.selectbox("🌐 Select language", languages, key="essay_lang")
    out = st.empty()
    if st.button("💡 Improve Essay", key="essay_btn"):
        if st.session_state.essay_input:
            prompt = f"Improve the grammar, clarity, and word choice of this essay. Show original and improved versions side by side. Write in {lang}: {st.session_state.essay_input}"
            result = generate_text(prompt, 400)
            out.success("✅ Essay Improved:")
            out.markdown(result.replace("\n", "  \n"))
        else:
            out.warning("🚨 Please paste your essay.")
    if st.button("🧹 Clear Chat", key="clear_essay"):
        st.session_state.essay_input = ""
        out.empty()
        st.rerun()
