# ☁️ Cloud Agent

An autonomous AI agent that can read, write, and execute files on your behalf — powered by LLMs via [OpenRouter](https://openrouter.ai/).

Cloud Agent is a CLI-based tool that connects to a large language model and equips it with a suite of **sandboxed file-system tools**, giving it the ability to explore directories, read files, write code, and run Python scripts — all within a safe, scoped working directory.

---

## ✨ Features

| Tool | Description |
|---|---|
| **`get_file_info`** | Lists directory contents (name, type, size) with path-boundary validation |
| **`get_file_content`** | Reads file content with automatic truncation at 10 000 chars |
| **`write_file`** | Creates or overwrites files, auto-creating parent directories |
| **`run_python_file`** | Executes `.py` files in a subprocess with a 30 s timeout and captures stdout/stderr |

All tools enforce **working-directory sandboxing** — the agent cannot access files outside the permitted directory.

---

## 🚀 Getting Started

### Prerequisites

- **Python 3.13+**
- **[uv](https://docs.astral.sh/uv/)** (recommended) or pip
- An **OpenRouter API key** → [openrouter.ai/keys](https://openrouter.ai/keys)

### Installation

```bash
# Clone the repo
git clone https://github.com/Jayanth-Rookie/Cloud-Agent.git
cd Cloud-Agent/aiagent

# Create a virtual environment & install dependencies
uv sync          # or: pip install -e .
```

### Configuration

Create a `.env` file inside the `aiagent/` directory:

```env
OPENROUTER_API_KEY=sk-or-v1-your-key-here
```

### Usage

```bash
python main.py "List all the files in this directory"

# With verbose output (shows token usage)
python main.py "Explain main.py" --verbose
```

---

## 📁 Project Structure

```
Cloud-Agent/
└── aiagent/
    ├── main.py                  # Entry point — CLI + LLM orchestration
    ├── config.py                # Global constants (MAX_CHARS)
    ├── functions/
    │   ├── get_file_info.py     # Directory listing tool
    │   ├── get_file_content.py  # File reading tool
    │   ├── write_file.py        # File writing tool
    │   └── run_py_file.py       # Python execution tool
    ├── calculator/              # Sample project for the agent to work on
    ├── test_*.py                # Test modules for each tool
    ├── pyproject.toml           # Project metadata & dependencies
    └── .env                     # API key (git-ignored)
```

---

## 🛡️ Safety

- **Path sandboxing** — every tool resolves absolute paths and rejects anything outside the working directory.
- **Execution timeout** — `run_python_file` kills subprocesses after 30 seconds.
- **Read truncation** — large files are capped at 10 000 characters to prevent token overflow.

---

## 📄 License

This project is open source. Feel free to use, modify, and distribute.
