# ResearchMind 🔬

**Multi-agent AI research system** — four specialized agents collaborate to search, scrape, write, and critique a polished research report on any topic.

Built with [LangChain](https://www.langchain.com/), [Mistral AI](https://mistral.ai/), and [Streamlit](https://streamlit.io/).

---

## Architecture

```
┌──────────────┐    ┌──────────────┐    ┌──────────────┐    ┌──────────────┐
│  01 SEARCH   │───▶│  02 READER   │───▶│  03 WRITER   │───▶│  04 CRITIC   │
│    Agent     │    │    Agent     │    │    Chain     │    │    Chain     │
│              │    │              │    │              │    │              │
│  Tavily web  │    │ BeautifulSoup│    │ Mistral LLM  │    │ Mistral LLM  │
│  search      │    │ deep scrape  │    │ structured   │    │ score +      │
│              │    │              │    │ report       │    │ feedback     │
└──────────────┘    └──────────────┘    └──────────────┘    └──────────────┘
```

### Step-by-step

| Step | Agent / Chain | What it does |
|------|--------------|---------------|
| **01 Search** | `build_search_agent()` | Queries Tavily for recent web results (titles, URLs, snippets) on the research topic. |
| **02 Reader** | `build_reader_agent()` | Picks the most relevant URL from search results and scrapes the full page content via BeautifulSoup. |
| **03 Writer** | `writer_chain` | Drafts a structured report with introduction, key findings, conclusion, and sources. |
| **04 Critic** | `critic_chain` | Reviews the report, assigns a score out of 10, lists strengths, areas to improve, and a one-line verdict. |

---

## Project structure

```
.
├── app.py              # Streamlit web UI
├── pipeline.py         # CLI runner (rich terminal output)
├── agents.py           # Agent & chain definitions
├── tools.py            # web_search + scrape_url LangChain tools
├── pyproject.toml      # Project metadata & dependencies
├── requirements.txt    # Pip-compatible dependency list
├── .env                # API keys (gitignored)
└── .streamlit/
    ├── config.toml     # Streamlit theme/config
    └── secrets.toml    # Streamlit secrets
```

---

## Setup

### 1. Clone & enter the project

```bash
git clone <repo-url> && cd deep-research-agent
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

Or with `uv`:

```bash
uv sync
```

### 3. Set your API keys

Create a `.env` file in the project root:

```env
MISTRAL_API_KEY=your-mistral-api-key
TAVILY_API_KEY=your-tavily-api-key
```

- [Mistral API key](https://console.mistral.ai/api-keys/)
- [Tavily API key](https://app.tavily.com/)

---

## Usage

### Web UI (Streamlit)

```bash
streamlit run app.py
```

Open `http://localhost:8501`, enter a research topic, and click **Run Research Pipeline**. Watch each agent step execute live and get the final report with critic feedback.

### CLI

```bash
python pipeline.py
```

Enter a topic at the prompt — the pipeline runs all four steps and prints results to the terminal with `rich` formatting.

---

## Configuration

| Setting | Where | Default |
|---------|-------|---------|
| LLM model | `agents.py` | `mistral-small-2603` |
| LLM temperature | `agents.py` | `0` |
| Search results | `tools.py` | `max_results=5` |
| Scrape char limit | `tools.py` | `3000` chars |
| Streamlit theme | `.streamlit/config.toml` | Dark theme |

To switch the LLM provider, replace `ChatMistralAI` in `agents.py` with any [LangChain chat model](https://python.langchain.com/docs/integrations/chat/) (OpenAI, Anthropic, Groq, etc.).

---

## Dependencies

- **LLM**: `langchain`, `langchain-mistralai`
- **Search**: `langchain-tavily`
- **Scraping**: `beautifulsoup4`, `requests`
- **UI**: `streamlit`
- **Utils**: `python-dotenv`, `tiktoken`, `rich`
