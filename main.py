from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Web API on CPU server"}

@app.get("/mistral")
async def mistral(prompt: str = "Tell me a joke"):
    # Proxy to GPU server
    try:
        response = requests.post(f"http://nucleus:11434/api/generate", json={
            "model": "mistral:7b-q4_0",
            "prompt": prompt
        })
        return response.json()
    except Exception as e:
        return {"error": f"Mistral unavailable: {str(e)}"}