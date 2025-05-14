Clone the repo
```bash
git clone [Repo link]
```

Develop your feature/fix

Create a branch if there is not one alread (keep them simple - logic, ui, misc)

Checkout your branch, add your changes, commit with good simple message of changes
```bash
git checkout [branch name]
git add .
git commit -m "details of changes"
```

Switch to main and pull latest version in repo (for conflict resolution)
```
git checkout main
git pull --rebase origin main
```

Merge your commit.

We are not doing Pull Requests for simplicity and faster development. 

We're trusting that you wont push breaking code. If you're unsure reach out to Rodrigo Cornidez for help.
```bash
git merge [branch name]
```

resolve any conflicts with your merge if any are present.

push updated main branch to repository
```bash
git push origin main

```