# Support-Bot
Бот-помощник через сервис [Dialogflow](https://dialogflow.cloud.google.com/).
 
Он отвечает на типичные вопросы, сложные – перенаправляет на операторов

Примеры работы:

![alt text](https://dvmn.org/filer/canonical/1569214094/323/ "Telegram bot")

![alt text](https://dvmn.org/filer/canonical/1569214089/322/ "Vk bot")



## Как установить

1. Создать DialogFlow [проект](https://cloud.google.com/dialogflow/docs/quick/setup).

2. Создать DialogFlow [агента](https://cloud.google.com/dialogflow/docs/quick/build-agent).

3. Создать [JSON-ключ](https://cloud.google.com/docs/authentication/getting-started).
    
4. Переименовать файл  `.env.example` в `.env`.
    
5. Добавить учетный данные в файл `.env`

    `TELEGRAM_TOKEN`  -   токен вашего бота в Telegram

    `VK_TOKEN` - токен вашего бота в VK

    `GOGGLE_ID_PROJECT` -  id вашего google проекта (из шага 1)
        
    `GOOGLE_APPLICATION_CREDENTIALS` - путь до json-ключа (из шага 3)
    
    `TELEGRAM_CHAT_ID_LOGGER` - чат id в который отправлять логи

    `TELEGRAM_TOKEN_LOGGER` - токен бота от имени которого отправляются логи

6. Python3 должен быть уже установлен. 

    Затем используйте pip (или pip3, есть есть конфликт с Python2) для установки зависимостей:
    ```
    pip install -r requirements.txt
   ```

7. Обучение бота

    заполнить по анологии файл `questions.json`
    ```
   python lerning_bot.py
   ```
## Как пользоваться
Запуск ботов:
    
    python telegram_bot.py
    python vk_bot.py



## Размещение на Heroku

1. Создаем [новое](https://dashboard.heroku.com/new-app) приложение.

2. Переходим в `Deploy`, подключаем репозиторий github.

3. Нажимаем `Deploy Branch`.

4. Устанавливаем и авторизовываемся в [heroku-cli](https://devcenter.heroku.com/articles/heroku-cli#download-and-install).

5. Прописываем переменные из `.env.example` в `Settings` -> `Config Vars`.



### Цель проекта
Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org).
