# Telegram ID: @Honest_es if you need help!

from pyrogram import Client, filters
import sqlite3 as db

con = db.connect('mydb.db', isolation_level = None, check_same_thread = False)
c = con.cursor()
c.execute("CREATE TABLE IF NOT EXISTS list (userID PRIMARY KEY, fileID TEXT, messageID Integer, caption TEXT)")

api_id = 00000 # Edit This Line ( Get api_ip from my.telegram.org )
api_hash = 'aaaaaaaaaaaaaaaaaaaaaaaa' # Edit This Line ( Get api_hash from my.telegram.org )
Token = 'bbbbbbbbbbbbbbbbbbbbbbbbbbbbb' # Edit This Line ( Get token from @botfather )
app = Client('Session', api_id = api_id, api_hash = api_hash, bot_token = Token)

@app.on_message(filters.command(["start"]) & filters.private)
def start(client, message):
    text = "سلام به رباتمون خوش اومدی😃 فایلت کووو بفرست بیاد" # Start message, you can edit it.
    app.send_message(message.chat.id, text)

@app.on_message(filters.private)
def on_message(client, message):
    ChatID = message.chat.id
    if message.document:
        FileInfo = message.document
        FileID = FileInfo.file_id
        ChannelFileInfo = app.send_document('ChannelID', FileID) # Edit channel ID to your channel's username
        MessageID = ChannelFileInfo.message_id
        c.execute(f'DELETE FROM list WHERE userID = {ChatID}')
        c.execute('INSERT or IGNORE INTO list (userID, fileID, messageID, caption) VALUES (?, ?, ?, ?)', 
                  (ChatID, FileID, MessageID, None))
        app.send_message(ChatID, 'پیام خود را وارد کنید') # you can edit this message
    if message.text:
        c.execute(f"SELECT * FROM list WHERE userID = {ChatID}")
        Database = c.fetchall()
        if len(Database) > 0:
            FileUrl = f"<a href ='https://t.me/attachfilenotimportantfile/{Database[0][2]}'>&#160;</a>" # Edit channel iD to your channel's username
            caption = message.text + FileUrl
            app.send_message(Database[0][0], caption, disable_web_page_preview = False, parse_mode = 'HTML')
    

app.run()
