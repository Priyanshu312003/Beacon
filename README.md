# Beacon 🔦

A research agent that searches the web, scrapes pages, and synthesizes a structured markdown report — all from a single topic input.

---

## How it works

1. **Search** — finds relevant URLs using Tavily API
2. **Scrape** — fetches and extracts clean text from each page
3. **Synthesize** — sends everything to GPT-4o-mini and generates a structured report
4. **Save** — outputs a clean markdown report to a file

---

## Project Structure

```
beacon/
├── main.py          # Entry point — wires everything together
├── search.py        # Web search via Tavily
├── scraper.py       # Page fetch + text extraction
├── synthesizer.py   # LLM report generation via GPT-4o-mini
├── utils.py         # Helper functions
├── .env             # API keys (not committed)
├── .gitignore
└── requirements.txt
```

---

## Setup

**1. Clone the repo**
```bash
git clone https://github.com/Priyanshu312003/Beacon.git
cd Beacon
```

**2. Create and activate virtual environment**
```bash
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # Mac/Linux
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Add API keys**

Create a `.env` file in the root:
```
TAVILY_API_KEY=your_tavily_key
OPENAI_API_KEY=your_openai_key
```

**5. Run**
```bash
python main.py
```

---

## Stack

| Layer | Tool |
|---|---|
| Web Search | [Tavily](https://tavily.com) |
| Scraping | `httpx` + `BeautifulSoup4` |
| LLM | OpenAI GPT-4o-mini |
| Output | Markdown report |

---

## Example

```
Enter research topic: What is Retrieval Augmented Generation?

Searching web...
Scraping 5 pages...
Synthesizing report...

Report saved to: output/rag_report.md
```

---

## Related Projects

- [DocMind](https://github.com/Priyanshu312003/docmind) — RAG pipeline from scratch (PyMuPDF, ChromaDB, Cohere reranking, Streamlit UI)

---

Built in public by [@afkpriyanshu](https://x.com/afkpriyanshu)