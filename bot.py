import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes
from datetime import datetime, timedelta

# Вставляю твой токен
import os
BOT_TOKEN = os.getenv('BOT_TOKEN')

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = []
    today = datetime.now()
    for i in range(7):
        day = today + timedelta(days=i)
        button_text = day.strftime("%d.%m.%Y")
        keyboard.append([InlineKeyboardButton(button_text, callback_data=button_text)])
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('Оберіть дату:', reply_markup=reply_markup)

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(text=f"Ви обрали дату: {query.data}")

def main():
    application = ApplicationBuilder().token(BOT_TOKEN).build()
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CallbackQueryHandler(button))
    application.run_polling()

if __name__ == '__main__':
    main()
