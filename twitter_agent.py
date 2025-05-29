import os
import openai
import tweepy
from dotenv import load_dotenv

load_dotenv()

# OpenAI key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Twitter OAuth1.0a creds
consumer_key    = os.getenv("TWITTER_API_KEY")
consumer_secret = os.getenv("TWITTER_API_SECRET")
access_token    = os.getenv("TWITTER_ACCESS_TOKEN")
access_secret   = os.getenv("TWITTER_ACCESS_SECRET")

# Twitter OAuth2.0 Client credentials (for future OAuth2 flows)
oauth2_client_id     = os.getenv("TWITTER_OAUTH2_CLIENT_ID")
oauth2_client_secret = os.getenv("TWITTER_OAUTH2_CLIENT_SECRET")

# Twitter Bearer token for App-only v2 endpoints
bearer_token = os.getenv("TWITTER_BEARER_TOKEN")

# Instantiate a Tweepy v2 Client with both OAuth1 and OAuth2 credentials
client = tweepy.Client(
    bearer_token=bearer_token,
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
    access_token=access_token,
    access_token_secret=access_secret,
    return_type=dict,
    wait_on_rate_limit=True
)

def generate_tweet(user_prompt: str) -> str:
    """Generate a short tweet using OpenAI GPT."""
    try:
        resp = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You’re a snappy tweet-writing assistant."},
                {"role": "user",   "content": f"Write a single tweet based on: {user_prompt}"}
            ],
            max_tokens=60,
            temperature=0.7
        )
        return resp.choices[0].message.content.strip()
    except Exception as e:
        return f"Error generating tweet: {e}"

def post_tweet(text: str) -> str:
    """Post a tweet under the authenticated user context."""
    try:
        response = client.create_tweet(text=text)
        data = response.get("data", {})
        return f"✅ Tweet posted: {data.get('text', '')} (ID: {data.get('id', '')})"
    except Exception as e:
        return f"Failed to post tweet: {e}"

def fetch_tweets(keyword: str) -> str:
    """Fetch recent public tweets matching a keyword."""
    try:
        resp = client.search_recent_tweets(
            query=keyword,
            max_results=10,
            tweet_fields=["author_id", "text"]
        )
        tweets = resp.get("data", [])
        if not tweets:
            return "No tweets found."
        results = []
        for t in tweets:
            user = client.get_user(id=t["author_id"], user_fields=["username"])
            username = user["data"]["username"]
            results.append(f"{username}: {t['text']}")
        return "\n\n".join(results)
    except Exception as e:
        return f"Failed to fetch tweets: {e}"
