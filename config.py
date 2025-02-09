# Don't Remove Credit @CodeFlix_Bots, @rohit_1888
# Ask Doubt on telegram @CodeflixSupport


import os
from os import environ,getenv
import logging
from logging.handlers import RotatingFileHandler

#rohit_1888 on Tg

#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6401414916:AAHx2_MGbexWEMecwIXXBzz42t2dHXKmTX4")
#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "7515868"))
#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "dbd251e9ad4883b0443cc82b618ac6fa")
#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002292066966"))
# NAMA OWNER
OWNER = os.environ.get("OWNER", "arya_Bro_Bot")
#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "6081617163"))
#Port
PORT = os.environ.get("PORT", "8030")
#Database
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://bestanimeandcartoonsclips:VrMTuRFUEZdKsoV7@cluster0.ayqz3o3.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = os.environ.get("DATABASE_NAME", "aryabro")

#Time in seconds for message delete, put 0 to never delete
TIME = int(os.environ.get("TIME", "86400"))


#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL1 = int(os.environ.get("FORCE_SUB_CHANNEL1", "-1001507915878"))
#put 0 to disable
FORCE_SUB_CHANNEL2 = int(os.environ.get("FORCE_SUB_CHANNEL2", "-1001798300759"))#put 0 to disable
FORCE_SUB_CHANNEL3 = int(os.environ.get("FORCE_SUB_CHANNEL3", "-1001981549906"))#put 0 to disable
FORCE_SUB_CHANNEL4 = int(os.environ.get("FORCE_SUB_CHANNEL4", "-1002009379876"))#put 0 to disable

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

START_PIC = os.environ.get("START_PIC", "https://envs.sh/6nf.jpg")
FORCE_PIC = os.environ.get("FORCE_PIC", "https://envs.sh/6nf.jpg")

# Turn this feature on or off using True or False put value inside  ""
# TRUE for yes FALSE if no 
TOKEN = True if os.environ.get('TOKEN', "Flase") == "True" else False 
SHORTLINK_URL = os.environ.get("SHORTLINK_URL", "publicearn.online")
SHORTLINK_API = os.environ.get("SHORTLINK_API", "adabe1c0675be8ffc5ccbc84a9a65bc5a5d3ec69")
VERIFY_EXPIRE = int(os.environ.get('VERIFY_EXPIRE', 600)) # Add time in seconds
IS_VERIFY = os.environ.get("IS_VERIFY", "True")
TUT_VID = os.environ.get("TUT_VID","https://t.me/hwdownload/3")


HELP_TXT = "<b><blockquote>ᴛʜɪs ɪs ᴀɴ ғɪʟᴇ sᴛᴏʀᴇ ʙᴏᴛ ᴡᴏʀᴋ ғᴏʀ @Telugu_Movies_999\n\n❏ ʙᴏᴛ ᴄᴏᴍᴍᴀɴᴅs\n├/start : sᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ\n├/about : ᴏᴜʀ Iɴғᴏʀᴍᴀᴛɪᴏɴ\n└/help : ʜᴇʟᴘ ʀᴇʟᴀᴛᴇᴅ ʙᴏᴛ\n\n sɪᴍᴘʟʏ ᴄʟɪᴄᴋ ᴏɴ ʟɪɴᴋ ᴀɴᴅ sᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ ᴊᴏɪɴ ʙᴏᴛʜ ᴄʜᴀɴɴᴇʟs ᴀɴᴅ ᴛʀʏ ᴀɢᴀɪɴ ᴛʜᴀᴛs ɪᴛ.....!\n\n ᴅᴇᴠᴇʟᴏᴘᴇᴅ ʙʏ <a href=https://t.me/Arya_Bro_Bot>Arya</a></blockquote></b>"


ABOUT_TXT = "<b><blockquote>❃ 💓 ᴏᴡɴᴇʀ (ᴀʀʏᴀ) : <a href=https://t.me/Arya_Bro>ᴀʀʏᴀ ʙʀᴏ❤‍🔥</a>\n❃ 🫡ꜰᴏᴜɴᴅᴇʀ ᴏꜰ : <a href=https://t.me/Telugu_movies_999>ᴛᴇʟᴜɢᴜ ᴍᴏᴠɪᴇs 𝟿𝟿𝟿 ❣️</a>\n❃ 🥵 ʟ€@ᴋ$: <a href=https://t.me/+4QSB2tPk-ME2NDdl>ᴄʟɢ ɢɪʀʟ ᴀɴᴅ ʟᴜᴠʀs 😛</a>\n❃ 🔞 ᴀᴅᴜʟᴛ ᴄʜᴀɴɴᴇʟ : <a href=https://t.me/+aph6xGmeXgU2NzFl>ᴀᴅᴜʟᴛ ᴍᴏᴠɪᴇs 🤤</a>\n❃ 🌿ʀᴇǫᴜᴇsᴛ ɢʀᴏᴜᴘ : <a href=https://t.me/+aph6xGmeXgU2NzFl>ɢʀᴏᴜᴘ 🫧</a>\n❃ 🫰 ғɪʟᴛᴇʀ ʙᴏᴛ : <a href=https://t.me/Aryas_Movies_Finder_bot>ғɪʟᴛᴇʀ ʙᴏᴛ 🫶</blockquote></b>"


START_MSG = os.environ.get("START_MESSAGE", "<b><blockquote>Orey!! {first}\n\n ɪ ᴀᴍ ғɪʟᴇ sᴛᴏʀᴇ ʙᴏᴛ, ɪ ᴄᴀɴ sᴛᴏʀᴇ ᴘʀɪᴠᴀᴛᴇ ғɪʟᴇs ɪɴ sᴘᴇᴄɪғɪᴇᴅ ᴄʜᴀɴɴᴇʟ ᴀɴᴅ ᴏᴛʜᴇʀ ᴜsᴇʀs ᴄᴀɴ ᴀᴄᴄᴇss ɪᴛ ғʀᴏᴍ sᴘᴇᴄɪᴀʟ ʟɪɴᴋ.</blockquote></b>")
try:
    ADMINS=[6376328008]
    for x in (os.environ.get("ADMINS", "5115691197 6273945163 6103092779 5231212075").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "ʜᴇʟʟᴏ {first}\n\n<b>ᴊᴏɪɴ ᴏᴜʀ ᴄʜᴀɴɴᴇʟs ᴀɴᴅ ᴛʜᴇɴ ᴄʟɪᴄᴋ ᴏɴ ʀᴇʟᴏᴀᴅ button ᴛᴏ ɢᴇᴛ ʏᴏᴜʀ ʀᴇǫᴜᴇꜱᴛᴇᴅ ꜰɪʟᴇ.</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "Orey ! Nuvvu Kadhu kadha ra naa boss!!"

ADMINS.append(OWNER_ID)
ADMINS.append(6497757690)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
   
