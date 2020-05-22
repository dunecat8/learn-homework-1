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
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
)


PROXY = {
    'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {
        'username': 'learn', 
        'password': 'python'
    }
}


def greet_user(update, context):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)


def talk_to_me(update, context):
    user_text = update.message.text.lower()
    if user_text.startswith('/planet'):
        if 'mars' in user_text:
            m = ephem.Mars()
            m.compute()
            update.message.reply_text('Mars is in ' + ephem.constellation(m)[1])
        elif 'venus' in user_text:
            v = ephem.Venus()
            v.compute()
            update.message.reply_text('Venus is in ' + ephem.constellation(v)[1])
        elif 'jupiter' in user_text:
            j = ephem.Jupiter()
            j.compute()
            update.message.reply_text('Jupiter is in ' + ephem.constellation(j)[1])
    else:
        update.message.reply_text(user_text)



def main():
    mybot = Updater('1295725652:AAFyQ7F_PN70ECbYinmV5MDSUwpYdwFL1Rg', request_kwargs=PROXY, use_context=True)
    
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()
       

if __name__ == "__main__":
    main()
