# `for` Loops

`for` loops offer us a way to repeat an action(s) several times.

All of the sample code provided in this file is in the for.py Python file for you to run, modify, and otherwise investigate.

---

## Most basic `for` loops

A `for` loop needs an iterable to go through and perform actions. This could be any type of iterable we've covered. Most simply, we can just use a `tuple` with counting numbers:

```python
for x in (0, 1, 2):
    print(x)
```

This produces the output:

```
0
1
2
```

The `for` loop goes through each element of the iterable and assigns it to the provided temporary variable name `x` (note that this could be any variable name that's not already in use). It goes through the elements in the order they are in the iterable.

Just like the conditionals, the colon `:` plays a key role by telling Python that the following instructions should be indented and performed within the context of the loop. After you are done with writing the actions in a loop, you just need to remove the indent on future code and it will happen after the loop.

Unfortunately, writing out a `tuple` with counting numbers is cumbersome and becomes ineffective as you need a loop to perform more iterations. Fortunately, we have a tool to help with this: the `range()` function

---

## `range()`

To more effectively use a basic for loop, we'll want to utilize the `range()` function.

The `range()` can take in a few different sets of arguments:

- The most simple is a single integer, which tells it to count from zero, up until just before the number provided. For example:

```python
print(list(range(5))) # Should turn the numbers from 0 to 4 into a list
```

This produces the output:

```
[0, 1, 2, 3, 4]
```

- We could provide two integers, which tells it to count from the first number to just before the second number. For example:

```python
print(list(range(3, 8))) # This should turn the numbers from 3 to 7 into a list
```

This produces the output:

```
[3, 4, 5, 6, 7]
```

- Finally, we can give three integers, which functions like two integers with the final argument giving a step size (how much to increase between each number, the default is 1!). For example:

```python
print(list(range(1, 10, 2))) # This should turn the odd numbers from 1 to 10 into a list
# It starts at 1, and adds 2 each time until it would hit 10 (or higher)
```

This produces the output:

```
[1, 3, 5, 7, 9]
```

The `range()` function gives us easy ways to control a for loop by performing a certain number of iterations (especially in the one integer parameter case). A basic use of the range function could expand our original for loop to provide more numbers very easily:

```python
for x in range(5):
    print(x)
```

This produces the output:

```
0
1
2
3
4
```

---

## Simple Iterable Indexing

We could also use our `range()` function to print information about elements of an iterable via their index, since range and index both start at 0!

Given we have some iterable:

```python
mylist = [3, 7, 2, 4, 0]
```

We could have range make a list of indices as long as our list using the `len()` function:

```python
for x in range(mylist.len()):
    print(mylist[x])
```

This produces the output:

```python
3
7
2
4
0
```

In Python, this is not considered to be as effective as it would be in other programming languages. To to do this better, we'll look at for each loops.
