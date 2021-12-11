from pyrogram import Client
import os
import wikipedia as wiki
from pyrogram import filters
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup
)


# configs
API_ID = int("3172113")
API_HASH = "0a858f5c94f7030ee71e7f65f6d1b965"
BOT_TOKEN = "2125872006:AAF2AWyM6FeZkCTN1o_fIbXqQlJ78gXHWQM"
LOG_CHANNEL = int("-1001551828970")

# handler
botcmd = Client(
    'wikiBot',
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
)
botcmd.run()
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



