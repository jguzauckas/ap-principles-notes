# This program will demonstrate the basic ideas around variables in Python

# For more information on these examples, check out variables.md

# Python automatically determines the type for your variable based on what it is declared as.
# Simple declarations are made with the single equals sign (=), which works for all of our types.
a = 5
b = 12.2
c = True
d = "String"

# Performing an operation on two variables or a variable with a constant does not necessarily
# change the value of the variable. For example, these do not change the value of a or b:
print(a, "+", b, "=", a + b)
print(a, "+", 5, "=", a + 5)
print("a is still", a, "and b is still", b)
# Even though we did a + b and a + 5, it did not save that value anywhere, just used it for a moment.

# To modify the value of a variable, we have to make another assignment. This could be an assignment
# to a different value:
a = 7  # Now a is 7 instead of 5
print("a is now", a)
# This could be an assignment to a calculation:
a = b + 8  # 12.2 + 8 is 20.2, Note that this changes a to a float!
print("a is now", a)
# This assignment could be self-referencing, which means it can be assigned using a calculation with
# its original value:
a = a - 4  # 20.2 - 4 is 16.2
print("a is now", a)

# We will often want to change the values of variables for many reasons. Similarly, we often
# want to change them based on their previous value (i.e. performing an operation on the old value)
# We can simplify this process with compound assignment operators, which allow us to perform
# a self-referencing calculation much more easily than before
# Compound assignment operators are a combination of the operation one is performing (+, -, *, /
# //, %, **) and the assignment operator, the equals sign (=). For example:
a += 4  # This compound assignment operator is the subtraction assignment, it subtracts the number
# on the right, and then assigns the new value to our variable
print("a is now", a)
# Lets show a sample of these compound operators:
a -= 5  # Add 5 then assign
print("a is now", a)

a *= 2  # Multiply by 2 then assign
print("a is now", a)

a /= 3  # True Divide by 3 then assign
print("a is now", a)

a //= 2  # Integer Divide by 2 then assign
print("a is now", a)

a %= 2  # Divide by 2 and take the remainder then assign
print("a is now", a)

a **= 3  # Raise to the power of 3 then assign
print("a is now", a)

# Some of these work with other types of variables as well, not just integers and floats.
# For example, + for strings means concatenate (put together)
print("d is", d)
d += "str"
print(
    "d is now", d
)  # Notice that it doesn't automatically add a space, we need to do that!
