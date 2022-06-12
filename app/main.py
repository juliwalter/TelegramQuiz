# import telegram bot 
from telegram import Poll
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# import helper functions
from helpers import *

# load environment variables from .env-file
from dotenv import load_dotenv
load_dotenv()

# initialize a quiz and config
import model 
quiz = model.quiz()
config = model.config()

def start(update, context) -> None:
    """Outputs all welocome text and help."""
    update.message.reply_text(config.welcome_output)
    help(update, context)

def question(update, context) -> None:
    """Starts a quiz."""
    # shuffle quiz question
    quiz.shuffle_question()

    # fet user id
    c_id = get_chat_id(update, context)

    # send question as poll to user
    message = context.bot.send_poll(
        chat_id=c_id, question=quiz.question, 
        options=quiz.answers, type=Poll.QUIZ, 
        correct_option_id=quiz.correct_answer, 
        open_period=config.open_period
    )

    update.message.reply_text(config.question_output)

def help(update, context) -> None:
    """Outputs all commands."""
    update.message.reply_text(config.help_output)

def change_config(update, context) -> None:
    update.message.reply_text('tbd!')

def echo(update, context) -> None:
    """Echoes the user message."""
    update.message.reply_text(update.message.text)

def main() -> None:
    updater = Updater(config.telegram_token, use_context=True)
    dp = updater.dispatcher

    # handle commands
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("question", question))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("config", change_config))

    # handle any other message
    dp.add_handler(MessageHandler(Filters.text, echo))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()