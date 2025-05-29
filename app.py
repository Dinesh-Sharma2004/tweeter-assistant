import gradio as gr
from twitter_agent import generate_tweet, post_tweet, fetch_tweets
import os

def agent_response(user_input, history):

    current_messages = []

    current_messages.append({"role": "user", "content": user_input})

    if user_input.strip().lower().startswith("search:"):
        keyword = user_input.strip()[7:].strip()
        result = fetch_tweets(keyword)
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
