import json
import logging
import os

import dialogflow_v2 as dialogflow
import google
from dotenv import load_dotenv

logger = logging.getLogger(__file__)


def start_train_agent(project_id):
    client = dialogflow.AgentsClient()
    parent = client.project_path(project_id)
    client.train_agent(parent)


def generate_intent(name, data):
    training_phrases = [{"parts": [{"text": question}]} for question in
                        data['questions']]
    return {
        "display_name": name,
        "messages": [{
            "text":
                {"text": [data['answer']]}
        }],
        "training_phrases": training_phrases
    }


if __name__ == '__main__':
    load_dotenv()
    logger.setLevel(logging.INFO)
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    logger.info('\u2705 Начинаем обучать бота ;) ')

    project_id = os.getenv('GOGGLE_ID_PROJECT')
    client = dialogflow.IntentsClient()
    parent = client.project_agent_path(project_id)

    with open("questions.json", "r") as my_file:
        questions = json.load(my_file)
        for intent, training_phrases in questions.items():
            try:
                response = client.create_intent(parent,
                                                generate_intent(intent,
                                                                training_phrases))
            except google.api_core.exceptions.InvalidArgument as e:
                logger.error(e)


    start_train_agent(project_id)
