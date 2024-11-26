import telebot
#from ..servicios.verificación import verificar_cliente

def setup(bot):
    @bot.message_handler(func=lambda message: message.text == 'Facturar')
    def facturar(message):
        #verificar_cliente(bot, message)
        bot.send_message(message.chat.id, "Por favor, envíe los detalles de la factura en el orden indicado.")

