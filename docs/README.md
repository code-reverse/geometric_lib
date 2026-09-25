# Math formulas
## Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²

## Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a

# Usage examples

## circle

```python
from geometric_lib import circle

# Calculate area and perimeter for circle
circle.area(5)          # 78.539...
circle.perimeter(5)     # 31.415...
```

## rectangle

```python
from geometric_lib import rectangle

# Calculate area and perimeter for rectangle
rectangle.area(3, 4)       # 12
rectangle.perimeter(3, 4)  # 14
```

## square

```python
from geometric_lib import square

# Calculate area and perimeter for square
square.area(5)       # 25
square.perimeter(5)  # 20
```

## triangle

```python
from geometric_lib import triangle

# Calculate area and perimeter for triangle
triangle.area(6, 4)       # 12.0
triangle.perimeter(3,4,5) # 12
```