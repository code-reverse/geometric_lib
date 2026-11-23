
def area(a):
    '''
    Считает площадь квадрата
        Принимает:
            a (int): длинна стороны квадрата
        Возвращает: 
            s (int): площадь квадрата
    '''
    if not isinstance(a, int):
        raise ValueError("Invalid input data type, expected integer")
    if a<=0:
        raise ValueError("Input data must be > 0")
    return a * a


def perimeter(a):
    '''
    Считает периметр квадрата
        Принимает:
            a (int): длинна стороны квадрата
        Возвращает: 
            p (int): периметр квадрата
    '''
    if not isinstance(a, int):
        raise ValueError("Invalid input data type, expected integer")
    if a<=0:
        raise ValueError("Input data must be > 0")
    return 4 * a
