from telegram.ext import Updater, CommandHandler, MessageHandler, Filters,CallbackQueryHandler,Dispatcher
from telegram import Update,Bot
from handler import start, get_image, callback_like
from flask import Flask, request
import os

# get token from environment variable
TOKEN = os.environ['TOKEN'] 

bot = Bot(token=TOKEN)

app = Flask(__name__)

@app.route('/', methods=['GET'])
def main():
    return 'OK'

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/webhook', methods=["POST", "GET"])
def hello():
    if request.method == 'GET':
        return 'hi from Python2022I'
    elif request.method == "POST":
        data = request.get_json(force = True)
        
        dispacher: Dispatcher = Dispatcher(bot, update_queue=None, workers=0)
        update:Update = Update.de_json(data, bot)
    
        #update 
                
        dispacher.add_handler(CallbackQueryHandler(callback_like))
        dispacher.add_handler(MessageHandler(Filters.photo,get_image))
        dispacher.add_handler(CommandHandler('start',start))


        
        dispacher.process_update(update)
        return 'ok'