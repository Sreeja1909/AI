from langchain_chroma import Chroma


def create_vector_db(chunks, embeddings):
    """
    Creates a Chroma vector database from document chunks.
    """

    vector_db = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory="./chroma_db"
    )

    return vector_db