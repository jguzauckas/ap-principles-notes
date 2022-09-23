Setting Local Git Username:
- Open Git Bash and enter the command (with your username):

git config --global user.name "jguzauckas"
- For simplicity, use your GitHub username as your local Git username.
- You can check if you set your local username properly:

git config --global user.name

***

Linking Git to your GitHub Account:
- Log in to GitHub in a browser.
- At the top right, click on your icon and from the drop-down menu select “Settings”.
- On the left side menu of settings, under the “Access” section, select “Emails”
- Scroll down and make sure the check box next to “Keep my email addresses private” is checked.
- Underneath the check box, it should have a paragraph explaining that GitHub will hide the email address linked to your account. Copy the email address given in that paragraph.
  - It should have the format “########+username@users.noreply.github.com”
  - For example, mine is “75325154+jguzauckas@users.noreply.github.com”
- In Git Bash, enter the following command (with your email):

git config --global user.email "75325154+jguzauckas@users.noreply.github.com"
- In the quotes, type in the email address you copied from GitHub.
- You can check if you set your email properly:

git config --global user.email


Creating a Personal Access Token (PAT):
Log in to GitHub in a browser.
At the top right, click on your icon and from the drop-down menu select “Settings”.
On the left side menu of settings, scroll down to the last options and select “Developer settings”.
On the left side menu of developer settings, select “Personal access tokens”.
Click the blue text highlighted “Generate a personal access token”.
On the “New personal access token” page, fill in the following:
Note: “Computer Lab Desktop”
Expiration: Custom… 06/30/2023
Select all leading checkboxes.
Select “Generate token” at the bottom of the page.
This should return you to the “Personal access tokens” page.
Copy the displayed token, do not close this tab for the time being.
Open a notepad and paste the token there so we can’t lose it from our clipboard.


Linking Git to GitHub:
Log in to GitHub in a browser.
On the left side where it says “Recent Repositories”, click on the repository titled “Windsor-CT-Computer-Science/git-github-fundamentals-username”.
On the right side, select the colored button “Code”
Check to make sure you’ve pasted your PAT somewhere so we don’t overwrite and lose it!
It should automatically have “HTTPS” highlighted, click the copy button next to the displayed link to copy it to your clipboard.
In Git Bash, enter the following command (with your link):
git clone https://github.com/Windsor-CT-Computer-Science/
git-github-fundamentals-jguzauckas.git
A window should pop up titled “Connect to GitHub”.
Select “Token” next to “Browser/Device”.
Copy and paste your PAT into this box and click “Sign in”.


Setting up Visual Studio Code:
Open Visual Studio Code.
Select File → Preferences → Settings
Or use CTRL + ,
At the top right, there should be a few buttons, click on the one titled “Open Settings (JSON)”.
The resulting file opened should just have curly brackets
Between the curly brackets, make a new line and paste in the following:
"terminal.integrated.profiles.windows":{"Git Bash":{"path":"C:\\Program Files\\Git\\bin\\bash.exe"},  },
"terminal.integrated.defaultProfile.windows": "Git Bash"
Use CTRL + S to save the changes.
Now close Visual Studio Code in its entirety.
Reopen Visual Studio Code.
Select Terminal → New Terminal
Or use CTRL + SHIFT + ` (key above tab/left of 1)
The Terminal will open at the bottom of the screen and should now function as an integrated Git Bash for us.


Testing the Git-GitHub Link:
At the top of Visual Studio Code, select File → Add Folder to Workspace…
In the Explorer window that opened, select the repository we cloned earlier, titled “git-github-fundamentals-username” and click “Add”.
On the left side, click the large icon titled “Explorer”.
Or use CTRL + SHIFT + E
Click on “README.md” to open the editor.
You should see the unformatted text that made up the article you read for homework.
At this point, we have not made any changes to the repository, so if we check the status, we should be up to date. Enter the following command:
git status
This should yield a multi-line message detailing that you are up to date with the original repository.
In the open editor for “README.md”, let’s add a line at the top saying that we’ve edited this document:
I have edited this document.

# :wave: The Basics of GitHub
…
You’ll notice that lines 1 and 2 are highlighted in green, indicating that they are newly added from the original file.
Use CTRL + S to save the changes to “README.md”.
Now in our Git Bash, enter the same command from earlier to check the status. We expect it to let us know that there have been changes made:
git status
This should yield a multi-line message detailing that you have modified “README.md” and that the changes have not been committed.
Now we want to prepare to commit changes to this repository by adding “README.md” to the list of files to commit:
git add README.md
If this works, no message should pop up.
Now we check the status again:
git status
This should yield a multi-line message detailing that you have prepared the updated “README.md” file for committing.
We are ready to commit our changes. Use the following command:
git commit -m “Updated README.md to show I can edit.”
Feel free to change the text in quotes to reflect what you’ve done. It should describe the changes included in the commit.
A line should show repeating your commit message (hence -m), and say that a file has been changed!
Open GitHub in a browser and open this repository!
Has the README.md updated with our change?
Let’s check our status again:
git status
It should now say that you are ahead of ‘origin/main’ by 1 commit.
Git allows you to prepare a set of changes with commit, and then update the GitHub repository with the “push” command (it actually suggests this in the output!)
Let’s send our commits to the remote repository on GitHub:
git push origin main
This should yield a multi-line message detailing it’s process for uploading the commits.
Now open GitHub in a browser and open this repository!
Now you’ll notice a message next to the file “README.md” that shows your commit message.
You should also see your changes to “README.md” in the preview below!
