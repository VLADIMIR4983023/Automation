import math


def square(side):
    area = side * side
    if not isinstance(area, int):
        area = math.ceil(area)
    return area


side_length = 5.5
square_area = square(side_length)
print(f"Площадь квадрата со стороной {side_length}: {square_area}")
