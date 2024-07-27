## Overview

![image](https://github.com/user-attachments/assets/43eed5cc-7322-4b0f-9ea1-cfae47199d49)

Load -> split -> Embedd -> store in vectoreBD
- Loading the medium blog- (TextLoader)
- Splitting the blog into smaller chunks- (TextSplitter)
- Embed the chunks and get vectors- (OpenAIEmbeddings)
- Store the embeddings in Pinecone vectorstore (PineconeVectorStore)


![RAG steps](https://github.com/user-attachments/assets/3b972ad9-38c5-4761-a845-8ecde675a2f7)
Source: AUTHOR


## Why are TextLoaders needed ?
- LLMs take text as input 
- But what if we want to process text from wahtsappp message, gogole drive, notion notebook, any pdf online etc...
- All the above mentoned sources are basically text
- But the come inn different format and have different semantic meaning
- So doc loaders are classes jmplemetation on to process and load different data and make it digestable by the LLMs

![image](https://github.com/user-attachments/assets/bd817abe-c80b-4e7b-823c-7903c98f8e8a)

Description: some of doc loaders provided by Langchain (source: Langchain official docs)

## TextSplitters ?
![image](https://github.com/user-attachments/assets/2312d8d4-55d6-427f-b004-31be56403d86)

source: Langchain official docs

## Embeddings
sentences(text) ---->  [encoder/ embedding model] ----> O O O O O (vector spaces)

### This is what embeddings in vector space looks like
vector spaces can be visualized in 2D or 3D for simplicity, Pinecone primarily operates in high-dimensional spaces to effectively handle the complexities of modern machine learning data.
![image](https://github.com/user-attachments/assets/3c0d4c53-8b1b-436c-90b9-ef3ef091e685)

SOURCE: AUTHOR

- If the emneddings are placed closer that means they have similar sematic meaning and are related to each other
- The red cluster is the query which is convertedd to text embedding(from text format)
- The red cluster is then placed in vector space
- The vector near the red vector(question) could have the answer to the query
- Then the relevant vector are calculated using cosine/ euclidean formula
- Shorter the distance more relevant the info to the question
- Finally, the relevant vecotrs with significant semantic meaning are converted into text(context) 
-  text spilt into chunks and augmented into prompt
-  BEFORE RETRIVAL: PROMPT -> Query
-  AFTER RETRIVAL: PROMPT -> Query + Context(chunks)





