# `while` Loops

`while` loops are a different kind of loop that allow us to iterate a set of actions as long as a condition is fulfilled.

All of the sample code provided in this file is in the while.py Python file for you to run, modify, and otherwise investigate.

---

## Basic `while` Loop

Instead of iterating a certain number of times, a while loop checks a condition after each iteration. If the condition becomes `False`, the `while` loop exits, while if the `while` loop becomes `True`, it begins another iteration.

A basic `while` loop would look like this:

```python
n = 10
while n < 100:
    print(n)
    n *= 2
```

This produces the output:

```
10
20
40
80
```

This while loop checks if `n < 100` after each iteration. If it is less than 100, it does another iteration, and if it is not, it moves on. Each iteration, the loop prints the value of `n`, and then doubles and saves its value for the next iteration.

---

## `while` Loops with Iterables

`while` loops are often used to build iterables that meet certain criteria. Let's use a `while` loop to have the user put together a list of names:

```python
names = []
boolCheck = True
while boolCheck:
    name = input("Enter a name (or nothing to stop): ")
    boolCheck = bool(name)
    names.append(name)
print(names)
```

This produces the output:

```
Enter a name (or nothing to stop): John
Enter a name (or nothing to stop): Jacob
Enter a name (or nothing to stop): Jingleheimer
Enter a name (or nothing to stop): Schmidt
Enter a name (or nothing to stop):
['John', 'Jacob', 'Jingleheimer', 'Schmidt', '']
```

This isn't perfect as we have a blank name in our list, but this gets the point across. Next we'll get a tool to fix the issue we have here with the blank name via a couple of keywords.
