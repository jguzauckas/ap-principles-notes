# Operations on Booleans

This will demonstrate the basic operations that can be performed on booleans

For a functioning example, check out boolean-operations.py and feel free to play around with some values for our variables to see how the operations behave!

First, let's define two boolean variables:

```python
a = True
b = False
```

---

## Integer Casting

**Integer casting** shows you the equivalent integer value of the boolean using `int()`. In Python, `True` is equal to `1` and `False` is equal to `0`:

```python
print("int("+str(a)+") =", int(a)) #a is True, so this should be 1
print("int("+str(b)+") =", int(b)) #b is False, so this should be 0
```

This produces the output:

```python
int(True) = 1
int(False) = 0
```

---

## not

The **not** operation flips the value of a boolean to its opposite using the keyword `not`. Simply, `True` becomes `False` and `False` becomes `True`:

```python
print("not", a, "=", not a) #Since a is True, this should be False
print("not", b, "=", not b) #Since b is False, this should be True
```

This produces the output:

```
not True = False
not False = True
```

---

## and

The **and** operation combines two boolean values using the keyword `and`. `and` takes in two boolean inputs (much like numeric operations take in two numbers) and outputs a value based on them. The way we describe `and`'s output is `True` if and only if both inputs are `True`, and `False` otherwise (that is if at least one or both of the inputs are `False`)

This table displays the possible outputs of `P and Q` where both `P` and `Q` are boolean values. We call this a truth tables as it displays all possible combinations of boolean values for operations like `and`. In this table, `T` stands for `True` and `F` stands for `False`:

| `P` | `Q` | `P and Q` |
| :-: | :-: | :-------: |
| `T` | `T` |    `T`    |
| `T` | `F` |    `F`    |
| `F` | `T` |    `F`    |
| `F` | `F` |    `F`    |

This table shows us that the only time `and` produces a `True` value is when both of the inputs are `True`.

In Python, statements using `and` could look like this:

```Python
print(a, "and", a, "=", a and a)
print(a, "and", b, "=", a and b)
print(b, "and", a, "=", b and a)
print(b, "and", b, "=", b and b)
```

This produces the output:

```
True and True = True
True and False = False
False and True = False
False and False = False
```

This mirrors our truth table values from above!

---

## or

The **or** operation combines two boolean values using the keyword `or`. `or` takes in two boolean inputs (much like numeric operations take in two numbers) and outputs a value based on them. The way we describe `or`'s output is `False` if and only if both inputs are `False`, and `True` otherwise (that is if at least one or both of the inputs are `True`). In the sense of description, this operation feels like an 'opposite' to `and`, as it does the same thing with `False` values that `and` does with `True`

This table displays the possible outputs of `P or Q` where both `P` and `Q` are boolean values. In this table, `T` stands for `True` and `F` stands for `False`:

| `P` | `Q` | `P or Q` |
| :-: | :-: | :------: |
| `T` | `T` |   `T`    |
| `T` | `F` |   `T`    |
| `F` | `T` |   `T`    |
| `F` | `F` |   `F`    |

In Python, statements using `or` could look like this:

```Python
print(a, "or", a, "=", a or a)
print(a, "or", b, "=", a or b)
print(b, "or", a, "=", b or a)
print(b, "or", b, "=", b or b)
```

This produces the output:

```
True or True = True
True or False = True
False or True = True
False or False = False
```

This mirrors our truth table values from above!
