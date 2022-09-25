# Showing output to the user is important, but so is getting information from the user!
# Our most basic way to do this is with the input() function.
# The input function will prompt the user to type an input string (and press enter) and will
# return that string to the program.
# Inside the parentheses, you put a string that you would like to prompt the user with.
input(
    "Enter your name: "
)  # This doesn't accomplish anything on its own, as we don't save the string!
# The most useful combination is to save this as a String variable so we can use it later:
name = input("Enter your name: ")  # now the name variable holds the users entered name
print(
    "Hello", name + "!"
)  # This is a use case for the input, incorporating it into a response!

# It is important to note an initial limitation of input: its always a string!
# Even if you enter a number, it treats it as a string:
a = input("Enter a number: ")
print(
    "The type of a is", type(a)
)  # this will show that a is a string even if the user entered a number

# We can force Python to reinterpret the input as another type by using casting
# Note: this is relatively ineffective with our current tools because a user entering the wrong type of
# information can break the program, but we'll show basic examples:
# to cast, we use the type name as a command (i.e., int(), float(), bool())
b = int(input("Enter an integer: "))
print("The type of b is", type(b))

c = float(input("Enter an float: "))
print("The type of c is", type(c))

d = bool(input("Enter an boolean (anything for True, blank for False): "))
print("The type of d is", type(d))

# Try and break the program by entering the wrong type of information when it prompts you!
