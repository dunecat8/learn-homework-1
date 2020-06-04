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
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler
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

CITIES = {
    'А': {'Архангельск', 'Амстердам', 'Алматы'},
    'Д': {'Дубна', 'Дублин'},
    'К': {'Калининград', 'Казань', 'Красноярск'},
    'М': {'Москва', 'Мурманск'},
    'Н': {'Нью-Йорк', 'Норильск'},
    'С': {'Санкт-Петербург', 'Сиэтл'}}

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


def cities_start(update, context):
    context.user_data["cities"] = CITIES.copy()
    context.user_data["round"] = 1
    update.message.reply_text('Назовите город')
    return 'cities_main'

def cities_main(update, context):
    user_city = update.message.text.title()
    if user_city[0] not in context.user_data["cities"].keys():
        update.message.reply_text('Такого города нет в списке! Назовите другой')
        return 'cities_main'
    print(user_city, context.user_data["cities"][user_city[0]], context.user_data["round"])
    if context.user_data["round"] != 1:
        last_char = context.user_data['last_char']
        if not user_city.startswith(last_char):
            update.message.reply_text(f'Город должен быть на букву {last_char}!')
            return 'cities_main'
    if user_city not in context.user_data["cities"][user_city[0]]:
        update.message.reply_text('Такого города нет в списке! Назовите другой')
        return 'cities_main'
    context.user_data["cities"][user_city[0]].remove(user_city)
    last_char = [user_city[-2] if user_city[-1] in ['ы', 'ь'] else user_city[-1]][0].upper()
    print(context.user_data["cities"][user_city[0]], last_char)
    if last_char not in context.user_data["cities"].keys():
        update.message.reply_text('Я сдаюсь!')
        return ConversationHandler.END
    if not context.user_data["cities"][last_char]:
        update.message.reply_text('Я сдаюсь!')
        return ConversationHandler.END
    bot_city = context.user_data["cities"][last_char].pop()
    update.message.reply_text(bot_city)
    update.message.reply_text('Ваш ход!')
    context.user_data['last_char'] = [bot_city[-2] if bot_city[-1] in ['ы', 'ь'] else bot_city[-1]][0].upper()
    context.user_data["round"] += 1
    return 'cities_main'


def cancel(update, context):
    update.message.reply_text('Спасибо за игру!')
    return ConversationHandler.END


def talk_to_me(update, context):
    user_command = update.message.text.split()[0]
    user_text = update.message.text.split()[1:]
    if user_command == '/planet':
        user_planet = update.message.text.split()[1]
        p = PLANETS.get(user_planet)()
        p.compute()
        result = ephem.constellation(p)[1]
        update.message.reply_text(f'{user_planet} is in {result}' )
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
    dp.add_handler(ConversationHandler(entry_points=[CommandHandler("cities", cities_start)],
                                       states={'cities_main': [MessageHandler(Filters.text & (~Filters.command), cities_main)]},
                                       fallbacks=[CommandHandler('cancel', cancel)]))
    dp.add_handler(CommandHandler("next_full_moon", next_full_moon))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))


    mybot.start_polling()
    mybot.idle()
       

if __name__ == "__main__":
    main()

