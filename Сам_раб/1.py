from datetime import datetime       # импорт класса datetime из модуля datetime.
from math import sqrt       # импорт функции sqrt из модуля math.

def main(**kwargs):     # объявление функции main с аргументом kwargs, который является словарем с именованными аргументами и их значениями.
    for key in kwargs.items():
        result = sqrt(key[1][0] ** 2 + key[1][1] ** 2)      # вычисление значения переменной result. key[1] обращается к значению пары ключ-значение,
                                                            # а key[1][0] и key[1][1] обращаются к элементам списка, которые являются значениями в паре.
        print(result)

if __name__ == '__main__':      # проверка, выполняется ли данный скрипт напрямую (а не импортируется в другой скрипт).
    start_time = datetime.now()     # создание объекта start_time, который хранит текущую дату и время.
    main(                                           # вызов функции main с передачей именованных аргументов в виде словаря.
        one = [10, 3],
        two = [5, 4],
        three = [15, 13],
        four = [93, 53],
        five = [133, 15]
    )
    time_costs = datetime.now() - start_time        # вычисление разницы между текущей датой и временем и значением объекта start_time.
                                                    # Результат сохраняется в переменной time_costs.
    print(f"Время выполнения программы - {time_costs}")     # вывод на экран строки с сообщением о времени выполнения программы,
                                                            # которое было сохранено в переменной time_costs.
