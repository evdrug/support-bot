# Support-Bot
Бот-помощник через сервис [Dialogflow](https://dialogflow.cloud.google.com/).
 
Он отвечает на типичные вопросы, сложные – перенаправляет на операторов


Примеры работы:

![alt text](https://dvmn.org/filer/canonical/1569214094/323/ "Telegram bot")
![alt text](https://dvmn.org/filer/canonical/1569214089/322/ "Vk bot")


[телеграм-бот](https://tlgg.ru/@hlmn_bot)  
[VK-бот](https://vk.com/club197757902)

## Как установить

Создать DialogFlow [проект](https://cloud.google.com/dialogflow/docs/quick/setup).  
Создать DialogFlow [агента](https://cloud.google.com/dialogflow/docs/quick/build-agent).  
Создать [JSON-ключ](https://cloud.google.com/docs/authentication/getting-started).  
Переименовать файл  `.env.example` в `.env`.  
Добавить учетный данные в файл `.env`  
* `TELEGRAM_TOKEN`  -   токен вашего бота в Telegram
* `VK_TOKEN` - токен вашего бота в VK
* `GOGGLE_ID_PROJECT` -  id вашего google проекта (из шага 1)
* `GOOGLE_APPLICATION_CREDENTIALS` - путь до json-ключа (из шага 3)
* `LOGGER_TELEGRAM_CHAT_ID` - чат id в который отправлять логи
* `LOGGER_TELEGRAM_TOKEN` - токен бота от имени которого отправляются логи
* `QUESTIONS_FILE` - путь к json файлу, для обучения бота

Python3 должен быть уже установлен.  
Затем используйте pip (или pip3, есть есть конфликт с Python2) для установки зависимостей:

```
pip install -r requirements.txt
```  
Для обучения бота, заполнить по аналогии файл `questions.json` и выполнить
```
python train_bot.py
```

## Как пользоваться
Запуск ботов:
```
python telegram_bot.py
python vk_bot.py
```


## Размещение на Heroku

Создаем [новое](https://dashboard.heroku.com/new-app) приложение.  
Переходим в `Deploy`, подключаем репозиторий github.  
Нажимаем `Deploy Branch`.  
Устанавливаем и авторизовываемся в [heroku-cli](https://devcenter.heroku.com/articles/heroku-cli#download-and-install).  
Прописываем переменные из `.env.example` в `Settings` -> `Config Vars`.  
Установку `GOOGLE_APPLICATION_CREDENTIALS` делаем по [инструкции](https://github.com/gerywahyunugraha/heroku-google-application-credentials-buildpack).  
Подключаем buildpacks через [CLI](https://elements.heroku.com/buildpacks/buyersight/heroku-google-application-credentials-buildpack) или на странице Settings, проверяем чтобы там же был `heroku/python`.  
Запускаем приложение через вкладку Resources или CLI : 

```
heroku ps:scale tg-bot=1 -a Имя_приложения
heroku ps:scale vk-bot=1 -a Имя_приложения
```
### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org).
