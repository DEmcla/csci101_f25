# Git Workflow Guide for Beginners

## The Basic Git Workflow

### 1. Initialize or Clone
**New project:**
```bash
git init
```

**Existing project:**
```bash
git clone <repository-url>
```

### 2. Make Changes
- Create, edit, or delete files using your preferred text editor
- Work on your project normally

### 3. Check Status
```bash
git status
```
This shows:
- Which files are modified
- Which files are staged for commit
- Which files are untracked

### 4. Stage Changes
```bash
git add <filename>     # Stage specific file
git add .              # Stage all changes
```

### 5. Commit Changes
```bash
git commit -m "Descriptive message about what you changed"
```

### 6. Push to Remote (if using GitHub/etc.)
```bash
git push
```

## Key Concepts

**Working Directory**: Where you edit files
**Staging Area**: Files prepared for the next commit
**Repository**: The complete history of your project

## Best Practices

1. **Commit often** - Small, focused commits are better than large ones
2. **Write good messages** - Future you will thank present you
3. **Check status frequently** - `git status` is your friend
4. **Pull before push** - When working with remotes, get latest changes first

## Common Scenarios

**Undo last commit (keep changes):**
```bash
git reset --soft HEAD~1
```

**See what changed in a file:**
```bash
git diff <filename>
```

**View commit history:**
```bash
git log --oneline
```