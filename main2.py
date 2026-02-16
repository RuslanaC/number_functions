import string

# ===== Функция 1: Подсчет чисел в строке меньше 5 =====
def count_numbers_less_than_5():
    s = input("Задача 1. Введите строку с числами: ")
    # разделяем строку по пробелам
    parts = s.split()
    count = 0
    for part in parts:
        if part.isdigit() and int(part) < 5:
            count += 1
    print(f"Количество чисел меньше 5: {count}")


# ===== Функция 2: Найти незадействованные символы латиницы =====
def unused_latin_letters():
    s = input("Задача 2. Введите строку: ")
    # переводим в нижний регистр для единообразия
    s_lower = s.lower()
    letters_in_text = set(c for c in s_lower if c in string.ascii_lowercase)
    unused_letters = set(string.ascii_lowercase) - letters_in_text
    print(f"Незадействованные латинские буквы: {' '.join(sorted(unused_letters))}")


# ===== Функция 3: Подсчет цифр больше 5 =====
def count_digits_greater_than_5():
    s = input("Задача 3. Введите строку с цифрами: ")
    count = 0
    for c in s:
        if c.isdigit() and int(c) > 5:
            count += 1
    print(f"Количество цифр больше 5: {count}")


# ===== Основная программа с выбором задачи =====
if __name__ == "__main__":
    print("Выберите задачу:")
    print("1 - Подсчитать количество чисел в строке меньше 5")
    print("2 - Найти все незадействованные символы латиницы")
    print("3 - Подсчитать количество цифр в строке больше 5")

    choice = input("Введите номер задачи (1/2/3): ")

    if choice == "1":
        count_numbers_less_than_5()
    elif choice == "2":
        unused_latin_letters()
    elif choice == "3":
        count_digits_greater_than_5()
    else:
        print("Некорректный ввод. Выберите 1, 2 или 3.")
