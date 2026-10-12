import os
from flask import Flask, request
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters
import asyncio

TOKEN = os.getenv("BOT_TOKEN")
app = Flask(__name__)

# Telegram App
application = Application.builder().token(TOKEN).build()

async def start(update: Update, context):
    await update.message.reply_text("Namaste Guru! 🙏 SS-BOT Live aaythu! File kalisu!")

async def handle_file(update: Update, context):
    await update.message.reply_text(f"File sikthu Guru! {update.message.document.file_name}")

application.add_handler(CommandHandler("start", start))
application.add_handler(MessageHandler(filters.Document.ALL, handle_file))

@app.route(f"/{TOKEN}", methods=['POST'])
def webhook():
    update = Update.de_json(request.get_json(force=True), application.bot)
    asyncio.run(application.process_update(update))
    return "ok"

@app.route("/")
def home():
    return "SS-BOT Running!"

if __name__ == "__main__":
    # Set webhook
    import requests
    url = f"https://ss-bot-y07t.onrender.com/{TOKEN}"
    requests.get(f"https://api.telegram.org/bot{TOKEN}/setWebhook?url={url}")
    app.run(host="0.0.0.0", port=10000)
