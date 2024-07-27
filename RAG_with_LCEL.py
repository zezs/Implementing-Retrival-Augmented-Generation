""""
What is LCEL?
- LCEL stands for Locality-Constrained Linear Embedding.
- It is a technique used to project high-dimensional data into a lower-dimensional space while preserving local relationships between data points.

Why use LCEL?
- LCEL reduces data complexity
- Preserves local relationships
- Improves the time efficiency of tasks like similarity search and clustering.
- Increases space efficiency by reducing storage requirements.
"""
import os
from dotenv import load_dotenv

from langchain_core.prompts import PromptTemplate
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_pinecone import PineconeVectorStore
from langchain import hub #prompt community

from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains.retrieval import create_retrieval_chain
from langchain_core.runnables import RunnablePassthrough

load_dotenv()

def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)


if __name__=="__main__":
    print("Retrieving...")

    embeddings = OpenAIEmbeddings()
    llm = ChatOpenAI()
    vectorstore = PineconeVectorStore( index_name=os.environ["INDEX_NAME"], embedding=embeddings)

    query = "What is Pinecone?" # prompt includes query or query+context(in RAG) 
    template = """
    Use the following pieces of context to asnwer the question at the end,
    If you don't know the asnwer, just say that you dont know, don't try to make up an answer.
    Keep the answer simple in max 4 lines.
    At the end of answer, Always give out a different Swami Vivekananda quote everytime

    {context}

    Question: {question}

    Answer:"""

    custom_rag_prompt = PromptTemplate.from_template(template)
    """
    - In the key of question we have a runnbalepassthrough object, when we invoke this chain and we will pass in as aurgument in key of question
    - the question value will remain unchanged, it will propogate to LLM as is
    - In question key: we have original input question
    - we retrieve the relevant info to asnwer the question
    - format docs: user-defined func to format docs 
    """
    rag_chain = (
                {"context":vectorstore.as_retriever() | format_docs, "question": RunnablePassthrough()}
                | custom_rag_prompt
                | llm
    )
    
    res = rag_chain.invoke(query)
    print(res)
    print("***************")
    print(res.content)