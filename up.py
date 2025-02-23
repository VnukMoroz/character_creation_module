
from math import sqrt


message = ('Добро пожаловать в самую лучшую программу для вычисления'
           'квадратного корня из заданного числа')

print(message)


def Calculate_Square_Root(Number):
    """Вычисляет квадратный корень
    """
    return sqrt(Number)


def calc(your_number):
    """
    Вычисляет квадратный корень
    """
    if your_number <= 0:
        return
    root = 0

    print(f'Мы вычислили квадратный корень из введённого вами числа.'
          f' Это будет: {calc(your_number)}')


print(message)

calc(25.5)