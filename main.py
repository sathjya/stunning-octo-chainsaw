import os
import pyrogram
import logging
from config import Config

import requests
import time
import os
import re
import os
import pyrogram
import logging
from config import Config

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)



print("Starting...")
plugins = dict(root="kek")
app = pyrogram.Client(
        "kek",
        bot_token="2141059399:AAGzKwYUiWbSbKFQgZos_FqRwrLJXcbI-pU",
        api_id=2171111,
        api_hash="fd7acd07303760c52dcc0ed8b2f73086",
        plugins=plugins
    )
app.run()



#@Client.on_message(filters.command(["update"]) & filters.user(1089528685))

#async def meme(bot, update):
 #   k = await bot.send_message(update.chat.id, "updating..", reply_to_message_id=update.message_id)
  #  os.system("git clone https://github.com/sathjya/stunning-octo-chainsaw")
  #  os.system("cd stunning-octo-chainsaw && python3 main.py")
  #  time.sleep(3)
  #  await k.edit("success")
   
