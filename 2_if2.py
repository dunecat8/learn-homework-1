"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""
list1 = ['шмель', 12, 'мухахаха', 'study']
list2 = ['шмель', 'двенадцать', 'мухаха', 'learn']

def main(str1, str2):
    if type(str1) == str and type(str2) == str:
        if str1 == str2:
            return 1
        elif len(str1) > len(str2):
            return 2
        elif str2 == 'learn':
            return 3
    else:
        return 0
    
if __name__ == "__main__":
    for str1, str2 in zip(list1,list2):
        print(main(str1, str2))

