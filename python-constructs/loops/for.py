# For more information on these samples, please
# see the for.md file, which has descriptions
# for everything

# Basic for loop
for x in (0, 1, 2):
    print(x)

# Range
print(list(range(5)))  # Should turn the numbers from 0 to 4 into a list

print(list(range(3, 8)))  # This should turn the numbers from 3 to 7 into a list

print(
    list(range(1, 10, 2))
)  # This should turn the odd numbers from 1 to 10 into a list

# Using range in for loop
for x in range(5):
    print(x)

# Sample list
mylist = [3, 7, 2, 4, 0]

# Using range to go through the indices of a list
for x in range(len(mylist)):
    print(mylist[x])
