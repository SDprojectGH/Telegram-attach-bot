# Telegram ID: @Honest_es if you need help!
from pyrogram import Client, filters
import sqlite3 as db
from config import Config
import Start

con = db.connect('mydb.db', isolation_level = None, check_same_thread = False)
c = con.cursor()
c.execute("CREATE TABLE IF NOT EXISTS list (userID PRIMARY KEY, fileID TEXT, messageID Integer, caption TEXT)")

app = Client('Session', api_id = Config.API_ID, api_hash = Config.API_HASH, bot_token = Config.TG_BOT_TOKEN)


@app.on_message(filters.command(["start"]) & filters.private)
def start(client, message):
    app.send_message(message.chat.id, text = f'Hi [{message.from_user.first_name}](tg://user?id={message.from_user.id}) I am Attach Bot. I can attach medias(and Files) to your long text.',
                     parse_mode='Markdown')

@app.on_message(filters.private)
def on_message(client, message):
    ChatID = message.chat.id
    Valid = (0,0)
    number = 0
    if message.document:
        FileID = message.document.file_id
        number = 1
          
    elif message.animation:
        FileID = message.animation.file_id
        number = 2
        
    elif message.voice:
        FileID = message.voice.file_id
        number = 3
    
    elif message.video:
        FileID = message.video.file_id
        number = 4
        
    elif message.audio:
        FileID = message.audio.file_id
        number = 5
        
    if number != 0:
        Valid = Start.start(ChatID, number)

    if message.text:
        c.execute(f"SELECT * FROM list WHERE userID = {ChatID}")
        Database = c.fetchall()
        if len(Database) > 0:
            caption = message.text + f"<a href ='https://t.me/{Config.CHANNEL_USERNAME}/{Database[0][2]}'>&#160;</a>"
            app.send_message(Database[0][0], caption, disable_web_page_preview = False, parse_mode = 'HTML')

    if Valid[0] == 1:
        CHANNEL_ID = Config.CHANNEL_USERNAME
        app.send_message(ChatID, 'Send me your text.')
        MessageID = eval(Valid[1]).message_id
        c.execute('INSERT or IGNORE INTO list (userID, fileID, messageID, caption) VALUES (?, ?, ?, ?)', 
                (ChatID, FileID, MessageID, None))
        
    

app.run()
