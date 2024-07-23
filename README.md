## Overview

![alt text](image.png)
Load -> split -> Embedd -> store in vectoreBD
- Loading the medium blog- (TextLoader)
- Splitting the blog into smaller chunks- (TextSplitter)
- Embed the chunks and get vectors- (OpenAIEmbeddings)
- Store the embeddings in Pinecone vectorstore (PineconeVectorStore)

## Why are TextLoaders needed ?
- LLMs take text as input 
- But what if we want to process text from wahtsappp message, gogole drive, notion notebook, any pdf online etc...
- All the above mentoned sources are basically text
- But the come inn different format and have different semantic meaning
- So doc loaders are classes jmplemetation on to process and load different data and make it digestable by the LLMs

![alt text](image-2.png)
Description: some of doc loaders provided by Langchain (source: Langchain official docs)

## TextSplitters ?
![alt text](image-3.png)
source: Langchain official docs

## Embeddings

sentences(text) ---->  [encoder/ embedding model] ----> O O O O O (vector spaces)