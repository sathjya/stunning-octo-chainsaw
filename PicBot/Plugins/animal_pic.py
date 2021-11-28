from pyrogram import Client, filters
import requests
import re

        
@Client.on_message(filters.command(["panda"]))
async def panda(bot, update):
    link = "https://some-random-api.ml/img/panda"
    r = requests.get(url=link).json()
    image_s = r["link"]
    await bot.send_photo(update.chat.id, image_s, reply_to_message_id=update.message_id)


@Client.on_message(filters.command(["cat"]))
async def cat(bot, update):
    link = "https://some-random-api.ml/img/cat"
    r = requests.get(url=link).json()
    image_s = r["link"]
    await bot.send_photo(update.chat.id, image_s, reply_to_message_id=update.message_id)


@Client.on_message(filters.command(["dog"]))
async def dog(bot, update):
    link = "https://some-random-api.ml/img/dog"
    r = requests.get(url=link).json()
    image_s = r["link"]
    await bot.send_photo(update.chat.id, image_s, reply_to_message_id=update.message_id)
