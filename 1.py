import collections

# Чтение содержимого файла
with open(r'C:\Users\Ivan\Desktop\статья.txt', 'r', encoding='utf-8') as file:
    content = file.read()

# Разбивка текста на слова
words = content.split()

# Подсчет количества слов
word_count = len(words)
print(f"Количество слов в тексте: {word_count}")

# Подсчет частоты встречаемости слов
word_freq = collections.Counter(words)

# Определение самого часто встречающегося слова
most_common_word = word_freq.most_common(1)[0][0]
print(f"Самое часто встречающееся слово: {most_common_word}")
