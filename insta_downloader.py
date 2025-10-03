import instaloader
import re
from pathlib import Path
import logging

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


def download_instagram_media(url: str, tmp_dir: str) -> dict:
    """
    Downloads Instagram media (video or picture) from a given URL to a temporary directory.

    Args:
        url: The URL of the Instagram post.
        tmp_dir: The directory to download the media to.

    Returns:
        A dictionary containing the file path and file name of the downloaded media.
    """
    logging.info(f"Attempting to download media from URL: {url}")
    match = re.search(r"/p/([^/]+)", url)
    if not match:
        match = re.search(r"/reel/([^/]+)", url)
    if not match:
        match = re.search(r"/tv/([^/]+)", url)

    if not match:
        logging.error("Invalid Instagram post URL provided.")
        raise ValueError("Invalid Instagram post URL")

    shortcode = match.group(1)
    logging.info(f"Extracted shortcode: {shortcode}")

    L = instaloader.Instaloader(
        download_videos=True,
        download_pictures=True,
        download_video_thumbnails=False,
        save_metadata=False,
    )

    try:
        post = instaloader.Post.from_shortcode(L.context, shortcode)
        logging.info(f"Downloading post from shortcode: {shortcode}")
        L.download_post(post, target=Path(tmp_dir))

        # Find the downloaded media file (video or picture)
        for f in Path(tmp_dir).iterdir():
            if f.suffix in [".mp4", ".jpg", ".jpeg", ".png"]:
                logging.info(f"Successfully downloaded media to: {f}")
                return {"filePath": str(f), "fileName": f.name}

        logging.error("Downloaded media not found in the temporary directory.")
        raise FileNotFoundError("Downloaded media not found.")

    except Exception as e:
        logging.error(f"An error occurred during download: {e}")
        raise e
