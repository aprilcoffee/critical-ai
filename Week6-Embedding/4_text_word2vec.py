from gensim.models import KeyedVectors
from gensim import downloader as api

# Download and load pre-trained GloVe model (smaller version: 100 dimensions)
print("Downloading GloVe model (this may take a moment)...")
model = api.load("glove-wiki-gigaword-100")
print("Model loaded!")

# Test 1: Find words similar to "king"
print("\n" + "="*50)
print("Words similar to 'king':")
print("="*50)
if "king" in model:
    similar_words = model.most_similar("king", topn=5)
    for word, score in similar_words:
        print(f"  {word}: {score:.3f}")
else:
    print("  'king' not found in vocabulary")

# Test 2: Embedding arithmetic - king - man + woman (should be close to queen)
print("\n" + "="*50)
print("Embedding arithmetic: king - man + woman")
print("="*50)
if all(word in model for word in ["king", "man", "woman"]):
    result_vector = model["king"] - model["man"] + model["woman"]
    similar = model.similar_by_vector(result_vector, topn=10)
    print("\nWords closest to (king - man + woman):")
    for word, score in similar:
        marker = " <-- expected" if word == "queen" else ""
        print(f"  {word}: {score:.3f}{marker}")
else:
    print("  Some words not found in vocabulary")
