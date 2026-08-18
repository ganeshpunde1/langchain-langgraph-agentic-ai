"""
Local Ollama chatbot example.

Uses a model running on your machine (via Ollama) instead of OpenAI.
LangSmith tracing still works if LANGCHAIN_TRACING_V2 is set in .env.
"""

import os

# Windows/Anaconda sometimes set bad SSL certificate paths that break HTTPS calls.
# Remove those broken values first, then point to the correct cert file from certifi.
os.environ.pop("SSL_CERT_FILE", None)
os.environ.pop("SSL_CERT_DIR", None)
os.environ.pop("REQUESTS_CA_BUNDLE", None)
os.environ.pop("CURL_CA_BUNDLE", None)

import certifi

os.environ["SSL_CERT_FILE"] = certifi.where()
os.environ["REQUESTS_CA_BUNDLE"] = certifi.where()

from dotenv import load_dotenv

# Load settings from .env (LangSmith keys, etc.)
load_dotenv()

from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama


def main():
    print("Hello from langchain-langgraph-agentic-ai application!")

    # Text we want the model to summarize
    information = """
    Amitabh Bachchan is a famous Indian actor born in 1942.
    He is known for Sholay, Don, Piku, and Kaun Banega Crorepati.
    """

    # Prompt template: {information} gets replaced with the text above
    summary_template = """
    Summarize {information} and give 2 interesting facts.
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    # ChatOllama talks to a local model — make sure Ollama is running and phi3:mini is pulled
    llm = ChatOllama(temperature=0, model="phi3:mini")

    # Chain = prompt first, then LLM (output of prompt goes into the model)
    chain = summary_prompt_template | llm
    response = chain.invoke({"information": information})

    print(response.content)


if __name__ == "__main__":
    main()
