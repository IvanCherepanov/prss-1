import math


def task_28(x: int, y: int):
    return math.asin(x + y)


def task_1(a: int, b: int, c: int, d: int):
    return (a <= c and b <= d) or (b <= c and a <= d)


def task_4(a1: float, a2: float, a3: float):
    c = math.sqrt(a1 + a2)
    b = a1 + 0.7 * a3
    return 0 <= c <= 5 and 0 <= b <= 10


def task_7(x: float, y: float):
    return math.log(x - y) - x / y


def task_10(a: int, b: int, c: int):
    if a >= b and a >= c and b >= c:
        return c, b, a
    elif a <= b and a >= c and b >= c:
        return c, a, b
    elif a <= b and a <= c and b <= c:
        return a, b, c
    elif a >= b and a >= c and b <= c:
        return b, c, a
    elif a >= b and a <= c and b <= c:
        return b, a, c
    else:
        return a, c, b
