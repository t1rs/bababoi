import datetime
import time

for i in range(5):
    # Получаем текущее время
    current_time = datetime.datetime.now()
    # Выводим текущее время
    print(current_time.strftime("%H:%M:%S"))
    # Задержка программы на 1 секунду
    time.sleep(1)
