#!/usr/bin/env python3
# Copyright (C) @subinps
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

from utils import LOGGER
try:
   import os
   from dotenv import load_dotenv
   from ast import literal_eval as is_enabled

except ModuleNotFoundError:
    import os
    import sys
    import subprocess
    file=os.path.abspath("requirements.txt")
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', file, '--upgrade'])
    os.execl(sys.executable, sys.executable, *sys.argv)


class Config:
    # Telegram API Stuffs
    load_dotenv()  # load environment variables from .env file
    ADMIN = os.environ.get("ADMINS", '')
    SUDO = [int(admin) for admin in (ADMIN).split()] 
    ADMINS = [int(admin) for admin in (ADMIN).split()] 
    
    # ─── ʏᴏᴜʀ ᴄᴜꜱᴛᴏᴍ ᴄʀᴇᴅᴇɴᴛɪᴀʟꜱ (ꜰᴏʀ ʀᴇɴᴅᴇʀ) ───
    API_ID = int(os.environ.get("API_ID", '38138069'))
    API_HASH = os.environ.get("API_HASH", "2ed313ebcc45cbcf65d1fc736ec71681")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "8970725347:AAFYEfmwyK54z7ipcUB-Yb2ET-4VJSo3Np8")     
    SESSION = os.environ.get("SESSION_STRING", "AQJF8NUAX8lJdoAM_A_O5C6pUrAxevv2PqwBOKpt9IhpfWFKknA2aBZoxvxil5bEX-vlK8JZPGNxmsqFPGv7RY2SQd1OC2XvAGXsYmJVaCeTONHL3tYbaJ-o_d73jUz0K61BKo2XbiXKo8rv_LMmTWUtEA7EQGmdvmTf-VrtpYhIJ1I-PXMcryarCSgExZKrw-PJVP-krIDBmBox024RXzWVxj0ocvrMXLgmvZZ5cP-ZSMinBMWrWCWGOQZ7wmK7DA-ltHDJ2PwgWKp7L3vunmDQ7LiV-59n3ShZmBLvbZuD6PSbIfcVhBB1jcUV24OL16JRpu4gPq0q6WroSiRSWo6RP6IvzgAAAAH_hA2LAA")

    # Stream Chat and Log Group
    CHAT = int(os.environ.get("CHAT", "-1003947649552")) 
    LOG_GROUP = os.environ.get("LOG_GROUP", "-1003947649552")

    # Stream 
    STREAM_URL = os.environ.get("STARTUP_STREAM", "https://www.youtube.com/watch?v=zcrUCvBD16k")
   
    # Database (MongoDB)
    DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://misssqn_db_user:Nova01@cluster0.6xxsrwq.mongodb.net/?retryWrites=true&w=majority")
    DATABASE_NAME = os.environ.get("DATABASE_NAME", "VCPlayerBot")

    # ─── ʀᴇɴᴅᴇʀ 24/7 ᴘɪɴɢ ꜱᴇᴛᴛɪɴɢꜱ (ʜᴇʀᴏᴋᴜ ʀᴇᴍᴏᴠᴇᴅ) ───
    PORT = int(os.environ.get("PORT", "8080")) # This web port keeps Render alive via Cron-jobs
    HEROKU_APP = None  # Disabled for Render

    # Optional Configuration
    SHUFFLE = is_enabled(os.environ.get("SHUFFLE", 'True'))
    ADMIN_ONLY = is_enabled(os.environ.get("ADMIN_ONLY", "False"))
    REPLY_MESSAGE = os.environ.get("REPLY_MESSAGE", False)
    EDIT_TITLE = os.environ.get("EDIT_TITLE", True)
    
    RECORDING_DUMP = os.environ.get("RECORDING_DUMP", False)
    RECORDING_TITLE = os.environ.get("RECORDING_TITLE", False)
    TIME_ZONE = os.environ.get("TIME_ZONE", "Asia/Kolkata")    
    IS_VIDEO = is_enabled(os.environ.get("IS_VIDEO", 'True'))
    IS_LOOP = is_enabled(os.environ.get("IS_LOOP", 'True'))
    DELAY = int(os.environ.get("DELAY", '10'))
    PORTRAIT = is_enabled(os.environ.get("PORTRAIT", 'False'))
    IS_VIDEO_RECORD = is_enabled(os.environ.get("IS_VIDEO_RECORD", 'True'))
    DEBUG = is_enabled(os.environ.get("DEBUG", 'False'))
    PTN = is_enabled(os.environ.get("PTN", "False"))

    # Quality vars
    E_BITRATE = os.environ.get("BITRATE", False)
    E_FPS = os.environ.get("FPS", False)
    CUSTOM_QUALITY = os.environ.get("QUALITY", "100")

    # Search filters for cplay
    FILTERS = [filter.lower() for filter in (os.environ.get("FILTERS", "video document")).split(" ")]

    # Player core vars
    GET_FILE = {}
    DATA = {}
    STREAM_END = {}
    SCHEDULED_STREAM = {}
    DUR = {}
    msg = {}

    SCHEDULE_LIST = []
    playlist = []
    CONFIG_LIST = ["ADMINS", "IS_VIDEO", "IS_LOOP", "REPLY_PM", "ADMIN_ONLY", "SHUFFLE", "EDIT_TITLE", "CHAT", 
    "SUDO", "REPLY_MESSAGE", "STREAM_URL", "DELAY", "LOG_GROUP", "SCHEDULED_STREAM", "SCHEDULE_LIST", 
    "IS_VIDEO_RECORD", "IS_RECORDING", "WAS_RECORDING", "RECORDING_TITLE", "PORTRAIT", "RECORDING_DUMP", "HAS_SCHEDULE", 
    "CUSTOM_QUALITY"]

    STARTUP_ERROR = None
    ADMIN_CACHE = False
    CALL_STATUS = False
    YPLAY = False
    YSTREAM = False
    CPLAY = False
    STREAM_SETUP = False
    LISTEN = False
    STREAM_LINK = False
    IS_RECORDING = False
    WAS_RECORDING = False
    PAUSE = False
    MUTED = False
    HAS_SCHEDULE = None
    IS_ACTIVE = None
    VOLUME = 100
    CURRENT_CALL = None
    BOT_USERNAME = None
    USER_ID = None

    if LOG_GROUP:
        LOG_GROUP = int(LOG_GROUP)
    else:
        LOG_GROUP = None

    if EDIT_TITLE in ["NO", 'False']:
        EDIT_TITLE = False
        LOGGER.info("Title Editing turned off")
    if REPLY_MESSAGE:
        REPLY_MESSAGE = REPLY_MESSAGE
        REPLY_PM = True
        LOGGER.info("Reply Message Found, Enabled PM MSG")
    else:
        REPLY_MESSAGE = False
        REPLY_PM = False

    if E_BITRATE:
       try:
          BITRATE = int(E_BITRATE)
       except:
          LOGGER.error("Invalid bitrate specified.")
          E_BITRATE = False
          BITRATE = 48000
       if not BITRATE >= 48000:
          BITRATE = 48000
    else:
       BITRATE = 48000
    
    if E_FPS:
       try:
          FPS = int(E_FPS)
       except:
          LOGGER.error("Invalid FPS specified")
          E_FPS = False
       if not FPS >= 30:
          FPS = 30
    else:
       FPS = 30
    try:
       CUSTOM_QUALITY = int(CUSTOM_QUALITY)
       if CUSTOM_QUALITY > 100:
          CUSTOM_QUALITY = 100
          LOGGER.warning("maximum quality allowed is 100, invalid quality specified. Quality set to 100")
       elif CUSTOM_QUALITY < 10:
          LOGGER.warning("Minimum Quality allowed is 10., Qulaity set to 10")
          CUSTOM_QUALITY = 10
       if 66.9 < CUSTOM_QUALITY < 100:
          if not E_BITRATE:
             BITRATE = 48000
       elif 50 < CUSTOM_QUALITY < 66.9:
          if not E_BITRATE:
             BITRATE = 36000
       else:
          if not E_BITRATE:
             BITRATE = 24000
    except:
       if CUSTOM_QUALITY.lower() == 'high':
          CUSTOM_QUALITY = 100
       elif CUSTOM_QUALITY.lower() == 'medium':
          CUSTOM_QUALITY = 66.9
       elif CUSTOM_QUALITY.lower() == 'low':
          CUSTOM_QUALITY = 50
       else:
          LOGGER.warning("Invalid QUALITY specified.Defaulting to High.")
          CUSTOM_QUALITY = 100


    # ─── ꜱᴛʏʟɪꜱʜ ꜱᴍᴀʟʟ ᴄᴀᴘs ʜᴇʟᴘ ꜱᴛʀɪɴɢꜱ ───
    
    PLAY_HELP = """
ʜᴇʟʟᴏ 👋 ɪ'ᴍ ᴀ ᴘᴏᴡᴇʀꜰᴜʟ ᴠᴄ ᴍᴜꜱɪᴄ ʙᴏᴛ!
ꜱᴛᴀʀᴛ ɪᴍɢ: https://files.catbox.moe/5tpjcq.jpg

__ʏᴏᴜ ᴄᴀɴ ᴘʟᴀʏ ᴜꜱɪɴɢ ᴀɴʏ ᴏꜰ ᴛʜᴇꜱᴇ ᴏᴘᴛɪᴏɴꜱ__

1. ᴘʟᴀʏ ᴀ ᴠɪᴅᴇᴏ ꜰʀᴏᴍ ᴀ ʏᴏᴜᴛᴜʙᴇ ʟɪɴᴋ.
ᴄᴏᴍᴍᴀɴᴅ: **/play**
__ʏᴏᴜ ᴄᴀɴ ᴜꜱᴇ ᴛʜɪꜱ ᴀꜱ ᴀ ʀᴇᴘʟʏ ᴛᴏ ᴀ ʏᴏᴜᴛᴜʙᴇ ʟɪɴᴋ ᴏʀ ᴘᴀꜱꜱ ʟɪɴᴋ ᴀʟᴏɴɢ ᴄᴏᴍᴍᴀɴᴅ.__

2. ᴘʟᴀʏ ꜰʀᴏᴍ ᴀ ᴛᴇʟᴇɢʀᴀᴍ ꜰɪʟᴇ.
ᴄᴏᴍᴍᴀɴᴅ: **/play**
__ʀᴇᴘʟʏ ᴛᴏ ᴀ ꜱᴜᴘᴘᴏʀᴛᴇ ᴍᴇᴅɪᴀ (ᴠɪᴅᴇᴏ/ᴀᴜᴅɪᴏ ꜰɪʟᴇ).__

3. ᴘʟᴀʏ ꜰʀᴏᴍ ᴀ ʏᴏᴜᴛᴜʙᴇ ᴘʟᴀʏʟɪꜱᴛ
ᴄᴏᴍᴍᴀɴᴅ: **/yplay**

4. ʟɪᴠᴇ ꜱᴛʀᴇᴀᴍ
ᴄᴏᴍᴍᴀɴᴅ: **/stream**
__ᴘᴀꜱꜱ ᴀ ʟɪᴠᴇ ꜱᴛʀᴇᴀᴍ ᴜʀʟ ᴛᴏ ᴘʟᴀʏ ɪᴛ.__

5. ᴄʜᴀɴɴᴇʟ ᴘʟᴀʏ
ᴄᴏᴍᴍᴀɴᴅ: **/cplay**
__ᴜꜱᴇ `/cplay @username` ᴛᴏ ᴘʟᴀʏ ᴀʟʟ ꜰɪʟᴇꜱ ꜰʀᴏᴍ ᴀ ᴄʜᴀɴɴᴇʟ.__

🎵 **ʙᴏᴛ:** @Doremoan_music_bot
📢 **ᴜᴘᴅᴀᴛᴇ:** [ɢᴇɴᴜ ʙᴏᴛ ꜱᴜᴘᴘᴏʀᴛ](https://t.me/Genu_Bot_Support)
"""

    SETTINGS_HELP = """
**ʏᴏᴜ ᴄᴀɴ ᴇᴀꜱɪʟʏ ᴄᴜꜱᴛᴏᴍɪᴢᴇ ʏᴏᴜʀ ᴘʟᴀʏᴇʀ:**

🔹ᴄᴏᴍᴍᴀɴᴅ: **/settings**

🔹ᴀᴠᴀɪʟᴀʙʟᴇ ᴄᴏɴꜰɪɢᴜʀᴀᴛɪᴏɴꜱ:
**ᴘʟᴀʏᴇʀ ᴍᴏᴅᴇ** - __ʀᴜɴ ᴘʟᴀʏᴇʀ 24/7 ᴏʀ ᴏɴʟʏ ᴡʜᴇɴ Qᴜᴇᴜᴇ ɪꜱ ꜰᴜʟʟ.__
**ᴠɪᴅᴇᴏ ᴇɴᴀʙʟᴇᴅ** - __ꜱᴡɪᴛᴄʜ ʙᴇᴛᴡᴇᴇɴ ᴀᴜᴅɪᴏ ᴀɴᴅ ᴠɪᴅᴇᴏ ᴍᴏᴅᴇ.__
**ᴀᴅᴍɪɴ ᴏɴʟʏ** - __ʀᴇꜱᴛʀɪᴄᴛ ɴᴏɴ-ᴀᴅᴍɪɴ ᴜꜱᴇʀꜱ ꜰʀᴏᴍ ᴜꜱɪɴɢ ᴘʟᴀʏ.__
**ᴇᴅɪᴛ ᴛɪᴛʟᴇ** - __ᴇᴅɪᴛ ᴠɪᴅᴇᴏᴄʜᴀᴛ ᴛɪᴛʟᴇ ᴛᴏ ᴄᴜʀʀᴇɴᴛ ꜱᴏɴɢ ɴᴀᴍᴇ.__
"""

    SCHEDULER_HELP = """
__ᴍᴜꜱɪᴄ ʙᴏᴛ ᴀʟʟᴏᴡꜱ ʏᴏᴜ ᴛᴏ ꜱᴄʜᴇᴅᴜʟᴇ ᴀ ꜱᴛʀᴇᴀᴍ ꜰᴏʀ ꜰᴜᴛᴜʀᴇ.__

ᴄᴏᴍᴍᴀɴᴅ: **/schedule**
__ʀᴇᴘʟʏ ᴛᴏ ᴀ ꜰɪʟᴇ/ʏᴏᴜᴛᴜʙᴇ ᴠɪᴅᴇᴏ ᴡɪᴛʜ ꜱᴄʜᴇᴅᴜʟᴇ ᴛɪᴍᴇ.__

ᴄᴏᴍᴍᴀɴᴅ: **/slist**
__ᴠɪᴇᴡ ʏᴏᴜʀ ᴄᴜʀʀᴇɴᴛ ꜱᴄʜᴇᴅᴜʟᴇᴅ ꜱᴛʀᴇᴀᴍꜱ.__

ᴄᴏᴍᴍᴀɴᴅ: **/cancel**
__ᴄᴀɴᴄᴇʟ ᴀ ꜱᴄʜᴇᴅᴜʟᴇ ʙʏ ɪᴛꜱ ɪᴅ.__
"""

    RECORDER_HELP = """
__ᴇᴀꜱɪʟʏ ʀᴇᴄᴏʀᴅ ᴀʟʟ ʏᴏᴜʀ ᴠɪᴅᴇᴏ ᴄʜᴀᴛꜱ ᴜꜱɪɴɢ ᴛʜᴇꜱᴇ ᴄᴏᴍᴍᴀɴᴅꜱ.__

ᴄᴏᴍᴍᴀɴᴅ: **/record**

1. **ʀᴇᴄᴏʀᴅ ᴠɪᴅᴇᴏ:** __ᴇɴᴀʙʟᴇ/ᴅɪꜱᴀʙʟᴇ ᴠɪᴅᴇᴏ ʀᴇᴄᴏʀᴅɪɴɢ.__
2. **ᴠɪᴅᴇᴏ ᴅɪᴍᴇɴꜱɪᴏɴ:** __ᴄʜᴏᴏꜱᴇ ᴘᴏʀᴛʀᴀɪᴛ ᴏʀ ʟᴀɴꜱᴄᴀᴘᴇ.__
3. **ᴄᴜꜱᴛᴏᴍ ᴛɪᴛʟᴇ:** __ᴜꜱᴇ `/rtitle [ᴛɪᴛʟᴇ]` ᴛᴏ ꜱᴇᴛ ʀᴇᴄᴏʀᴅɪɴɢ ɴᴀᴍᴇ.__
"""

    CONTROL_HELP = """
__ᴍᴀɴᴀɢᴇ ʏᴏᴜʀ ʟɪᴠᴇ ꜱᴛʀᴇᴀᴍꜱ ᴇᴀꜱɪʟʏ:__

• **/skip** - __ꜱᴋɪᴘ ᴄᴜʀʀᴇɴᴛ ꜱᴏɴɢ__
• **/pause** - __ᴘᴀᴜꜱᴇ ᴛʜᴇ ꜱᴛʀᴇᴀᴍ__
• **/resume** - __ʀᴇꜱᴜᴍᴇ ᴛʜᴇ ꜱᴛʀᴇᴀᴍ__
• **/volume** - __ᴄʜᴀɴɢᴇ ᴠᴏʟᴜᴍᴇ (1-200)__
• **/leave** - __ʟᴇᴀᴠᴇ ᴛʜᴇ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ__
• **/clearplaylist** - __ᴄʜᴀɴɢᴇ ᴀʟʟ Qᴜᴇᴜᴇꜱ__
• **/vcmute** - __ᴍᴜᴛᴇ ᴛʜᴇ ᴘʟᴀʏᴇʀ__
• **/vcunmute** - __ᴜɴᴍᴜᴛᴇ ᴛʜᴇ ᴘʟᴀʏᴇʀ__
"""

    ADMIN_HELP = """
__ᴍᴀɴᴀɢᴇ ʙᴏᴛ ᴀᴅᴍɪɴꜱ ᴇᴀꜱɪʟʏ:__

ᴄᴏᴍᴍᴀɴᴅ: **/vcpromote**
__ᴘʀᴏᴍᴏᴛᴇ ᴀ ᴜꜱᴇʀ ᴛᴏ ʙᴏᴛ ᴀᴅᴍɪɴ ʟɪꜱᴛ.__

ᴄᴏᴍᴍᴀɴᴅ: **/vcdemote**
__ʀᴇᴍᴏᴠᴇ ᴀ ᴜꜱᴇʀ ꜰʀᴏᴍ ᴀᴅᴍɪɴ ʟɪꜱᴛ.__

ᴄᴏᴍᴍᴀɴᴅ: **/refresh**
__ʀᴇꜰʀᴇꜱʜ ᴀᴅᴍɪɴ ᴄᴀᴄʜᴇ ᴏꜰ ᴄʜᴀᴛ.__
"""

    MISC_HELP = """
ᴄᴏᴍᴍᴀɴᴅ: **/export**
__ᴇxᴘᴏʀᴛ ᴄᴜʀʀᴇɴᴛ ᴘʟᴀʏʟɪꜱᴛ ᴀꜱ ᴊꜱᴏɴ.__

ᴄᴏᴍᴍᴀɴᴅ: **/logs**
__ɢᴇᴛ ʟɪᴠᴇ ᴇʀʀᴏʀ ʟᴏɢꜱ ᴏꜰ ᴛʜᴇ ʙᴏᴛ.__

ᴄᴏᴍᴍᴀɴᴅ: **/env** / **/config**
__ᴄᴏɴꜰɪɢᴜʀᴇ ᴠᴀʀꜱ ᴅɪʀᴇᴄᴛʟʏ ꜰʀᴏᴍ ᴄʜᴀᴛ.__
"""

    ENV_HELP = """
**ᴀᴠᴀɪʟᴀʙʟᴇ ᴇɴᴠ ᴠᴀʀꜱ ꜰᴏʀ ᴄᴏɴꜰɪɢᴜʀᴀᴛɪᴏɴ:**

1. `API_ID` / `API_HASH` - __ʏᴏᴜʀ ᴛᴇʟᴇɢʀᴀᴍ ᴄʀᴇᴅᴇɴᴛɪᴀʟꜱ.__
2. `BOT_TOKEN` - __ᴛᴏᴋᴇɴ ꜰʀᴏᴍ ʙᴏᴛꜰᴀᴛʜᴇʀ.__
3. `SESSION_STRING` - __ʏᴏᴜʀ ᴀꜱꜱɪꜱᴛᴀɴᴛ ꜱᴛʀɪɴɢ ꜱᴇꜱꜱɪᴏɴ.__
4. `CHAT` - __ɢʀᴏᴜᴘ/ᴄʜᴀɴɴᴇʟ ɪᴅ ᴡʜᴇʀᴇ ʙᴏᴛ ᴘʟᴀʏꜱ.__
5. `DATABASE_URI` - __ᴍᴏɴɢᴏᴅʙ ᴄᴏɴɴᴇᴄᴛɪᴏɴ ꜱᴛʀɪɴɢ.__
6. `LOG_GROUP` - __ʟᴏɢ ɢʀᴏᴜᴘ ɪᴅ ꜰᴏʀ ʙᴏᴛ ᴀᴄᴛɪᴠɪᴛʏ.__
"""
