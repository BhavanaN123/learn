# ---------------------------------------------------------------------
# RAG STEP 1 & 2: INDEXING AND RETRIEVAL (New Example: Physics Laws)
# GOAL: Illustrate retrieval of scientific concepts based on keyword and semantic match.
# ---------------------------------------------------------------------
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import SentenceTransformerEmbeddings
from langchain_core.documents import Document

# --- KNOWLEDGE BASE & QUERY ---
# Updated Knowledge Base: Now focusing on famous laws of motion.
knowledge_base = [
    "Newton's first law states that an object will remain at rest or in uniform motion unless acted upon by a net external force.",
    "The second law, often summarized as F=ma, relates an object's mass (m) and acceleration (a) to the applied net force (F).",
    "Galileo Galilei is considered the father of modern observational astronomy and the scientific method."
]
# Updated Query: Asking for a specific law.
user_query = "Summarize the law that relates force to mass and acceleration."

# 1. Indexing Setup
# documents: The chunked text ready for the vector store.
documents = [Document(page_content=text) for text in knowledge_base]
# embeddings: The model used to convert text to vectors.
embeddings = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
# vectorstore (chroma): The database that stores the vectors.
vectorstore = Chroma.from_documents(documents, embeddings)
print(f"✅ Indexing Complete: {len(documents)} documents stored and vectorized.")

# 2. Retrieval Step
retrieved_results = vectorstore.similarity_search_with_score(user_query, k=1) 

if retrieved_results:
    best_document = retrieved_results[0][0]
    best_score = retrieved_results[0][1]
    context_for_llm = best_document.page_content
    
    print(f"\n--- RETRIEVAL SUCCESS (Score: {best_score:.4f}) ---")
    print(f"Context Found: {context_for_llm}")

    # 3. Augmentation Step (Prepares the prompt for the next file)
    augmented_prompt = f"""
    CONTEXT:
    ---
    {context_for_llm}
    ---
    QUESTION: {user_query}
    ANSWER:
    """
    
    # Pass the result to the Generation step
    print("\n--- AUGMENTED PROMPT (Ready for LLM) ---")
    print(augmented_prompt.strip())
else:
    print("❌ Retrieval Failed: No relevant documents found.")