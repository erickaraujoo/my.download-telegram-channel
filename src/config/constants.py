import os
from dotenv import load_dotenv

load_dotenv()

channel_names = [nome.strip() for nome in os.getenv("CHANNEL_NAMES").split(",")]
download_type_names = ["Mídias"]
