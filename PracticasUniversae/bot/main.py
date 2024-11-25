import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import telebot
#from flask import Flask, request
from config import TOKEN # AÑADIR WEBHOOK_URL
from app.handlers import inicio # facturación, registro

bot = telebot.TeleBot(TOKEN)
#app = Flask(__name__)

inicio.setup(bot)
#facturar.setup(bot)
#registrar.setup(bot)    

#@app.route('/' + TOKEN, methods=['POST'])
#def getMessage():
    #json_str = request.get_data().decode('UTF-8')
    #update = telebot.types.Update.de_json(json_str)
    #bot.process_new_updates([update])
    #return "!", 200

#@app.route('/')
#def webhook():
    #bot.remove_webhook()
    #bot.set_webhook(url=WEBHOOK_URL + TOKEN)
    #return "Webhook set", 200

bot.polling(none_stop=True)