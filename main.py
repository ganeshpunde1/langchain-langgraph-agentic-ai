import os

from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

load_dotenv()


def main():
    print("Hello from langchain-langgraph-agentic-ai application!")
    # print(os.environ.get("OPENAI_API_KEY"))

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
    llm = ChatOpenAI(temperature=0, model="gpt-4o-mini")
    chain = summary_prompt_template | llm
    response = chain.invoke({"information": information})
    print(response)
    print(response.content)


if __name__ == "__main__":
    os.environ.pop("SSL_CERT_FILE", None)
    os.environ.pop("SSL_CERT_DIR", None)
    main()
