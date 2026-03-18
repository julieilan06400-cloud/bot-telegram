from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    filters,
    ContextTypes,
)
import os

TOKEN = os.getenv("TOKEN")

keyboard = ReplyKeyboardMarkup(
    [
        ["Voir les offres", "Tarifs"],
        ["Commander", "Contact"],
    ],
    resize_keyboard=True
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Bienvenue chez Juliebot 💖\n\n"
        "Je propose des bisous virtuels, câlins symboliques et messages doux.\n"
        "Choisis une option dans le menu :",
        reply_markup=keyboard
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "Voir les offres":
        await update.message.reply_text(
            "Nos offres 💌\n\n"
            "1. Bisou virtuel 💋\n"
            "2. Câlin symbolique 🤗\n"
            "3. Message doux personnalisé 💖\n"
            "4. Pack tendresse 🌸"
        )

    elif text == "Tarifs":
        await update.message.reply_text(
            "Tarifs 💸\n\n"
            "Bisou virtuel : 5€\n"
            "Câlin symbolique : 8€\n"
            "Message doux personnalisé : 12€\n"
            "Pack tendresse : 20€"
        )

    elif text == "Commander":
        await update.message.reply_text(
            "Pour commander, envoie :\n\n"
            "Nom :\n"
            "Offre choisie :\n"
            "Pour qui :\n"
            "Message personnalisé :\n"
            "Contact :"
        )

    elif text == "Contact":
        await update.message.reply_text(
            "Contact service client 💬\n\n"
            "Réponds ici avec ta demande ou contacte :\n"
            "@tonpseudo_telegram"
        )

    else:
        await update.message.reply_text(
            "Merci 💕\n"
            "Utilise les boutons du menu :\n"
            "Voir les offres, Tarifs, Commander, Contact."
        )

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

app.run_polling()
