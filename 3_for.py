"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""
stats = [{'school_class': '5a', 'scores': [4,3,5,5,4]},
          {'school_class': '5b', 'scores': [5,3,2,3,4]},
          {'school_class': '5c', 'scores': [4,4,5,5,4]}]

def main():
    all_scores = [score for item in stats for score in item['scores']]
    for item in stats:
        item['mean score'] = float(sum(item['scores']) / len(item['scores']))
    school_mean = sum(all_scores) / len(all_scores)
    print(f'Средний балл по школе: {school_mean}')
    for item in stats:
        print(f'Средний балл по классу {item["school_class"]}: {item["mean score"]}')

if __name__ == "__main__":
    main()
