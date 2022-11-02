# `math` Module

The `math` module in Python is a basic module that offers a lot of useful mathemtical functions that are not otherwise available in Python. In this section, we'll look through some of the opportunities that `math` provides to us.

All of the sample code provided in this file is in the math-samples.py Python file for you to run, modify, and otherwise investigate.

---

## `import math`

As with any module, our first step to utilizing it is to `import` it!

```python
import math
```

---

## `ceil()` and `floor()`

The ceiling and floor functions in mathematics represent types of rounding of decimal numbers to integers. To put it most simply, ceiling always rounds up, and floor always rounds down.

To be more precise, ceiling will return the smallest integer greater than or equal to the input number. This means that no matter how close the number would be to traditionally rounding down, we will still go up. Here is example use of the `ceil()` function:

```python
print(math.ceil(5))
print(math.ceil(4.9))
print(math.ceil(4.5))
print(math.ceil(4.1))
print(math.ceil(4))
```

This produces the output:

```
5
5
5
5
4
```

Here we can see that `5`, `4.9`, `4.5`, and `4.1` all round up to `5`, while `4` doesn't go up to the "or equal to" nature of the function.

Floor works similarly with rounding down, defined as the largest integer less than or equal to the input number. This means that no matter how close the number would be to traditionally rounding up, we will still go down. Here is example use of the `floor()` function:

```python
print(math.floor(5))
print(math.floor(4.9))
print(math.floor(4.5))
print(math.floor(4.1))
print(math.floor(4))
```

This produces the output:

```
5
4
4
4
4
```

Here we can see that the result is very much "opposite" to ceiling, so `4.9`, `4.5`, `4.1`, and `4` all round down to `4`, while `5` doesn't go down to the "or equal to" nature of the function.

---

## `fsum()`

In previous projects, we've used loops to go through a list of numbers and add them all together (think of when we calculated averages!). The `fsum` function takes in an iterable as an input, and automatically adds all of the values together for us!

As an example of what this could look like let's define a list called `grades` with 10 scores in it:

```python
grades = [90, 100, 92, 83, 67, 70, 75, 94, 96, 89]
```

Here is the traditional way we would have calculated the average grade with our tools:

```python
sum = 0
for grade in grades:
    sum += grade
print(f"The average grade is {sum / len(grades):.2f}")
```

The `for` loop goes through and adds each grade in the list to a running total called `sum`, which we at the end divide by the length of `grades` (the number of grades) to calculate an average. This produces the output:

```
The average grade is 85.60
```

Now using `fsum`, we can calculate the sum of all of the grades in one line instead of multiple lines with a `for` loop:

```python
sum = math.fsum(grades)
print(f"The average grade is {sum / len(grades):.2f}")
```

This produces the output:

```
The average grade is 85.60
```

Helping to demonstrate this works, we got the same output! `fsum` can be used with any iterable of numerical values to find a total sum of all of the values!

---

## `prod()`

Similar to `fsum`, we can also find the product (multiplication) of all of the values in an iterable! While this is often less useful, it works very similarly. Taking our grades from above, let's look at how we would have previously calculated the product of all of the values:

```python
product = 1
for grade in grades:
    product *= grade
print(f"The product of all the grades is {product:,}")
```

Note that we start `product` at `1`, while we started `sum` at `0`! Using the `prod()` function, we simplify it similarly:

```python
product = math.prod(grades)
print(f"The product of all the grades is {product:,}")
```

Both of these produce the output:

```
The product of all the grades is 19,414,742,219,712,000,000
```

---

## `factorial()`

One final mathematical function we will look at is the factorial. In real mathematics we use the exclamation point `!` to represent taking the factorial of an integer. Taking the factorial of an integer is multiplying it by every integer below it, all the way down to `1`.

For example, to calculate `3!`, which we would say as "three factorial", we multiply `3 * 2 * 1` to get `6`. For small integers, this is fairly easy, but for larger numbers, even like `20`, it gets much more difficult. Let's make Python do it for us:

```python
print(f"20! = {math.factorial(20):,}")
```

This produces the output:

```
20! = 2,432,902,008,176,640,000
```

---

## `pi`

Some mathematical constants are really long and complex decimals. We might want to use them in our programs, so the `math` module offers them to us as constants for us to utilize. The one we will look at is `pi`, which we know traditionally is equal to about `3.14...`. To access it, we just use `math.pi`. Let's calculate the area of a circle as an example:

```python
print(f"The area of a circle with a radius of 5 is {math.pi * 5 ** 2:.2f}")
```

This produces the output:

```
The area of a circle with a radius of 5 is 78.54
```

---

To learn more about everything offered by the `math` module in Python, check out the official documentation [here](https://docs.python.org/3/library/math.html).
