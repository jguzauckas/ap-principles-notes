# Improving Function Readability

Functions are used all the time, and we want to make sure everyone (including ourselves) are able to quickly and easily identify what a function does, and what information it works with.

All of the sample code provided in this file is in the function-readability.py Python file for you to run, modify, and otherwise investigate.

---

## Type Hints

While Python is not as restrictive as other programming languages in the sense that we do not have to declare the types of the parameters of a function, or its output, it does have **type hints** which allow us label what types we _expect_ something to have to help readers understand the intention behind some code.

Let's start with a function in the style we previously wrote in:

```python
def fullname(first, last):
    return first + " " + last
```

While it is short and concise, it would help to make it clear what types of information we are working with. First, let's _hint_ at the types of our parameters using the colon `:` operator:

```python
def fullname(first: str, last: str):
    return first + " " + last
```

Here, our parameter names have not changed from the previous function, and after the colon we offer a suggestion as to what type we expect to be passed in, in this case `str`. Note that we hint at each parameter's type, and could easily have parameters of different types in the same function!

Now, we can also make it more clear what type we expect the function to return using the `->` operator after our function's name:

```python
def fullname(first: str, last: str) -> str:
    return first + " " + last
```

Note that ` -> str` comes before our colon `:`. In this case, we are saying that the expected output of `fullname` is of the type `str`, which is useful for situations where something might need to be programmed based on the expected return type.

It can also be important to highlight when a function doesn't return anything (think of our basic examples with just some basic `print()` statements). To note this, we use the keyword `None` in place of a type after the arrow:

```python
def hello(name: str) -> None:
    print(f"Hello {name}!")
```

This helps others (and you in the future) to quickly understand that the function doesn't return anything without having to look through the body of it.
