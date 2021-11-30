import os
import pyrogram
import logging
from config import Config

import requests
import time
import os
import re
logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)


if __name__ == "main" :
    print("Starting...")
    plugins = dict(root="kek")
    app = pyrogram.Client(
        "kek",
        bot_token=Config.BOT_TOKEN,
        api_id=Config.API_ID,
        api_hash=Config.API_HASH,
        plugins=kek
    )
    app.run()

#@Client.on_message(filters.command(["update"]) & filters.user(1089528685))

#async def meme(bot, update):
 #   k = await bot.send_message(update.chat.id, "updating..", reply_to_message_id=update.message_id)
  #  os.system("git clone https://github.com/sathjya/stunning-octo-chainsaw")
  #  os.system("cd stunning-octo-chainsaw && python3 main.py")
  #  time.sleep(3)
  #  await k.edit("success")
   