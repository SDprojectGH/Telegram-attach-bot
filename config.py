import os

class Config(object):
  TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")
  CHANNEL_USERNAME = os.environ.get("CHANNEL_USERNAME", "")
  #CHANNEL_ID = int(os.environ.get("CHANNEL_ID", 12345))
  #CHANNEL_USERNAME without '@'
  
  API_ID = int(os.environ.get("API_ID", ""))
  API_HASH = os.environ.get("API_HASH", "")
  # Give it from my.telegram.org
