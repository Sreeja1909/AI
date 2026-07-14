from langchain_openai import ChatOpenAI
from loaders import load_pdf
from splitter import split_documents
from embedding import get_embedding_model
from vectordb import create_vector_db
from retriever import retrieve_context
from generator import generate_answer
from dotenv import load_dotenv

load_dotenv()

# Load the PDF
docs = load_pdf("data/dentalcodes.pdf")

# Create the splitter
chunks = split_documents(docs)

# Create embedding model
embeddings = get_embedding_model()

vector_db = create_vector_db(
    chunks,
    embeddings
)

#print("Chroma DB created successfully!")

query = "what is the cost for root canal ?"

context = retrieve_context(vector_db, query)

answer = generate_answer(
    query,
    context
)

print(answer)