from openai import OpenAI
from fastapi import FastAPI
from pydantic import BaseModel

# Initialize OpenAI client
client = OpenAI(api_key='dummy')


app = FastAPI()

class userInput(BaseModel):
    prompt: str

def chat_with_gpt(prompt):
    # Generate completion based on user input
    chat_completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    # Extract and return bot's response
    bot_response = chat_completion.choices[0].message.content
    return bot_response

@app.post("/ChatBot")
def chatbot(user_input: userInput):
    bot_response = chat_with_gpt(user_input.prompt)
    return bot_response

# Example conversation loop
# while True:
#     user_input = input("You: ")
#     if user_input.lower() == 'exit':
#         print("Goodbye!")
#         break
#     bot_response = chat_with_gpt(user_input)
#     print("Bot:", bot_response)
