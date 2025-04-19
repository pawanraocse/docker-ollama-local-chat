import requests
from config import MODEL_NAME, OLLAMA_CONTAINER

def chat_with_model():

    print("Chat with Gemma! Type 'exit' to quit.")
    
    while True:
        prompt = input("\nYou: ")
        if prompt.lower() in ["exit", "quit"]:
            break

        res = requests.post(
            "http://ollama:11434/api/generate",  # Use container name as hostname
            json={
                "model": MODEL_NAME,
                "prompt": prompt,
                "stream": False
            }
        )

        if res.ok:
            print("Gemma:", res.json()["response"].strip())
        else:
            print("Error:", res.text)

if __name__ == "__main__":
    chat_with_model()
