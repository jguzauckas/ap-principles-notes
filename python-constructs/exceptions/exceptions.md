# Exceptions

In English, we always joke that there is an exception to every rule. In programming, we may have things that we don't want to happen in our code, things that a computer might not be able to do (i.e., divide by 0). We call these, `exception`s.

In Python, we call an exception that is detected during the execution of a program an `error`.

All of the sample code provided in this file is in the exceptions.py Python file for you to run, modify, and otherwise investigate.

---

## Automatic Errors

While we will be doing some work with using exceptions and errors ourselves, Python already does some of these automatically. Here is an example of code that causes an error:

```python
print("This is the first line")
a = 10 / 0
print("This is the third line")
```

This produces the output:

```
This is the first line
Traceback (most recent call last):
  File "c:\Users\john\exceptions\exceptions.py", line 2, in <module>
    a = 10 / 0
ZeroDivisionError: division by zero
```

We see that our first `print` statement works fine, but then we have a `traceback`.

A `traceback` is Python trying to tell us where an exception came up to cause the error. In this case, it is very simple, just on line 2 of this Python file where we try to do `a = 10 / 0`. Sometimes when we start involving classes and functions, these tracebacks can have more pieces too them, showing the chain of calls that led to the issue.

Finally, we have the last output line, which tells us about the type of error. There are a variety of included exception types in Python, some of which we'll discuss in detail in another section. In this case, we had a `ZeroDivisionError`, which is helpfully named, as it happens when you try to divide by 0. After the exception name, it also includes a brief description of the exception, which in this case is `division by zero`.

---

## Tracebacks

While we saw a basic example of a `traceback` before, let's take a closer look at a slightly more complex one to better understand the information it provides:

```python
def dividebyzero():
    return 1 / 0


print(dividebyzero())
```

This produces the output:

```
Traceback (most recent call last):
  File "c:\Users\john\exceptions\exceptions.py", line 10, in <module>
    print(dividebyzero())
  File "c:\Users\john\exceptions\exceptions.py", line 7, in dividebyzero
    return 1 / 0
ZeroDivisionError: division by zero
```

This `traceback` starts and ends the same way as our first example. It titles that this is a `traceback` so we know what we are reading, and ends with the type of exception, which in this case was again a `ZeroDivisionError`.

The difference is in the middle, as this time we have two parts rather than the one from before. Oftentimes an exception can come up after we've shifted through different parts of a program through classes and functions. To help us, a `traceback`, _traces_ our steps to get the point of causing the exception.

Reading from top to bottom, it tells us where we started in the program, and from there where that led us to an issue. The first reference is to line 10, where we made the call `print(dividebyzero())`. On its own, this line causes no issues, as our `print` and `dividebyzero` calls are written properly and will execute as they should. The problem with this line comes from the `return` of the `dividebyzero` function, which has a problem before it can return a value, resulting in our exception.

This leads into the second part, which references line 7 in `dividebyzero` (note that this is earlier in our code, as it has to move up to the `dividebyzero` function). This being the last step of the traceback, is where the actual exception comes up, as we try to do `1 / 0`.

`Tracebacks` are a tool for us to determine where issues in our code are and the problems they are causing so they can more easily be found and fixed.
