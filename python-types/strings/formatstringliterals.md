# Formatting String Literals

In Python 3.6 and later, we can use another method to format string literals (not variables) with f-strings or Formatted String Literals

For a functioning example, check out formatstringliterals.py and feel free to play around with some values for our variables to see how the operations behave!

---

## f-Strings

We often use string literals throughout code when we won't need to reuse something. When we do need to reuse something, format() is a better bet!

f-strings allow us to do calculations when creating a string and easily replace certain values with variables when we want. Here is an example:

```python
first = "John"
last = "Guzauckas"
print(f"My name is {first} {last}.")
```

This produces the output:

```
My name is John Guzauckas.
```

Unlike `format()` where we'd need to write things like first and last multiple times to replace them correctly, we can do it much more succinctly with f-strings

We can even do calculations within the string and display the answer!

```python
grade1 = 78
grade2 = 93
print(f"Your average grade was {(grade1 + grade2) / 2}, good job!")
```

This produces the output:

```
Your average grade was 85.5, good job!
```

In this example, Python does the average calculation and then puts the answer in the string

Our formatting types from formattingtypes.py also work in f-strings, giving us more customization options, even on a calculation!

```python
print(f"Your average grade was {(grade1 + grade2) / 2:.2f}")
```

This produces the output:

```
Your average grade was 85.50
```

This prints the same line but forces the output to have 2 fixed decimal points (:.2f)

```python
people = 7753000000  # Current world population estimate
print(f"There are currently estimated to be {people:,} on Earth.")
```

This produces the output:

```
There are currently estimated to be 7,753,000,000 on Earth.
```

This utilizes our commas as thousands separators! (:,)
