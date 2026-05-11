import json
import faiss
import numpy as np

from sentence_transformers import SentenceTransformer

print("Loading embedding model...")

model = SentenceTransformer('all-MiniLM-L6-v2')

print("Reading catalog data...")

with open("app/catalog.json", "r", encoding="utf-8") as f:

    catalog = json.load(f)

texts = []

for item in catalog:

    text = item["name"]

    texts.append(text)

print("Creating embeddings...")

embeddings = model.encode(texts)

dimension = embeddings.shape[1]

print("Embedding dimension:", dimension)

index = faiss.IndexFlatL2(dimension)

index.add(np.array(embeddings))

faiss.write_index(index, "app/shl_index.faiss")

print("FAISS index created successfully!")