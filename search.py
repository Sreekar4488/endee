import json
import numpy as np
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')

with open("data/vectors.json") as f:
    database = json.load(f)

def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

def search_bug(query):
    query_vector = model.encode(query)

    results = []

    for item in database:
        score = cosine_similarity(query_vector, item["vector"])
        results.append((score, item))

    results.sort(reverse=True, key=lambda x: x[0])

    return results[:3]