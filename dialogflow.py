import os

import dialogflow_v2 as dialogflow
from dotenv import load_dotenv

load_dotenv()


def detect_intent_texts(session_id, texts, language_code, is_fallback=False):
    session_client = dialogflow.SessionsClient()

    session = session_client.session_path(os.getenv('GOGGLE_ID_PROJECT'),
                                          session_id)

    for text in texts:
        text_input = dialogflow.types.TextInput(
            text=text, language_code=language_code)

        query_input = dialogflow.types.QueryInput(text=text_input)

        response = session_client.detect_intent(
            session=session, query_input=query_input)
        if is_fallback and response.query_result.intent.is_fallback:
            return None
        return response.query_result.fulfillment_text
