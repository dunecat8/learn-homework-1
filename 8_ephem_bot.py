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


def greet_user(update, context):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text('Добрый день!')


def talk_to_me(update, context):
    user_text = getattr(getattr(update, 'message'), 'text')
    if user_text.lower() == '/planet mars':
        m = ephem.Mars()
        m.compute()
        update.message.reply_text('Mars is in ' + ephem.constellation(m)[1])
    elif user_text.lower() == '/planet venus':
        v = ephem.Venus()
        v.compute()
        update.message.reply_text('Venus is in ' + ephem.constellation(v)[1])
    elif user_text.lower() == '/planet jupiter':
        j = ephem.Jupiter()
        j.compute()
        update.message.reply_text('Jupiter is in ' + ephem.constellation(j)[1])
    else:
        update.message.reply_text(user_text)


def main():
    mybot = Updater(st.API_KEY, request_kwargs=PROXY, use_context=True)
    
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()
       

if __name__ == "__main__":
    main()
