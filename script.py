import math


# Функция 1
def count_even_not_coprime(n: int) -> int:
    count = 0
    for i in range(2, n + 1, 2):
        if math.gcd(i, n) > 1:
            count += 1
    return count


# Функция 2
def max_digit_not_divisible_by_3(n: int) -> int:
    digits = [int(d) for d in str(abs(n))]
    suitable_digits = [d for d in digits if d % 3 != 0]
    return max(suitable_digits) if suitable_digits else -1


# Вспомогательная функция
def smallest_divisor(n: int) -> int:
    if n % 2 == 0:
        return 2
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return i
    return n


# Функция 3
def product_special(n: int) -> int:
    min_div = smallest_divisor(n)

    max_number = -1
    for i in range(n - 1, 0, -1):
        if math.gcd(i, n) > 1 and i % min_div != 0:
            max_number = i
            break

    sum_digits = sum(int(d) for d in str(abs(n)) if int(d) < 5)

    if max_number == -1:
        return 0

    return max_number * sum_digits


# ===== ЗАПУСК ПРОГРАММЫ =====
if __name__ == "__main__":
    n = int(input("Введите число: "))

    result1 = count_even_not_coprime(n)
    result2 = max_digit_not_divisible_by_3(n)
    result3 = product_special(n)

    print("Количество четных чисел, не взаимно простых с n:", result1)
    print("Максимальная цифра, не делящаяся на 3:", result2)
    print("Результат третьей функции:", result3)

