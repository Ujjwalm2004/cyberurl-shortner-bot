import os
from pyrogram import Client

API_ID = int(os.environ.get("API_ID", ""))
API_HASH = os.environ.get("API_HASH", "")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
me = Client.get_me()
username = me.username
BOT_USERNAME = os.environ.get("BOT_USERNAME", f"{username}")
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", ""))
