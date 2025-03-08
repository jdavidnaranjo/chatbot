import asyncio
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, CallbackContext
import os

# Obtener el TOKEN del bot desde las variables de entorno
TOKEN = os.getenv("TOKEN")

# Función para mostrar el menú principal con /start
async def start(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [InlineKeyboardButton("📌 Proceso de Admisión", callback_data="admision")],
        [InlineKeyboardButton("📚 Curso de Nivelación", callback_data="nivelacion")],
        [InlineKeyboardButton("🎓 Carreras que ofrece la Universidad", callback_data="carreras")],
        [InlineKeyboardButton("📞 Contactos", callback_data="contactos")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "Bienvenido al chatbot de la Unidad de Admisión y Registro de La Universidad de Las Fuerzas Armadas ESPE.\n\n"
        "Seleccione una opción:",
        reply_markup=reply_markup
    )

# Función para manejar las respuestas de los botones
async def button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    await query.answer()

    if query.data == "admision":
        await query.message.reply_text(
            "📌 Proceso de Admisión\n\n"
            "📅 Fechas de admisión: 18 de diciembre de 2024 hasta las 22h00 del 6 de enero de 2025.\n"
            "📝 Fechas de evaluación: 25 al 27 de enero de 2025."
        )

    elif query.data == "nivelacion":
        await query.message.reply_text(
            "📚 Curso de Nivelación\n\n"
            "El curso de nivelación es obligatorio para todos los aspirantes que han aceptado un cupo en la Universidad."
        )

    elif query.data == "contactos":
        await query.message.reply_text(
            "📍 Información de Contacto:\n"
            "📌 Dirección: Av. General Rumiñahui s/n y Ambato, Sangolquí – Ecuador\n"
            "📞 Teléfono: (593)23989-400 Ext 1401 – 1402\n"
            "📧 Correos:\n"
            "   ✉️ admisiones@espe.edu.ec\n"
            "   ✉️ asistencia.academica@espe.edu.ec"
        )

# Configuración del bot
async def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))

    print("✅ Bot iniciado en Railway... 🚀")
    await app.run_polling()

# Ejecutar el bot sin usar asyncio.run()
import asyncio

if __name__ == "__main__":
    import sys

    if sys.platform == "win32":
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    # Solución específica para Railway (Evita "event loop already running")
    from telegram.ext import Application

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    
    app = Application.builder().token(TOKEN).build()
    
    app.run_polling()
