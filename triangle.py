def area(a, h): 
    '''
    Считает площадь треугольника
        Параметры:
            a (int): длинна стороны
            h (int): высота проведенная из вершины в a

        Возвращаемое значение:
            s (float): площадь треугольника
    '''
    if not isinstance(a, int) or not isinstance(h, int):
        raise ValueError("Invalid input data type, expected integer")
    if a<=0 or h<=0:
        raise ValueError("Input data must be > 0")
    return a * h / 2 

def perimeter(a, b, c): 
    '''
    Считает периметр треугольника
        Парамеры:
            a (int): первая сторона треугольника
            b (int): вторая сторона треугольника
            c (int): третья сторона треугольника

        Возвращаемое значение:
            p (int): периметр треугольника
    '''
    if not isinstance(a, int) or not isinstance(b, int) or not isinstance(c, int):
        raise ValueError("Invalid input data type, expected integer")
    if a+b <= c or a+c <= b or b+c <= a:
        raise ValueError("Invalid input triangle, expected")
    if a<=0 or b<=0 or c<=0:
        raise ValueError("Input data must be > 0")
    return a + b + c 
