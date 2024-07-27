# LCEL: Langchain embedding library
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

    query = "What is Pinecone in machine learning?" # prompt includes query or query+context(in RAG) 
    query1 = "List all pinecone features ?"

    # Initializes a vector store with Pinecone, using a specific index name and embedding method.
    vectorstore = PineconeVectorStore( index_name=os.environ["INDEX_NAME"], embedding=embeddings)

    # pre-defined prompt template for retrieval-based question-answering.
    retrieval_qa_chat_prompt = hub.pull("langchain-ai/retrieval-qa-chat")

    # chain to combine retrieved documents from vectorDB using the language model and the prompt.
    combine_docs_chain = create_stuff_documents_chain(llm, retrieval_qa_chat_prompt)

    """
    - The retrival_chain uses vectorstore.as_retriever() to find documents related to the query in the Pinecone vector store.
    - The retrieved documents are passed to combine_docs_chain, which uses the language model and the retrieval_qa_chat_prompt to process and combine the documents into a coherent response.
    """
    
    # Sets up a retrieval chain that uses the vector store for retrieving and combines results with the documents chain.
    retrival_chain = create_retrieval_chain(retriever=vectorstore.as_retriever(), combine_docs_chain=combine_docs_chain)

    result = retrival_chain.invoke(input={"input": query1})
    print(result['answer'])
    
