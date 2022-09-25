# Variables

This will demonstrate the basic ideas around variables in Python

For a functioning example, check out variables.py and feel free to play around with some values for our variables to see how everything behaves!

---

## Automatic Typing

Python automatically determines the type for your variable based on what it is declared as.

Simple declarations are made with the single equals sign (=), which works for all of our types.

```python
a = 5
b = 12.2
c = True
d = "String"
```

In this example, Python knew that a whole number like `5` should be an `int` (integer), a decimal like `12.2` should be a `float` (floating point number), the keyword `True` should be a `bool` (boolean), and anything in quotes like `"String"` should be a `str` (string).

---

## Operations and Variable Values

Performing an operation on two variables or a variable with a constant does not necessarily change the value of the variable. For example, these do not change the value of a or b:

```python
print(a, "+", b, "=", a + b)
print(a, "+", 5, "=", a + 5)
print("a is still", a, "and b is still", b)
```

This produces the output:

```
5 + 12.2 = 17.2
5 + 5 = 10
a is still 5 and b is still 12.2
```

Even though we did `a + b` and `a + 5`, it did not save that value anywhere, just used it for a moment.

---

## Modifying Variables - Assignments

To modify the value of a variable, we have to make another assignment. This could be an assignment to a different value:

```python
a = 7  # Now a is 7 instead of 5
print("a is now", a)
```

This produces the output:

```
a is now 7
```

This could also be an assignment to a calculation:

```python
a = b + 8  # 12.2 + 8 is 20.2, Note that this changes a to a float!
print("a is now", a)
```

This produces the output:

```
a is now 20.2
```

Finally, this assignment could be self-referencing, which means it can be assigned using a calculation with its original value:

```python
a = a - 4  # 20.2 - 4 is 16.2
print("a is now", a)
```

This produces the output:

```
a is now 16.2
```

---

## Modifying Variables - Compound Assignments

We will often want to change the values of variables for many reasons. Similarly, we often want to change them based on their previous value (i.e. performing an operation on the old value).

We can simplify this process with compound assignment operators, which allow us to perform a self-referencing calculation much more easily than before.

Compound assignment operators are a combination of the operation one is performing (for example, `+`, `-`, `*`, `/`, `//`, `%`, `**`) and the assignment operator, the equals sign `=`. For example, lets look at **addition assignment**:

```python
a += 4  # This does the same thing as `a = a - 4`
print("a is now", a)
```

This produces the output:

```
a is now 20.2
```

Lets show a sample of the other compound operators:

**Subtraction Assignment**

```python
a -= 5  # subtract 5 then assign
print("a is now", a)
```

This produces the output:

```
a is now 15.2
```

**Multiplication Assignment**

```python
a *= 2  # Multiply by 2 then assign
print("a is now", a)
```

This produces the output:

```
a is now 30.4
```

**True Division Assignment**

```python
a /= 3  # True Divide by 3 then assign
print("a is now", a)
```

This produces the output:

```
a is now 10.133333333333333
```

**Integer Division Assignment**

```python
a //= 2  # Integer Divide by 2 then assign
print("a is now", a)
```

This produces the output:

```
a is now 5.0
```

**Modulo/Remainder Assignment**

```python
a %= 2  # Divide by 2 and take the remainder then assign
print("a is now", a)
```

This produces the output:

```
a is now 1.0
```

**Exponentiation Assignment**

```python
a **= 3  # Raise to the power of 3 then assign
print("a is now", a)
```

This produces the output:

```
a is now 1.0
```

This may look like exponentiation didn't do anything, but that's just this situation, since `1.0` raised to the power of `3` is still `1.0`.

---

## Compound Assignment on Other Types

Some of these work with other types of variables as well, not just integers and floats.

For example, `+` for strings means concatenate (put together):

```python
print("d is", d)
d += "str"
print(
    "d is now", d
)
```

This produces the output:

```
d is String
d is now Stringstr
```

Notice that it doesn't automatically add a space between the strings, we would need to do that!
