def divide(a: int, b: int) -> float:
    if b == 0:
        raise ZeroDivisionError("We can't divide by zero")
    return a / b


c = divide(5, 0)

lst = ["a", "b", "c", "d", "e"]
print(lst[10])

dct = {"a": 1, "b": 2, "c": 3}
print(dct["d"])

# print(name)

num = 2.5**1000000

num = 2 / "Hello"

import math

math.sqrt(-1)

5 / 0
