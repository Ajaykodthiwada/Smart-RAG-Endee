from app.embeddings import get_embedding

database = []

def store_data(text):
    vector = get_embedding(text)
    database.append((text, vector))

def search(query):
    query_vector = get_embedding(query)
    results = sorted(database, key=lambda x: x[1] @ query_vector, reverse=True)
    return [r[0] for r in results[:3]]

def load_data():
    store_data("AI is Artificial Intelligence")
    store_data("Machine Learning is part of AI")
    store_data("Deep Learning uses neural networks")