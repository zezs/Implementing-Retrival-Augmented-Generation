import os

from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
load_dotenv()

if __name__=="__main__":
    print("Retrieving...")

    embeddings = OpenAIEmbeddings()
    llm = ChatOpenAI()

    query = "What is Photosynthesis?" # prompt includes query or query+context(in RAG) 
    prompt = PromptTemplate.from_template(template=query)
    chain = prompt | llm
    result = chain.invoke(input={})
    print(result.content)