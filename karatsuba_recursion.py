import re


def recursive_karatsuba(a: int, b: int) -> int:

    if a < 10 or b < 10:
        return a * b

    m = max(len(str(a)), len(str(b)))
    m2 = m // 2
    
    a1, a2 = divmod(a, 10**m2)
    b1, b2 = divmod(b, 10**m2)

    z0 = recursive_karatsuba(a2, b2)  # a2 * b2
    z1 = recursive_karatsuba(a1 + a2, b1 + b2)  # (a1 + a2) * (b1 + b2)
    z2 = recursive_karatsuba(a1, b1)  # a1 * b1

    return (z2 * 10**(2 * m2)) + ((z1 - z2 - z0) * 10**m2) + z0

def test_recursive_karatsuba():
    test_cases = [
        (1462, 5448, 1462 * 5448),
        (772468, 928846, 772468 * 928846),
        (123456789, 987654321, 123456789 * 987654321),
        (0, 12345, 0),  
        (12345, 0, 0),
        (99999, 99999, 99999 * 99999) 
    ]

    for x, y, expected in test_cases:
        result = recursive_karatsuba(x, y)
        assert result == expected, f"Ошибка при умножении {x} * {y}: {result} != {expected}"
        print(f"Тест {x} * {y} прошел успешно. Ответ: {result}")

test_recursive_karatsuba()