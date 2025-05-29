## AI Twitter Agent
This project implements a simple AI-powered Twitter agent that can perform two main actions:

Generate and post a new tweet based on a user prompt, leveraging Google's Gemini AI.

Fetch recent public tweets matching a specific keyword from Twitter.

The agent is built with a Gradio interface for easy interaction, making it a conversational tool for managing basic Twitter tasks.

# ✨ Features
AI-Powered Tweet Generation: Uses Google's gemini-2.0-flash model to craft concise tweets from your prompts.

Tweet Posting: Publishes generated tweets directly to your authenticated Twitter account.

Keyword-Based Tweet Search: Retrieves recent public tweets related to a given keyword.

Efficient Twitter API Usage: Utilizes Twitter API v2's expansions to fetch user details efficiently, reducing API calls and improving search performance.

User-Friendly Interface: A simple chat-based interface powered by Gradio.

# 🛠️ Technologies Used
Python 3.x

tweepy: A Python library for accessing the Twitter API.

requests: For making HTTP requests to the Google Gemini API.

python-dotenv: For loading environment variables from a .env file.

gradio: For building the interactive web user interface.

# 🚀 Setup and Installation
Follow these steps to get your AI Twitter Agent up and running.

1. Clone the Repository
git clone <your-repository-url> # Replace with your actual repository URL
cd ai-twitter-agent # Or whatever your project folder is named

2. Create a Virtual Environment (Recommended)
python -m venv venv
source venv/bin/activate # On Windows: .\venv\Scripts\activate

3. Install Dependencies
Install the required Python packages using pip:

pip install -r requirements.txt

requirements.txt content:

requests==2.31.0
tweepy==4.14.0
python-dotenv==1.0.0
gradio==4.29.0 # Or the version you are using

4. Set Up Environment Variables (.env file)
You need to obtain API keys and tokens from Twitter Developer and Google AI Studio. Create a file named .env in the root directory of your project (the same directory as twitter_agent.py and app.py) and add the following:

# Google Gemini API Key
GEMINI_API_KEY="YOUR_GOOGLE_GEMINI_API_KEY"

# Twitter API v1.0a Credentials (for posting tweets)
TWITTER_API_KEY="YOUR_TWITTER_CONSUMER_KEY"
TWITTER_API_SECRET="YOUR_TWITTER_CONSUMER_SECRET"
TWITTER_ACCESS_TOKEN="YOUR_TWITTER_ACCESS_TOKEN"
TWITTER_ACCESS_SECRET="YOUR_TWITTER_ACCESS_SECRET"

# Twitter API v2 Bearer Token (for searching tweets)
# You can generate this from your Twitter Developer App settings
TWITTER_BEARER_TOKEN="YOUR_TWITTER_BEARER_TOKEN"

# Twitter OAuth2.0 Client credentials (optional, for future OAuth2 flows)
# Not strictly used in current implementation but good to have if you intend to expand
TWITTER_OAUTH2_CLIENT_ID="YOUR_TWITTER_OAUTH2_CLIENT_ID"
TWITTER_OAUTH2_CLIENT_SECRET="YOUR_TWITTER_OAUTH2_CLIENT_SECRET"

Important Notes for API Keys:

Google Gemini API Key: Get this from Google AI Studio.

Twitter API Keys/Tokens:

Go to the Twitter Developer Platform.

Create a new project and app.

Under your app's settings, find "Keys and tokens".

Generate Consumer Keys (API Key & Secret) and Access Token & Secret (for OAuth 1.0a User Context). Make sure your app has "Read and Write" permissions for posting tweets.

Generate a Bearer Token (for OAuth 2.0 App-only).

5. Run the Application
Once all dependencies are installed and your .env file is configured, you can run the Gradio application:

python app.py

The application will start, and you'll see a local URL (e.g., http://127.0.0.1:7860) in your terminal. Open this URL in your web browser to interact with the agent. If share=True is enabled in app.py, Gradio will also provide a public URL that you can share.

📝 How to Use the Agent
Once the Gradio interface is open in your browser, you can interact with the AI Twitter Agent in the chat window:

To Generate and Post a Tweet:

Simply type your prompt or idea for a tweet.

Example: Write a tweet about the importance of open source.

The agent will generate a tweet using Gemini and then attempt to post it to your Twitter account. You'll receive a confirmation message with the tweet text and ID.

To Fetch Recent Tweets by Keyword:

Start your command with search: followed by the keyword you want to search for.

Example: search:artificial intelligence news

The agent will search Twitter for recent tweets matching your keyword and display a list of results, including the username of the author.

⚠️ Troubleshooting
Error: GEMINI_API_KEY not found in environment variables.

Make sure you have created a .env file in the correct directory and that GEMINI_API_KEY is set correctly within it.

Failed to fetch tweets: 400 Bad Request The max_results query parameter value [X] is not between 10 and 100

This error indicates that the max_results parameter sent to the Twitter API was outside its allowed range. The code has been updated to default to 10, but ensure no custom count value passed to fetch_tweets is causing this.

Failed to fetch tweets: [Any other error] or Failed to post tweet: [Any other error]

Check your Twitter API credentials: Double-check all TWITTER_API_KEY, TWITTER_API_SECRET, TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_SECRET, and TWITTER_BEARER_TOKEN in your .env file. Ensure there are no typos and that they correspond to the correct access levels (e.g., "Read and Write" for posting).

Twitter API Rate Limits: If fetch_tweets or post_tweet seems to hang or take a very long time without an explicit error, you might be hitting Twitter's rate limits. The tweepy client is configured to wait_on_rate_limit=True, meaning it will pause execution until the limit resets (typically after 15 minutes). Check your Twitter Developer Portal for your current rate limit status.

"Error generating tweet: Unexpected API response structure."

This might indicate an issue with the Gemini API response. Ensure your GEMINI_API_KEY is valid and the Gemini service is operational.

Gradio Interface Not Loading:

Ensure app.py is running without errors in your terminal. Check if the port (default 7860) is

