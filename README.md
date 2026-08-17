# LangChain Project Setup

## Git Commands

```bash
git checkout --orphan project/hello-world
git rm -rf .
git status
git add .
git commit -m "environment setup"
git push --set-upstream origin project/hello-world
````

## UV Commands

```bash
uv --help
pip3 install uv
uv init
```

## Install Dependencies

```bash
uv add langchain langchain-openai python-dotenv black isort
uv add langchain-ollama
```

## Useful Links

* UV: [https://docs.astral.sh/uv/](https://docs.astral.sh/uv/)
* python-dotenv: [https://pypi.org/project/python-dotenv/](https://pypi.org/project/python-dotenv/)
* OpenAI Platform: [https://platform.openai.com/home](https://platform.openai.com/home)
* Google AI Studio: [https://aistudio.google.com/api-keys?project=gen-lang-client-0044244967](https://aistudio.google.com/api-keys?project=gen-lang-client-0044244967)

## OpenAI 429 Error

```text
openai.RateLimitError: Error code: 429

You exceeded your current quota.
Please check your plan and billing details.

code: insufficient_quota
```

## Possible Solutions

* Add OpenAI API credits or enable billing.
* Try a different model/provider.
* Use Gemini or Groq.
* Use Ollama locally.

## Ollama Example

```bash
uv add langchain-ollama
```

```python
from langchain_ollama import ChatOllama

llm = ChatOllama(model="llama3.2")
```

```
```
