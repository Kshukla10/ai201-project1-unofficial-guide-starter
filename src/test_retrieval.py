from retrieval import retrieve

queries = [
    "How does the UIC meal plan system work?",
    "What are common complaints about UIC dining?",
    "What do students say about portion sizes in UIC dining halls?",
]

for q in queries:
    print("QUERY:", q)
    hits = retrieve(q, k=3)
    for i, h in enumerate(hits, 1):
        print("  Rank", i, "| distance:", round(h["distance"], 4), "| source:", h["source"])
        print("  Text:", h["text"][:200])
        print()
    print("=" * 60)