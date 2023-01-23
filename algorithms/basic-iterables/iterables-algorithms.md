# Iterables Algorithms

When using iterables, there are a few algorithms that are needed frequently, so I wanted to address some basics here.

---

## Checking if a Value is Present in an Iterable

Sometimes we want to know if a certain value appears in an iterable (note that if we wanted to know how many times it shows up, we could use the `count()` function for lists). Often though, we just care if it is in the iterable, `True`, or if it is not, `False`. To do this, we have a simplified process using the keyword `in`:

```python
my_list = [12, 15, 11, 16, 18, 14]
print(11 in my_list)
print(10 in my_list)
```

This produces the following output:

```
True
False
```

All we need is to write the value we are looking for, and `in iterable` to see if it is present, and it returns a boolean value for us to use if we need it. This works on all types, not just numbers!

---

## Looping Through an Iterable with Indices (Index) Available

Often we might want to loop through an iterable, but want access to the index (i.e. position) we are currently on. To do this, we introduce the `enumerate()` function. Our traditional for loop to go through an iterable would look like this:

```python
my_list = [12, 15, 11, 16, 18, 14]
for item in my_list:
```

Unfortunately, this does not let us see which index we are currently looking at. Using `enumerate(iterable)`, we can get access to that as well:

```python
my_list = [12, 15, 11, 16, 18, 14]
for pos, item in enumerate(my_list):
```

Note now that we have two variables in our loop: `pos` and `item`. The first variable (regardless of name, in this case `pos`), will always represent the index of the current item (starting from 0). The second variable (regardless of name, in this case, `item`) will always represent the current value in the list (i.e., 12, 15, etc.).

Now if we wanted to know where a certain element shows up, we could do the following:

```python
my_list = [12, 15, 11, 16, 18, 14]
for pos, item in enumerate(my_list):
    if item == 15:
        print(pos)
```

This produces the output:

```
1
```

This small loop will now print the index of each time the value `15` shows up in our list!