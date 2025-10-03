import os
import shutil
import time
from pathlib import Path
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import uvicorn
import threading
import logging

from insta_downloader import download_instagram_media

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

app = FastAPI()

TMP_DIR = Path(__file__).parent / "tmp"
if not TMP_DIR.exists():
    TMP_DIR.mkdir()

# Serve static files from the 'public' directory
app.mount("/public", StaticFiles(directory="public"), name="public")
app.mount("/videos", StaticFiles(directory=TMP_DIR), name="videos")


class DownloadRequest(BaseModel):
    url: str


@app.middleware("http")
async def log_requests(request: Request, call_next):
    logging.info(f"Incoming request: {request.method} {request.url}")
    response = await call_next(request)
    return response


@app.get("/")
async def read_index():
    return FileResponse("public/index.html")


@app.get("/about")
async def read_about():
    return FileResponse("public/about.html")


@app.get("/terms")
async def read_terms():
    return FileResponse("public/terms.html")


@app.get("/privacy")
async def read_privacy():
    return FileResponse("public/privacy.html")


@app.get("/contact")
async def read_contact():
    return FileResponse("public/contact.html")


@app.post("/download")
async def download(request: DownloadRequest):
    try:
        logging.info(f"Download request for URL: {request.url}")
        result = download_instagram_media(request.url, str(TMP_DIR))
        logging.info(f"Download successful for URL: {request.url}")
        return {"downloadUrl": f"/videos/{result['fileName']}"}
    except Exception as e:
        logging.error(f"Download failed for URL: {request.url} - {e}")
        raise HTTPException(status_code=400, detail=str(e))


def cleanup_old_files():
    """Cleanup old files (TTL: 1 hour)"""
    while True:
        now = time.time()
        for f in TMP_DIR.glob("*"):
            if f.is_file():
                if now - f.stat().st_mtime > 3600:
                    logging.info(f"Deleting old file: {f}")
                    os.remove(f)
        time.sleep(1800)


@app.on_event("startup")
async def startup_event():
    logging.info("Server starting up.")
    cleanup_thread = threading.Thread(target=cleanup_old_files, daemon=True)
    cleanup_thread.start()
    logging.info("Cleanup thread started.")


@app.on_event("shutdown")
async def shutdown_event():
    logging.info("Server shutting down.")


if __name__ == "__main__":
    logging.info("Starting server with uvicorn.")
    uvicorn.run(app, host="0.0.0.0", port=3000)
