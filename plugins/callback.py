from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, Message
from pyrogram.errors import UserNotParticipant, QueryIdInvalid
from configs import *


@Client.on_callback_query()
async def callback(bot: Client, query: CallbackQuery):
    me = await bot.get_me()
    cb_data = query.data

    if cb_data == "delete":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass

    elif cb_data == "help":
        await query.message.edit(
            HELP_TEXT.format(me.mention),
            reply_markup=InlineKeyboardMarkup(
              [
                  [InlineKeyboardButton("Sᴇᴛ Aᴩɪ", callback_data="api"),
                   InlineKeyboardButton("Cᴏᴍᴍᴀɴᴅs", callback_data="commands")],
                  [InlineKeyboardButton("Aʙᴏᴜᴛ", callback_data="api"),
                   InlineKeyboardButton("Eᴀʀɴ Mᴏɴᴇʏ", callback_data="earn_money")],
                  [InlineKeyboardButton("Sᴜᴩᴩᴏʀᴛ Gʀᴏᴜᴩ", url=f"https://t.me/cyberstock_support"),
                   InlineKeyboardButton("Bᴀᴄᴋ", callback_data="start")]
              ]
            )
        )
      
    elif cb_data == "about":
      await query.message.edit(
        ABOUT_TEXT.format(me.first_name),
        reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("Hᴇʟᴩ Mᴇɴᴜ", callback_data="help"),
                     InlineKeyboardButton("Eᴀʀɴ Mᴏɴᴇʏ", callback_data="earn_money")],
                    [InlineKeyboardButton("Sᴜᴩᴩᴏʀᴛ Gʀᴏᴜᴩ", url=f"https://t.me/cyberstock_support")],
                    [InlineKeyboardButton("Bᴀᴄᴋ", callback_data="start")]
                ]
        )
      )
      
    elif cb_data == "earn_money":
        await query.message.edit(
            text="๏Yᴏᴜ ᴄᴀɴᴇᴀʀɴ ᴜsɪɴɢ ᴏᴜʀ ᴏғғɪᴄɪᴀʟ sʜᴏʀᴛɴᴇʀ sɪᴛᴇ [Cʏʙᴇʀᴜʀʟ.ɪɴ](cyberurl.in).\n๏Sɪɢɴ ᴜᴩ ᴀɴᴅ ɢᴇɴʀᴀᴛᴇ sʜᴏʀᴛ ʟɪɴᴋs ᴀɴᴅ sʜᴀʀᴇ ᴛʜᴇᴍ ᴛᴏ ᴇᴀʀɴ ᴍᴏɴᴇʏ.",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("Hᴇʟᴩ", callback_data="help"),
                        InlineKeyboardButton("Aʙᴏᴜᴛ", callback_data="about")
                    ],
                    [
                        InlineKeyboardButton("Sᴜᴩᴩᴏʀᴛ Gʀᴏᴜᴩ", url=f"https://t.me/cyberstock_support"),
                        InlineKeyboardButton("Bᴀᴄᴋ", callback_data="start")
                    ]
                ]
            )
        )

    elif cb_data == "start":
        await query.message.edit(
            START_TEXT.format(query.from_user.mention),
            reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("Hᴇʟᴩ Mᴇɴᴜ", callback_data="help"),
                 InlineKeyboardButton("Eᴀʀɴ Mᴏɴᴇʏ", callback_data="earn_money")],
                [InlineKeyboardButton("Cʜᴀɴɴᴇʟ", url="https://t.me/Cyber_Url"),
                 InlineKeyboardButton("Sᴜᴩᴩᴏʀᴛ", url="https://t.me/cyberstock_support")],
                [InlineKeyboardButton("Cʟᴏsᴇ ❌", callback_data="delete")]
            ]
            )
        )
            
    elif cb_data == "rfrsh":
        if FSUB_CHANNEL:
            try:
                user = await bot.get_chat_member(FSUB_CHANNEL, query.message.chat.id)
                if user.status == "banned":
                    await query.message.edit(
                        text="Sorry Sir, You are Banned to use me. Contact my [Support Group](https://t.me/Ng_SupportS).",
                        disable_web_page_preview=True
                    )
                    return
            except UserNotParticipant:
                await query.message.edit(
                    text="**I Don't like Your Silliness, Don't Be Oversmart! 😑**\n\n",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("😇 Join Channel 😇", url=f"https://t.me/{FSUB_CHANNEL}")
                            ],
                            [
                                InlineKeyboardButton("🔄 Refresh 🔄", callback_data="rfrsh")
                            ]
                        ]
                    )
                )
                return

            await query.message.edit(
                START_TEXT.format(query.from_user.mention),
                disable_web_page_preview=True,
                reply_markup=InlineKeyboardMarkup(
                  [
                    [InlineKeyboardButton("Hᴇʟᴩ Mᴇɴᴜ", callback_data="help"),
                     InlineKeyboardButton("Eᴀʀɴ Mᴏɴᴇʏ", callback_data="earn_money")],
                    [InlineKeyboardButton("Cʜᴀɴɴᴇʟ", url="https://t.me/Cyber_Url"),
                    [InlineKeyboardButton("Cʟᴏsᴇ ❌", callback_data="delete")]
                  ]
                )
            )
            
              
      
