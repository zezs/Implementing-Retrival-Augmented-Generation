import os
from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader

load_dotenv()

if __name__ == "__main__":
    print("Ingestion...")

    # init textloader obj giving the file path
    loader = TextLoader("D:\Projects\GenAI\Implementing Retrival Augmented Generation\mediumblog1.txt")
    
    #loading the file into langchain doc
    document = loader.load()

    print("Splitting...")