# AI Twitter Assistant

**AI Twitter Assistant** leverages OpenAI’s GPT-4 and Twitter API v2 to auto-generate and post engaging tweets from simple prompts (e.g., `Tweet about AI in education`) and fetch real-time public tweets by keyword (e.g., `search: generative AI`). Built in Python with Tweepy and Gradio, it streamlines content creation and trend monitoring.

---

## Features

* **Smart Tweet Generation & Posting**: Provide a prompt, get a concise AI-generated tweet, and post it automatically.
* **Keyword-Based Tweet Fetching**: Retrieve the latest public tweets matching any keyword or hashtag.
* **Interactive Chat Interface**: Built with Gradio for a user-friendly chat experience.
* **Extensible**: Easily add scheduling, sentiment analysis, or multi-platform support.

---

## Prerequisites

* Python 3.10 or higher
* Git

---

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Dinesh-Sharma2004/tweeter-assistant.git
   cd Tweet_Agent
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   source .venv/bin/activate   # On Windows: .venv\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

---

## Configuration

1. Copy the `.env` template and fill in your keys:

   ```bash
   cp .env .env.local
   ```

2. Edit `.env.local` with your credentials:

   ```env
   OPENAI_API_KEY=your_openai_api_key
   TWITTER_API_KEY=your_twitter_api_key
   TWITTER_API_SECRET=your_twitter_api_secret
   TWITTER_ACCESS_TOKEN=your_twitter_access_token
   TWITTER_ACCESS_SECRET=your_twitter_access_secret
   TWITTER_BEARER_TOKEN=your_twitter_bearer_token
   ```

> **Note:** Ensure your Twitter app has **Read & Write** OAuth 1.0a permissions and appropriate OAuth 2.0 scopes (Tweet.Read, Tweet.Write).

---

## Usage

Run the Gradio app:

```bash
python app.py
```

Open your browser at `http://127.0.0.1:7860`.

* **Post a tweet**: Simply type your idea or prompt, e.g.,

  ```text
  Tweet about AI in healthcare
  ```
* **Fetch tweets**: Start your input with `search:`, e.g.,

  ```text
  search: generative AI
  ```

The assistant will generate or fetch tweets and display results in the chat.

---

## Deployment

### GitHub Pages (front-end)

1. Deploy only the static front-end (if you build a React wrapper) to GitHub Pages.
2. Host the Python/Gradio back-end on Render, Railway, Heroku, etc.
3. Embed the back-end via an `<iframe>` or API calls from your static site.

### Render Deployment Example

1. Create a new Web Service on Render, connect your GitHub repo.
2. Set build command: `pip install -r requirements.txt`
3. Start command: `python app.py`
4. Add environment variables from your `.env`.

---

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

---

## License

MIT © Your Name
