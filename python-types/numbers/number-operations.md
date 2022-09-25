# Operations on Numbers (Integers and Floats)

This will demonstrate the basic operations that can be performed on integers and floats.

For a functioning example, check out number-operations.py and feel free to play around with some values for our variables to see how the operations behave!

First, let's define two integer variables and two float variables to work with:

```python
a = 15
b = 6
x = 3.4
y = 7.6
```

---

## Addition

**Addition** `+` works as we'd expect:

```python
print(a, "+", b, "=", a + b)
print(x, "+", y, "=", x + y)
```

This produces the output:

```
15 + 6 = 21
3.4 + 7.6 = 11.0
```

When using an integer and a float in a calculation, everything is treated as a float:

```python
print(a, "+", x, "=", a + x)
```

This produces the output:

```
15 + 3.4 = 18.4
```

---

## Subtraction

**Subtraction** `-` works similarly to addition:

```python
print(a, "-", b, "=", a - b)
print(x, "-", y, "=", x - y)
```

This produces the output:

```
15 - 6 = 9
3.4 - 7.6 = -4.199999999999999
```

Note that the answer to `3.4 - 7.6` should be `-4.2`, but it appears as `-4.199999999999999`. This is a drawback of how a floating point number system is stored on a computer. For all intents and purposes, this answer will function as `-4.2` for us.

Again, using an integer and a float in a calculation, everything is treated as a float:

```python
print(a, "-", x, "=", a - x)
```

This produces the output:

```
15 - 3.4 = 11.6
```

While the previous calculation had trouble using `-4.2`, this one had no trouble using `11.6`. This is again due to how floating point number systems work on a computer.

---

## Multiplication

**Multiplication** `*` works as we expect multiplication to work:

```python
print(a, "*", b, "=", a * b)
print(x, "*", y, "=", x * y)
print(a, "*", x, "=", a * x) #Mixing int and float creates a float
```

This produces the output:

```
15 * 6 = 90
3.4 * 7.6 = 25.84
15 * 3.4 = 51.0
```

---

## True Division

**True division** `/` works the way we expect division to, creating a decimal when needed:

```python
print(a, "/", b, "=", a / b)
print(x, "/", y, "=", x / y)
print(a, "/", x, "=", a / x)
```

This produces the output:

```
15 / 6 = 2.5
3.4 / 7.6 = 0.4473684210526316
15 / 3.4 = 4.411764705882353
```

---

## Integer Division

**Integer division** `//` does traditional division and then rounds _towards zero_ to the nearest whole number:

```python
print(a, "//", b, "=", a // b)
print(x, "//", y, "=", x // y)
print(a, "//", x, "=", a // x)
```

This produces the output:

```
15 // 6 = 2
3.4 // 7.6 = 0.0
15 // 3.4 = 4.0
```

From the previous operation, we can see how the rounding for integer division works. `15 / 6` had produced `2.5` which with integer division rounds down to `2`.

When floats are involved, we can see that the answer is provided as a whole number float, as `0.4473684210526316` rounds down to `0.0` and `4.411764705882353` rounds down to `4.0`

If we had a negative number, for example like `-0.4473684210526316`, it would round towards zero to get `0.0`.

---

## Modulo/Remainder

**Modulo/Remainder** `%` does division and returns the remainder (what was left over after doing division)

```python
print(a, "%", b, "=", a % b) #This reads as "the remainder when doing a / b"
print(x, "%", y, "=", x % y)
print(a, "%", x, "=", a % x)
```

This produces the output:

```
15 % 6 = 3
3.4 % 7.6 = 3.4
15 % 3.4 = 1.4000000000000004
```

To elaborate on this operation, as it is a less traditional arithmetic operation, you take away the divisor `6` from the dividend `15` until you cannot take away anymore (without going past zero). For us that would be `15 - 6 = 9 - 6 = 3`. You'll notice that we took away the divisor twice, which is where the `2` from our integer division earlier came from. The `3` we had left over is our remainder.

---

## Exponentiation

**Exponentiation** `**` raises the first number to the second number:

```python
print(a, "**", b, "=", a ** b) #This is effectively doing a^b
print(x, "**", y, "=", x ** y)
print(a, "**", x, "=", a ** x)
```

This produces the output:

```
15 ** 6 = 11390625
3.4 ** 7.6 = 10945.604950929635
15 ** 3.4 = 9970.347169336872
```

A more intuitive way to remember the `**` for this operation is the fact that exponentiation is repeated multiplication, the symbol for it repeats `*` as `**`.
