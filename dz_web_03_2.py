from concurrent.futures import ProcessPoolExecutor
from multiprocessing import cpu_count
from time import perf_counter


def get_divisors(n):
    """Створює список з дільниками."""

    return [i for i in range(1, n + 1) if n % i == 0]


def factorize(*numbers):
    """Повертає списки дільників усіх чисел, переданих у функцію."""
    
    result = []

    for n in numbers:
        result.append(get_divisors(n))
    return result


def factorize_multithread(*numbers, workers=4):
    """Повертає списки дільників усіх чисел, переданих у функцію.
    Обчислення з використанням багатопотокості."""

    with ProcessPoolExecutor(max_workers=workers) as executor:
        results = list(executor.map(get_divisors, numbers))
    return results


if __name__ == "__main__":
    
    # спочатку перевіряємо швидкість виконання в 1 потік
    start = perf_counter()
    a, b, c, d  = factorize(128, 255, 99999, 10651060)

    assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]

    end = perf_counter()
    print(f"Час виконання в 1 потік: {end - start:.6f} секунд")

    # тепер перевіряємо швидкість виконання в багато потоків
    start = perf_counter()
    a, b, c, d = factorize_multithread(128, 255, 99999, 10651060, workers=cpu_count())

    assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]

    end = perf_counter()
    print(f"Час виконання в {cpu_count()} потоків: {end - start:.6f} секунд")
