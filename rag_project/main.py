# qa.py
from loader import load_documents

def simple_faq_answer(user_question: str) -> str:
    docs = load_documents()
    faq_doc = next(d for d in docs if d["id"] == "sql_faq")
    lines = [line.strip() for line in faq_doc["text"].splitlines() if line.strip()]

    best_match = None
    best_score = 0

    # Very naive matching: count overlapping words
    user_words = set(user_question.lower().split())

    for i, line in enumerate(lines):
        if line.lower().startswith("q:"):
            question_text = line[2:].strip().lower()
            q_words = set(question_text.split())
            score = len(user_words & q_words)
            if score > best_score:
                best_score = score
                best_match = i

    if best_match is None or best_score == 0:
        return "Sorry, I don't know the answer yet."

    # Assume the next non-empty line after Q is the A
    for j in range(best_match + 1, len(lines)):
        if lines[j].lower().startswith("a:"):
            return lines[j][2:].strip()

    return "Sorry, I couldn't find an answer."
    

if __name__ == "__main__":
    while True:
        q = input("Ask a SQL question (or 'quit'): ")
        if q.lower() == "quit":
            break
        print("Answer:", simple_faq_answer(q))
