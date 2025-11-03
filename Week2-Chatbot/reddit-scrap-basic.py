import praw

# https://www.reddit.com/prefs/apps

# Initialize Reddit instance
reddit = praw.Reddit(
    client_id="ID",
    client_secret="Secret",
    user_agent="my_scraper/1.0"
)

# Scrape from a specific subreddit
subreddit = reddit.subreddit("Python")  # Change to your subreddit

# Get hot posts
print("=== HOT POSTS ===")
for post in subreddit.hot(limit=10):
    print(f"Title: {post.title}")
    print(f"Score: {post.score}")
    print(f"URL: {post.url}")
    print(f"Comments: {post.num_comments}")
    print(f"Text: {post.selftext[:200]}...")
    print("-" * 80)

# Get comments from a post
print("\n=== COMMENTS ===")
for post in subreddit.hot(limit=1):
    post.comments.replace_more(limit=0)  # Load all comments
    for comment in post.comments.list()[:5]:
        print(f"Author: {comment.author}")
        print(f"Score: {comment.score}")
        print(f"Body: {comment.body[:200]}...")
        print("-" * 40)