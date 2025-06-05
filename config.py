from dotenv import load_dotenv
import os

load_dotenv()

# Configuration settings
OUTPUT_DIR = "output"
DOWNLOAD_DIR = "downloads"
os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(DOWNLOAD_DIR, exist_ok=True)
