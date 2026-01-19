import sys
import umap
import plotly.graph_objects as go
from gensim.models import Word2Vec

# Get file path from command line or use default
path = sys.argv[1] if len(sys.argv) > 1 else "wiki_selection.txt"

# Read text file
with open(path, "r", encoding="utf-8") as f:
    text = f.read().lower()

# Extract tokens (words) from text
tokens = []
for word in text.split():
    cleaned = word.strip(".,!?;:\"'()[]{}")
    if cleaned:
        tokens.append(cleaned)

# Split tokens into chunks for Word2Vec training
# Word2Vec needs sentences, so we create chunks of 10 words
sentences = []
chunk_size = 10
for i in range(0, len(tokens), chunk_size):
    chunk = tokens[i:i+chunk_size]
    sentences.append(chunk)

if len(sentences) < 2:
    print("Not enough text.")
    raise SystemExit(0)

# Train Word2Vec model
w2v = Word2Vec(
    sentences=sentences,
    vector_size=50,
    window=5,
    min_count=1,
    sg=1,
    workers=1
)

# Get unique tokens that exist in Word2Vec vocabulary
unique_tokens = set(tokens)
vocab_tokens = []
for token in unique_tokens:
    if token in w2v.wv:
        vocab_tokens.append(token)
vocab_tokens = sorted(vocab_tokens)

# Get embeddings for all tokens
features = []
for token in vocab_tokens:
    features.append(w2v.wv[token])

# Reduce to 2D using UMAP
reducer = umap.UMAP(n_neighbors=5, min_dist=0.2, random_state=42)
points = reducer.fit_transform(features)

# Create interactive plot
fig = go.Figure(data=go.Scatter(
    x=points[:, 0],
    y=points[:, 1],
    mode='markers',
    marker=dict(size=5, color='blue', opacity=0.6),
    text=vocab_tokens,
    hovertemplate='<b>%{text}</b><br>X: %{x:.2f}<br>Y: %{y:.2f}<extra></extra>',
))

fig.update_layout(
    title="Word2Vec Token Embeddings (Interactive UMAP)",
    xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
    yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
    hovermode='closest',
    width=1200,
    height=800,
)

fig.show()
