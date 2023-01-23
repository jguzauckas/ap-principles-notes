# Statistics Module

Oftentimes when we have a set of numbers we want to do some basic statistics on them. With our new tools from last class, like the `sum` function, this has gotten easier, but the statistics module can make this process even more straight-forward.

---

## `import statistics`

Since this is a module, we need to import `statistics` for our use in a program. The word 'statistics' is a mouthful, we'll use our `as` keyword to give it a shorter name for use in our program, which is typically `stats`, so it would look like:

```python
import statistics as stats
```

---

## `mean`

First method up is taking an average, or mean, of a set of numbers. To do this, we use the `stats.mean()` method, where all we need is to give it an iterable of numbers to calculate with:

```python
my_list = [14, 13, 13, 15, 16, 18, 20]
print(stats.mean(my_list))
```

This will produce the following output:

```
15.571428571428571
```

---

## `median`

Our next measure of center is the median method. Median finds the middle number in a set of numbers, which helps to eliminate the problems outliers would cause in an average. This works much the same as the mean, so it is `stats.median()`, where you give it an iterable of numbers to work on:

```python
my_list = [14, 13, 13, 15, 16, 18, 20]
print(stats.median(my_list))
```

This produces the following output:

```
15
```

---

## `mode`

Our final measure of center is the mode function, which finds the most common value in a set of numbers. Again much like our previous two functions, we use `stats.mode()` where we give it an iterable of numbers to work with:

```python
my_list = [14, 13, 13, 15, 16, 18, 20]
print(stats.mode(my_list))
```

This produces the following output:

```
13
```
