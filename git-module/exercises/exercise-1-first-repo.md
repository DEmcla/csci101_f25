# Exercise 1: Creating Your First Repository

## Objective
Learn to initialize a Git repository and make your first commit.

## Steps

1. **Create a project directory**
   ```bash
   mkdir my-first-project
   cd my-first-project
   ```

2. **Initialize Git repository**
   ```bash
   git init
   ```

3. **Create a simple file**
   ```bash
   echo "Hello, Git!" > hello.txt
   ```

4. **Check repository status**
   ```bash
   git status
   ```

5. **Add file to staging area**
   ```bash
   git add hello.txt
   ```

6. **Make your first commit**
   ```bash
   git commit -m "Add hello.txt with greeting message"
   ```

7. **View commit history**
   ```bash
   git log
   ```

## Questions to Consider
- What did `git status` show before and after adding the file?
- Why do we need to add files to the staging area before committing?
- What information does `git log` provide?

## Challenge
Add another file called `about.txt` with information about yourself, then commit it with an appropriate message.