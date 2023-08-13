import os
from pyrogram import Client

API_ID = int(os.environ.get("API_ID", ""))
API_HASH = os.environ.get("API_HASH", "")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
me = Client.get_me()
username = me.username
name = me.first_name
BOT_USERNAME = os.environ.get("BOT_USERNAME", f"{username}")
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", ""))
FSUB_CHANNEL = os.environ.get("FSUB_CHANNEL")
START_TXT = f'''Hᴇʟʟᴏ {}, I Aᴍ {name}!.
๏ I ᴄᴀɴ Cᴏɴᴠᴇʀᴛ ʏᴏᴜʀ ʟɪɴᴋs ᴛᴏ Sʜᴏʀ ʟɪɴᴋs ᴜsɪɴɢ ʏᴏᴜ [ᴀᴩᴜ](https://cyberurl.m/member/tools/api).
๏ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ Hᴇʟᴩ Mᴇɴᴜ ʙᴜᴛᴛᴏɴ ʙᴇʟᴏᴡ ᴛᴏ ɢᴇᴛ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ᴀʙᴏᴜᴛ ᴍʏ ᴄᴏᴍᴍᴀɴᴅs.
'''
