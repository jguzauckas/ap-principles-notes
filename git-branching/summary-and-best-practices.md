# Summary and Best Practices

## Summary

In summary, branching is a way for us to make a separate set of changes in a git repository, potentially across multiple commits, and then merge them into the primary parts of a project when we are ready. This allows these changes to not affect the rest of the project until we are ready for them to do so, while still enjoying the benefits of git while working on them.

The basic process takes the following form:

- Create a new branch
- Move the `HEAD` pointer to the new branch
- Make and commit changes on new branch
- Move the `HEAD` pointer back to `main`
- Merge changes into `main`
- Delete the new branch

---

## Best Practices

Here are a couple of best practices to consider when using branching:

- `git fetch` and `git pull` before making any merges into `main`, in case you are missing any changes from GitHub.
- Always check which branch you are on before committing any changes to make sure you are in the correct branch.

---

## Commands To Remember

For all of the following commands, the blank (`_______`) should be filled in with the name of a branch.

To create a branch:

```bash
git branch _______
```

To move the `HEAD` pointer:

```bash
git checkout _______
```

To merge a branch into the current branch:

```bash
git merge _______
```

To delete a branch:

```bash
git branch -d _______
```

To push a branch to GitHub:

```bash
git push origin _______
```