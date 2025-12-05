# ---------------------------------------------------------------------
# RAG: Simplified Retrieval Component - NOW SHOWING SIMILARITY SCORES
# Focus: Turning text into searchable data (Indexing) and finding the
# most relevant piece of text for a given query (Retrieval).
# ---------------------------------------------------------------------
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import SentenceTransformerEmbeddings
from langchain_core.documents import Document

# --- STEP 1 & 2: INDEXING (Memorizing the Knowledge) ---

# 1. Knowledge Base (The information the RAG system "knows")
knowledge_base = [
        "Marie Curie was a physicist and chemist who pioneered research on radioactivity. She was the first woman to win a Nobel Prize.",
        "Thomas Edison was an American inventor and businessman who developed many devices, most notably the practical electric light bulb and the phonograph.",
        "Leonardo da Vinci was an Italian polymath of the High Renaissance who is considered one of the greatest painters of all time.",
        "Ada Lovelace, an English mathematician, is often regarded as the first computer programmer for her work on Charles Babbage's proposed mechanical general-purpose computer, the Analytical Engine."
        # "hello World!"
]
# Convert the text into a format the vector store understands
documents = [Document(page_content=text) for text in knowledge_base]

# 2. Embedding Model (The "Memory Translator")
# This model converts the text into a list of numbers (a vector/embedding).
# Sentences with similar meanings will have vectors that are numerically "close" to each other.
embeddings = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
# print(embeddings)
# 3. Vector Store (The "Indexed Memory")
# This creates the index where the vector-translated documents are stored.
vectorstore = Chroma.from_documents(documents, embeddings)
# print(vectorstore)
print(f"✅ Indexing Complete: {len(documents)} documents stored and vectorized.")


# --- STEP 3: RETRIEVAL (Looking up the Answer and Score) ---

# The question we want to ask
user_query = "Who developed the electric light bulb and what was his other major invention?"
print(f"\n--- Searching for the top 3 results for: '{user_query}' ---")

# Search for the top 3 most similar document chunks, returning the score as well.
# Score is the Euclidean distance (L2 norm) between the query vector and the document vector.
retrieved_results = vectorstore.similarity_search_with_score(user_query, k=3) 

# Display the retrieved context and its similarity score
if retrieved_results:
    print("\n[Retrieved Results (Context + Similarity Score)]")
    
    # We iterate over the list of (Document, Score) tuples
    for i, (doc, score) in enumerate(retrieved_results):
        print(f"\n--- Result #{i + 1} (Score: {score:.4f}) ---")
        print(doc.page_content)
else:
    print("No relevant documents found.")