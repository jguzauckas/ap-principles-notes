# `Handling`

When we deal with exceptions in code in ways that prevents them from disrupting the program running, we call it **handling**

Unfortunately, `raise` doesn't stop the exception from causing problems, it just helps us highlight where we expect them to come up. To handle them, we use `try`.

All of the sample code provided in this file is in the raise.py Python file for you to run, modify, and otherwise investigate.

---

## `try`-`except`

Just like in English we would say to "try" something even if we don't expect it to work, we use `try` in Python to have the program attempt to execute some code, but be prepared for there to be issues.

`try` cannot be used on its own though, and must be followed by something, traditionally `except`, where we highlight what exception might come up and what to do in that context.

Here is a code segment that demonstrates a basic `try`-`except` block:

```python
def divide(a: int, b: int) -> float:
    try:
        return a / b
    except Exception:
        print("There was an error")


print(divide(1, 0))
print(divide(2, 1))
```

This produces the output:

```
There was an error
None
2.0
```

Whereas before a call to divide by zero would halt the program, now it is caught and addressed, and the program can continue on to do a second division that it has no problems with.

Notice that it prints out `None` for `divide(1, 0)`, as it stops the `return` from happening with the `except` line and therefore has no return type.

We also notice that we don't get as much detailed information as a `raised` exception from before, in this case we don't even know what kind of exception came up! This can be fixed though.

---

## Specific `except` Exceptions

Like with `raise`, we might often have an idea about what exception might come up when we use `try`-`except`, and we have syntax to allow us to be more specific:

```python
def divide(a: int, b: int) -> float:
    try:
        return a / b
    except ZeroDivisionError as zde:
        print(zde)


print(divide(1, 0))
print(divide(2, 1))
```

This produces the output:

```
division by zero
None
2.0
```

The only thing that has changed from our previous example was our `except` section, where we now offer a type of exception and use the `as` keyword to give it a temporary name to refer to the found exception: in this case, `zde`.

---

## Multiple `except`s

Sometimes we might be worried about multiple types of exceptions coming up in a block, and so we can use more than one `except` to prepare for them:

```python
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
```

This produces the output:

```
division by zero
None
2.0
```

The output has not changed from our previous example, but our block is now resilient to multiple exceptions: namely `ZeroDivisionError` and `OverflowError`. Additionally, we can also have a general `except` at the end to handle any other exceptions that pop up.

---

## `raise` in `except`

If we feel an exception is important enough to stop the program, we can still use the `raise` keyword, and its even simpler to use than before:

```python
def divide(a: int, b: int) -> float:
    try:
        return a / b
    except ZeroDivisionError as zde:
        print(zde)
        raise


print(divide(1, 0))
print(divide(2, 1))
```

This produces the output:

```
division by zero
Traceback (most recent call last):
  File "c:\Users\john\exceptions\handling.py", line 46, in <module>
    print(divide(1, 0))
  File "c:\Users\john\exceptions\handling.py", line 40, in divide
    return a / b
ZeroDivisionError: division by zero
```

Notice that to raise the correct exception, we didn't have to put anything after `raise`. Due to the `except` block, `raise` has context for the exception.

---

## `else`

We can follow our `try`-`except` with `else` to give further instructions in the event that there were no exceptions that came up. This allows us to only put the worrisome code in the `try` section and put any additional steps later on. Here is an example:

```python
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
```

This produces the output:

```
division by zero
The result was 2.0
```

Most importantly, this allows us to make it clear what code we are worried about throwing exceptions and isolate it in the `try` section, so that the `except` information can directly follow.

Placing everything else that would happen after in `else` declutters the initial `try` and makes clear what will happen when an exception is not hit.
