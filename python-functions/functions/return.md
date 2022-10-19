# `return`

With basic functions down, we can make them more useful. We can use a function to get new information for a program to work with. To have a function send a value back after it is called, we use the `return` keyword.

The return.py file has all the sample code from this markdown file for you to run and modify as you'd like to get a better sense of how they work!

---

## Basic Example

Let's define the simplest return function we can:

```python
def sendback(name):
    return name
```

This function takes in a parameter `name`, and then sends it back to the program to do whatever it wants with it. An initial call to this function appears as though nothing happens:

```python
sendback("John")
```

This doesn't produce any output! To better utilize a function that returns, we need to treat a call to our function as if it is equivalent to a value (because the function will send back a value!)

```python
name = sendback("John")
print(name)
```

This produces the output:

```
John
```

This function isn't really helpful, but demonstrates the basic use of a function with `return`.

---

## Basic Useful Example

Let's look at an example that is more useful. Let's say at various times in a program we need to frequently apply several operations to a number, like calculating interest on a bank account:

```python
def interest(money):
    money *= 1.03 ** 10 #10 years of 3% interest
    money *= 1.02 ** 15 # 15 years of 2% interest
    return money
```

Now lets call our function:

```python
total = interest(1000)
print(f"In 25 years, your $1,000 will become ${total:.2f}")
```

This produces the output:

```
In 25 years, your $1,000 will become $1808.73
```

Even if we just need to do that kind of calculation twice in a program, this function will start to save us time (and lines of code).

---

## Incorporating Other Tools

We can make functions even more powerful by incorporating other tools like conditionals. Here is a classic example:

```python
def max(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2
```

Lets call our function:

```python
print(max(10, 12))
```

This produces the output:

```
12
```

If functions are able to make decisions, our programs become a lot more powerful!
