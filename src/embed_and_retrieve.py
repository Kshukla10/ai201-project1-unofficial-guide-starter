"""
Milestone 4: Embed chunks and test retrieval
Domain: UIC Campus Dining Reviews
Embedding model: all-MiniLM-L6-v2
Vector store: ChromaDB (in-memory)
"""

import json
import chromadb
from sentence_transformers import SentenceTransformer

# Load chunks
CHUNKS_PATH = "chunks.json"   

with open(CHUNKS_PATH) as f:
    chunks = json.load(f)

print(f"Loaded {len(chunks)} chunks.\n")

# Set up embedding model 
print("Loading embedding model (all-MiniLM-L6-v2)...")
model = SentenceTransformer("all-MiniLM-L6-v2")

# Embed all chunks
texts = [c["text"] for c in chunks]
print("Embedding chunks — this may take a moment...")
embeddings = model.encode(texts, show_progress_bar=True)
print(f"Embeddings shape: {embeddings.shape}\n")

# Load into ChromaDB 
client = chromadb.Client()   
collection = client.create_collection(
    name="uic_dining",
    metadata={"hnsw:space": "cosine"}   
)

collection.add(
    ids=[f"{c['source']}_{c['chunk_id']}" for c in chunks],
    embeddings=embeddings.tolist(),
    documents=texts,
    metadatas=[
        {"source": c["source"], "chunk_id": c["chunk_id"]}
        for c in chunks
    ],
)
print(f"Stored {collection.count()} chunks in ChromaDB.\n")


# Retrieval function
def retrieve(query: str, k: int = 5):
    """Return the top-k most relevant chunks with source info and distance."""
    query_embedding = model.encode([query]).tolist()
    results = collection.query(
        query_embeddings=query_embedding,
        n_results=k,
        include=["documents", "metadatas", "distances"],
    )
    hits = []
    for doc, meta, dist in zip(
        results["documents"][0],
        results["metadatas"][0],
        results["distances"][0],
    ):
        hits.append({"text": doc, "source": meta["source"], "distance": round(dist, 4)})
    return hits


# Test with evaluation-plan queries
test_queries = [
    "Which UIC dining location is rated best for food quality?",
    "What do students say about portion sizes in UIC dining halls?",
    "What do students say about the variety of food options at UIC dining halls?",
    "How does the UIC meal plan system work?",
    "What are common complaints about UIC dining?",
]

for i, query in enumerate(test_queries, 1):
    print("=" * 70)
    print(f"Query {i}: {query}")
    print("-" * 70)
    hits = retrieve(query, k=5)
    for rank, h in enumerate(hits, 1):
        print(f"  Rank {rank} | distance: {h['distance']} | source: {h['source']}")
        # Print first 200 chars of the chunk for readability
        preview = h["text"][:200].replace("\n", " ")
        print(f"  Preview: {preview}...")
        print()