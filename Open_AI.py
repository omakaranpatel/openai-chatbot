import streamlit as st
from openai import OpenAI
import time

# Configure OpenAI API Key
client = OpenAI(api_key="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")

# Function to handle chatbot logic with rate limiting
def chatbot_response(user_input):
    # Introduce a delay to avoid hitting rate limits
    time.sleep(1) # Wait for 1 second

    response = client.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        response_format={"type": "json_object"},
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_input}
        ]
    )
    return response.choices[0].message.content

# Streamlit UI
st.title("OpenAI Chatbot")

user_input = st.text_input("Type your message here:")
if user_input:
    try:
        response = chatbot_response(user_input)
        st.write(f"Chatbot: {response}")
    except Exception as e:
        st.write(f"Error: {e}")
