def factorial(n: int) -> int:
    """Обчислює факторіал невід'ємного цілого числа n."""
    if not isinstance(n, int):
        raise TypeError("Аргумент має бути цілим числом")
    if n < 0:
        raise ValueError("Факторіал визначений лише для невід'ємних чисел")
    if n in (0, 1):
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def is_even(n: int) -> bool:
    """Перевіряє, чи є ціле число парним."""
    if not isinstance(n, int):
        raise TypeError("Аргумент має бути цілим числом")
    return n % 2 == 0