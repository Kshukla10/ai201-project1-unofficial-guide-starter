import json

def load_chunks():
    with open("chunks.json", "r", encoding="utf-8") as f:
        return json.load(f)