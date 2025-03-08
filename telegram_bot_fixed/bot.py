import os
import threading
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, CallbackContext

# Obtener el TOKEN del bot desde las variables de entorno
TOKEN = os.getenv("TOKEN")

# Función para mostrar el menú principal con /start
def start(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [InlineKeyboardButton("📌 Proceso de Admisión", callback_data="admision")],
        [InlineKeyboardButton("📚 Curso de Nivelación", callback_data="nivelacion")],
        [InlineKeyboardButton("🎓 Carreras que ofrece la Universidad", callback_data="carreras")],
        [InlineKeyboardButton("📞 Contactos", callback_data="contactos")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text(
        "Bienvenido al chatbot de la Unidad de Admisión y Registro de La Universidad de Las Fuerzas Armadas ESPE.\n\n"
        "Seleccione una opción:",
        reply_markup=reply_markup
    )

# Función para manejar las respuestas de los botones
def button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()

    if query.data == "admision":
        query.message.reply_text(
            "📌 Proceso de Admisión\n\n"
            "📅 Fechas de admisión: 18 de diciembre de 2024 hasta las 22h00 del 6 de enero de 2025.\n"
            "📝 Fechas de evaluación: 25 al 27 de enero de 2025."
        )

    elif query.data == "nivelacion":
        query.message.reply_text(
            "📚 Curso de Nivelación\n\n"
            "El curso de nivelación es obligatorio para todos los aspirantes que han aceptado un cupo en la Universidad."
        )

    elif query.data == "contactos":
        query.message.reply_text(
            "📍 Información de Contacto:\n"
            "📌 Dirección: Av. General Rumiñahui s/n y Ambato, Sangolquí – Ecuador\n"
            "📞 Teléfono: (593)23989-400 Ext 1401 – 1402\n"
            "📧 Correos:\n"
            "   ✉️ admisiones@espe.edu.ec\n"
            "   ✉️ asistencia.academica@espe.edu.ec"
        )

    elif query.data == "carreras":
        keyboard = [
            [InlineKeyboardButton("📍 Sangolquí - Matriz", callback_data="sangolqui")],
            [InlineKeyboardButton("📍 Sede Latacunga", callback_data="latacunga")],
            [InlineKeyboardButton("📍 Sede Santo Domingo", callback_data="santo_domingo")],
            [InlineKeyboardButton("💻 Modalidad en Línea", callback_data="en_linea")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        query.message.reply_text("🎓 Carreras que ofrece la Universidad. Seleccione una sede:", reply_markup=reply_markup)

    elif query.data == "sangolqui":
        query.message.reply_text(
            "📍 Sangolquí - Matriz\n\n"
            "🎓 Carreras Presenciales:\n"
            "- Administración de Empresas\n"
            "- Ingeniería Agropecuaria\n"
            "- Biotecnología\n"
            "- Comercio Exterior\n"
            "- Contabilidad y Auditoría\n"
            "- Educación Inicial\n"
            "- Electrónica y Automatización\n"
            "- Ingeniería Civil\n"
            "- Ingeniería Geoespacial\n"
            "- Mecánica\n"
            "- Mecatrónica\n"
            "- Medicina\n"
            "- Mercadotecnia\n"
            "- Pedagogía de la Actividad Física y del Deporte\n"
            "- Relaciones Internacionales\n"
            "- Software\n"
            "- Tecnologías de la Información\n"
            "- Telecomunicaciones\n"
            "- Turismo"
        )

    elif query.data == "latacunga":
        query.message.reply_text(
            "📍 Sede Latacunga\n\n"
            "🎓 Carreras Presenciales:\n"
            "- Contabilidad y Auditoría\n"
            "- Electromecánica\n"
            "- Electrónica y Automatización\n"
            "- Ingeniería Automotriz\n"
            "- Mecatrónica\n"
            "- Petroquímica\n"
            "- Software\n"
            "- Turismo\n"
            "- Tecnología Superior en Automatización e Instrumentación\n"
            "- Tecnología Superior en Electromecánica\n"
            "- Tecnología Superior en Logística y Transporte\n"
            "- Tecnología Superior en Mecánica Aeronáutica\n"
            "- Tecnología Superior en Mecánica Automotriz\n"
            "- Tecnología Superior en Redes y Telecomunicaciones\n"
            "- Tecnología Superior en Seguridad y Prevención de Riesgos Laborales"
        )

    elif query.data == "santo_domingo":
        query.message.reply_text(
            "📍 Sede Santo Domingo\n\n"
            "🎓 Carreras Presenciales:\n"
            "- Ingeniería Agropecuaria\n"
            "- Biotecnología\n"
            "- Tecnologías de la Información"
        )

    elif query.data == "en_linea":
        query.message.reply_text(
            "💻 Modalidad en Línea\n\n"
            "🎓 Carreras Disponibles:\n"
            "- Educación Inicial\n"
            "- Educación Básica\n"
            "- Turismo\n"
            "- Pedagogía de los Idiomas Nacionales y Extranjeros (Mención: Inglés)\n"
            "- Economía\n"
            "- Tecnologías de la Información"
        )

# Función para iniciar el bot en un hilo separado
def run_bot():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))

    print("✅ Bot iniciado en Railway sin asyncio... 🚀")
    app.run_polling()

if __name__ == "__main__":
    bot_thread = threading.Thread(target=run_bot)
    bot_thread.start()
