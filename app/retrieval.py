import json
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

print("Loading retrieval model...")

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Load FAISS index
print("Loading FAISS index...")
index = faiss.read_index("app/shl_index.faiss")

# Load catalog
print("Loading catalog...")

with open("app/catalog.json", "r", encoding="utf-8") as f:
    catalog = json.load(f)


def search_assessments(query, top_k=5):
    """
    Search most relevant SHL assessments
    """

    # Convert query to embedding
    query_embedding = model.encode([query])

    query_embedding = np.array(query_embedding).astype("float32")

    # Search FAISS
    distances, indices = index.search(query_embedding, top_k)

    results = []

    for idx in indices[0]:

        if idx < len(catalog):

            item = catalog[idx]

            results.append({
                "name": item.get("name"),
                "url": item.get("url"),
                "test_type": item.get("test_type", "General")
            })

    return results


# Testing locally
if __name__ == "__main__":

    query = "Java developer assessment"

    print(f"\nSearching for: {query}\n")

    results = search_assessments(query)

    print("Top Results:\n")

    for result in results:
        print(result)