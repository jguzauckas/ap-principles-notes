# String Formatting Types

Sometimes we want the information we pass into a string to be dealt with in a certain way, and for that, we have formatting types!

For a functioning example, check out formattingtypes.py and feel free to play around with some values for our variables to see how the operations behave!

---

## Formatting with `:`

There are several types of formatting we apply to the blanks using `:`

### Negative vs. Positive Numbers

Normally when we enter a number, it will show a negative sign (-) if the number is negative, and nothing ( ) if the number is positive. We can format the blank to show a positive sign (+) if the number is positive using :+

```python
line1 = "Your balance is currently {:+}"
```

Now whatever number we enter, it will have to have either a - or +

```python
print(line1.format(-5))
print(line1.format(5))
```

This produces the output:

```
Your balance is currently -5
Your balance is currently +5
```

### Large Numbers

By default, large numbers will just be displayed as the long list of digits, making it harder to read. Python can insert separators (`,` or `_`) between thousands groupings to make it easier `:,` to use commas as a thousands separator or could also do `:_` for underscore separators

```python
line2 = "This is useful for large numbers like {:,}."
print(line2.format(12345678910))
```

This produces the output:

```
This useful for large numbers like 12,345,678,910.
```

### Fixing Decimal Places

Sometimes we want to make decimal places consistent. Fixed point numbers "fix" or make constant the number of decimal places displayed. `:f` for fixed point numbers (guaranteed number of decimal places), default is 6. This also works when we might pass in an integer but want decimal places

```python
line3 = "I passed in an integer but we write it as {:f}"
print(line3.format(10))
```

This produces the output:

```
I passed in an integer but we write it as 10.000000
```

6 is an arbitrary amount of decimal places, and in some cases we need more or less. We can modify the same type to specify how many decimal places we want `:.#f` for fixed point numbers - guaranteed `#` decimal places shown. This still will convert other types to float and limit the decimal places

```python
line4 = "We write money to hundredths, no further like {:.2f}" #2 decimal places for money!
print(line4.format(5.732))
```

This produces the output:

```
We write money to hundredths, no further like 5.73
```

### Percentages

Computers and calculators often view percentages as decimals from 0 to 1 for 0% to 100%. We can give format() a decimal and have it display it as an appropriate percentage `:%` to convert to percentage i.e., 0.7 = 70%

```python
line5 = "{:%} of students passed the test"
print(line5.format(0.9575)) #This is 95.75%
```

This produces the output:

```
95.750000% of students passed the test
```

Just like with fixed point numbers, we often want to control decimal places of percentages it works similarly - `:.#%` for a percentage - guaranteed `#` decimal places shown

```python
line6 = "{:.2%} of students passed the test"
print(line6.format(0.9575))
line7 = "{:.0%} of students passed the test"
print(line7.format(0.9575))
```

This produces the output:

```
95.75% of students passed the test
96% of students passed the test
```

---

## Formatting with Numbered/Named Blanks

We can still incorporate our numbering or naming from the first file by putting them before the colon in our formatting

```python
line8 = "My first number is {0:.2f} and the second number is {1:.2f}"
print(line8.format(4.758, 0.886)) #Will fill blanks in order
line9 = "My first number is {num1:.2f} and the second percentage is {num2:.2%}"
print(line9.format(num1 = 4.758, num2 = 0.886)) #Will fill blanks according to reference
```

This produces the output:

```
My first number is 4.76 and the second number is 0.89
My first number is 4.76 and the second percentage is 88.60%
```

We can mix and match these formatting types as we need them in strings

```python
change = 4
average = 0.795
line10 = """While the change from one class to another was {:+} points,
the average grade on the exams were only {:.0%}."""
print(line10.format(change, average))
```

This produces the output:

```
While the change from one class to another was +4 points,
the average grade on the exams were only 80%.
```
