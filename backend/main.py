# uvicorn main:app
# uvicorn main:app --reload

# Main imports
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from decouple import config
import openai

# Custom imports
from functions.openai_requests import convert_audio_to_text

# Initialize the app
app = FastAPI()


# CORS - origins
origins = [
    "http://localhost:5173",
    "http://localhost:5174",
    "http://localhost:4173",
    "http://localhost:4174",
    "http://localhost:3000"
]

# CORS - middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]

)
# Health check endpoint
@app.get("/health")
async def root():
    return {"message": "healthy!"}

# Get the audio
@app.post("/post-audio-get/")
async def get_audio(file: UploadFile=File(...)):
    
    audio_input = open("voice.mp3", 'rb')
    text = convert_audio_to_text(audio_input)
    return {"text": text}


# Post the audio
# Note: not playing in browser when using the post request
# @app.post("/post-audio/")
# async def post_audio(file: UploadFile=File(...)):
#     print("hello")




