# Напишіть програму, яка відкриває файл для читання та обробляє помилку FileNotFoundError, якщо файл не знайдено.

try:
    fp = "text.txt"
    file = open(fp, 'r', encoding='utf-8')
    print(file)

except FileNotFoundError:
    print("File is not found :(")
