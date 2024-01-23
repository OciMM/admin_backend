import random
import string

# Задаем длину строки
length = 10

# Создаем строку из случайных букв и цифр
random_string = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))

print(random_string)
