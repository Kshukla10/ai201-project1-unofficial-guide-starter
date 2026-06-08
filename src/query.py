"""
query.py
Chains retrieval → grounded generation via Groq LLM.
"""
import os
from groq import Groq
from dotenv import load_dotenv
from retrieval import retrieve
from pathlib import Path

load_dotenv()
groq_client = Groq(api_key=os.getenv("GROQ_API_KEY"))

SYSTEM_PROMPT = """You are a helpful assistant that answers questions about UIC campus dining.
Answer the question using ONLY the information provided in the context below.
If the context does not contain enough information to answer the question, say:
"I don't have enough information on that in my documents."
Do NOT use any outside knowledge. Always cite which source document(s) your answer came from."""

def ask(question: str, k: int = 5) -> dict:
    # Retrieve relevant chunks
    hits = retrieve(question, k=k)

    # Build context string from chunks
    context_parts = []
    for i, h in enumerate(hits, 1):
        context_parts.append(f"[{i}] (source: {h['source']})\n{h['text']}")
    context = "\n\n".join(context_parts)

    #Build the user message
    user_message = f"""Context:
{context}

Question: {question}

Answer (cite sources by filename):"""

    # Call Groq LLM
    response = groq_client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_message},
        ],
        temperature=0.2,
        max_tokens=512,
    )

    answer = response.choices[0].message.content.strip()

    # Collect unique sources from retrieved chunks
    sources = list(dict.fromkeys(h["source"] for h in hits))

    return {
        "answer": answer,
        "sources": sources,
        "chunks": hits,
    }


# Quick test when run directly
if __name__ == "__main__":
    test_questions = [
        "What do students say about portion sizes in UIC dining halls?",
        "How does the UIC meal plan system work?",
        "What is the best pizza place in Chicago?",  # out-of-scope test
    ]

    for q in test_questions:
        print("=" * 70)
        print(f"Q: {q}")
        result = ask(q)
        print(f"A: {result['answer']}")
        print(f"Sources: {', '.join(result['sources'])}")
        print()