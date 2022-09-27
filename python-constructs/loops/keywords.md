# Keywords

There are two keywords that offer a lot of functionality for our loops: `break` and `continue`.

All of the sample code provided in this file is in the keywords.py Python file for you to run, modify, and otherwise investigate.

---

## `break`

Sometimes we hit a point in our loop where due to a certain condition being met, we don't want to continue on. The `break` keyword allows us to instantly end a loop and move on.

For example, let's start with an iterable:

```python
surnames = ["Kirchmeier", "Pointek", "Guzauckas",  "Lorenzet"]
```

Let's say I want to print out all the elements in this list until I reach my name, then stop. I could do this with out break keyword:

```python
for name in surnames:
    if name == "Guzauckas":
        break
    print(name)
```

This produces the output:

```
Kirchmeier
Pointek
```

The `break` allowed us to exit the loop when we wanted to!

---

## `continue`

Sometimes we may not want to necessarily entirely exit a loop when something happens, but we may want to move on to the next iteration and skip some steps. The `continue` keyword allows us to skip the rest of an iteration and move on to the next.

Let's say I want to print out the list of names, but this time instead of stopping before my name, I just want to skip my name. The code doesn't look all that different:

```python
for name in surnames:
    if name == "Guzauckas":
        continue
    print(name)
```

This produces the output:

```
Kirchmeier
Pointek
Lorenzet
```

This time, we still didn't print my name, but we didn't leave `"Lorenzet"` out in the process!
