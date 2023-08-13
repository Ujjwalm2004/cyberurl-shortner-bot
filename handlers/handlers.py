from configs import *
from database import db
from pyrogram import Client
from pyrogram.types import Message
import requests as re


async def force_sub(c, m):
    if FSUB_CHANNEL:
        try:
            user = await c.get_chat_member(FSUB_CHANNEL, message.from_user.id)
            if user.status == "banned":
                await m.reply_text("Sorry, you are banned 🥲")
                return 400
        except UserNotParticipant:
            await m.reply_text(
                text="Hey bruh, you have to subscribe to my update channel to use me",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("Jᴏɪɴ Cʜᴀɴɴᴇʟ 📣", url=f"{FSUB_CHANNEL}"),
                            InlineKeyboardButton("Sᴜᴩᴩᴏʀᴛ", url="https://t.me/cyberstock_support")
                        ],
                        [
                            InlineKeyboardButton("Rᴇғʀᴇsʜ 🔄", callback_data="rfrsh")
                        ]
                    ]
                )
            )
            return 400
    return 200


async def adduser(c, m):
    if not await db.is_user_exist(m.from_user.id):
        await db.add_user(message.from_user.id)
        if LOG_CHANNEL:
            await c.send_message(
                LOG_CHANNEL,
                f"#new_user :-\n\n{m.from_user.mention} started @{BOT_USERNAME}!"
            )

async def handle_private_message(c, m):
    await adduser(c, m)
    fsub = await force_sub(c, m)
    if fsub == 400:
        return


async def get_shorturl(link, u_id: int):
    try:
        api = await db.get_api(u_id)
      
        site = f'https://cyberurl.in/api'
        params = {'api': api, 'url': link}
        r = re.get(site, params=params)
        rs = r.json()
        if 'status' in rs and rs['status'] == 'success' and 'shortenedUrl' in rs:
            return rs['shortenedUrl']

    except re.exceptions.RequestException as e:
        print(f"Error occurred while accessing the shortening service: {e}")
    except ValueError as ve:
        print(f"Invalid response data from shortening service: {ve}")
