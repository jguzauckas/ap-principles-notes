# git Branches

Right now we are using git very lineally, meaning we make changes and move forward in time, and can revert those changes to move backwards in time, but everything is happening consecutively, so moving backwards and forwards is very simple.

Let's add some complexity to this so that we have more opportunities open to us through the concept of **branching**

---

## The Process of Branching

In the following diagram, each gray box represents a commit in a repository, where 1 is the initial commit (the creation of the repository), and 2 and 3 are subsequent commits in that repository. If needed, we could revert the repository to a previous commit, say if you need to remove sets of changes to start fresh on an issue. Note that the arrows between commits move backwards, as a commit contains a reference to the commit it came after so it knows the order of things.

![Diagram 1 - Basic Commits](pictures/1.png)

Sometimes though, we want to branch out and try to make a change to one section while ignoring the rest and be able to go back to the older state to work on other things, without losing that special progress.

### The `main` Branch

Conveniently enough, git has a feature for this called **branching**. Every git repository has at least one branch, which is named `main` by default (this is where `git push origin main` comes from).

Branches are stored as a pointer to a commit. By default, your `main` branch points to the most recent commit you've made, so it knows about the most recent version of files.

In the following diagram, the yellow box represents a branch pointer within our sample repository, with its name labeled. We can see it points to commit 3, as the most recent commit.

![Diagram 2 - main Branch](pictures/2.png)

### The `HEAD` Pointer

The branch you are currently looking at, which again by default has been `main`, has a special pointer called `HEAD` pointing to it to tell git where you are currently looking in a repository's history.

If and when you move your `main` branch back in time to a different version of things, the `HEAD` branch follows.

In the following diagram, the pink box now represents the `HEAD`, which we can see pointing to the `main` branch, which still points to commit 3. So git uses this `HEAD` pointer to determine what version of everything we are looking at.

![Diagram 3 - HEAD Branch](pictures/3.png)

### `git branch`

We can add new branches whenever we'd like using the `git branch` command and following it with the name we'd like to assign to our branch. To name a branch, we typically try to use a name that helps give context to why we needed a branch. A basic name could be `testing`. Running the command `git branch testing`, we create a new branch `testing`, though from our perspective it looks like nothing changed.

In the following diagram, we see the results of our branch creation. The new branch `testing` is pointing to the same commit as our branch `main`, and the `HEAD` has not changed, as just creating a branch does not change your perspective to that branch.

![Diagram 4 - Adding New Branch](pictures/4.png)

### Moving the `HEAD` Pointer

Any changes we make and commit right now will still affect the `main` branch, as that's where the `HEAD` is pointing. If we want to leave the `main` branch and work with our new `testing` branch, we can move the `HEAD` pointer with the `git checkout` command, which is followed by the name of the branch we want to move to, in this case `testing`. Running the command `git checkout testing`, successfully moves `HEAD` to point to `testing`, though again from our perspective it looks like nothing changed.

In the following diagram, we see the results of moving `HEAD`. Nothing changed from our perspective because even though `HEAD` is pointing at `testing` instead of `main`, `testing` and `main` were pointing at the same commit: commit 3.

![Diagram 5 - Moving HEAD](pictures/5.png)

### Making a Commit on a Branch

At this point any changes and commits we make will be under the `testing` branch and leave the `main` branch behind on commit 3. Let's say we make some changes and commit them, creating commit 4. Note that this commit feels no different from commits on the main branch, and the commands look exactly the same.

The following diagram shows how git sees the repository. The new commit 4 points back to commit 3 as the commit that came before it, but `main` did not follow along, and is staying at commit 3. Anyone looking at main in the future (including yourself) will not see the changes made within the `testing` branch.

![Diagram 6 - Making New Commit on Branch](pictures/6.png)

### Moving the `HEAD` Pointer

The power of branches is that if we put our work in the `testing` branch on hold for a moment, we could continue working on `main` from the commit 3 versions, or even create another branch to work with. To switch back to `main` we use the `git checkout` command again, citing the `main` branch as the branch we want `HEAD` to switch to. After running `git checkout main`, our repository would change to show the information stored in commit 3, and not our more recent information from commit 4.

The following diagram shows how git perceives the repository now, with the only difference being that `HEAD` is now looking at `main` instead of `testing`, and therefore sees the information from commit 3 rather than 4.

![Diagram 7 - Moving HEAD](pictures/7.png)

### `git merge`

Branches are great for developing software and testing implementations, but we don't want to leave our new code off in its own branch forever. Let's say we are ready to implement the changes in commit 4 after testing. To combine the information from `testing` and implement it in `main`, we do what we call a **merge**. This is a command we need to be more careful with, as it can make significant changes to a repository.

To make a merge, you first want to make sure that `HEAD` is pointing to the branch you want to merge **into**, which we could also think of as the branch you want to hold all the new information. This is often `main`, and we know based on the previous diagram that `HEAD` is currently pointing to `main`, so we are all set to continue. The command is `git merge`, followed by the name of the branch we want to merge changes from, which for us in this case is the `testing` branch. Running the command
`git merge testing`, results in the repository updating to show a combination of the original material from commit 3 and any new/changed material from commit 4, all put together, or **merged**.

The following diagram shows how git perceives the repository now, and since our merge was simple, it just pulled `main` (and therefore `HEAD`) over to commit 4 so now they are looking at the same information, and we successfully merged the changes from the `testing` branch into our `main` branch.

![Diagram 8 - Merging Branch into main](pictures/8.png)

### Deleting Branches

When merging in changes like we just did, we'll often end up with a branch that has fulfilled it's purpose and is no longer needed. In this case, since we've merged the changes from `testing` into `main`, and don't have a particular purpose for further use of `testing`, we are ready to get rid of it as it's not tracking anything useful.

To delete branches, we use the same `git branch` command, with an option using a hyphen `-`. The option we will use is `-d`, which stands for delete, in conjunction with the name of the branch we are deleting: `testing`. Since our `HEAD` is pointing at `main`, we will not notice anything changing when we run the command `git branch -d testing`.

The following diagram shows how git perceives the repository now, which has the only change of our `testing` branch being no longer present.

![Diagram 9 - Deleting Branches](pictures/9.png)

It is important to note that our system of branching, making changes, and then merging back in could happen with
more than one commit. Often, branches will involve multiple commits making a variety of changes, and you can merge
all of them into the `main` branch at once as if it was just a single commit.
