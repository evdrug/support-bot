import logging
import os
import random

import vk_api
from dotenv import load_dotenv
from vk_api.longpoll import VkLongPoll, VkEventType

from dialogflow import detect_intent_texts
from telegram_logger import TelegramLogsHandler

logger = logging.getLogger(__file__)


def echo(event, vk_api):
    user_id = event.user_id,
    message = event.text,
    answer = None
    try:
        answer = detect_intent_texts(user_id, message, 'ru', is_fallback=True)
    except Exception as e:
        logger.exception(f'\ud83c\udd98 DialogFlow error\n {e}')

    if answer:
        vk_api.messages.send(
            user_id=user_id,
            message=answer,
            random_id=random.randint(1, 1000)
        )


if __name__ == "__main__":
    load_dotenv()
    logger.setLevel(logging.INFO)
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    logger.addHandler(TelegramLogsHandler())

    vk_session = vk_api.VkApi(token=os.getenv('VK_TOKEN'))
    logger.info('\u2705 Бот запущен')
    vk_api = vk_session.get_api()
    longpoll = VkLongPoll(vk_session)
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            echo(event, vk_api)
