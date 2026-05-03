# AI Creativity Playground

An AI-powered web app for writers, students, and creatives — from story generation to essay improvement, all in one place.

**Live Demo:** [Try it on Hugging Face](https://huggingface.co/spaces/Mahrukhh/ai_creativity_playground)

---

## Features

| Tool | Description |
|------|-------------|
| Story Generator | Turn any idea into a creative story |
| Poem Creator | Generate poems on any theme or topic |
| Emoji Story | Tell fun stories using emojis |
| Slogan Generator | Create catchy slogans for any brand or concept |
| Study Notes Generator | Simplify complex topics into bullet-point notes |
| Essay Improver | Enhance grammar, clarity, and word choice |

---

## Multilingual Support

Supports 12 languages including English, Urdu, Hindi, Arabic, French, Spanish, Japanese, Turkish, and more.

---

## Tech Stack

| Tool | Purpose |
|------|---------|
| Python | Core language |
| Streamlit | Frontend UI |
| Groq API (LLaMA3) | AI text generation |
| PyMuPDF | PDF file reading |
| python-docx | Word file reading |
| Hugging Face Spaces | Deployment |

---

## Project Structure

```
ai-creativity-playground/
│
├── app.py              # Main Streamlit app (all 6 tools)
├── requirements.txt
└── README.md
```

---

## How to Run Locally

```bash
# 1. Clone the repo
git clone https://github.com/mahrukhmobin/ai-creativity-playground.git

# 2. Install dependencies
pip install -r requirements.txt

# 3. Add your Groq API key in .env file
# GROQ_API_KEY=your_key_here

# 4. Run the app
streamlit run app.py
```

---

## Use Cases

- Students generating quick notes from lectures or uploaded PDFs
- Writers looking for story or poem inspiration
- Anyone needing to polish an essay or create a slogan

---

*Built by [Mahrukh Mobin](https://github.com/mahrukhmobin) — Computer Engineering Student @ UET Lahore*
