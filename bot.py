from pyrogram import Client, idle, __version__ as pv
from configs import *

class cybershortner(Client):
    def main():
        plugins = dict(root="plugins")
        bot = Client(
            "cyberurlshortner",
            bot_token=BOT_TOKEN,
            api_id=API_ID,
            api_hash=API_HASH,
            plugins=plugins,
            workers=500,
            in_memory=True
        )
       
        bot.start()
        print(f"{BOT_USERNAME} with latest version({pv}) Started successfully..😎🤏")
        idle()

  if __name__ == "__main__":
    cybershortner.main()
