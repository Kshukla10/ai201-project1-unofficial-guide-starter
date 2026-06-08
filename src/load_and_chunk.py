from pathlib import Path
import re
import json

DATA_DIR = "data"

CHUNK_SIZE = 500
OVERLAP = 75


def clean_text(text):
    # Remove extra whitespace
    text = re.sub(r"\s+", " ", text)

    # Remove common HTML entities
    text = text.replace("&amp;", "&")
    text = text.replace("&nbsp;", " ")

    return text.strip()


def chunk_text(text, chunk_size=CHUNK_SIZE, overlap=OVERLAP):
    chunks = []

    start = 0

    while start < len(text):
        end = start + chunk_size

        chunks.append(text[start:end])

        start += chunk_size - overlap

    return chunks


all_chunks = []

for file_path in Path(DATA_DIR).glob("*.txt"):

    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()

    cleaned_text = clean_text(text)

    chunks = chunk_text(cleaned_text)

    print(f"\nLoaded: {file_path.name}")
    print(f"Chunks: {len(chunks)}")

    all_chunks.extend(chunks)

print("\n===== SAMPLE CHUNKS =====")

for i, chunk in enumerate(all_chunks[:5]):
    print(f"\nChunk {i+1}")
    print(chunk[:400])

print(f"\nTotal Chunks: {len(all_chunks)}")


with open("chunks.json", "w", encoding="utf-8") as f:
    json.dump(all_chunks, f, indent=2)