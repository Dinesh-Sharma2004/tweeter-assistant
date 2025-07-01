import gradio as gr
from twitter_agent import generate_tweet, post_tweet, fetch_tweets, delete_tweet
import os

def agent_response(user_input, history):
    current_messages = []
    current_messages.append({"role": "user", "content": user_input})

    if user_input.strip().lower().startswith("search:"):
        keyword = user_input.strip()[7:].strip()
        result = fetch_tweets(keyword)
    elif user_input.strip().lower().startswith("delete:"):
        try:
            tweet_id = user_input.strip()[7:].strip()
            if not tweet_id.isdigit():
                result = "Error: Please provide a valid tweet ID (numbers only) after 'delete:'."
            else:
                result = delete_tweet(tweet_id)
        except Exception as e:
            result = f" Error processing delete command: {e}"
    else: 
        tweet_text = generate_tweet(user_input)
        result = post_tweet(tweet_text)

    current_messages.append({"role": "assistant", "content": result})
    return current_messages

iface = gr.ChatInterface(
    fn=agent_response,
    title="AI Twitter Agent",
    theme="default",
    type="messages",
)

if __name__ == "__main__":
    port = int(os.getenv("PORT", 7860))
    iface.launch(server_name="0.0.0.0", server_port=port)
