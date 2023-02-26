import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters,CallbackContext,CallbackQueryHandler
from telegram import Update
from handler import start, get_image, callback_like
import logging

import os

# get token from environment variable
TOKEN = os.environ['TOKEN'] 

# Updater 
updater = Updater(token=TOKEN)

# Dispatcher
dp = updater.dispatcher



dp.add_handler(CommandHandler('start', start))
dp.add_handler(MessageHandler(Filters.photo, get_image))
dp.add_handler(CallbackQueryHandler(callback_like))
updater.start_polling()
updater.idle()

