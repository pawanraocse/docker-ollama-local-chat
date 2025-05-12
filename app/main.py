from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import os
from pathlib import Path
from init_ollama import wait_for_ollama
from contextlib import asynccontextmanager
import requests
import logging
from config import OLLAMA_HOST, MODEL_NAME


# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create documents directory if it doesn't exist
DOCUMENTS_DIR = Path("/app/documents")
DOCUMENTS_DIR.mkdir(exist_ok=True)

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Lifespan event handler for FastAPI"""
    # Startup
    if not wait_for_ollama():
        raise Exception("Failed to initialize Ollama service")
    yield
    # Shutdown
    pass

app = FastAPI(title="Local Support Bot", lifespan=lifespan)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Local Support Bot API is running"}

@app.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    """
    Upload a document to be processed and embedded
    """
    file_path = DOCUMENTS_DIR / file.filename
    with open(file_path, "wb") as buffer:
        content = await file.read()
        buffer.write(content)
    return {"filename": file.filename, "status": "uploaded"}

@app.get("/query")
async def query(question: str):
    """
    Query the AI with a question
    """
    try:
        logger.info(f"Received question: {question}")
        
        # Call Ollama API
        ollama_url = f"{OLLAMA_HOST}/api/generate"
        payload = {
            "model": MODEL_NAME,
            "prompt": question,
            "stream": False
        }
        
        logger.info(f"Sending request to Ollama API: {ollama_url}")
        logger.info(f"Payload: {payload}")
        
        response = requests.post(ollama_url, json=payload)
        logger.info(f"Ollama API response status: {response.status_code}")
        
        if response.status_code == 200:
            result = response.json()
            logger.info(f"Ollama API response: {result}")
            return {"answer": result.get("response", "No response from AI")}
        else:
            error_msg = f"Failed to get response from AI. Status code: {response.status_code}, Response: {response.text}"
            logger.error(error_msg)
            return {"error": error_msg}
            
    except Exception as e:
        error_msg = f"Error querying AI: {str(e)}"
        logger.error(error_msg)
        return {"error": error_msg}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 