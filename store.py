import json
from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer('all-MiniLM-L6-v2')

# load bugs
with open("data/bugs.json") as f:
    bugs = json.load(f)

data = []

for bug in bugs:
    embedding = model.encode(bug["error"])
    data.append({
        "error": bug["error"],
        "solution": bug["solution"],
        "vector": embedding.tolist()
    })

# save vectors
with open("data/vectors.json", "w") as f:
    json.dump(data, f)

print("Bug embeddings stored successfully!")