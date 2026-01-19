from gensim.models import Word2Vec

# Training corpus
corpus = [
    "king queen man woman prince princess",
    "boy girl child",
    "dog cat animal pet",
    "car bus train vehicle",
    "pizza burger salad food",
    "sunny beach ocean sand",
    "rainy city street umbrella",
    "computer laptop phone device",
    "book read write story",
    "music song play listen",
]

# Split each sentence into words
tokenized_corpus = []
for sentence in corpus:
    tokenized_corpus.append(sentence.split())

# Train Word2Vec model
w2v = Word2Vec(
    sentences=tokenized_corpus,
    vector_size=50,
    window=3,
    min_count=1,
    sg=1,
    workers=1
)

# Analogy test: queen + (king - man)
# This should find words similar to "queen" in the same way "king" is to "man"
queen_vector = w2v.wv["queen"]
king_vector = w2v.wv["king"]
man_vector = w2v.wv["man"]

combo_vector = queen_vector + (king_vector - man_vector)

# Find words most similar to the result vector
similar_words = w2v.wv.similar_by_vector(combo_vector, topn=10)

print("Word2Vec Analogy: queen + (king - man)")
print("\nMost similar words:")
for word, score in similar_words:
    print(f"  {word}: {score:.3f}")

# Show similar words for comparison
print("\n\nSimilar words:")
for word in ["king", "queen", "man"]:
    print(f"\n{word}:")
    similar = w2v.wv.most_similar(word, topn=5)
    for similar_word, score in similar:
        print(f"  {similar_word}: {score:.3f}")
