# for each Loops

for each loops are a concept extension of `for` loops where we look at iterating over objects rather than just numbers.

All of the sample code provided in this file is in the foreach.py Python file for you to run, modify, and otherwise investigate.

---

## Basic for each Loop

A for each loop in Python looks no different from a `for` loop, since in Python they function the same way. The difference comes in the fact that we put in an iterable of objects rather than just numbers.

For example, let's start with an iterable:

```python
surnames = ["Guzauckas", "Kirchmeier", "Pointek", "Lorenzet"]
```

Before, we had code that was much harder to read to loop through the elements in a list like this:

```python
for x in range(len(surnames)):
    print(surnames[x])
```

This same code could be written as an easier for each loop:

```python
for name in surnames:
    print(name)
```

Both produce the same output:

```
Guzauckas
Kirchmeier
Pointek
Lorenzet
```

In both cases, we saved ourselves from writing multiple print statements to call each name by iterating over the list

---

## `enumerate()`

Sometimes we want easy access to both the elements of an iterable, as well as their indices. The `enumerate()` function lets us do this in a loop easily.

Inside of `enumerate`, we provide an iterable to split up, and where we'd normally write one variable in the `for` loop, we write two separated by a comma `,`:

```python
for position, name in enumerate(surnames):
    print(position)
```

This produces the output:

```
0 Guzauckas
1 Kirchmeier
2 Pointek
3 Lorenzet
```

This loop produces `tuple` pairs of indices and elements and assigns one piece to each of our variables `position` and `name`.

Conveniently, we can use both of those variables independently to do whatever we need:

```python
for position, name in enumerate(surnames):
    print(f"{name} is in position {position}.")
```

This produces the output:

```
Guzauckas is in position 0.
Kirchmeier is in position 1.
Pointek is in position 2.
Lorenzet is in position 3.
```

This opens up a lot of possibilities for us in our iterables, as now no matter how big they are, we can perform actions with them!
