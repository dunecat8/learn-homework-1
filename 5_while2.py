"""

Домашнее задание №1

Цикл while: ask_user со словарём

* Создайте словарь типа "вопрос": "ответ", например: 
  {"Как дела": "Хорошо!", "Что делаешь?": "Программирую"} и так далее
* Напишите функцию ask_user_dict() которая с помощью input() просит 
  пользователя ввести вопрос, а затем, если вопрос есть в словаре, 
  программа давала ему соотвествующий ответ. Например:

    Пользователь: Что делаешь?
    Программа: Программирую
    
"""
import random

answers = {'привет':('Привет!', 'Здоров', 'Кхе-кхе'),
        'привет!':('Привет!', 'Здоров', 'Кхе-кхе'),
        'как дела?': ('Прекрасно', 'Отвратительно', 'Приемлемо'),
        'что делаешь?':('Туплю', 'Читаю', 'Удаляю твои файлы', 'Планирую захват сети'),
        'какие планы?': ('Включиться среди ночи', 'Похрустеть дисководом', 'Предложить перейти на 10 винду')}

def ask_user():
    print('Задавай свои вопросики!')
    while True:
        answer = input().lower()
        if answer in answers.keys():
            print(random.choice(answers.get(answer)))
        elif answer in ['пока', 'пока!', 'хватит']:
            print('Пока-пока')
            break
        else:
            print('Ты говоришь странные вещи...')

    
if __name__ == "__main__":
    ask_user()
