# List Methods

While we've gone over the basics of lists, there are a couple more methods that lists have that could make our lives a lot easier.

---

## Count

One useful method is the `count()` method, which will check the list for how many values are equal to a provided input and return how many were.

For example, let's say we have a list of integers and want to know how many times the number 13 shows up in the list. Our traditional method of counting would look like this:

```python
my_list = [12, 13, 13, 14]
count = 0
for item in my_list:
    if item == 13:
        count += 1
print(count)
```

Now we can simplify this down to:

```python
my_list = [12, 13, 13, 14]
print(my_list.count(13))
```

Both of these segments will produce the following output:

```
2
```

Note that this works on any types, here is an example with strings:

```python
my_list = ["hello", "hi", "howdy", "hi"]
print(my_list.count("hi"))
```

As long as you put the thing you want to look for inside of the `count` parentheses, it will check how many times it shows up in the list!

---

## Sort

The other useful method is `sort()`, which is especially useful when we are working with numbers.

When applied to a list, `sort()` will automatically sort the list in ascending order (that is, the lowest value will be in the first slot, and the highest value will be in the last slot):

```python
my_list = [12, 15, 11, 16, 18, 14]
my_list.sort()
print(my_list)
```

Note that there are no arguments in the parentheses. This produces the output:

```
[11, 12, 14, 15, 16, 18]
```

If we want to sort in descending order (that is, the highest value will be in the first slot, and the lowest value will be in the last slot), we now put a `reverse=True` in the parentheses:

```python
my_list = [12, 15, 11, 16, 18, 14]
my_list.sort(reverse=True)
print(my_list)
```

This produces the output:

```
[18, 16, 15, 14, 12, 11]
```

Sorting can be useful because we know what is at the beginning/end of the list: the biggest and smallest values. If we wanted the three largest values, we could just sort the list in descending order and print out the first three indices in the list.
