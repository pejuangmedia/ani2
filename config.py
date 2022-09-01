import os
from telethon import TelegramClient

api_id = '7120601' #os.environ.get('API_ID')
api_hash = 'aebd45c2c14b36c2c91dec3cf5e8ee9a'  #os.environ.get('API_HASH')
bot_token = '1920905087:AAE-3G2wZsjpuuSnWzQT8z_jbzwvQFAQ154' #os.environ.get('BOT_TOKEN')

bot = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)
