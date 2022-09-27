# We can effectively put blanks in a String and fill them in using the format function
# This allows us to have strings that can easily change portions of their values
# without starting over every time

# Blanks are marked using curly braces, here is the most basic example of a "blank"
line1 = "My name is {}!"
# If we were to print the string line1 as is, we would see the curly braces, which doesn't look nice
print(line1)
# We can do our stringname.format() to pass in argument(s) to fill in any blank(s)
print(line1.format("John Guzauckas"))

# Can have and fill in multiple blanks using multiple sets of curly braces
line2 = "My first name is {} and my last name is {}."
# To fill in multiple blanks, just list multiple values in format() using commas between
# The blanks are filled in the same order you write your values in
print(line2.format("John", "Guzauckas"))

# When we start to use a few blanks, it can be harder to keep track of which blank is which
# To help ease this problem, we can number the blanks (remember zero-indexing!)
line3 = "My first name is {0} and my last name is {1}."
# Now it will still fill in order, but it can be easier for us to identify which piece goes where
print(line3.format("John", "Guzauckas"))

# To get even more clarity, we can assign temporary "names" to each blank to be referenced later
line4 = "My first name is {first} and my last name is {last}."
# To fill in, we need to let format() know which value is for which reference by using
# reference = value
print(line4.format(first="John", last="Guzauckas"))

# Sometimes we might need to repeat a blank, and with names they will automatically be used
# as many times as needed. See here two {first} blanks
line5 = (
    "My first name is {first} and my last name is {last}, but you can call me {first}."
)
# The print statement doesn't look different because it "John" twice
print(line5.format(first="John", last="Guzauckas"))

# This repeating blanks works with the numbering too (not two {0} here)
# This can, however, get a little more confusing with more blanks required
line6 = "My first name is {0} and my last name is {1}, but you can call me {0}."
# Here, since "John" has index 0, it is filled in everywhere 0 is asked for
print(line6.format("John", "Guzauckas"))

# If we were just using empty braces, we would have to repeat inputs to achieve the same result.
line7 = "My first name is {} and my last name is {}, but you can call me {}."
# Note here that we have "John" here twice
print(line7.format("John", "Guzauckas", "John"))

# Classic input statements gathering a string and assigning it to a variable
firstname = input("What is your first name? ")
lastname = input("What is your last name? ")
# A string asking for two unique blanks
line8 = "My first name is {0} and my last name is {1}."
# Can utilize string variables as arguments in format to be more dynamic
print(line8.format(firstname, lastname))

# A string asking for two (potentially similar) blanks
line9 = "I am {} years old. This statement is {}"
# Format will automatically convert types to string to plug them in, like int, float, and bool
print(line9.format(24, True))
