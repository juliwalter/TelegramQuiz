# TelegramQuiz
### Table of Contents 
  * [What does TelegramQuiz do?](#what-does-telegramquiz-do?)
  * [Setup](#setup)
  * [Run TelegramBot](#run-telegramquiz)
  * [Configure TelegramQuiz](#set-telegramquiz-questions)
  * [Try TelegramQuiz](#try-telegramquiz)

## What does TelegramQuiz do?

TelegramQuiz is a python based script, which feeds your Telegram bot with multiple-choice questions. The following commands can be performed with this bot
* /start - Welcomes the user and prints out the /help output
* /question - Diplays a multiple-choice question to user
* /help - Displays all commands and bot interactions to user
* /config - Displays a menu for quiz parameter adjustments (tbd)
* Any other message will be echoed to user

## Setup

Open your shell, navigate to desired directory

```
$ cd /this/is/a/directory
```

and clone the repository.

```
$ git clone https://github.com/juliwalter/TelegramQuiz.git
```

Make sure to create a file *.env* in the *app* folder and add the following line to it whereat 'your_token_id' has to be replaced by your personal Telegram bot token.

```
TELEGRAM_TOKEN='your_token_id'
```

Create a virtual environment *venv* by typing following
```
$ python3 -m venv venv
```

activate it by 
```
$ source venv/bin/activate
```

and install the following modules.
```
$ pip install python-telegram-bot --upgrade
$ pip install python-dotenv
$ pip install pandas
```


Deactivate the virtual environment to finish setup.
```
$ deactivate
```

## Run TelegramQuiz
Activate the virtual environment
```
$ source venv/bin/activate
```

from the projects root directory run the *app.py* script.
```
$ python app.py
```

To stop the script hit *ctrl* + *c*.

## Set TelegramQuiz questions
In *'app/database/questions.csv'* one can change the desired questions within the TelegramQuiz-Bot by providing the data in the following way. <br><br> 
![](images/Questions_DataStructure.png)

## Try TelegramQuiz
Try TelegramQuiz your own by scanning the following QR-Code or clicking [here](https://t.me/quizzle_shizzle_bot). <br><br> 
![drawing](images/Bot_QR.png)
