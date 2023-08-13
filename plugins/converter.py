from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message


@filters.private
def link_filter(_, __, message):
    return message.text.startswith('http')

@Client.on_message(filters.text & link_filter)
async def shorten_link(c, m):
  u_id = m.from_user.id
  u_api = await db.get_api(u_id)
  if u_api:
    
  links = message.text.split('\n')
  short_links = []
  
  for link in links:
    short_link = short_url(link)
    if short_link:
      short_links.append(shortened_link)
      
      if len(shortened_links) == 1:
        await message.reply(f"Here's your shortened link: {shortened_links[0]}")
      elif len(short_links) > 1:
        msg = "Here are the shortened links:\n\n"
        
        for n, shortened_link in enumerate(short_links):
          msg += f"{n + 1}. {shortened_link}\n"
        
        await m.reply(msg)
      else:
        await m.reply("Oops! Something went wrong while shortening the links.")
