from telebot.types import ReplyKeyboardMarkup, KeyboardButton

def setup(bot):
    @bot.message_handler(commands=['start'])
    def bienvenida(message):
        botones = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=True)
        botones.add(
            KeyboardButton('Registrar'),
            KeyboardButton('Facturar')
        )
        bot.send_message(message.chat.id, "Bienvenido al bot de facturación. Pulsa registrar para el registro de un nuevo cliente o facturar para generar una nueva factura.", reply_markup=botones)