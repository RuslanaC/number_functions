import math

def count_even_not_coprime(n: int) -> int:
    count = 0
    for i in range(2, n + 1, 2):  # перебираем только четные
        if math.gcd(i, n) > 1:
            count += 1
    return count

