# Looking at Consecutive Elements of an Iterable - Easy

Oftentimes, problems may require us to look at consecutive elements of an iterable to determine an answer. This section will go through the easier way to do this, with indices (indexes).

---

## Using `enumerate`

Since the `enumerate` function gives us access to an index as we move through the list, we can use basic algebra like `index - 1` to represent the previous element in an iterable. This would look something like this:

```python
my_list = [1, 2, 3, 4, 5, 6, 7]
count = 0
for pos, item in enumerate(my_list):
    if item == my_list[pos - 1]:
        count += 1
print(count)
```

This loop counts how many consecutive pairs of elements are equal. It starts by comparing the first element to the last (offering a wrap-around effect), as the first index is 0, so `pos - 1` is -1, which represents the last index. In this case, no consecutive pair is equal (`1, 7; 2, 1; 3, 2; 4, 3; 5, 4; 6, 5; 7, 6`), so the result is:

```
0
```

---

## Getting a set of three consecutive elements

Using the same technique, we could check a set of three consecutive elements using `pos`, `pos - 1`, and `pos - 2`:

```python
my_list = [1, 2, 3, 4, 5, 6, 7]
count = 0
for pos, item in enumerate(my_list):
    if item + my_list[pos - 1] + my_list[pos - 2] > 10:
        count += 1
print(count)
```

This time, we add sets of three consecutive elements together and check how many of these sets add up to be greater than 10. These sets would be `1, 7, 6; 2, 1, 7; 3, 2, 1; 4, 3, 2; 5, 4, 3; 6, 5, 4; 7, 6, 5`, and in this case we expect 4 of them to add up to be greater than 10, resulting in the output:

```
4
```