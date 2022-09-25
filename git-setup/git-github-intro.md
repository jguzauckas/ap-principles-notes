Scenario:

- You are working on a small project on your computer, learning the basics of Python. You are using Git locally as you work to help keep track of your project. You realize early on that you would like to get this repository on GitHub too so that you can access it remotely. What can we do?
- This is going to be an opportunity to practice some skills related to Git and GitHub, and make our first Python program!

---

Step 0: More setup

- We want to change one default setting with Git to be more appropriate.
- The default branch name for new repositories is `master`, which is decidedly less appropriate in the modern day (despite being accurate in computer-specific language).
  - The new widely-accepted default name is `main` instead, except in instances where legacy systems require `master` to be used.
- Open Git Bash
- Enter the following command:

```
git config --global init.defaultBranch main
```

- To check if it worked, enter the command without the last “main”:

```
git config --global init.defaultBranch
```

---

Step 1: Creating a fresh local repository

- Open VS Code
- Select Terminal → New Terminal
  - Or use CTRL + SHIFT + ` (key above tab/left of 1)
  - This should be a Git Bash based on the work we did last class!
- Check to make sure you aren’t in any other active projects, you can tell by the header in your Git Bash. It should look like this:

```
john@DESKTOP-23C3071 MINGW64 ~
```

- If there is anything after the “~”, it means we are in a repository and need to close it before continuing. It might look something like this:

```
john@DESKTOP-23C3071 MINGW64 ~/git-github-fundamentals-name
```

- To change this, you need to close the VS Code workspace. At the top go File → Close Workspace (you don’t need to save).
- If you reopen the terminal with Terminal → New Terminal or CTRL + SHIFT + `, you should now see the correct header for no repository.
- Now that we are not in an active repository, we are able to create a new one. To make a new repository, we first need to make a new folder. We want this folder to have the name of our future repository. Use this command:

```
mkdir first-python-project
```

- `mkdir` is the command for **m**a**k**ing a new folder (or **dir**ectory), and the rest is our name for it. I am using dashes (-) instead of spaces, since GitHub will do that with a repository name anyways.
- To check if we successfully created our folder, we can use the following command to check if we can see it:

```
ls
```

- `ls` is short for **l**i**s**t, meaning we display a list of files and folders in our current directory.
- At this point, first-python-project is just a folder/directory and not a repository. To change this, we need to navigate into the folder, using the following command:

```
cd first-python-project
```

- `cd` is the command for **c**hanging **d**irectory/folder, so we gave it a folder it can currently see (listed in `ls`) to navigate to.
- Your Git Bash header should now look like this:

```
john@DESKTOP-23C3071 MINGW64 ~/first-python-project
```

- At this point, we are ready to initialize our directory into a Git repository. To do this, we use the following command:

```
git init
```

- It should say:

```
Initialized empty Git repository in [filepath]
```

- You will notice a change to your header:

```
john@DESKTOP-23C3071 MINGW64 ~/first-python-project (main)
```

- Those two pieces show us that we have successfully created a Git repository out of this directory, with the branch named main.

---

Step 2 - Creating the same repository in GitHub

- Log in to GitHub in a browser.
- On the left side where it says “Recent Repositories”, click the colored button titled “New”
- Make sure the selected Repository template is “No template”.
- For repository name, use the same name as our local Git repository,

```
first-python-project
```

- You do not need to fill out a description but can if you would like to.
- Select “Private” instead of “Public” so that this repository is not open to anyone to see.
- Make sure the checkbox next to “Add a README file” is not checked.
- Make sure the chosen .gitignore template is “None”.
- Make sure the chosen license is “None”.
- At this point, you can click the colored button at the bottom labeled “Create repository”.
- Along the list of sections for this repository, go to “Settings”
- Under the “Access” section on the left side, select “Collaborators”
- In the middle, select the colored button labeled “Add people”
- Enter Mr. G’s GitHub username, `jguzauckas`, and pick my profile.
- Click the colored button labeled “Add jguzauckas to this repository”.
- This way, I’ll be able to see your repository and check your progress. You will want to do this for any repository you make for this class!

---

Step 3 - Adding a README.md file to our local repository (and committing)

- Open Visual Studio Code.
- At the top left, select File → Add Folder to Workspace…
- From the explorer, click once on our project folder `first-python-project` and click “Add” at the bottom right.
- Open a terminal (if not already opened) with Terminal → New Terminal (or the shortcut CTRL + SHIFT + `).
- The Git Bash should automatically show the correct repository:

```
john@DESKTOP-23C3071 MINGW64 ~/first-python-project (main)
```

- We are going to add our “README.md” file using the Git Bash terminal, using the following command:

```
touch README.md
```

- Select the button at the top left labeled “Explorer” (or use the shortcut CTRL + SHIFT + E).
- Clicking the dropdown on our folder should now show a `README.md` file, with a U next to it meaning it is untracked.
- If we enter our status command, we should see that it knows the `README.md` file is there, but is not tracking it:

```
git status
```

- To tell Git to track the `README.md` file, we need to use the add command:

```
git add README.md
```

- Now we can check to make sure it is tracking the file by using the status command again:

```
git status
```

- Now we are ready to make our initial commit to this local repository:

```
git commit -m “Added README.md file”
```

---

Step 4 - Linking the local repository and the GitHub repository

- Log in to GitHub in a browser.
- On the left side, where it says “Recent repositories”, you should find your recently created `username/first-python-project` repository and click on it.
- You should see a screen that has “Quick setup” on it. Click the copy button next to the link on screen to copy the link to your clipboard.
- In Visual Studio Code, make sure you have a Git Bash terminal open with it displaying our local repository:

```
john@DESKTOP-23C3071 MINGW64 ~/first-python-project (main)
```

- We are going to tell Git about the GitHub repository using the remote add origin command:

```
git remote add origin [url]
```

- To complete the link, we need to push our initial commit to GitHub’s repository:

```
git push -u origin main
```

- We use the -u to set the upstream tracking reference for Git to the GitHub repository.
- At this point, you should be able to go back to your repository on GitHub in the browser and refresh the page (circular arrow at the top left or F5) and it will show your README.md. Now Git and GitHub are linked.

---

Step 5 - Actually Programming! Making a basic `HelloWorld.py` application

- You should have Visual Studio Code open, with the `first-python-project` folder visible in the Explorer window on the left side, and a Git Bash terminal open at the bottom with our repository included in the header.
- In Git Bash, use the touch command to create a Python file:

```
touch HelloWorld.py
```

- `.py` is the file extension for Python files.
- You should see this pop up in the Explorer window immediately.
- Now if you click on `HelloWorld.py` in the Explorer window, it will open up a blank file in the editor.
- You may get a prompt here to install Python extensions, say yes and follow any prompts it gives you!
- We are going to pause before we actually write any Python to practice another commit. We are going to commit having created the `HelloWorld.py file`, not necessarily having filled it in yet. The commands for this would look like:

```
git status
git add HelloWorld.py
git status
git commit -m “Added HelloWorld.py”
git status
git push origin main
git status
```

- Note: As we get more comfortable with Git, the constant git status calls will not be as necessary. It is important to check periodically to make sure that we understand how Git is tracking our work, but it is not necessary between every step.
- Now we are ready to write some code. We are going to start very simple with a Hello World program. This will only take one line in the `HelloWorld.py` file:

```
print(“Hello, World!”)
```

- Once you have entered the print statement, save the file using CTRL + S.
- Now we are going to test that it works by running the file by selecting the triangular button at the top right with the label “Run Python File”
  - It is going to open a new terminal tab at the bottom titled “Python”, and your output should appear there.
- Now we can’t see our previous Git Bash anymore, so we are going to use the names on the bottom right to select “bash” so we can see our previous commands.
- Now we are ready to commit our updated HelloWorld.py file:

```
git status
git add HelloWorld.py
git status
git commit -m “Added print to HelloWorld.py”
git status
git push origin main
git status
```

- Now that we have a working Python file, we should update our `README.md` file to say what we have in this repository. Click on `README.md` in the Explorer to open it for editing.
- In your README.md, write a couple of lines about what this repository is for. Example:

```
This is a practice repository for me to practice my Git skills and start learning Python.
The HelloWorld.py file is a simple program to print the phrase “Hello, World!”
```

- Use CTRL + S to save your `README.md`
- Now we have to commit our updates to `README.md`:

```
git status
git add README.md
git status
git commit -m “Updated README.md to include new features.”
git status
git push origin main
git status
```

- At this point you should be able to check this repository in GitHub and see your `README.md` and `HelloWorld.py` files with everything updated!
