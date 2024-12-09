from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext


def start(update: Update, context: CallbackContext):
    update.message.reply_text('Привет! Я твой бот.')


def help_command(update: Update, context: CallbackContext):
    update.message.reply_text('Я могу выполнять следующие команды:\n'
                              '/start - начать общение\n'
                              '/help - получить помощь')


if __name__ == '__main__':
    # Замените 'YOUR_TOKEN_HERE' на токен вашего бота
    updater = Updater("7620101380:AAGVsxcS-MjR7JbaDS9eY5JKjdX5sBNX3ZI")

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('help', help_command))

    updater.start_polling()
    updater.idle()