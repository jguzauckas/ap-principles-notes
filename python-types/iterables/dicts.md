# Dictionaries

Dictionaries are another way to store multiple items in a single variable. They are the most unique of the four structures we've covered

Dictionaries are made up of `key:value` pairs, where the `key` functions as a sort of index. We use the `:` to show the pair, where the left is always the `key` and the right is always the `value`.

Dictionaries are defined using square brackets `{ }`.

Elements in dictionaries are separated using commas `,`.

To learn more about dictionaries, go over to the dicts.py file and play around with variables and values to see what happens!

---

## Creating a Dictionary

Like we discussed in sets, dictionaries and sets share the same grouping symbols in curly brackets `{ }`, but Python defaults empty curly brackets to a dictionary. So to create an empty dictionary, we can just use empty curly brackets `{ }`:

```python
var1 = {}
print(var1)
```

This produces the output:

```
{}
```

To create a dictionary with elements, we can just list out `key:value` pairs separated by commas `,` in curly brackets `{ }`:

```python
var1 = {
    "Damario": 10,
    "Zainab": 10,
    "Saad": 12,
    "Gage": 12,
}  # We often write with multiple lines for readability
print(var1)  # Prints the pairs in curly brackets
```

This produces the output:

```
{'Damario': 10, 'Zainab': 10, 'Saad': 12, 'Gage': 12}
```

In this example, we make the dictionary multiple lines to help improve readability. We also show that dictionaries can multiples of the same values, as long as they have different keys. You cannot repeat keys!

---

## Indexing (Keying) a Dictionary

While dictionaries don't have indices, we can print individual elements using their keys. Even though the keys may not be integers, we still use the square bracket notation to request the individual element:

```python
print(var1["Damario"])
```

This produces the output:

```
10
```

### Viewing all Elements

We have some built in methods to view all elements in a dictionary in a few different ways.

First is the `keys()` method, which displays all the keys in a dictionary:

```python
print(var1.keys())
```

This produces the output:

```
dict_keys(['Damario', 'Zainab', 'Saad', 'Gage'])
```

Similarly, we have the `values()` method, which displays all the values in a dictionary:

```python
print(var1.values())
```

This produces the output:

```
dict_values([10, 10, 12, 12])
```

Notice that both `keys()` and `values()` display their output with the square brackets `[ ]`, which we know means they are represented as a list!

Finally, we have the `items()` method, which displays all the pairs in a dictionary:

```python
print(var1.items())  # It shows them as a list of tuples
```

This produces the output:

```
dict_items([('Damario', 10), ('Zainab', 10), ('Saad', 12), ('Gage', 12)])
```

Notice that the `items()` method displays the `key:value` pairs as a list (square brackets `[ ]`) of two-element tuples (parentheses `( )`)!

### Checking for Presence

Just like sets, we can use the `in` keyword to check if a **key** is present:

```python
print("Cody" in var1)  # Should be false, no "Cody" key
print("Gage" in var1)  # Should be true, there is a "Gage" key
```

This produces the output:

```
False
True
```

---

## Modifying Dictionaries

Similar to lists, dictionaries are changeable, so we can change individual elements or add/remove elements.

### Changing an Element

To change an element, we can assign a new value to its key:

```python
print(var1["Zainab"])  # Currently 10
var1["Zainab"] = 11
print(var1["Zainab"])  # Now 11
```

This produces the output:

```
10
11
```

We have an alternative to this, which is the `update()` method. The parameter for the `update()` method is a dictionary with a single `key:value` pair using the key of the element you want to change:

```python
var1.update({"Zainab": 10})
print(var1["Zainab"])  # Now back to 10
```

This produces the outcome:

```
10
```

### Adding an Element

The same two methods above we used to change the value of an element work to add a new value to the dictionary. The difference is that the `key` will be new, as opposed to a `key` already in use:

```python
var1["Nathan"] = 12
var1.update({"Nigel": 10})
print(var1)
```

This produces the output:

```
{'Damario': 10, 'Zainab': 10, 'Saad': 12, 'Gage': 12, 'Nathan': 12, 'Nigel': 10}
```

### Removing an Element

We have three functions that can remove elements: `pop()`, `popitem()`, and `clear()`

`pop()` will search for a given key and remove the pair it is a part of:

```python
var1.pop("Gage")
print(var1)
```

This produces the output:

```
{'Damario': 10, 'Zainab': 10, 'Saad': 12, 'Nathan': 12, 'Nigel': 10}
```

`popitem()` removes the last inserted element into the dictionary, and does not require a paramter:

```python
var1.popitem()  # This should remove Nigel
print(var1)
```

This produces the output:

```
{'Damario': 10, 'Zainab': 10, 'Saad': 12, 'Nathan': 12}
```

Finally, `clear()` allows us to empty a dictionary while still maintaining its reference as a dictionary at all:

```python
var1.clear()
print(var1)
```

This produces the output:

```
{}
```

---

## Duplicate Values

As we've seen in our sample dictionary, we can have duplicate values, as long as they have unique keys. Keys cannot have duplicates, as that would make it difficult for the dictionary to reference the correct value at any given time.

---

## Dictionary Length

We can find out how many `key:value` pairs are in a dictionary by using the length function `len()`:

```python
print(len(var1))  # Can just use stand-alone
print(f"There are {len(var1)} elements in var1")  # Using f-string!
```

This produces the output:

```
0
There are 0 elements in var1
```

As this shows, we can call length on a dictionary to get the number of pairs, and can utilize it as we could any other integer.

---

## Data Types

In a dictionary, we can mix and match data types with some restrictions:

- Keys should be an immutable type (think our basic types: `int`, `float`, `bool`, and `str`)
- While not required, it is strongly recommended that all of your keys be the same type.
- You values paired with keys can be any types and can be mixed throughout

Here is a sample dictionary with `keys` that are type `int` and values of a variety of types:

```python
var1 = {
    2: "Hello",
    4: 3.2,
    8: 2,
    11: True,
}  # Note that my keys are all the same type - int
print(var1)
```

This produces the output:

```
{2: 'Hello', 4: 3.2, 8: 2, 11: True}
```
