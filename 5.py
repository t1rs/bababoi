import re

def count_nouns(file_path):
    with open(r'C:\Users\Ivan\Desktop\input.txt', 'r') as file:
        text = file.read()

    # Используем регулярное выражение для поиска существительных
    nouns = re.findall(r'\b[A-Z][a-zA-Z]*\b', text)

    return len(nouns)

# Пример использования
file_path = 'text.txt'  # замените на путь к вашему файлу
noun_count = count_nouns(file_path)
print('Количество существительных в файле:', noun_count)
