# Comments

As you've seen me use frequently, comments are a way for programmers to leave information about a program behind, either for themselves in the future or for others!

The comments.py file has all the sample code from this markdown file for you to run and modify as you'd like to get a better sense of how this works!

---

## General Comments

PEP 8 says the following about comments:

- Comments should be complete sentences with the first word capitalized and ending with a period
- When you have multiple sentences, you should have two spaces at the end of a sentence period, and no spaces after the last sentence
- For paragraphs of information, separate paragraphs by a line with just a blank comment

To make a basic comment, we use the `#` symbol followed by a single space and then our information. Here is a few basic examples:

```python
# This is a simple comment.
# This is one sentence.  This is another sentence.
#
# This is now a different paragraph due to the blank comment above.
```

These comments follow the rules prescribed above, but the most important things have not been said:

1. Comments should accurately reflect the program (make sure to update your comments if you update the code!)
2. Comments should only be used to describe something that is not immediately obvious (don't state that you are `setting a variable` for example)

---

## Inline Comments

Sometimes, we want to put a small note after a line of code to help clarify what it is accomplishing. In Python, we try to use them infrequently, and only when absolutely necessary.

PEP 8 requires that an inline comment be separated by at least two spaces from the end of the line of code to help differentiate, and we use the same `#` symbol:

```python
money = 100  # Set money to 100
money *= (1 + 0.02) ** 10  # Interest calculation for 10 years at 2%
```

The first line would be a comment that does not meet PEP 8 because it does not provide any useful information, it's clear from the statement that we are setting money to be 100.

The second line is an example of a helpful inline comment, especially, if the context was not very present in your code that we were working with money.

As with many things, the usefulness of inline comments (and comments in general) is contextual.
