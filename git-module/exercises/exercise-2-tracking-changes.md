# Exercise 2: Tracking Changes

## Objective
Practice making multiple commits and understanding how Git tracks file changes.

## Setup
Start with the repository from Exercise 1, or create a new one with a `notes.txt` file.

## Steps

1. **Modify an existing file**
   ```bash
   echo "Git is a distributed version control system." >> notes.txt
   ```

2. **Check what changed**
   ```bash
   git status
   git diff
   ```

3. **Stage and commit the change**
   ```bash
   git add notes.txt
   git commit -m "Add definition of Git to notes"
   ```

4. **Make another change**
   ```bash
   echo "Created by Linus Torvalds in 2005." >> notes.txt
   ```

5. **View the difference again**
   ```bash
   git diff
   ```

6. **Commit the second change**
   ```bash
   git add notes.txt
   git commit -m "Add Git creation info to notes"
   ```

7. **Review your commit history**
   ```bash
   git log --oneline
   ```

## Questions
- What does `git diff` show you?
- How does the output of `git log --oneline` differ from `git log`?
- Why are good commit messages important?

## Challenge
Create a file called `git-commands.txt` and add Git commands you've learned, committing after each addition.