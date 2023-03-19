from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware

import shutil
import os
from pathlib import Path
import aiohttp
import asyncio
import uvicorn
import time

app = FastAPI()

app.add_middleware(
  CORSMiddleware,
  allow_origins=["*"],
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)

UPLOAD_DIR = 'uploads'
Path(UPLOAD_DIR).mkdir(parents=True, exist_ok=True)

@app.post("/api/save-audio")
async def save_audio(audio: UploadFile = File(...)):
    audio_file_path = os.path.join(
        UPLOAD_DIR, f"recorded_audio_{int(time.time())}{Path(audio.filename).suffix}"
    )

    with open(audio_file_path, "wb") as buffer:
        shutil.copyfileobj(audio.file, buffer)

    return {"message": "Audio file saved successfully"}


async def get_public_ip():
    async with aiohttp.ClientSession() as session:
        async with session.get("https://api.ipify.org?format=json") as response:
            data = await response.json()
            return data["ip"]


if __name__ == "__main__":


    PORT = int(os.environ.get("PORT", 3000))
    try:
        public_ip = asyncio.run(get_public_ip())
        print(f"Server is running on https://{public_ip}:{PORT}")
        print("Local:               http://localhost:3000")
    except Exception as error:
        print("Error fetching public IP:", error)
        print(f"Server is running on port {PORT}")

    uvicorn.run(app, host="0.0.0.0", port=PORT)