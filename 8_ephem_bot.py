"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход 
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите 
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите 
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import logging
import ephem
import settings as st
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from datetime import datetime

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
)


PROXY = {
    'proxy_url': st.PROXY_URL,
    'urllib3_proxy_kwargs': {
        'username': st.PROXY_USERNAME,
        'password': st.PROXY_PASSWORD
    }
}

PLANETS = {
    'Mercury': ephem.Mercury,
    'Venus': ephem.Venus,
    'Mars': ephem.Mars,
    'Jupiter': ephem.Jupiter,
    'Saturn': ephem.Saturn,
    'Uranus': ephem.Uranus,
    'Neptune': ephem.Neptune
}


def greet_user(update, context):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text('Добрый день!')


def next_full_moon(update, context):
    today = datetime.today()
    result = ephem.next_full_moon(today)
    print(result)
    update.message.reply_text(f'Дата следующего полнолуния: {result}')


def word_form(wordcount):
    if 11 <= wordcount % 100 <= 14:
        return 'слов'
    elif wordcount % 10 == 1:
        return 'слово'
    elif 2 <= wordcount % 10 <= 4:
        return 'слова'
    else:
        return 'слов'


def talk_to_me(update, context):
    user_command = update.message.text.split()[0]
    user_text = update.message.text.split()[1:]
    if user_command == '/planet':
        user_planet = update.message.text.split()[1]
        p = PLANETS.get(user_planet)()
        p.compute()
        result = ephem.constellation(p)[1]
        update.message.reply_text(f'{user_planet} is in ' + result)
    elif user_command == '/wordcount':
        if user_text:
            wordcount = len([word for word in user_text if word.isalpha()])
            words = word_form(wordcount)
            update.message.reply_text(f'{wordcount} {words}')
    else:
        update.message.reply_text(update.message.text)


def main():
    mybot = Updater(st.API_KEY, request_kwargs=PROXY, use_context=True)
    
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("next_full_moon", next_full_moon))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()
       

if __name__ == "__main__":
    main()
