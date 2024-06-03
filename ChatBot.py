from openai import OpenAI
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Initialize OpenAI client
client = OpenAI(api_key='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')

app = FastAPI()

class UserInput(BaseModel):
    prompt: str

def chat_with_gpt(prompt: str) -> str:
    try:
        chat_completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        bot_response = chat_completion.choices[0].message.content
        return bot_response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/ChatBot")
def chatbot(user_input: UserInput):
    bot_response = chat_with_gpt(user_input.prompt)
    return {"response": bot_response}
