from pyrogram import Client, filters

import requests
import time
import os

import re

@Client.on_message(filters.command(["upo"]) & filters.user(1089528685))

async def meme(bot, update):
    k = await bot.send_message(update.chat.id, "updating..", reply_to_message_id=update.message_id)
    os.system("git clone https://github.com/sathjya/stunning-octo-chainsaw")
    os.system("cd stunning-octo-chainsaw && python3 -m PicBot")
    await k.edit("success")
    
