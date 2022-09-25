# This program will demonstrate the basic operations that can be performed
# on strings

# For more information on these examples, check out string-operations.md

# First, let's define three string variables
a = "Hello World"
b = "Mr. Guzauckas"
# Notice that here, I defined one string using single quotes and one using double quotes
c = """This is
a multi-line
string."""
# Triple single or double quotes will allow a multi-line string.

# Concatenating uses the + operator to combine strings
print("\nConcatenate:")
print('Combining "' + a + '" and "' + b + '" produces "' + a + b + '"')


# Length (len) returns the length of a given string
print("\nLength:")
print('The length of "' + a + '" is', len(a), "characters")
print('The length of "' + b + '" is', len(b), "characters")
print('The length of "' + c + '" is', len(c), "characters")
# len returns an integer, which you could use to calculate something
print(
    "The total length of the three strings is", len(a) + len(b) + len(c), "characters"
)

# Indexing allows you to see the character at a given location in the String
print("\nIndexing:")
# Python uses zero indexing, which means the first character is at location 0
print('The first character of "' + a + '" is', a[0])
# We can use len to dynamically find the last character, which will be at len - 1
print('The last character of "' + a + '" is', a[len(a) - 1])
# We can also use a negative index to indicate wrapping around to the back of the string
print('The last character of "' + b + '" is', b[-1])

# Slicing allows us to take a set of characters out of a string
print("\nSlicing:")
# Python uses zero indexing, which means the first character is at location 0
# Slicing goes from the begin index to the character just before the end index
print('The characters from position 3 to 7 of "' + a + '" are "' + a[3:7] + '"')
# Slicing can just give a beginning index and go to the end index by skipping the first number
print(
    'The characters from the beginning to position 6 of "' + b + '" are "' + b[:6] + '"'
)
# Slicing can just give an end index and start from the beginning by skipping the second number
print('The characters from position 4 to the end of "' + b + '" are "' + b[4:] + '"')
