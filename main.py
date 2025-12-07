import os
import requests
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

app = FastAPI()

class ChatRequest(BaseModel):
    chat: str

@app.post("/chat")
async def chat_endpoint(data: ChatRequest):
    try:
        if not data.chat:
            raise ValueError("chat field required")

        url = "https://api.groq.com/openai/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {GROQ_API_KEY}",
            "Content-Type": "application/json",
        }
        payload = {
            "model": "llama-3.1-8b-instant",  # UPDATED MODEL (working 2025)
            "messages": [{"role": "user", "content": data.chat}],
            "temperature": 0.7
        }

        response = requests.post(url, headers=headers, json=payload)
        response_json = response.json()

        # Debug log
        print(response_json)

        # Error from API?
        if "error" in response_json:
            raise Exception(response_json["error"]["message"])

        return {"response": response_json["choices"][0]["message"]["content"]}

    except Exception as e:
        raise HTTPException(status_code=500, detail="LLM error: " + str(e))
