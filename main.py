import openai
import os
from fastapi import FastAPI

app = FastAPI()

# Load OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.post("/chat")
async def chat(query: dict):
    user_message = query.get("message", "")

    response = openai.ChatCompletion.create(
        model="gpt-4-turbo",
        messages=[{"role": "system", "content": "You are a project management assistant."},
                  {"role": "user", "content": user_message}]
    )

    return {"response": response["choices"][0]["message"]["content"]}

@app.get("/")
async def root():
    return {"message": "Project Manager Chatbot is Running!"}
