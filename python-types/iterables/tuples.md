# Tuples

Tuples are a way to store multiple items in a single variable.

Tuples are defined using round brackets (parentheses) `( )`.

Elements in tuples are separated using commas `,`.

To learn more about tuples, go over to the tuples.py file and play around with variables and values to see what happens!

---

## Creating a tuple

To create a tuple, we just need to list at least one object in round brackets:

```python
var1 = ("Damario", "Zainab", "Saad", "Gage")
print(var1) # Prints the elements in round brackets
```

This produces the output:

```
('Damario', 'Zainab', 'Saad', 'Gage')
```

We can see that it reproduces the same tuple that we entered. It does choose to use single quote `'` as opposed to double quotes `"` for the strings, but that doesn't make a difference.

Note the phrasing above of "at least one object". For some iterables, you may start with one object and want to add some later. In the case of tuples, we cannot add more elements, rather we'd have to rewrite the tuple entirely. Regardless, creating a tuple with one element is still possible:

```python
var1 = ("Damario",)
print(var1)
```

This produces the output:

```
('Damario',)
```

The comma `,` here is critical, it tells Python that this is a tuple, even if there is just one object. Without the comma, Python would interpret this as a string instead.

Can use the `tuple()` constructor to convert other iterables, like list or string into a tuple. Passing these other iterables into the constructor converts them to a tuple for us to use:

```python
l = [1, 2, 3] # Sample list, don't worry about this for now
var2 = tuple(l) # Copy and covert the list to a tuple
print(var2) # Still prints elements in round brackets
```

This produces the output:

```
(1, 2, 3)
```

Conveniently, the constructor maintains the order of the iterable it was passed in, making them look identical.

We can do this with a string as well, where it takes each character of the string and puts it in the tuple:

```python
var2 = tuple("Hello")  # Takes the characters as elements
print(var2)  # Prints out the individual characters tuple
```

This produces the output:

```
('H', 'e', 'l', 'l', 'o')
```

---

## Indexing a Tuple

We can print individual elements using an index, just like strings.

Remember the indices start at 0, and we use square brackets next to the tuple to tell it we want to find an index.

```python
print(var1[0])
print(var2[1])
```

This produces the output:

```
Damario
e
```

---

## No Modifying Tuples

Note that if I want to change a tuple. I will need to create a new one, as they are immutable. If you end up needing to do this, it isn't a problem, especially for smaller tuples, but if you know you will need to change a value or add/remove values, you should consider another structure. We can just redefine a tuple using assignment:

```python
var1 = ("Damario", "Zainab", "Saad", "Gage", "John")
# This will not update the original var1 tuple, it will create a new one
print(var1)
```

This produces the output:

```
('Damario', 'Zainab', 'Saad', 'Gage', 'John')
```

This creates a new tuple under the same variable containing the new information.

---

## Duplicate Values

As we saw earlier in the `"Hello"` tuple, tuples can have duplicate values, as the indices will still be unique. We can define tuples with as many duplicate values as we want:

```python
var3 = (5, 5, 5) #This tuple won't be very helpful, but demonstrates this
print(var3)
print(var3[2])
```

This produces the output:

```
(5, 5, 5)
5
```

---

## Tuple Length

We can find out how many elements are in a tuple by using the length function `len()` (similar to strings).

```python
print(len(var1)) #Can just use stand-alone
print(f"There are {len(var1)} elements in var1") #Using f-string!
```

This produces the output:

```
5
There are 5 elements in var1
```

As this shows, we can call length on a tuple to get the number of elements, and can utilize it as we could any other integer.

---

## Data Types

Tuples can hold any data type, and can mix and match within the same tuple:

```python
var4 = ("John", 24, 5.75, True)
print(var4)
print(var4[1])
print(len(var4))
```

This produces the output:

```
('John', 24, 5.75, True)
24
4
```

Despite having mixed data types, this tuple can still perform any of its basic functions!
