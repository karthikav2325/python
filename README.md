# 📄 Simple Document Question Answering using RAG

A **beginner-friendly** project that teaches the core idea behind
**Retrieval-Augmented Generation (RAG)** — no LangChain, no vector databases,
no complicated frameworks. Just plain Python.

---

## What is RAG?

RAG stands for **Retrieve → Augment → Generate**.

Instead of asking an AI to answer from memory, we:

1. **Retrieve** — find the relevant pieces of information from your own document
2. **Augment** — add those pieces to the question as extra context
3. **Generate** — let Gemini create the final answer using only that context

### Final RAG Flow

```
Document
   ↓
Chunks           ← split the text into small pieces
   ↓
Search           ← convert chunks & question to TF-IDF vectors
   ↓
Relevant Chunks  ← pick the top 3 by cosine similarity
   ↓
Question + Chunks
   ↓
Gemini
   ↓
Answer
```

---

## Technologies Used

| Library | Purpose |
|---|---|
| `streamlit` | Web UI |
| `pypdf` | Read PDF files |
| `scikit-learn` | TF-IDF vectors + cosine similarity |
| `google-generativeai` | Gemini API |
| `python-dotenv` | Load API key from `.env` |

No LangChain · No ChromaDB · No FAISS · No Docker

---

## Project Structure

```
simple_rag/
│
├── app.py            ← entire application (one file)
├── requirements.txt  ← dependencies
├── .env              ← your Gemini API key (never commit this!)
└── .gitignore        ← keeps .env out of git
```

---

## Setup & Installation

### 1 — Create a virtual environment

```bash
python -m venv venv
```

### 2 — Activate it

**Windows:**
```bash
venv\Scripts\activate
```

**macOS / Linux:**
```bash
source venv/bin/activate
```

### 3 — Install dependencies

```bash
pip install -r requirements.txt
```

### 4 — Add your Gemini API key

Open `.env` and replace the placeholder:

```
GEMINI_API_KEY=your_actual_key_here
```

> Get a free key at: https://aistudio.google.com/app/apikey

### 5 — Run the app

```bash
python -m streamlit run app.py
```

The app will open automatically at `http://localhost:8501`.

---

## How to Use

| Step | What happens |
|---|---|
| **Upload PDF** | App reads and stores the document |
| **Split** | Text is broken into ~500-character chunks |
| **Vectors** | Each chunk is converted to a TF-IDF number vector |
| **Ask** | Your question is also vectorized |
| **Retrieve** | Top 3 most similar chunks are found via cosine similarity |
| **Generate** | Question + chunks are sent to Gemini; it answers from context only |

---

## Key Concepts for Students

### TF-IDF (Term Frequency - Inverse Document Frequency)

Converts text into numbers:
- Words that appear **often in a chunk** but **rarely across all chunks** get a high score
- Common words like "the", "is" get a low score (filtered out)

### Cosine Similarity

Measures how "similar" two number vectors are:
- **1.0** = identical direction (perfect match)
- **0.0** = no overlap at all

The chunk with the **highest similarity score** is the most relevant to your question.

---

## Troubleshooting

| Problem | Fix |
|---|---|
| `GEMINI_API_KEY` error | Check your `.env` file; make sure there are no extra spaces |
| Network / connection error | Check your internet; disable VPN; click Ask again (auto-retries 3x) |
| No text extracted from PDF | The PDF may be scanned/image-based — use a text-based PDF |
| `ModuleNotFoundError` | Make sure venv is activated and you ran `pip install -r requirements.txt` |

---

## License

MIT — free to use and modify for learning purposes.
