# The code in this file comes from the functions.md file with notes about how basic
# functions work in Python. Use this file to play around with functions and get a
# better idea of how they work, and see the markdown file for more detailed notes
# on how they work.

# Most basic function
def printhw():
    print("Hello, World!")


# Call to basic function
printhw()

# Function with a parameter
def hello(name):
    print(f"Hello {name}!")


# Failed call to a function with a parameter
# hello()

# Call to a function with a parameter
hello("John")

# Function with two parameters
def hello(name1, name2):
    print(f"Hello {name1} and {name2}!")


# Call to a function with a two variables, using a variable
name = "Nathan"
hello(name, "Cody")

# Creating a function meant for an iterable parameter
def hellos(names):
    for name in names:
        print(f"Hello {name}!")


# Calling the function with a tuple
tup = ("Rianah", "Nafiza", "Christina", "Denae")
hellos(tup)

# Accidentally calling the function with a string
hellos("Madeline")

# Function with default value parameter
def hi(name="World"):
    print(f"Hello {name}!")


# Calls to function with parameter default value
hi("Josiah")
hi()
