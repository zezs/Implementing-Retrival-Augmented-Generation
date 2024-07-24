import os

from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_pinecone import PineconeVectorStore
from langchain import hub #prompt community

from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains.retrieval import create_retrieval_chain

load_dotenv()

if __name__=="__main__":
    print("Retrieving...")

    embeddings = OpenAIEmbeddings()
    llm = ChatOpenAI()

    query = "What is Photosyntesis?" # prompt includes query or query+context(in RAG) 
    prompt = PromptTemplate.from_template(template=query)
    chain = prompt | llm
    result = chain.invoke(input={})
    print(result.content)
