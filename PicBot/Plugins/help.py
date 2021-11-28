from pyrogram import Client, filters

@Client.on_message(filters.command(["help"]))
async def help_menu(bot, update):
     text = f"**Hey theese are the available commands:**\n"
     text += f"➤ /start - To start Me:)\n"
     text += f"➤ /help - To get this message\n"
     text += f"➤ /dog - sends a random dog image\n"
     text += f"➤ /cat - sends a random cat image\n"
     text += f"➤ /panda - sends a random panda image\n"
     text += f"➤ /meme - sends a random meme"
     await bot.send_message(update.chat.id, text=text)
