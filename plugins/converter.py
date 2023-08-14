from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from handlers.handlers import short_url
from database.users import db
import requests
from urllib.parse import quote



@Client.on_message(filters.text & filters.private)
async def shorten_link(_, message: Message):
    if not message.text.startswith("http://") and not message.text.startswith("https://"):
        snd_msg = await message.reply_text("Send http:// or https:// link to short")
        return snd_msg

    u_id = message.from_user.id
    u_api = await db.get_api(u_id)
    if u_api:
        links = message.text.split('\n')
        short_links = []

        for link in links:
            short_link = await shrt_limk(link, u_api)
            if short_link:
                short_links.append(short_link)

        if len(short_links) == 1:
            await message.reply(f"__Hᴇʀᴇ ɪs ʏᴏᴜʀ Sʜᴏʀᴛ Lɪɴᴋ__: `{short_links[0]}`(Tᴀᴩ ᴛᴏ Cᴏᴩʏ)")
        elif len(short_links) > 1:
            msg = "__Hᴇʀᴇ ᴀʀᴇ ʏᴏᴜʀ Sʜᴏʀᴛ Lɪɴᴋs__:\n\n"

            for n, shortened_link in enumerate(short_links):
                msg += f"{n + 1}. {shortened_link}\n"

            await message.reply(msg)
        else:
            await message.reply("Something went wrong while shortening the links.")


async def shrt_limk(url, u_api):
    try:
        res = requests.get(f'https://cyberurl.in/api?api={u_api}&url={quote(url)}')
        res.raise_for_status()
        data = res.json()
        shorted = data.get('shortenedUrl')
        return shorted

