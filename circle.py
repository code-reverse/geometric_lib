import math


def area(r):
    '''
    Считает площадь окружности
        Принимает:
            r (int): радиус окружности
        Возвращает: 
            s (float): площадь окружности
    '''
    if not isinstance(r, int):
        raise ValueError("Invalid input data type, expected integer")
    if r<=0:
        raise ValueError("Input data must be > 0")
    return math.pi * r * r


def perimeter(r):
    '''
    Считает длинну окружности
        Принимает:
            r (int): радиус окружности
        Возвращает: 
            p (float): длинну окружности
    '''
    if not isinstance(r, int):
        raise ValueError("Invalid input data type, expected integer")
    if r<=0:
        raise ValueError("Input data must be > 0")
    return 2 * math.pi * r

