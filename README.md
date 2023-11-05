# Тема 5. Базовые коллекции: множества, списки
Отчет по Теме #5 выполнил:
- Акользин Иван Сергеевич
- АИС-21-1

| Задание | Сам_раб | 
| ------ | ------ | 
| Задание 1 | + |
| Задание 2 | + |
| Задание 3 | + |
| Задание 4 | + |
| Задание 5 | + |

знак "+" - задание выполнено; знак "-" - задание не выполнено;

## Задание 1
### 1)	Ресторан на предприятии ведет учет посещений за неделю при помощи кода работника. У них есть список со всеми посещениями за неделю. Ваша задача почитать: 
• Сколько было выдано чеков 
• Сколько разных людей посетило ресторан 
• Какой работник посетил ресторан больше всех раз 
Список выданных чеков за неделю: [8734, 2345, 8201, 6621, 9999, 1234, 5678, 8201, 8888, 4321, 3365, 1478, 9865, 5555, 7777, 9998...

### Результат.
![Меню](https://github.com/vladimir-12343/Software_Engineering_0/blob/Тема_5/pic/ex1.png)
## Вывод 
1)print("Количество чеков - ", len(my_list)) выводит общее количество чеков (элементов) в списке my_list.
2)my_set = set() создает пустое множество my_set, которое будет использоваться для отслеживания уникальных работников, посетивших ресторан.
3)Затем код использует цикл for для итерации по элементам my_list. 
4)После завершения цикла, код выводит следующую информацию:
    print("Количество людей, посетивших ресторан один раз - ", len(my_set)) выводит количество уникальных работников, посетивших ресторан один раз.
    print(f"Наибольшее количество посещений было у работника с кодом - {meaning}. В количестве - {number} раз") выводит информацию о работнике с максимальным количеством посещений и количестве посещений.

## Задание 2
### 2)	На физкультуре студенты сдавали бег, у преподавателя физкультуры есть список всех результатов, ему нужно узнать • Три лучшие результата • Три худшие результата • Все результаты начиная с 10 Ваша задача помочь ему в этом. Список результатов бега: [10.2, 14.8, 19.3, 22.7, 12.5, 33.1, 38.9, 21.6, 26.4, 17.1, 30.2, 35.7, 16.9, 27.8, 24.5, 16.3, 18.7, 31.9, 12.9, 37.4]
![Меню](https://github.com/vladimir-12343/Software_Engineering_0/blob/Тема_5/pic/ex2.png)
## Выводы
1)Создает копию списка my_list и сохраняет ее в copy_list.
2)Определяет длину списка my_list и сохраняет ее в leng.
3)Сортирует исходный список my_list в порядке возрастания.
4)Выводит три наилучших (с наименьшими значениями) результата из отсортированного my_list.
5)Выводит три наихудших (с наибольшими значениями) результата из отсортированного my_list.
6)Выводит все результаты из copy_list, начиная с элемента с индексом 10 (включая его).


## Задание 3
### 3)	Преподаватель по математике Aпридумал странную задачку. У вас есть три списка с элементами, каждый элемент которых – длина стороны треугольника, ваша задача найти площади двух треугольников, составленные из максимальных и минимальных элементов полученных списков. Результатом выполнения задачи будет: листинг кода, и вывод в консоль, в котором будут указаны два этих значения.
Три списка:
one = [12, 25, 3, 48, 71] 
two = [5, 18, 40, 62, 98] 
three = [4, 21, 37, 56, 84]

![Меню](https://github.com/vladimir-12343/Software_Engineering_0/blob/Тема_5/pic/ex3.png)
![Меню](https://github.com/vladimir-12343/Software_Engineering_0/blob/Тема_5/pic/ex3.1.png)
![Меню](https://github.com/vladimir-12343/Software_Engineering_0/blob/Тема_5/pic/ex3.2.png)
## Выводы
1)Создает три списка: one, two и three, каждый из которых содержит пять чисел.
2)Объединяет все три списка в один my_conList.
3)Сортирует my_conList в порядке возрастания.
4)Вычисляет площадь треугольника, образованного минимальными тремя элементами списка, с использованием функции Heron.SquareHeron.
5)Вычисляет площадь треугольника, образованного максимальными тремя элементами списка, также с использованием функции Heron.SquareHeron.
6)Выводит площади обоих треугольников.
Формулу Герона взял в Теме_4.

  
## Задание 4
### Никто не любит получать плохие оценки, поэтому Борис решил это исправить. Допустим, что все оценки студента за семестр хранятся в одном списке. Ваша задача удалить из этого списка все двойки, а все тройки заменить на четверки. Списки оценок (проверить работу программы на всех трех вариантах): [2, 3, 4, 5, 3, 4, 5, 2, 2, 5, 3, 4, 3, 5, 4] [4, 2, 3, 5, 3, 5, 4, 2, 2, 5, 4, 3, 5, 3, 4] [5, 4, 3, 3, 4, 3, 3, 5, 5, 3, 3, 3, 3, 4, 4]

![Меню](https://github.com/vladimir-12343/Software_Engineering_0/blob/Тема_5/pic/ex4.png)
![Меню](https://github.com/vladimir-12343/Software_Engineering_0/blob/Тема_5/pic/ex4.1.png)
![Меню](https://github.com/vladimir-12343/Software_Engineering_0/blob/Тема_5/pic/ex4.2.png)
## Выводы
1)Создает список my_list, содержащий различные целые числа.
2)Создает пустой список my_list1, в который будут добавляться элементы из my_list с определенными условиями.
3)Использует цикл for для итерации по элементам my_list.
4)Внутри цикла проверяет условия:
    Если элемент не равен 2, выполняется следующая проверка.
    Если элемент равен 3, то он заменяется на 4.
    Затем элемент добавляется в список my_list1.
5)Выводит список my_list1, который содержит элементы из my_list, в которых числа 3 заменены на 4, и элементы, равные 2, удалены.


## Задание 5
### 5)	Вам предоставлены списки натуральных чисел, из них необходимо сформировать множества. При этом следует соблюдать это правило: если какое-либо число повторяется, то преобразовать его в строку по следующему образцу: например, если число 4 повторяется 3 раза, то в множестве будет следующая запись: само число 4, строка «44», строка «444». Множества для теста: list_1 = [1, 1, 3, 3, 1] list_2 = [5, 5, 5, 5, 5, 5, 5] list_3 = [2, 2, 1, 2, 2, 5, 6, 7, 1, 3, 2, 2]
![Меню](https://github.com/vladimir-12343/Software_Engineering_0/blob/Тема_5/pic/ex5.png)
![Меню](https://github.com/vladimir-12343/Software_Engineering_0/blob/Тема_5/pic/ex5.1.png)
![Меню](https://github.com/vladimir-12343/Software_Engineering_0/blob/Тема_5/pic/ex5.2.png)
## Выводы
1)Создает список list_1, содержащий целые числа.
2)Сортирует list_1 в порядке возрастания.
3)Создает пустой список list для хранения результатов.
4)Инициализирует переменные number и str1.
5)Использует цикл for для итерации по элементам list_1.
6)Внутри цикла проверяет, если текущий элемент item равен предыдущему элементу number. Если да, то он добавляет item к строке str1 и затем добавляет str1 в список list.
7)Если текущий элемент item отличается от предыдущего number, то он сбрасывает строку str1 на пустую строку и повторяет процесс.
8)Затем код проходит по списку list и заменяет одиночные цифры (строки длиной 1) обратно на целые числа.
9)Наконец, выводит список list, который содержит уникальные элементы из list_1 сгруппированные в виде последовательностей строк или целых чисел, где одиночные цифры были восстановлены.

Итак, код преобразует список list_1 в список list, где одинаковые числа объединены в строки, и заменяет одиночные цифры на целые числа.






