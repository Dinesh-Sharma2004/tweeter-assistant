import os
import requests 
import tweepy
from dotenv import load_dotenv

load_dotenv()

consumer_key    = os.getenv("TWITTER_API_KEY")
consumer_secret = os.getenv("TWITTER_API_SECRET")
access_token    = os.getenv("TWITTER_ACCESS_TOKEN")
access_secret   = os.getenv("TWITTER_ACCESS_SECRET")

oauth2_client_id     = os.getenv("TWITTER_OAUTH2_CLIENT_ID")
oauth2_client_secret = os.getenv("TWITTER_OAUTH2_CLIENT_SECRET")

bearer_token = os.getenv("TWITTER_BEARER_TOKEN")

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
    """Generate a short tweet using Google Gemini."""
    try:
        apiKey = os.getenv("GEMINI_API_KEY", "")
        if not apiKey:
            return "Error: GEMINI_API_KEY not found in environment variables."

        apiUrl = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={apiKey}"

        payload = {
            "contents": [
                {
                    "role": "user",
                    "parts": [{"text": f"Write a single tweet based on: {user_prompt}"}]
                }
            ]
        }

        response = requests.post(apiUrl, json=payload)
        response.raise_for_status()

        result = response.json()
        
        if result.get("candidates") and len(result["candidates"]) > 0 and \
           result["candidates"][0].get("content") and \
           result["candidates"][0]["content"].get("parts") and \
           len(result["candidates"][0]["content"]["parts"]) > 0:
            text = result["candidates"][0]["content"]["parts"][0]["text"]
            return text.strip()
        else:
            return "Error generating tweet: Unexpected API response structure."

    except requests.exceptions.RequestException as req_err:
        return f"Error connecting to Gemini API: {req_err}"
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

def fetch_tweets(keyword: str, count: int = 10) -> str: 
    """
    Fetch recent public tweets matching a keyword, including author usernames
    efficiently using expansions.
    """
    try:
        actual_count = max(10, min(count, 100))

        resp = client.search_recent_tweets(
            query=keyword,
            max_results=actual_count,
            tweet_fields=["author_id", "text"],
            expansions=["author_id"],
            user_fields=["username"]
        )

        tweets = resp.get("data", [])
        includes = resp.get("includes", {})
        users = includes.get("users", [])

        if not tweets:
            return "No tweets found."

        user_map = {user["id"]: user["username"] for user in users}

        results = []
        for t in tweets:
            author_id = t.get("author_id")
            username = user_map.get(author_id, "Unknown User")
            results.append(f"{username}: {t['text']}")
        return "\n\n".join(results)
    except Exception as e:
        return f"Failed to fetch tweets: {e}"

