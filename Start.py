import sqlite3 as db
from config import Config
con = db.connect('mydb.db', isolation_level = None, check_same_thread = False)
c = con.cursor()
c.execute("CREATE TABLE IF NOT EXISTS list (userID PRIMARY KEY, fileID TEXT, messageID Integer, caption TEXT)")

def start(CHATID, num):
    if num == 1:
        ChannelFileInfo = 'app.send_document(CHANNEL_ID, FileID)'
    elif num == 2:
        ChannelFileInfo = 'app.send_animation(CHANNEL_ID, FileID)'
    elif num == 3:
        ChannelFileInfo = 'app.send_voice(CHANNEL_ID, FileID)'
    elif num == 4:
        ChannelFileInfo = 'app.send_video(CHANNEL_ID, FileID)'
    elif num == 5:
        ChannelFileInfo = 'app.send_audio(CHANNEL_ID, FileID)'
    c.execute(f'DELETE FROM list WHERE userID = {CHATID}')

    Valid = 1
    return Valid , ChannelFileInfo
