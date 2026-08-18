# React Search Agent - Project Setup

## 1. Create a New Orphan Git Branch

```bash
git checkout --orphan project/react-search-agent
git rm -rf .
git status
git add .
git commit -m "environment setup"
git push
git push --set-upstream origin project/react-search-agent
```

## 2. Install and Initialize `uv`

Check `uv` help:

```bash
uv --help
```

Install `uv`:

```bash
pip3 install uv
```

Initialize the project:

```bash
uv init
```

## 3. Install Project Dependencies

```bash
uv add langchain langchain-openai python-dotenv langchain-ollama langchain-tavily tavily-python black isort
```

## Dependencies

- `langchain` - Core LangChain framework
- `langchain-openai` - OpenAI integration for LangChain
- `python-dotenv` - Load environment variables from `.env`
- `langchain-ollama` - Ollama integration for LangChain
- `langchain-tavily` - Tavily search integration for LangChain
- `tavily-python` - Tavily Python SDK
- `black` - Python code formatter
- `isort` - Python import sorter
