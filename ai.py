"""
Install the Google AI Python SDK

$ pip install google-generativeai

See the getting started guide for more information:
https://ai.google.dev/gemini-api/docs/get-started/python
"""

import os

import google.generativeai as genai

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

# Create the model
# See https://ai.google.dev/api/python/google/generativeai/GenerativeModel
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

with open("ai_instructions.txt") as f:
    ai_instructions = f.read()

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",  # gemini-1.5-pro keeps throwing an internal error idk why
    generation_config=generation_config,
    # safety_settings = Adjust safety settings
    # See https://ai.google.dev/gemini-api/docs/safety-settings


    system_instruction=ai_instructions,
)

# Every user has his own chat history here
# every time you redeploy the bot, it will start a new chat for every user.
# I don't know if this noticeably affects the memory when dealing with a lot of users
chat_sessions = {}


def send_message_to_user(user_id, message) -> str:
    if not chat_sessions.get(user_id):
        chat_sessions[user_id] = model.start_chat()

    return chat_sessions[user_id].send_message(message).text
