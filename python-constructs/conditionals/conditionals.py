# This file contains the sample code from conditionals.md
# so you can see it in action by running this program and
# also change values to see how the behavior changes!

# Boolean Comparisons
print("Hello" == "hello")  # False
print(3 != 4)  # True
print(4 > 2)  # True
print(5 >= 5)  # True
print(4 < 2)  # False
print(3 <= 2)  # False

# Boolean Operators
age = 9
print(age < 10 or age > 20)  # True or False is True

# if Statements
age = 24
if age >= 18:
    print("You are an adult")

# if-else Statements
age = 16
if age >= 18:
    print("You are an adult")
else:
    print("You are not an adult")

# if-elif-else Statements
age = 10
if age >= 18:
    print("You are an adult")
elif age >= 13:
    print("You are a teenager")
elif age >= 9:
    print("You are a tween")
else:
    print("You are very young")

# Ternary Operator
print("You are an adult") if age >= 18 else print("You are not an adult")
