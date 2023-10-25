from triangle import calculate_area

# Получение данных от пользователя
side_a = float(input("Введите длину стороны a: "))
side_b = float(input("Введите длину стороны b: "))
side_c = float(input("Введите длину стороны c: "))

# Вычисление площади треугольника
area = calculate_area(side_a, side_b, side_c)

# Вывод результата
print("Площадь треугольника:", area)
