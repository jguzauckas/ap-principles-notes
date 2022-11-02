# `random` Module

The `random` module in Python is a basic module that offers some random generation for numbers that are not otherwise available in Python. In this section, we'll look through some of the opportunities that `random` provides to us.

All of the sample code provided in this file is in the random-samples.py Python file for you to run, modify, and otherwise investigate.

---

## `import random`

As with any module, our first step to utilizing it is to `import` it!

```python
import random
```

---

## `random()`

The only function we will touch on from the `random` module is the `random()` function, which generates a random number between `0.0` and `1.0` (it could be `0.0`, it cannot be `1.0`, so essentially `0.0` to `0.999...`). The `random()` function doesn't take any parameters, so you just use the empty parentheses:

```python
print(f"Your random number is {random.random()}")
```

When I ran this program, it produced the output:

```
Your random number is 0.6327980898772724
```

Running it again, I get:

```
Your random number is 0.8237904105584828
```

An important trait about the `random` module is that these results will change each time you run the program!

---

## `randint()`

When we look to use random numbers, often we are looking for a random integer, not a float. This is the use of `randint()`, which takes in two arguments: a minimum and a maximum value. To be more precise, this function returns a random integer between the minimum and maximum (and could be equal to the minumum or the maximum).

Let's find a random number from 1 to 10:

```python
print(f"A random number from 1 to 10 is {random.randint(1, 10)}")
```

The first time I ran it, I got:

```
A random number from 1 to 10 is 9
```

The second time I got:

```
A random number from 1 to 10 is 10
```

---

To learn more about everything offered by the `random` module in Python, check out the official documentation [here](https://docs.python.org/3/library/random.html).
