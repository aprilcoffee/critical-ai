import praw

reddit = praw.Reddit(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
    user_agent="my_scraper/1.0"
)

subreddit = reddit.subreddit("technology")

# Hot posts
for post in subreddit.hot(limit=5):
    print(f"HOT: {post.title}")

# New posts
for post in subreddit.new(limit=5):
    print(f"NEW: {post.title}")

# Top posts (by time period)
for post in subreddit.top(time_filter="week", limit=5):  # day, week, month, year, all
    print(f"TOP: {post.title}")

# Rising posts
for post in subreddit.rising(limit=5):
    print(f"RISING: {post.title}")

# Search within subreddit
for post in subreddit.search("python tutorial", limit=5):
    print(f"SEARCH: {post.title}")