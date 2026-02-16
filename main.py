# Функция 1: Проверка, является ли строка палиндромом
def is_palindrome():
    s = input("Задача 1. Введите строку для проверки палиндрома: ")
    s_clean = s.lower().replace(" ", "")  # игнорируем пробелы и регистр
    if s_clean == s_clean[::-1]:
        print("Строка является палиндромом.")
    else:
        print("Строка не является палиндромом.")


# Функция 2: Подсчёт количества слов в строке
def count_words():
    s = input("Задача 2. Введите строку с словами через пробел: ")
    words = s.split()
    print(f"Количество слов: {len(words)}")


# Функция 3: Подсчёт количества различных цифр в числе
def count_unique_digits():
    number = input("Задача 3. Введите натуральное число: ")
    if not number.isdigit():
        print("Ошибка: введено не число.")
        return
    unique_digits = set(number)
    print(f"Количество различных цифр: {len(unique_digits)}")


# ===== Основная программа, которая запускает все функции по очереди =====
if __name__ == "__main__":
    print("Решаем задачи по очереди...\n")

    is_palindrome()
    print()  # пустая строка для удобства
    count_words()
    print()
    count_unique_digits()
    print("\nВсе задачи решены.")
