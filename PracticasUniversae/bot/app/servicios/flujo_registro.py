#from app.utils.creacion_json import crear_json
#from app.servicios.flujo_facturacion import iniciar_facturacion

usuario_data = {}
#chat_id puede ser global pero parece que puede dar problemas de concurrencia (preguntar)

def registrar_cliente(bot, message):
        bot.send_message(message.chat.id, "Por favor, envíe los detalles del cliente en el orden indicado.")
        guardar_nombre(bot, message)

def guardar_nombre(bot, message):
        bot.send_message(message.chat.id, "NOMBRE COMPLETO")
        chat_id = message.chat.id 
        usuario_data[chat_id] = {"nombre": message.text}
        bot.register_next_step_handler(message, lambda message:guardar_direccion(bot, message))

def guardar_direccion(bot, message):
        bot.send_message(message.chat.id, "DIRECCIÓN")
        chat_id = message.chat.id
        usuario_data[chat_id]["direccion"] = message.text
        bot.register_next_step_handler(message, lambda message:guardar_telefono(bot, message))

def guardar_telefono(bot, message):
        bot.send_message(message.chat.id, "TELÉFONO")
        chat_id = message.chat.id
        usuario_data[chat_id]["telefono"] = message.text
        bot.register_next_step_handler(message, lambda message:guardar_doc_identidad(bot, message))

def guardar_doc_identidad(bot, message):
        bot.send_message(message.chat.id, "DNI/NIE/CIF")
        chat_id = message.chat.id
        usuario_data[chat_id]["doc_identidad"] = message.text
        bot.register_next_step_handler(message, lambda message:guardar_email(bot, message))

def guardar_email(bot, message):
        bot.send_message(message.chat.id, "CORREO ELECTRÓNICO")
        chat_id = message.chat.id
        usuario_data[chat_id]["email"] = message.text
        bot.register_next_step_handler(message, lambda message:guardar_fecha(bot, message))

def guardar_fecha(bot, message):
        bot.send_message(message.chat.id, "FECHA DE REGISTRO (dd/mm/aaaa)")
        chat_id = message.chat.id
        usuario_data[chat_id]["fecha_registro"] = message.text
        bot.register_next_step_handler(message, lambda message:guardar_cliente(bot, message))

def guardar_cliente(bot, message):
        chat_id = message.chat.id
        #datos_cliente = usuario_data[chat_id]
        #crear_json(nombre_json, datos_cliente)
        bot.send_message(message.chat.id, "Cliente registrado con éxito.")
        del usuario_data[chat_id]

#dar opcion a salir, registrar otro cliente o facturar??
