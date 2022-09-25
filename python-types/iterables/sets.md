# Sets

Sets are another way to store multiple items in a single variable, and are our first general iterable, rather than a sequence like tuples and lists. This is our first and only basic iterable that doesn't keep a specific order of elements.

Sets are defined using square brackets `{ }`.

Elements in Sets are separated using commas `,`.

To learn more about sets, go over to the sets.py file and play around with variables and values to see what happens!

---

## Creating a Set

To create a set, we can just list out values separated by commas `,` in curly brackets `{ }`:

```python
var1 = {"Damario", "Zainab", "Saad", "Gage"}
print(var1)  # Prints the elements in curly brackets
```

This produces the output:

```
{'Gage', 'Zainab', 'Damario', 'Saad'}
```

An important note here is that the set has changed order from the elements we entered. As a matter of fact, every time you run this program the elements will change orders, so when you run this code, it probably will produce a different order from my example here.

Since we can add and remove elements from a set, it makes some sense to want to create a blank set to add to later.

Unfortunately, sets and dictionaries share the same symbols in `{ }`, and Python assumes empty curly brackets are a dictionary, so to make an empty set we must use the `set()` constructor with no parameters passed in:

```python
var2 = set()  # Can generate a blank set to add to later
print(var2)  # Just prints set() to represent empty set
```

This produces the output:

```
set()
```

Again, since empty curly brackets are intended to be interpreted as dictionaries, it even writes an empty set as `set()` for clarity.

Just like our other iterables, we can use the `set()` constructor to turn other iterables into sets:

```python
t = (1, 2, 3)  # Sample tuple
var2 = set(t)  # Copy and covert the tuple to a set
print(var2)  # Still prints elements in square brackets

var2 = set("Hello")  # Takes the characters as elements
print(var2)  # Prints out the individual characters list
```

This produces the output:

```
{1, 2, 3}
{'H', 'o', 'l', 'e'}
```

Even though sets don't care about order, they'll list numerical values in order due to the ease of doing so.

In the case of the string `"Hello"`, it does not keep that order and shuffles the letters.

Also important to note that sets cannot have duplicates, so there is only one element `'l'` in the set, even though our input string `"Hello"` had two.

---

## No Indexing a Set

Unfortunately sets do not keep track of their elements via index so we cannot call for specific locations in the set as the values are shuffled differently every time.

This means we can't print specific elements of a set, our only solution is to print all elements of a set. As a sample, we'll use a for loop here, but talk more specifics about them later:

```python
for elem in var2:
    print(elem)
```

This produces the output:

```
H
o
l
e
```

### Checking for Presence

Even though we can't utilize individual elements like in other iterables, we can check for the presence of values in a set using the `in` keyword. Importantly, one of the major advantages of sets is that they are extremely efficient at determining if they contain elements. If your primary use case is determining if values are in a set, sets can be a powerful tool:

```python
print("h" in var2)  # Should be false, no lowercase 'h'
print("H" in var2)  # Should be true, there is uppercase 'H'
```

This produces the output:

```
False
True
```

The keyword `in` returns a boolean value for presence, with a `True` if an element is in a set and `False` if not.

---

## Modifying Sets

Sets are somewhat modifiable. You can add and remove elements, but cannot modify individual elements. Fortunately, being able to do the combination of removing an element and adding a new one can replace some of the functionality of modifying an individual element.

### Removing Elements

We have three functions that can remove elements: `remove()`, `discard()`, and `pop()`

`remove()` searches for an item and removes it, but will have an error if the item cannot be found. Depending on the situation, you may or may not want that error functionality. The parameter you provide `remove()` is the value of the element you want removed:

```python
var2.remove("H")
print(var2)
```

This produces the output:

```
{'o', 'l', 'e'}
```

`discard()` does the same thing as remove, but will not have an error if the item cannot be found:

```python
var2.discard("h")  # This will not do anything because there is no 'h'
print(var2)
var2.discard("o")
print(var2)
```

This produces the output:

```
{'o', 'l', 'e'}
{'l', 'e'}
```

`pop()` in our other iterables would take in an index as a parameter, but sets don't have indices. In this case, `pop()` doesn't take in any parameters and just removes the last element in the set.

```python
var2.pop()  # Just removes the current last element
print(var2)
```

This produces the output:

```
{'e'}
```

Remember that order doesn't matter in sets, so we have to be careful as we won't always know which element is the last!

### Adding Elements

To add elements, we have the `add()` function. `add()` takes in the value to add as a parameter, and adds it to the list.

```python
var2.add("p")
print(var2)
```

This produces the output:

```
{'p', 'e'}
```

Note that the order doesn't matter for sets so this doesn't show up at the end!

We also have the `update()` function to add on the elements from another iterable:

```python
t = (1, 2, 3)
var2.update(t)
print(var2)
```

This produces the output:

```
{1, 2, 3, 'e', 'p'}
```

Note that due to the nature of numerical values, the set lists them first1

---

## No Duplicate Values

Remember that due to the lack of indexing, sets cannot have duplicate values!

---

## Set Length

We can find out how many elements are in a set by using the length function `len()`

```python
print(len(var1))  # Can just use stand-alone
print(f"There are {len(var1)} elements in var1")  # Using f-string!
```

This produces the output:

```
4
There are 4 elements in var1
```

As this shows, we can call length on a set to get the number of elements, and can utilize it as we could any other integer.

---

## Data Types

Sets can hold any data type, and can mix and match within the same set:

```python
var4 = {"John", 24, 5.75, True}
print(var4)
print(len(var4))
```

This produces the output:

```
{24, True, 5.75, 'John'}
4
```
