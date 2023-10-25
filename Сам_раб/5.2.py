import math

def calculate_area(side_a, side_b, side_c):
    # Расчет полупериметра
    s = (side_a + side_b + side_c) / 2
    # Вычисление площади треугольника по формуле Герона
    area = math.sqrt(s * (s - side_a) * (s - side_b) * (s - side_c))
    return area
