# Iterables Overview

When programming, often we don't want to store just one value at a time, we want to store many.

We call the base overarching data structure an **iterable**:

- A collection of objects that can be accessed one at a time (fundamental form)
- Can be iterated over to get each object (hence the name iterable)
- They may not support indices/indexing
- We might not be able to call for any specific object without calling for all objects
- They may not support length
- We might not be able to ask for the number of objects in the iterable

For reference, a string is an example of a specialized kind of iterable, as Python really views it as a collection of characters, and each character is assigned an index to maintain the order of the string. We'll see that strings interact very nicely with other iterables due to this relationship.

A subset of iterables that we use often are referred to as **sequences**:

- All sequences are an iterables, with more functionality
- The added functionality is guaranteed indices/indexing and length
- Can still be iterated over to get each object (hence still being an iterable)
- Two types of sequences: mutable and immutable
  - **Immutable** - cannot be modified after creation (could be replaced)
  - **Mutable** - can be modified after creation

We are going to cover four primary types of iterables. Each has their own functionality and purposes, making them uniquely useful. The four types are:

1. Tuples (Immutable Sequences)
2. Lists (Mutable Sequences)
3. Sets (Iterables)
4. Dictionaries (Iterables)

I recommend this order as you learn about iterables as it carefully introduces different functionalities as we move through the types.

The following table displays information about each of these four types. Some of this information might not make sense initially, but refer back to it as we learn more about each type of iterable. See below the table for brief descriptions of what each row represents:

|            Type             |  Set  |                Dictionary\*                |  List  |  Tuple  |
| :-------------------------: | :---: | :----------------------------------------: | :----: | :-----: |
|            Name             | `set` |                   `dict`                   | `list` | `tuple` |
|           Symbol            | `{ }` |                  `{ : }`                   | `[ ]`  |  `( )`  |
|          Ordered?           |  No   |                    Yes                     |  Yes   |   Yes   |
|          Indexed?           |  No   |                   Keyed                    |  Yes   |   Yes   |
| Change individual elements? |  No   |                    Yes                     |  Yes   |   No    |
|    Add/remove elements?     |  Yes  |                    Yes                     |  Yes   |   No    |
|     Duplicate members?      |  No   |         Keys - No<br>Values - Yes          |  Yes   |   Yes   |
|        Element types        |  Any  | Keys - Immutable Types<br>Values - Any\*\* |  Any   |   Any   |
|     Mix element types?      |  Yes  |      Keys - Yes\*\*\*<br>Values - Yes      |  Yes   |   Yes   |

\* Dictionaries are unique in that they store pairs of information in a system of keys and values. The keys are the way you can reference a given value, just like in a dictionary you can find a word's definition by searching for the word.

\*\* Even though dictionaries store in pairs, the values and keys do not have to be the same type.

\*\*\* While you are allowed to mix the types of keys, it is strongly recommended to stick to one type for your keys to ease use of the iterable.

**Name** - keyword used to referred to the iterable in Python

**Symbol** - the grouping symbols used to define a structure of that type.

**Ordered?** - does the structure care about the order of or keep track of the order of elements?

**Indexed?** - does the structure maintain indices to keep track of each element? Dictionaries use a key system that replaces the functionality of indices.

**Change individual elements?** - given an existing structure of this type, can we modify one of the individual objects it holds?

**Add/remove elements?** - given an existing structure of this type, can we add new elements or remove existing elements without rewriting the entire structure?

**Duplicate members?** - can the structure contain two or more elements of the same type that contain the same value?

**Element types** - what types of objects can the structure store?

**Mix element types?** - can our structures store objects of various types or only one type at a time?
