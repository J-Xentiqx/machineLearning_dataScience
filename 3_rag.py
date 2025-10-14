from sentence_transformers import SentenceTransformer
import numpy as np

from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer("all-MiniLM-L6-v2")

documents = [
    "Python ist eine Programmiersprache",
    "Machine Learning nutzt Algorithmen",
    "Embeddings repräsentieren Text als Vektoren",
    "Katzen sind beliebte Haustiere",
    "Neuronale Netze lernen aus Daten"
]

doc_embeddings = model.encode(documents)

def semantic_search(query, documents, doc_embeddings, model, top_k=3):
    query_embedding = model.encode([query])

    similarities = cosine_similarity(query_embedding,doc_embeddings)[0]

    top_indicies = np.argsort(similarities)[::-1][:top_k]

    results = [(documents[i], similarities[i]) for i in top_indicies]

    return results

query = "Wie funktioniert künstliche Intelligenz?"
results = semantic_search(query, documents, doc_embeddings, model)

for i, (doc, score) in enumerate (results, 1):
    print(f"{i}. {doc} {score:.3f}")