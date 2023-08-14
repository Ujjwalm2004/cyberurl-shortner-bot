from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from handlers.handlers import short_url
from database.users import db


@Client.on_message(filters.text & link_filter)
async def shorten_link(_, message):
    u_id = message.from_user.id
    u_api = await db.get_api(u_id)
    if u_api:
        links = message.text.split('\n')
        short_links = []

        for link in links:
            short_link = short_url(link, u_api)
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
