from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(filters.command(["start"]))
async def start(bot, update):
    text=f"__Hello!__\nI'm Picturebot\nCheck /help to get available commands"
    mypic="https://telegra.ph//file/894df85d26b8b72f0745b.jpg"
    await bot.send_photo(
            update.chat.id,
            mypic,
            text,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("Dev", url="t.me/Sniper_xd")]]
            ),
        )
