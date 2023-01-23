# Iterables Methods

Python has several functions built-in that work on iterables to produce helpful/common results.

---

## Sum

When we want to know the sum of the values in an iterable (of any type), we can just use the `sum()` function. Placing your iterable in the parentheses will run the function on your iterable and calculate the sum. Here is how we traditionally calculated the sum:

```python
my_list = [12, 15, 11, 16, 18, 14]
total = 0
for item in my_list:
    total += item
print(total)
```

Now with our new method:

```python
my_list = [12, 15, 11, 16, 18, 14]
print(sum(my_list))
```

These both produce the following output:

```
86
```

This will work on all of our iterable types so far, and offer a new easy way to get a total from a list.

---

## Maximum and Minimum

When we want to know the biggest or smallest values in an iterable, the `max()` and `min()` functions offer a simple solution. Just like `sum()`, placing your iterable in the parentheses will run the functions on your iterable and find the maximum or minimum value of the iterable, respectively. Here is how we traditionally found maximums and minimums:

```python
my_list = [12, 15, 11, 16, 18, 14]
maximum = 0
minimum = 100
for item in my_list:
    if item > maximum:
        maximum = item
    elif item < minimum:
        minimum = item
print(maximum)
print(minimum)
```

```python
my_list = [12, 15, 11, 16, 18, 14]
print(max(my_list))
print(min(my_list))
```

These both produce the following output:

```
18
11
```

Both of these functions offer simplified ways of finding these important values, which we often need to do!
