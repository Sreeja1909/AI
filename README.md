# Retrieval-Augmented Generation (RAG) Application

A modular Retrieval-Augmented Generation (RAG) application built using **Python**, **LangChain**, **OpenAI**, and **ChromaDB**. The application answers questions from a PDF document by retrieving relevant information through semantic search and generating responses using GPT-4.1 Mini.

The project is organized into separate modules for document loading, chunking, embedding generation, vector storage, retrieval, and response generation to improve readability and maintainability.

---

## Features

- Load PDF documents
- Split documents into overlapping chunks
- Generate embeddings using OpenAI
- Store embeddings in ChromaDB
- Perform semantic search
- Generate context-aware responses using GPT-4.1 Mini
- Modular project structure

---

## Tech Stack

- Python
- LangChain
- OpenAI API
- ChromaDB
- python-dotenv

---

## Project Structure

```
AI/
│
├── app.py                  # Main application
├── loaders.py              # PDF document loading
├── splitter.py             # Document chunking
├── embeddings.py           # OpenAI embedding model
├── vectordb.py             # ChromaDB operations
├── retriever.py            # Semantic retrieval
├── generator.py            # Response generation
│
├── data/
│   └── dentalcodes.pdf
│
├── chroma_db/
│
├── .env
├── requirements.txt
└── README.md
```

---

## How It Works

1. Load a PDF document.
2. Split the document into overlapping chunks.
3. Generate embeddings for each chunk using OpenAI.
4. Store the embeddings in ChromaDB.
5. Convert the user's question into an embedding.
6. Retrieve the most relevant document chunks using semantic search.
7. Send the retrieved context along with the user's question to GPT-4.1 Mini.
8. Return the generated answer.

## Skills Demonstrated

- Retrieval-Augmented Generation (RAG)
- Semantic Search
- Vector Embeddings
- ChromaDB
- LangChain
- Prompt Engineering
- OpenAI API Integration
- Modular Python Development

---

## Future Enhancements

- Multiple document support
- Conversation memory
- Streamlit interface
- FastAPI deployment
- Response citations with page references
- Docker support

---

## Author

**Sreeja Voruganty**
