from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
import os

PORT = int(os.environ.get("PORT", 8443))


BOT_TOKEN = "8355649306:AAEkSbV0ExKwU9Kbgqr0j8-lfY12q2IeaUk"  # Replace with your actual token

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello, world!")

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, hello))

app.run_polling()
app.run(port=PORT)
