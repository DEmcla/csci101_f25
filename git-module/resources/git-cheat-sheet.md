# Git Command Cheat Sheet

## Repository Setup
```bash
git init                    # Initialize a new Git repository
git clone <url>             # Clone a remote repository
```

## Basic Workflow
```bash
git status                  # Check repository status
git add <file>              # Add file to staging area
git add .                   # Add all files to staging area
git commit -m "message"     # Commit staged changes
git log                     # View commit history
git log --oneline          # Compact commit history
```

## Viewing Changes
```bash
git diff                    # Show unstaged changes
git diff --staged          # Show staged changes
git show <commit-hash>     # Show specific commit details
```

## Remote Repositories
```bash
git remote add origin <url> # Add remote repository
git push -u origin main     # Push and set upstream branch
git push                    # Push to remote (after upstream set)
git pull                    # Pull changes from remote
git remote -v              # List remote repositories
```

## Useful Tips
- Write clear, descriptive commit messages
- Commit early and often
- Use present tense in commit messages ("Add feature" not "Added feature")
- Check `git status` frequently
- Use `git log --oneline` for quick history overview