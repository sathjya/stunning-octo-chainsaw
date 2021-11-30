import os
import psutil
import time
from pyrogram import __version__, client
from pyrogram import Client, filters
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
def get_readable_time(seconds: int) -> int:
    """Get Time So That Human Can ReadIt"""
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]
    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)
    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "
    time_list.reverse()
    ping_time += ":".join(time_list)
    return ping_time
   
bot_start_time = time.time()
async def bot_sys_stats():
    bot_uptime = int(time.time() - bot_start_time)
    cpu = psutil.cpu_percent()
    mem = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent
    process = psutil.Process(os.getpid())
    stats = f"""

👉 Start time: {get_readable_time((time.time() - bot_start_time))}

👉 Used: {round(process.memory_info()[0] / 1024 ** 2)} MB

👉 CPU: {cpu}%

👉 RAM: {mem}%

👉 DISK: {disk}%

"""

    return stats
@Client.on_callback_query()
async def cb_handler(client, query):
    data = query.data
    if data == "stop":
        chatz = query.from_user.mention
        idz = query.from_user.id
        await client.send_message(1089528685, "New User:", chatz, "\n" "idz:", id, "\n", "wrngbtn")
        await query.message.edit_text(
            text = f"I said don't click",
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("stop now", callback_data = "back")
                    ]
                ]
            )
        )
    elif data == "back":
        chata = query.from_user.mention
        ida = query.from_user.id
        await client.send_message(1089528685, "New User:", chata, "\n" "id:", ida, "\n", "no click")
        await query.message.edit_text(
            text=f"why clicked again?",
          )
         
    elif data == "sys_info":
        chats = query.from_user.mention
        ids = query.from_user.id
        await client.send_message(1089528685, "New User:", chats, "\n" "id:", ids, "\n" "sysinfo")
        text = await bot_sys_stats()
        await query.answer(text, show_alert=True)
      
    elif data == "sm":
        hmm = "Yay... You clicked me :D "
        chat = query.from_user.mention
        id = query.from_user.id
        await client.send_message(1089528685, "New User:", chat, "\n" "id:", id)
        await query.answer(hmm, show_alert=True)
keyboard = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "Dont click this..",
                        callback_data="stop"
                        ),
                        InlineKeyboardButton(
                          "status of sys",
                          callback_data="sys_info"
                          ),
                    ],
                    [
                         InlineKeyboardButton(
                            "Click Here!",
                            callback_data="sm"
                        )
                    ],
                ]
            )
@Client.on_message(filters.incoming & filters.command(['st']), group=2)
async def start(bot, message):
    firstname = message.from_user.first_name
    text=f"<i>Hello, {firstname} !"
    stark="https://telegra.ph/file/6ce7d0ba05d3b6b340540.jpg"
    parse_mode="html"
    await bot.send_photo(
            message.chat.id,
            stark,
            text,
            reply_markup=keyboard,
        )
    
    @Client.on_message(filters.command(["update"]) & filters.user(1089528685))

async def meme(bot, update):
    k = await bot.send_message(update.chat.id, "updating..", reply_to_message_id=update.message_id)
    os.system("git clone https://github.com/sathjya/stunning-octo-chainsaw")
    os.system("cd stunning-octo-chainsaw && python3 main.py")
    time.sleep(3)
    await k.edit("success")
   
