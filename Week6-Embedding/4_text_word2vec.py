from gensim.models import Word2Vec

# Training corpus - each string is a sentence
corpus = [
    "king queen man woman prince princess",
    "boy girl child",
    "dog cat animal pet",
    "car bus train vehicle",
    "pizza burger salad food",
    "sunny beach ocean sand",
    "rainy city street umbrella",
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

# Find words similar to "king"
similar_words = w2v.wv.most_similar("king", topn=3)
print("Word2Vec similar to 'king':", similar_words)
