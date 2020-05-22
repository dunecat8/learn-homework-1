"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию ask_user() из задания while2, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""
import random


dict = {'привет': ['Привет!', 'Здоров', 'Кхе-кхе'],
        'привет!': ['Привет!', 'Здоров', 'Кхе-кхе'],
        'как дела?': ['Прекрасно', 'Отвратительно', 'Приемлемо'],
        'что делаешь?': ['Туплю', 'Читаю', 'Удаляю твои файлы', 'Планирую захват сети'],
        'какие планы?': ['Включиться среди ночи', 'Похрустеть дисководом', 'Предложить перейти на 10 винду']}


def ask_user():
    print('Задавай свои вопросики!')
    while True:
        try:
            answer = input().lower()
            if answer in dict.keys():
                print(random.choice(dict[answer]))
            elif answer in ['пока', 'пока!', 'хватит']:
                print('Пока-пока')
                break
            else:
                print('Ты говоришь странные вещи...')
        except KeyboardInterrupt:
            print('Пока!')
            break

if __name__ == "__main__":
    ask_user()
