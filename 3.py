import math

def calculate_area(sides):
    a, b, c = sides
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area

def calculate_triangle_areas(one, two, three):
    min_one = min(one)
    max_one = max(one)

    min_two = min(two)
    max_two = max(two)

    min_three = min(three)
    max_three = max(three)

    area1 = calculate_area([min_one, min_two, min_three])
    area2 = calculate_area([max_one, max_two, max_three])

    return area1, area2
one = [12, 25, 3, 48, 71]
two = [5, 18, 40, 62, 98]
three = [4, 21, 37, 56, 84]

area1, area2 = calculate_triangle_areas(one, two, three)

print("Площадь треугольника, составленного из минимальных элементов:", area1)
print("Площадь треугольника, составленного из максимальных элементов:", area2)
