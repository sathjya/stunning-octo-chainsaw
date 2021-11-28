import os
import pyrogram
import logging
from PicBot.config_var import Config

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)


if __name__ == "__main__" :
    print("Starting Bot...")
    plugins = dict(root="PicBot/Plugins")
    app = pyrogram.Client(
        "PicBot",
        bot_token=Config.BOT_TOKEN,
        api_id=Config.API_ID,
        api_hash=Config.API_HASH,
        plugins=plugins
    )
    app.run()
