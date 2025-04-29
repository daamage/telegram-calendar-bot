{\rtf1\ansi\ansicpg1251\cocoartf2580
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import logging\
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup\
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes\
from datetime import datetime, timedelta\
\
# \uc0\u1042 \u1089 \u1090 \u1072 \u1074 \u1083 \u1103 \u1102  \u1090 \u1074 \u1086 \u1081  \u1090 \u1086 \u1082 \u1077 \u1085 \
import os\
BOT_TOKEN = os.getenv('BOT_TOKEN')\
\
logging.basicConfig(level=logging.INFO)\
logger = logging.getLogger(__name__)\
\
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):\
    keyboard = []\
    today = datetime.now()\
    for i in range(7):\
        day = today + timedelta(days=i)\
        button_text = day.strftime("%d.%m.%Y")\
        keyboard.append([InlineKeyboardButton(button_text, callback_data=button_text)])\
    reply_markup = InlineKeyboardMarkup(keyboard)\
    await update.message.reply_text('\uc0\u1054 \u1073 \u1077 \u1088 \u1110 \u1090 \u1100  \u1076 \u1072 \u1090 \u1091 :', reply_markup=reply_markup)\
\
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):\
    query = update.callback_query\
    await query.answer()\
    await query.edit_message_text(text=f"\uc0\u1042 \u1080  \u1086 \u1073 \u1088 \u1072 \u1083 \u1080  \u1076 \u1072 \u1090 \u1091 : \{query.data\}")\
\
def main():\
    application = ApplicationBuilder().token(BOT_TOKEN).build()\
    application.add_handler(CommandHandler('start', start))\
    application.add_handler(CallbackQueryHandler(button))\
    application.run_polling()\
\
if __name__ == '__main__':\
    main()\
}