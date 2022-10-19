def divide(a: int, b: int) -> float:
    try:
        return a / b
    except Exception:
        print("There was an error")


print(divide(1, 0))
print(divide(2, 1))


def divide(a: int, b: int) -> float:
    try:
        return a / b
    except ZeroDivisionError as zde:
        print(zde)


print(divide(1, 0))
print(divide(2, 1))


def divide(a: int, b: int) -> float:
    try:
        return a / b
    except ZeroDivisionError as zde:
        print(zde)
    except OverflowError as ofe:
        print(ofe)
    except Exception:
        print("Some other error happened")


print(divide(1, 0))
print(divide(2, 1))


def divide(a: int, b: int) -> float:
    try:
        return a / b
    except ZeroDivisionError as zde:
        print(zde)
        raise


print(divide(1, 0))
print(divide(2, 1))


def divide(a: int, b: int) -> float:
    try:
        result = a / b
    except ZeroDivisionError as zde:
        print(zde)
    else:
        print(f"The result was {result}")
        return result


divide(1, 0)
divide(2, 1)
