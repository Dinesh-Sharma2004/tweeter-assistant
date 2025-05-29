import os
import openai
import tweepy
from dotenv import load_dotenv

load_dotenv()

# Load keys
bearer_token      = os.getenv("TWITTER_BEARER_TOKEN")
consumer_key      = os.getenv("TWITTER_API_KEY")
consumer_secret   = os.getenv("TWITTER_API_SECRET")
access_token      = os.getenv("TWITTER_ACCESS_TOKEN")
access_secret     = os.getenv("TWITTER_ACCESS_SECRET")
openai.api_key    = os.getenv("OPENAI_API_KEY")

# Create a v2 Client
client = tweepy.Client(
    bearer_token=bearer_token,
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
    access_token=access_token,
    access_token_secret=access_secret,
    return_type=dict   # makes responses easier to parse
)

def generate_tweet(user_prompt):
    try:
        resp = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You’re a snappy tweet-writing assistant."},
                {"role": "user", "content": f"Write a single tweet based on: {user_prompt}"}
            ],
            max_tokens=60,
            temperature=0.7
        )
        return resp.choices[0].message.content.strip()
    except Exception as e:
        return f"Error generating tweet: {e}"

def post_tweet(text):
    try:
        # v2 endpoint
        response = client.create_tweet(text=text)
        # response looks like {'data': {'id': '...', 'text': '...'}}
        tweet_id = response["data"]["id"]
        tweet_text = response["data"]["text"]
        return f"✅ Tweet posted (v2): {tweet_text} (ID: {tweet_id})"
    except Exception as e:
        return f"Failed to post tweet: {e}"

def fetch_tweets(keyword, count=5):
    try:
        # v2 recent search (up to last 7 days)
        resp = client.search_recent_tweets(query=keyword, max_results=count, tweet_fields=["author_id","text"])
        tweets = resp.get("data", [])
        if not tweets:
            return "No tweets found."
        results = []
        for t in tweets:
            # get username via user lookup
            user = client.get_user(id=t["author_id"], user_fields=["username"])
            username = user["data"]["username"]
            results.append(f"{username}: {t['text']}")
        return "\n\n".join(results)
    except Exception as e:
        return f"Failed to fetch tweets: {e}"
