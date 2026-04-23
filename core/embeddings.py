class EmbeddingEngine:
    def __init__(self):
        print("Embedding Engine initialized")

    def embed(self, text):
        # simple logic (temporary)
        return [float(len(text)) % 1, 0.5, 0.8, 0.3]