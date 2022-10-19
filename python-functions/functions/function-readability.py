# For more information on these samples, please
# see the function-readability.md file, which has
# descriptions for everything

# No type hints
def fullname(first, last):
    return first + " " + last

# Type hints for parameters
def fullname(first: str, last: str):
    return first + " " + last

# Type hint for return type
def fullname(first: str, last: str) -> str:
    return first + " " + last

# None return type
def hello(name: str) -> None:
    print(f"Hello {name}!")