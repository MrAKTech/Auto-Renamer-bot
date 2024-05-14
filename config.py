import re, os, time
id_pattern = re.compile(r'^.\d+$') 

class Config(object):
    # pyro client config
    API_ID    = os.environ.get("API_ID", "")
    API_HASH  = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "") 

    # database config
    DB_NAME = os.environ.get("DB_NAME","")     
    DB_URL  = os.environ.get("DB_URL","")
 
    # other configs
    BOT_UPTIME  = time.time()
    START_PIC   = os.environ.get("START_PIC", "https://graph.org/file/4b306f4b15c23a8f22e58.jpg")
    ADMIN       = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '').split()]
    FORCE_SUB   = os.environ.get("FORCE_SUB", "") 
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", ""))
    
    # wes response configuration     
    WEBHOOK = bool(os.environ.get("WEBHOOK", "True"))


class Txt(object):
    # part of text configuration
        
    START_TXT = """Hello {} 
    
➻ This Is An Advanced And Yet Powerful Rename Bot.
    
➻ Using This Bot You Can Auto Rename Of Your Files.
    
➻ This Bot Also Supports Custom Thumbnail And Custom Caption.
    
➻ Use /tutorial Command To Know How To Use Me.
    
<b>Bot Is Made By @Madflix_Bots</b>"""
    
    FILE_NAME_TXT = """<b><u>SETUP AUTO RENAME FORMAT</u></b>

Use These Keywords To Setup Custom File Name

✓ episode :- To Replace Episode Number
✓ quality :- To Replace Video Resolution

<b>➻ Example :</b> <code> /autorename [S1-Eepisode] [quality] Naruto Shippuden [@Anime_Infinitrly] </code>

<b>➻ Your Current Auto Rename Format :</b> <code>{format_template}</code> """
    
    ABOUT_TXT = f"""<b>😊 ᴍʏ ɴᴀᴍᴇ :</b> <a href='https://t.me/Auto_Renamer_XBot'>Auto Renamer Bot ⚡</a>
<b>๏ ʟᴀɴɢᴜᴀɢᴇ :</b> <a href='https://python.org'>Python 3</a>
<b>๏ ʟɪʙʀᴀʀʏ :</b> <a href='https://pyrogram.org'>Pyrogram 2.0</a>
<b>๏ sᴇʀᴠᴇʀ :</b> <a href='https://heroku.com'>Heroku</a>
<b>๏ ᴄʜᴀɴɴᴇʟ :</b> <a href='https://t.me/Madflix_Bots'>Madflix Botz</a>
<b>๏ ᴅᴇᴠᴇʟᴏᴘᴇʀ :</b> <a href='https://t.me/CallAdminRobot'>Jishu Developer</a>
    
<b>♻️ Bot Made By :</b> @ZPro_Bots"""

    
    THUMBNAIL_TXT = """<b><u>🖼️  HOW TO SET THUMBNAIL</u></b>
    
⦿ You Can Add Custom Thumbnail Simply By Sending A Photo To Me....
    
⦿ /viewthumb - Use This Command To See Your Thumbnail
⦿ /delthumb - Use This Command To Delete Your Thumbnail"""

    CAPTION_TXT = """<b><u>📝  HOW TO SET CAPTION</u></b>
    
⦿ /set_caption - Use This Command To Set Your Caption
⦿ /see_caption - Use This Command To See Your Caption
⦿ /del_caption - Use This Command To Delete Your Caption"""

    PROGRESS_BAR = """\n
<b>๏ sɪᴢᴇ</b> : {1} | {2}
<b>๏ ᴅᴏɴᴇ</b> : {0}%
<b>๏ sᴘᴇᴇᴅ</b> : {3}/s
<b>๏ ᴇᴛᴀ</b> : {4} """
    
    
    DONATE_TXT = """<b>🥲 Thanks For Showing Interest In Donation! ❤️</b>
    
If You Like My Bots & Projects, You Can 🎁 Donate Me Any Amount From 20 Rs Upto Your Choice.
    
<b>🛍 UPI ID:</b> <code>anime-legend@axl</code> """
    
    HELP_TXT = """<b>Hey</b> {}
    
Here Is The Help For My Commands."""





# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @Madflix_Bots
# Developer @JishuDeveloper

