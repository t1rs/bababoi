def find_max_min(numbers):
    min_num = numbers[0]
    max_num = numbers[0]
    for num in numbers:
        if num < min_num:
            min_num = num
        if num > max_num:
            max_num = num
    return (min_num, max_num)

print(find_max_min([-10, -20, -30, -40]))
