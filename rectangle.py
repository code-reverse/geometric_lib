def area(a, b): 
    '''
    Считает площадь прямоугольника
        Принимает:
            a (int): первая сторона прямоугольника
            b (int): вторая сторона прямоугольника
        Возвращает:
            s (int): площадь прямоугольника
    '''
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Invalid input data type, expected integer")
    if a<=0 or b<=0:
        raise ValueError("Input data must be > 0")
    return a * b 

def perimeter(a, b): 
    '''
    Считает периметр прямоугольника
        Принимает:
            a (int): первая сторона прямоугольника
            b (int): вторая сторона прямоугольника
        Возвращает:
            p (int): периметр прямоугольника
    '''
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Invalid input data type, expected integer")
    if a<=0 or b<=0:
        raise ValueError("Input data must be > 0")
    return (a + b) * 2