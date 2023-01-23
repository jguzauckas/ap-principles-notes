# Looking at Consecutive Elements of an Iterable - Advanced

Oftentimes, problems may require us to look at consecutive elements of an iterable to determine an answer. This section will go through the more complex, but more powerful way to do this, with the `zip()` function.

---

## Using `zip`

The `zip()` function takes in multiple iterables and returns a `zip` object, which is an iterable that holds tuples. The tuples hold matched up elements from the multiple iterables passed in.

For example, given the following three lists, zip produces the following result:

```python
list1 = [1, 2, 3, 4, 5, 6]
list2 = [2, 4, 6, 8, 10, 12]
list3 = [3, 6, 9, 12, 15, 18]
print(list(zip(list1, list2, list3)))
```

This produces the following output:

```
[(1, 2, 3), (2, 4, 6), (3, 6, 9), (4, 8, 12), (5, 10, 15), (6, 12, 18)]
```

We can see that this combines all of the first elements into one tuple, all of the second elements into the next, and so on.

---

## Combining Elements of the Same Iterable

Just like the simple method, we want to combine consecutive pairs of elements from the same iterables. We can do this through the use of slicing, just like we were using with strings earlier in the year. Here is an example where we get the pairs of consecutive elements from a list:

```python
list1 = [1, 2, 3, 4, 5, 6]
print(list(zip(list1, list1[1:])))
```

Notice here that the first `zip()` argument is just the original `list1`, and the second argument is `list1` that has been sliced to start at the second element and continue to the end. This produces the following result:

```
[(1, 2), (2, 3), (3, 4), (4, 5), (5, 6)]
```

We do have a problem here though, which is that if we needed to, this does not wrap around and collect the pair `(6, 1)` like our simpler method did. To do this, we can use the `+` operator with lists to combine them temporarily.

To work this out, note that we need our second argument that was sliced to loop back around and grab the first element at the end. This is what the result would look like:

```python
list1 = [1, 2, 3, 4, 5, 6]
print(list(zip(list1, list1[1:] + [list1[0]])))
```

Notice that the `list1[0]` is in its own set of brackets. This is so Python treats it as a list of one element, and can add it to `list1[1:]` without issue. This produces the following output:

```
[(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 1)]
```

---

## Using in Loops

Since the `zip()` function creates an iterable of tuples, we can use multiple arguments in the loop to get the individual value from those tuples, much like we used to use `pos, item` to get the position and value of an item from `enumerate()`. Here is an example of what it would look like:

```python
list1 = [1, 2, 3, 4, 5, 6]
count = 0
for first, second in zip(list1, list1[1:] + [list1[0]]):
    if first == second:
        count += 1
print(count)
```

While the `for` loop line is a little bit more difficult to write, it can save us a lot of time inside of the loop later on since we don't have to deal with indices (indexes).

Note that if we ever need indices, we can pair this with enumerate to get three numbers, a position, and two values:

```python
list1 = [1, 2, 3, 4, 5, 6]
count = 0
for pos, (first, second) in enumerate(zip(list1, list1[1:] + [list1[0]])):
    if first == second:
        count += 1
print(count)
```

Note the `(first, second)` in the loop declaration. This is because zip creates tuples and then we pair an index with them, so we have to acknowledge that the information is in the form of an integer (index) and two integers in a tuple.

---

## Brief example with three elements

Three elements with zip works similarly, but requires some additional thinking about how we combine our list into one bigger set:

```python
list1 = [1, 2, 3, 4, 5, 6]
count = 0
for first, second, third in zip(list1, list1[1:] + [list1[0]], list1[2:] + list1[:2]):
    if first + second + third > 10:
        count += 1
print(count)
```

Notice that my third argument in `zip()` has a slice of `list1` starting at the third element, and adds on the first two elements via another slice afterwards (even though 2 is the third element, slicing stops before the index given!).
