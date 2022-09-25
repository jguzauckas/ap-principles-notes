# Lists

Lists are another way to store multiple items in a single variable, and are effectively tuples with added modifiability.

Lists are defined using square brackets `[ ]`.

Elements in lists are separated using commas `,`.

To learn more about lists, go over to the lists.py file and play around with variables and values to see what happens!

---

## Creating a List

To start, we can make an empty list. This has potential value because lists can be modified so we can add to it later (whereas tuples were restricted):

```python
var1 = []  # Creates an empty list
print(var1)
```

This produces the output:

```
[]
```

To create a non-empty list, we just need to list at least one object in square brackets:

```python
var1 = ["Damario", "Zainab", "Saad", "Gage"]
print(var1) #Prints the elements in square brackets
```

This produces the output:

```
['Damario', 'Zainab', 'Saad', 'Gage']
```

We can see that it reproduces the same list that we entered. It does choose to use single quote `'` as opposed to double quotes `"` for the strings, but that doesn't make a difference.

If you go to make a list with one element, unlike tuples, we do not need a comma `,` as Python interprets the square brackets as a list regardless.

Can use the `list()` constructor to convert other iterables, like tuple or string into a list. Passing these other iterables into the constructor converts them to a list for us to use:

```python
t = (1, 2, 3) #Sample tuple
var2 = list(t) #Copy and covert the tuple to a list
print(var2) #Still prints elements in square brackets
```

This produces the output:

```
[1, 2, 3]
```

Conveniently, the constructor maintains the order of the iterable it was passed in, making them look identical.

We can do this with a string as well, where it takes each character of the string and puts it in the list:

```python
var2 = list("Hello") #Takes the characters as elements
print(var2) #Prints out the individual characters list
```

This produces the output:

```
['H', 'e', 'l', 'l', 'o']
```

---

# Indexing a List

We can print individual elements using an index, like string.

Remember the indices start at 0, and we use square brackets next to the list to tell it we want to find an index:

```python
print(var1[2])
print(var2[0])
```

This produces the output:

```
Saad
H
```

---

## Modifying Lists

Unlike tuples, lists are changeable, so we can change individual elements or add/remove elements.

### Changing an Element

To change an element, we assign a new value to the index:

```python
var2[2] = 4
#This will update the original list and replace the value in the
#third position with 4
print(var2)
```

This produces the output:

```
['H', 'e', 4, 'l', 'o']
```

### Removing an Element

We have two primary options to remove elements: `remove()` and `pop()`.

`remove()` chooses the value to remove based on its **value**:

```python
var2.remove(4)
print(var2) #No more random 4!
```

This produces the output:

```
['H', 'e', 'l', 'o']
```

That use of `remove()` found the value `4` in the list and removed it.

`pop()` chooses the value to remove based on its **index**:

```python
var2.pop(1) # Removes character at second index
print(var2)
```

This produces the output:

```
['H', 'l', 'o']
```

That use of `pop()` found the element at index `1` and removed it.

## Adding Elements

To add an elements, we have two primary options: `append()` and `insert()`.

`append()` adds the element to the **end of the list**:

```python
var2.append('!')
print(var2)
```

This produces the output:

```
['H', 'l', 'o', '!']
```

`insert()` lets us choose where in the list we want the new element by providing an index and **shifting all other elements to the right**.

In the function, we provide two parameters: the first is the index we'd like to insert at and the second is the value we want inserted there, separated by a comma `,`:

```python
var2.insert(2, 'l') #Inserts 'l' at the provided index 2
var2.insert(1, 'e') #Adds back the 'e' from earlier
print(var2)
```

This produces the output:

```
['H', 'e', 'l', 'l', 'o', '!']
```

We can also add any iterable to the end of the list using `extend()`

`extend()` takes in an iterable and will add all of its elements onto the end of the list:

```python
t = tuple("What's up?")
var2.extend(t)
print(var2)
```

This produces the output:

```
['H', 'e', 'l', 'l', 'o', '!', 'W', 'h', 'a', 't', "'", 's', ' ', 'u', 'p', '?']
```

---

## Duplicate Values

As we've seen with our `"Hello"` list, lists can have duplicate values, as the indices will still be unique. We can define a list with as many duplicate values as we want:

```python
var3 = [5, 5, 5] #This list won't be very helpful, but demonstrates this
print(var3)
print(var3[2])
```

This produces the output:

```
[5, 5, 5]
5
```

---

## List Length

We can find out how many elements are in a list by using the length function `len()`

```python
print(len(var1)) #Can just use stand-alone
print(f"There are {len(var1)} elements in var1") #Using f-string!
```

This produces the output:

```
4
There are 4 elements in var1
```

As this shows, we can call length on a list to get the number of elements, and can utilize it as we could any other integer.

---

## Data Types

Lists can hold any data type, and can mix and match within the same list:

```python
var4 = ["John", 24, 5.75, True]
print(var4)
print(var4[1])
print(len(var4))
```

This produces the output:

```
['John', 24, 5.75, True]
24
4
```
