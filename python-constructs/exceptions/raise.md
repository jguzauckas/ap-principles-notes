# Raising Exceptions

When an exception comes up in a problem, we say that an exception has been `raised`, or brought up.

In this section, we will talk about how to `raise` exceptions ourselves, to preempt issues that could come up in our code.

All of the sample code provided in this file is in the raise.py Python file for you to run, modify, and otherwise investigate.

---

## `raise`

In Python, we have the keyword `raise` to initiate a reference to a type of exception. Raising an exception ourselves helps to pinpoint where issues come up, as we've tried to predict them in advance. Here is an example where we `raise` a `ZeroDivisionError`:

```python
def divide(a: int, b: int) -> float:
    if b == 0:
        raise ZeroDivisionError("We can't divide by zero")
    return a / b


c = divide(5, 0)
```

This produces the output:

```
Traceback (most recent call last):
  File "c:\Users\john\exceptions\raise.py", line 7, in <module>
    c = divide(5, 0)
  File "c:\Users\john\exceptions\raise.py", line 3, in divide
    raise ZeroDivisionError("We can't divide by zero")
ZeroDivisionError: We can't divide by zero
```

On the one hand, this doesn't look much different from our previous examples raising a `ZeroDivisionError`, but we were prepared for the exception to come up and even left a personalized message to go with this exception type this time. With any exception type, you can provide a message to pass to the user when the exception is raised just by putting a `str` in the exception.

---

## Types of Exceptions

There are many types of exceptions that come up and cause errors. In this section, we'll discuss `IndexError`, `KeyError`, `NameError`, `OverflowError`, `TypeError`, `ValueError`, and `ZeroDivisionError`.

### `IndexError`

An `IndexError` occurs when you try to use an index that is not within the bounds of an iterable, like trying to take the 10th element of a list that only has 5 objects. Here is an example that would cause an `IndexError`:

```python
lst = ["a", "b", "c", "d", "e"]
print(lst[10])
```

This produces the output:

```
Traceback (most recent call last):
  File "c:\Users\john\exceptions\raise.py", line 10, in <module>
    print(lst[10])
IndexError: list index out of range
```

### `KeyError`

A `KeyError` is an exception like `IndexError` but for dictionaries, as they use `keys` instead of `indices`. This occurs when you try to access a key that doesn't exist currently. Here is an example that would cause a `KeyError`:

```python
dct = {"a": 1, "b": 2, "c": 3}
print(dct["d"])
```

This produces the output:

```
Traceback (most recent call last):
  File "c:\Users\john\exceptions\raise.py", line 13, in <module>
    print(dct["d"])
KeyError: 'd'
```

### `NameError`

A `NameError` occurs when you try to utilize a local or global `name` that Python doesn't know about. In this case `name` could be a variable or other kind of object that we would refer to via a name. Here is an example that would cause a `NameError`:

```python
print(name)
```

This produces the output:

```
Traceback (most recent call last):
  File "c:\Users\john\exceptions\raise.py", line 15, in <module>
    print(name)
NameError: name 'name' is not defined
```

### `OverflowError`

An `OverflowError` occurs when an arithmetic operation produces a value too large for the computer to represent. In other languages, this could occur with `integers` or `floats`, but due to how Python handles `integers` (dynamically using more storage as needed), this exception will only occur with `floats`, and even then, it can be hard to get a number that high. Here is an example that would cause an `OverflowError`:

```python
num = 2.5**1000000
```

This produces the output:

```
Traceback (most recent call last):
  File "c:\Users\john\exceptions\raise.py", line 17, in <module>
    num = 2.5**1000000
OverflowError: (34, 'Result too large')
```

### `TypeError`

A `TypeError` occurs when you attempt to perform operations on incompatible types. Here is an example that would cause a `TypeError`:

```python
num = 2 / "Hello"
```

This produces the output:

```
Traceback (most recent call last):
  File "c:\Users\john\exceptions\raise.py", line 19, in <module>
    num = 2 / "Hello"
TypeError: unsupported operand type(s) for /: 'int' and 'str'
```

### `ValueError`

A `ValueError` occurs when an operation or function receives a value of the correct type, but an innappropriate value to perform its job. Here is an example that would case a `ValueError`:

```python
import math

math.sqrt(-1)
```

This produces the output:

```
Traceback (most recent call last):
  File "c:\Users\john\exceptions\raise.py", line 23, in <module>
    math.sqrt(-1)
ValueError: math domain error
```

In this case, we pass an integer into the square root function, which is the correct type, but it has a negative value, which the function cannot work with.

### `ZeroDivisionError`

A `ZeroDivisionError` occurs when the program tries to divide by zero. Here is an example of a `ZeroDivisionError`:

```python
5 / 0
```

This produces the output:

```
Traceback (most recent call last):
  File "c:\Users\john\exceptions\raise.py", line 25, in <module>
    5 / 0
ZeroDivisionError: division by zero
```

---

Any of these exception types can be brought up manually using our `raise` keyword, when we might expect problems in certain contexts.
