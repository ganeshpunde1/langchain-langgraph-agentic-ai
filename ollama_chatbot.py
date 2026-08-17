import os

# FIX MUST BE HERE — before any imports that use httpx
os.environ.pop("SSL_CERT_FILE", None)
os.environ.pop("SSL_CERT_DIR", None)

from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama

load_dotenv()


def main():
    print("Hello from langchain-langgraph-agentic-ai application!")

    information = """
    Amitabh Bachchan is a famous Indian actor born in 1942.
    He is known for Sholay, Don, Piku, and Kaun Banega Crorepati.
    """

    summary_template = """
    Summarize {information} and give 2 interesting facts.
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    llm = ChatOllama(model="phi3:mini")
    chain = summary_prompt_template | llm
    response = chain.invoke({"information": information})

    print(response.content)


if __name__ == "__main__":
    main()
