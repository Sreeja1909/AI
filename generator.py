from langchain_openai import ChatOpenAI


def generate_answer(query, context):
    """
    Generates an answer using the retrieved context.
    """

    llm = ChatOpenAI(
        model="gpt-4.1-mini",
        temperature=0
    )

    prompt = f"""
You are a helpful AI assistant.

Answer the user's question using ONLY the context below.

If the answer is not present in the context,
say "I couldn't find that information in the document."

Question:
{query}

Context:
{context}

Answer:
"""

    response = llm.invoke(prompt)

    return response.content