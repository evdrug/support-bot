import logging
import os

from dotenv import load_dotenv
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from dialogflow import detect_intent_texts
from telegram_logger import TelegramLogsHandler

logger = logging.getLogger(__file__)


def start(bot, update):
    logger.debug(update.message)
    update.message.reply_text("Здравствуйте.")


def echo(bot, update):
    session_id = update.message.chat.id
    text = update.message.text
    message = None
    try:
        message = detect_intent_texts(session_id, [text], 'ru')
    except Exception as e:
        logger.exception(f'\ud83c\udd98 DialogFlow error\n {e}')
    if message:
        bot.sendMessage(chat_id=session_id, text=message)


if __name__ == '__main__':
    load_dotenv()
    logger.setLevel(logging.INFO)
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    updater = Updater(token=os.getenv('TELEGRAM_TOKEN'))
    logger.addHandler(TelegramLogsHandler(updater.bot))
    logger.info('\u2705 Бот запущен')
    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(
        MessageHandler(Filters.text, echo))
    updater.start_polling()
