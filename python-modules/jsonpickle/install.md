# JSON vs. Python Objects

JSON works really well with the basic types in Python, but runs into issues with custom Classes/Objects, since according to JSON, dictionaries are objects.

`jsonpickle` is a module that offers tools to turn our custom classes and objects into something JSON can work with.

All of the sample code provided in this file is in the install.py Python file for you to run, modify, and otherwise investigate.

---

## Installing `jsonpickle`

This is our first module that is not already included in our install of Python, which means we need to tell the computer to add it so that we can `import` and use it.

To install a module, we use the **p**ackage **i**nstaller for **p**ython, which is shortened to `pip`.

`pip` is an option to select when installing Python, but even if it was not selected, Python comes with the means to enable it afterwards.

To start, you can test if you have `pip` enabled, in git bash try the following command:

```bash
pip install jsonpickle
```

If this goes through and walks through a few steps, `pip` is enabled and you are good to go. If this produces the following error:

```
pip: command not found
```

then we are going to have to enable `pip` ourselves.

First step to enabling `pip` is to make sure Python has downloaded and updated `pip` to the latest version. To do this, we use two separate commands in git bash:

```bash
py -m ensurepip --upgrade
```

and then:

```bash
py -m pip install --upgrade pip
```

Now we are ready tell Windows how to find `pip`, via the `path`. First step is to open the Windows Run dialogue by either searching "run" or hitting Windows + R. Once the dialogue is open, type `sysdm.cpl` and hit enter or click "OK".

This should open up the `System Properties` window, where we'll want to go to the `Advanced` tab at the top.

At the bottom right of the `Advanced` section, there should be a button titled `Environment Variables...`. Click on it.

In the new window titled `Environment Variables`, there are two main sections that have boxes drawn around them: `User variables for ____` and `System Variables`. Regardless of your access on your computer, we will be working with the first section titled `User variables for ____`.

Click on the variable labeled `Path`, which should highlight the whole row blue. Now hit the `Edit...` button, which should open yet another window titled `Edit environment variable`.

Along the right side, hit the `New` button. In the area to write that becomes highlighted, paste the following, two different times:

```
%USERPROFILE%\AppData\Roaming\Python\Python310\Scripts
```

```
%USERPROFILE%\AppData\Local\Programs\Python\Python310\Scripts
```

On each subsequent window, hit the "OK" button until all of the `System Properties`-related windows are closed.

Now in `git bash`, you should be able to enter the following command without any issues:

```
pip install jsonpickle
```

If you are still having issues please reach out to Mr. Guzauckas.

---

## `import`

As this is a module, we will want to import it alongside our normal `json` module, so the top of your program should look like this:

```python
import json
import jsonpickle
```
