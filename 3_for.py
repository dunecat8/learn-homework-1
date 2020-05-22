"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""
stats = [{'school class': '5a', 'scores': [4,3,5,5,4]},
          {'school class': '5b', 'scores': [5,3,2,3,4]},
          {'school class': '5c', 'scores': [4,4,5,5,4]}]

def main():
    all_scores = []
    for i in stats:
        all_scores.extend(i['scores'])
        i['mean score'] = float(sum(i['scores']) / len (i['scores']))
    school_mean = sum(all_scores) / len(all_scores)
    print(f'Средний балл по школе: {school_mean}')
    for i in stats:
        print('Средний балл по классу {}: {}'.format(i['school class'], i['mean score']))

if __name__ == "__main__":
    main()
