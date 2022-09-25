# Basic Data Types in Python

- In a programming language, a type is a property assigned to values used by the program.
  - This property describes the rules that the given value has to follow, and which operations can be performed with it.
  - Examples of types are integers, floats, booleans, strings, etc.
- Python will automatically assign a type to a variable when it is declared/initialized. Here is an example code segment defining the four basic types of variables:

```python
a = 3 		#integer (int)
b = 2.1 	#float (float)
c = True 	#boolean (bool)
d = “Hello”     #string (str)
```

---

## Number Operations:

- Addition `+`
- Subtraction `-`
- Multiplication `*`
- True Division `/`
- Integer Division `//`
- Modulus/Remainder `%`
- Exponentiation `**`

---

## Boolean Operations:

- Integer Casting `int()`
  - `False` is 0 and `True` is 1
- Not `not`
  - Flip the boolean value
- And `and`
  - `True` if and only if both inputs are `True`, otherwise `False`
- Or `or`
  - `False` if and only if both inputs are `False`, otherwise `True`

---

## String Operations:

- Strings can be built with either single quotes `‘ ‘` or double quotes `“ “`
  - Multiline strings can be created with triple quotes (either `‘’’ ‘’‘` or `“”” “””`)
- Length `len()`
  - Number of characters in a string
- Indexing `[#]`
  - The character at position `#`, where the numbering starts at 0.
- Slicing `[#:#]`, `[:#]`, and `[#:]`
  - A chunk of the string defined by the `#`
  - `[#:#]` a chunk from starting position to ending position
  - `[:#]` a chunk from beginning to ending position
  - `[#:]` a chunk from starting position to end
