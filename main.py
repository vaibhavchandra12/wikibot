from pyrogram import Client
from config import Config
import os
import wikipedia as wiki
from pyrogram import filters
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup
)


# configs
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
LOG_CHANNEL = int(os.getenv("LOG_CHANNEL"))

# handler
botcmd = Client(
    'wikiBot',
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
)
botcmd.send_message({LOG_CHANNEL}, "Started")
print("Started")


#functions
def get_wiki(word):
    try:
        return wiki.summary(word)
    except:
        return "Not Found"
    
# working
@botcmd.on_message(filters.text & filters.private & ~filters.bot)
async def start(botcmd, message):
    msg= message.text.lower()
    user= umessage.from_user.first_name
    chatid= message.chat.id
    print("{}: {}".format(user, msg))
    if(msg.startswith('wiki')):
        botcmd.reply(
            text=get_wiki(msg[5:]),
            disable_web_page_preview=True
        )
        print("wikiBot: Wikipedia summery of {}".format(msg[5:]))
    else:
        bot.reply(
            text="Invalid Command Join @x3ninja for Support"
        )
        print("wikiBot: Invalid command")


botcmd.run()
