# # Функция 1: Проверка, является ли строка палиндромом
# def is_palindrome():
#     s = input("Задача 1. Введите строку для проверки палиндрома: ")
#     s_clean = s.lower().replace(" ", "")  # игнорируем пробелы и регистр
#     if s_clean == s_clean[::-1]:
#         print("Строка является палиндромом.")
#     else:
#         print("Строка не является палиндромом.")
#
#
# # Функция 2: Подсчёт количества слов в строке
# def count_words():
#     s = input("Задача 2. Введите строку с словами через пробел: ")
#     words = s.split()
#     print(f"Количество слов: {len(words)}")
#
#
# # Функция 3: Подсчёт количества различных цифр в числе
# def count_unique_digits():
#     number = input("Задача 3. Введите натуральное число: ")
#     if not number.isdigit():
#         print("Ошибка: введено не число.")
#         return
#     unique_digits = set(number)
#     print(f"Количество различных цифр: {len(unique_digits)}")
#
#
# # ===== Основная программа, которая запускает все функции по очереди =====
# if __name__ == "__main__":
#     print("Решаем задачи по очереди...\n")
#
#     is_palindrome()
#     print()  # пустая строка для удобства
#     count_words()
#     print()
#     count_unique_digits()
#     print("\nВсе задачи решены.")

import re

# Словарь месяцев на русском
months = [
    "января", "февраля", "марта", "апреля", "мая", "июня",
    "июля", "августа", "сентября", "октября", "ноября", "декабря"
]


def find_dates(text: str):
    # Создаём шаблон для регулярного выражения
    # День: 1-31, Месяц: только из списка, Год: 4 цифры
    month_pattern = "|".join(months)
    date_pattern = r"\b([1-9]|[12][0-9]|3[01])\s+(" + month_pattern + r")\s+(\d{4})\b"

    matches = re.findall(date_pattern, text)

    # Преобразуем к читаемому виду
    dates = ["{} {} {}".format(day, month, year) for day, month, year in matches]

    return dates


# ===== Пример использования =====
if __name__ == "__main__":
    text = input("Введите текст с датами: ")
    dates = find_dates(text)

    if dates:
        print("Найденные даты:")
        for d in dates:
            print(d)
    else:
        print("Даты не найдены.")
