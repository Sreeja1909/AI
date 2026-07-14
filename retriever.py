def retrieve_context(vector_db, query, k=3):
    """
    Retrieves the most relevant chunks from the vector database
    and returns them as a single context string.
    """

    results = vector_db.similarity_search(
        query,
        k=k
    )

    context = "\n\n".join(
        [doc.page_content for doc in results]
    )

    return context