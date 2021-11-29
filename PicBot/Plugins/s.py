import os

import psutil

import time

from pyrogram import __version__, client

from pyrogram import Client, filters

from bot import SUPPORT_CHAT_LINK

from pyrogram import Client, filters

from bot.config import Messages as tr

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

assistant_version = "V1.0"

async def bot_sys_stats():

    version = assistant_version

    bot_uptime = int(time.time() - bot_start_time)

    cpu = psutil.cpu_percent()

    mem = psutil.virtual_memory().percent

    disk = psutil.disk_usage("/").percent

    process = psutil.Process(os.getpid())

    stats = f"""

Naveen_xD@Mr.Stark

--------------------------

✘ VERSION: {version}

✘ UPTIME: {get_readable_time((time.time() - bot_start_time))}

✘ BOT: {round(process.memory_info()[0] / 1024 ** 2)} MB

✘ CPU: {cpu}%

✘ RAM: {mem}%

✘ DISK: {disk}%

"""

    return stats

@Client.on_callback_query()

async def cb_handler(client, query):

    data = query.data

    if data == "about":

        await query.message.edit_text(

            text = f"<b>My name : <b/>Gdrive hexbot</i>\n<b>○ Creator : <a href='https://t.me/hexbots'>HEXBOTS</a>\n Language : <code>Python3</code>\n○ Library : <a href='https://docs.pyrogram.org/'>Pyrogram {__version__}</a></b>",

            disable_web_page_preview = True,

            reply_markup = InlineKeyboardMarkup(

                [

                    [

                        InlineKeyboardButton("🔙Back", callback_data = "back")

                    ]

                ]

            )

        )

    elif data == "back":

        firstname = query.from_user.first_name

        await query.message.edit_text(

            text=f"<i>Hello, {firstname} !\nNice To Meet You, Well I Am A Powerfull gdrive up bot For everyone!`\nMade with love by </i>HEXBOTS",

            reply_markup=keyboard,

          )

          

    elif data == "sys_info":

        text = await bot_sys_stats()

        await query.answer(text, show_alert=True)

@Client.on_message(filters.incoming & filters.command(['a']), group=2)

def _a(client, message):

    client.send_message(chat_id = message.chat.id,

        text = tr.START_MSG.format(message.from_user.mention),

        reply_to_message_id = message.message_id

    )

@Client.on_message(filters.incoming & filters.command(['help']), group=2)

def _help(client, message):

    client.send_message(chat_id = message.chat.id,

        text = tr.HELP_MSG[1],

        reply_markup = InlineKeyboardMarkup(map(1)),

        reply_to_message_id = message.message_id

    )

help_callback_filter = filters.create(lambda _, __, query: query.data.startswith('help+'))

@Client.on_callback_query(help_callback_filter)

def help_answer(c, callback_query):

    chat_id = callback_query.from_user.id

    message_id = callback_query.message.message_id

    msg = int(callback_query.data.split('+')[1])

    c.edit_message_text(chat_id = chat_id,    message_id = message_id,

        text = tr.HELP_MSG[msg],    reply_markup = InlineKeyboardMarkup(map(msg))

    )

def map(pos):

    if(pos==1):

        button = [

            [InlineKeyboardButton(text = '👉', callback_data = "help+2")]

        ]

    elif(pos==len(tr.HELP_MSG)-1):

        button = [

            [

             InlineKeyboardButton(text = 'Support Chat', url = SUPPORT_CHAT_LINK),

             InlineKeyboardButton(text = 'Feature Request', url = "https://t.me/hexbotsdg")

            ],

            [InlineKeyboardButton(text = '👈', callback_data = f"help+{pos-1}")]

        ]

    else:

        button = [

            [

                InlineKeyboardButton(text = '👈', callback_data = f"help+{pos-1}"),

                InlineKeyboardButton(text = '👉', callback_data = f"help+{pos+1}")

            ],

        ]

    return button

keyboard = InlineKeyboardMarkup(

                [

                    [

                        InlineKeyboardButton(

                            "😎 About me 😎",

                        callback_data="about"

                        ),

                        InlineKeyboardButton(

                          "🖥System stats 🖥",

                          callback_data="sys_info"

                          ),

                    ],

                    [

                         InlineKeyboardButton(

                            "✨Click Here!✨",

                            callback_data="sm"

                        )

                    ],

                ]

            )

@Client.on_message(filters.incoming & filters.command(['start']), group=2)

async def start(bot, message):

    firstname = message.from_user.first_name

    text=f"<i>Hello, {firstname} !\nNice To Meet You, Well I Am A Powerfull gdrive up bot For everyone!`\nMade with love by </i>HEXBOTs"

    stark="https://telegra.ph/file/6ce7d0ba05d3b6b340540.jpg"

    parse_mode="html"

    await bot.send_photo(

            message.chat.id,

            stark,

            text,

            reply_markup=keyboard,

        )
