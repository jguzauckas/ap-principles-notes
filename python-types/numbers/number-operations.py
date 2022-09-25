# This program will demonstrate the basic operations that can be performed
# on integers and floats

# For more information on these examples, check out number-operations.md

# First, let's define two integer variables and two float variables to work with
a = 15
b = 6
x = 3.4
y = 7.6

# Addition (+) works as we'd expect
print("\nAddition:")
print(a, "+", b, "=", a + b)
print(x, "+", y, "=", x + y)
# Using an integer and a float in a calculation treats everything as a float
print(a, "+", x, "=", a + x)


# Subtraction (-) is similar to addition
print("\nSubtraction:")
print(a, "-", b, "=", a - b)
print(x, "-", y, "=", x - y)
# Using an integer and a float in a calculation treats everything as a float
print(a, "-", x, "=", a - x)

# Multiplication (*) works as expected
print("\nMultiplication:")
print(a, "*", b, "=", a * b)
print(x, "*", y, "=", x * y)
# Using an integer and a float in a calculation treats everything as a float
print(a, "*", x, "=", a * x)

# True division (/) works the way normal division does
print("\nTrue Division:")
print(a, "/", b, "=", a / b)
print(x, "/", y, "=", x / y)
# Using an integer and a float in a calculation treats everything as a float
print(a, "/", x, "=", a / x)

# Integer division (//) does normal division and then rounds down to the nearest whole number
print("\nInteger Division:")
print(a, "//", b, "=", a // b)
print(x, "//", y, "=", x // y)
# Using an integer and a float in a calculation treats everything as a float
print(a, "//", x, "=", a // x)

# Modulo/Remainder (%) does division and returns the remainder
print("\nModulo/Remainder:")
print(a, "%", b, "=", a % b)
print(x, "%", y, "=", x % y)
# Using an integer and a float in a calculation treats everything as a float
print(a, "%", x, "=", a % x)

# Exponentiation (**) raises the first number to the second number
print("\nExponentiation:")
print(a, "**", b, "=", a**b)
print(x, "**", y, "=", x**y)
# Using an integer and a float in a calculation treats everything as a float
print(a, "**", x, "=", a**x)
