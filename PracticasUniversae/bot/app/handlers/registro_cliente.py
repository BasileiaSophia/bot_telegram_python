import telebot
from ..servicios.flujo_registro import registrar_cliente

def setup(bot):
    @bot.message_handler(func=lambda message: message.text == 'Registrar')
    def registrar(message):
        registrar_cliente(bot, message)
       
