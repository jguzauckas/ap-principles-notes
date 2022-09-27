# For more information on these samples, please
# see the while.md file, which has descriptions
# for everything

# Basic while loop
n = 10
while n < 100:
    print(n)
    n *= 2

# Iterable while loop
names = []
boolCheck = True
while boolCheck:
    name = input("Enter a name (or nothing to stop): ")
    boolCheck = bool(name)
    names.append(name)
print(names)
