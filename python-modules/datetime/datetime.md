# `datetime` Module

The `datetime` module in Python is a basic module that offers easier interactions with dates and times that are not otherwise available in Python. In this section, we'll look through some of the opportunities that `datetime` provides to us.

All of the sample code provided in this file is in the datetime-samples.py Python file for you to run, modify, and otherwise investigate.

---

## `import datetime`

As with any module, our first step to utilizing it is to `import` it! With `datetime`, we will utilize the `from` keyword to only import the `datetime` class contained within it.

```python
from datetime import datetime
```

As odd as this looks, `datetime` has a lot of potential classes like `date`, `time`, `datetime`, etc. so we are only importing the `datetime` class to make things simpler for ourselves.

---

## `datetime` Objects

For some background, `datetime` objects hold a lot of information:

- `year` - Year of the date
- `month` - Month of the date (1 for January, 12 for December)
- `day` - Day of the date
- `hour` - Hour of the time (24 hour time, so 2 PM is 14)
- `minute` - Minute of the time (0 to 59)
- `second` - Second of the time (0 to 59)
- `microsecond` - Millionths of a second of the time (0 to 999999)
- `tzinfo` - Timezone information

This means we can have extremely precise information about a date and time!

To create a datetime object, you would use a constructor like the classes we made:

```python
my_date = datetime(2022, 10, 31, 14)
print(my_date)
```

You are required to give a `year`, `month`, and `day` in the constructor, and everything after (`hour` and beyond in our list) is not required, but can be included to be more precise! Based on the attributes above, we expect this to be 10/31/2022 at 2 PM:

```
2022-10-31 14:00:00
```

We can see here an example of the datetime `__str__()` method, as it printed out a nice simple version of the date and time.

---

## `now()`

The `now()` function returns a `datetime` object using the current system date and time (pulling it from your computer!). We can use this to create an object to work with based on the current date and time when you run a program:

```python
current_date = datetime.now()
print(current_date)
```

At the time of writing, this produced the following output:

```
2022-10-31 00:35:40.873405
```

---

## Comparing Datetimes

We can use our typical math comparison operators (such as `==`, `>`, and `<`) to compare two datetimes. Here is an example using our `my_date` and `current_date` variables we created above:

```python
print(f"{my_date} is greater than {current_date} is {my_date > current_date}")
```

At the time of writing, this produced the following output:

```
2022-10-31 14:00:00 is greater than 2022-10-31 00:38:40.447068 is True
```

---

To learn more about everything offered by the `datetime` module in Python, check out the official documentation [here](https://docs.python.org/3/library/datetime.html).
