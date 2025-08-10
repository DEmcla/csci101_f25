# Your First Git Repository
*CSCI 101 - Git Module - Lesson 3*

---

## Learning Objectives
By the end of this lesson, you will:
- Create your first Git repository from scratch
- Learn the 5 essential Git commands every developer uses
- Make your first commit with a meaningful message
- Understand the basic Git workflow

**Time Estimate:** 45 minutes  
**Prerequisites:** Git installed and configured (Lesson 2 completed)

---

## The 5 Essential Git Commands

Before we start, let's focus on just **5 commands** that handle 90% of daily Git usage:

| Command | What It Does | When You Use It |
|---------|--------------|-----------------|
| `git init` | Creates a new repository | Once per project |
| `git status` | Shows what's changed | All the time! |
| `git add` | Stages files for commit | Before every commit |
| `git commit` | Saves changes permanently | When work is complete |
| `git log` | Shows commit history | To see what you've done |

**That's it!** Master these 5 commands and you can use Git effectively.

---

## Creating Your First Repository

### Step 1: Choose Your Location

First, let's create a good place for your Git projects:

**All Platforms:**
```bash
# Navigate to your home directory
cd ~

# Create a folder for your CS projects
mkdir csci-projects
cd csci-projects
```

**What this does:**
- `cd ~` goes to your "home" directory (like `/Users/yourname` on Mac/Linux, or `C:\Users\yourname` on Windows)
- `mkdir` creates a new folder called "csci-projects"
- `cd csci-projects` moves into that folder

### Step 2: Create Your Project Folder

```bash
# Create a folder for your first Git project
mkdir my-first-repo
cd my-first-repo
```

### Step 3: Initialize the Git Repository

Here's the magic command:
```bash
git init
```

**You should see:**
```
Initialized empty Git repository in /path/to/your/folder/.git/
```

**🎉 Congratulations! You just created your first Git repository!**

### What Just Happened?
- Git created a hidden `.git` folder that stores all version history
- Your folder is now a "repository" (or "repo" for short)
- Git is ready to start tracking changes in this folder

---

## Understanding Git Status

The most important command you'll use is `git status`. Let's try it:

```bash
git status
```

**You should see something like:**
```
On branch main

No commits yet

nothing to commit (create/copy files and use "git add" to track)
```

**What this tells you:**
- **On branch main**: You're on the default branch (like the main timeline)
- **No commits yet**: You haven't saved any versions yet
- **nothing to commit**: There are no changes to save

**💡 Pro Tip:** Run `git status` constantly. It tells you exactly what's happening in your repository.

---

## Creating Your First File

Let's create something to track. We'll start with a simple text file.

### Platform-Specific File Creation

**Git Bash (Windows) or Terminal (Mac/Linux):**
```bash
echo "Hello, Git! This is my first repository." > README.txt
```

**Alternative (All Platforms) - Using a Text Editor:**
1. Open your favorite text editor (Notepad, TextEdit, VS Code, etc.)
2. Create a new file
3. Type: `Hello, Git! This is my first repository.`
4. Save as `README.txt` in your `my-first-repo` folder

### Check Status Again

```bash
git status
```

**Now you should see:**
```
On branch main

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
    README.txt

nothing added to commit but untracked files present (use "git add" to track)
```

**What this means:**
- **Untracked files**: Git sees `README.txt` but isn't tracking changes yet
- Git gives you helpful hints: use `git add` to start tracking

---

## The Git Workflow Explained

Git has a three-step workflow:

```
Working Directory → Staging Area → Repository
     (edit files)  →  (git add)  →  (git commit)
```

### 1. Working Directory
- **What it is**: The folder where you edit files
- **What you do**: Create, modify, delete files normally
- **Current state**: You have `README.txt` here

### 2. Staging Area (The "Shopping Cart")
- **What it is**: Files prepared for the next commit
- **Analogy**: Like a shopping cart - you add items before "checking out"
- **What you do**: Use `git add` to put files here

### 3. Repository (Permanent Storage)
- **What it is**: Where Git permanently stores versions
- **What you do**: Use `git commit` to save staged files forever

---

## Staging Your First File

Now let's move `README.txt` to the staging area:

```bash
git add README.txt
```

**No output is normal** - Git is quiet when commands succeed.

### Check Status Again

```bash
git status
```

**You should see:**
```
On branch main

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
    new file:   README.txt
```

**What changed:**
- `README.txt` is now in the staging area
- Git says "Changes to be committed" - it's ready to save permanently
- The file is highlighted in green (if your terminal shows colors)

---

## Making Your First Commit

A **commit** is like taking a snapshot of your project at a specific moment. Let's create one:

```bash
git commit -m "Add README file with project description"
```

**You should see something like:**
```
[main (root-commit) a1b2c3d] Add README file with project description
 1 file changed, 1 insertion(+)
 create mode 100644 README.txt
```

**🎉 Congratulations! You made your first commit!**

### Understanding the Output
- **[main (root-commit) a1b2c3d]**: Branch name and unique commit ID
- **Add README file...**: Your commit message
- **1 file changed, 1 insertion(+)**: Summary of changes

### About Commit Messages
The `-m "message"` part is crucial. Good commit messages:
- **Start with a verb**: Add, Fix, Update, Remove
- **Are specific**: "Add README file" not "added stuff"
- **Describe WHY**, not just what: "Fix login bug causing crashes"

---

## Viewing Your History

Let's see the history of your repository:

```bash
git log
```

**You should see:**
```
commit a1b2c3dedf1234567890abcdef1234567890abcd (HEAD -> main)
Author: Your Name <your.email@example.com>
Date:   Mon Oct 23 10:30:00 2023 -0500

    Add README file with project description
```

**What this shows:**
- **commit a1b2c3d...**: Unique identifier for this commit
- **Author**: Your name and email (from configuration)
- **Date**: When you made the commit
- **Message**: What you wrote with `-m`

### Compact History View

For a cleaner view, try:
```bash
git log --oneline
```

**Output:**
```
a1b2c3d Add README file with project description
```

Much cleaner for daily use!

---

## Practice: Make Another Commit

Let's practice the workflow with a second file:

### Step 1: Create Another File

**Command line approach:**
```bash
echo "This project helps me learn Git basics." > description.txt
```

**Or create manually** in your text editor and save as `description.txt`

### Step 2: Check Status
```bash
git status
```

You should see `description.txt` as an untracked file.

### Step 3: Stage the File
```bash
git add description.txt
```

### Step 4: Check Status Again
```bash
git status
```

Now it should be in "Changes to be committed."

### Step 5: Commit the File
```bash
git commit -m "Add project description file"
```

### Step 6: View Updated History
```bash
git log --oneline
```

You should now see two commits!

---

## 🎯 Checkpoint: Essential Skills Check

Before moving forward, make sure you can do these tasks **without looking at notes:**

### Test Yourself
1. **Create a new Git repository**
   <details>
   <summary>Solution</summary>
   
   ```bash
   mkdir test-repo
   cd test-repo
   git init
   ```
   </details>

2. **Check repository status**
   <details>
   <summary>Solution</summary>
   
   ```bash
   git status
   ```
   </details>

3. **Stage a file for commit**
   <details>
   <summary>Solution</summary>
   
   ```bash
   git add filename.txt
   ```
   </details>

4. **Make a commit with a good message**
   <details>
   <summary>Solution</summary>
   
   ```bash
   git commit -m "Add filename with specific purpose"
   ```
   </details>

5. **View commit history**
   <details>
   <summary>Solution</summary>
   
   ```bash
   git log --oneline
   ```
   </details>

**Can you do all 5 from memory?** If not, practice a bit more before continuing.

---

## Common Beginner Mistakes (And How to Avoid Them)

### Mistake 1: Forgetting to Stage Files
**Problem:** You make changes but forget `git add`
```bash
# You modify README.txt
git commit -m "Update README"  # This commits nothing!
```

**Solution:** Always check `git status` before committing
```bash
git status           # See what's changed
git add README.txt   # Stage the changes
git commit -m "Update README"  # Now it works
```

### Mistake 2: Poor Commit Messages
**Bad examples:**
- "changes"
- "stuff"
- "fix"
- "asdfgh"

**Good examples:**
- "Add user registration form"
- "Fix calculation error in grade average"
- "Update README with installation instructions"

### Mistake 3: Committing Too Much at Once
**Problem:** Working for hours, then making one giant commit
**Solution:** Commit every time you complete a logical piece of work

### Mistake 4: Not Using `git status` Enough
**Problem:** Being unsure what's staged, what's changed, what's committed
**Solution:** Run `git status` constantly - it's your best friend

---

## Real-World Applications

### For Your Assignments
```bash
# Start working on Assignment 1
mkdir assignment-1
cd assignment-1
git init

# Work on your code...
echo "print('Hello, World!')" > hello.py
git add hello.py
git commit -m "Add basic hello world program"

# Continue developing...
# (edit hello.py to add more features)
git add hello.py
git commit -m "Add user input functionality"

# When ready to submit
git log --oneline  # Review your progress
```

### For Group Projects
```bash
# Each team member starts the same way
mkdir team-project
cd team-project
git init

# Individual work gets committed regularly
git add my-part.py
git commit -m "Implement user authentication module"
```

### For Learning and Experimentation
```bash
# Try different approaches safely
git commit -m "Working version of algorithm"

# Experiment with improvements
# (make changes)
git add .
git commit -m "Attempt optimization - might break things"

# If experiment fails, you can always go back!
```

---

## What You've Accomplished

**🏆 You now know:**
- How to create Git repositories from scratch
- The 5 essential Git commands for daily use
- The three-step Git workflow (working → staging → repository)
- How to write good commit messages
- How to view your project history

**🚀 You can:**
- Track changes in any project
- Create meaningful snapshots of your work
- Never lose work again (as long as you commit!)
- Build a history of your development progress

---

## What's Next?

In the next lesson, we'll dive deeper into the Git workflow. You'll learn:
- How to see exactly what changed in your files
- How to stage only specific parts of files
- How to write better commit messages
- How to handle different types of file changes

But first, make sure you're comfortable with these 5 basic commands. **Practice makes perfect!**

**Continue to:** `lessons/04-the-git-workflow.md`

---

## Quick Reference

### The 5 Essential Commands
```bash
git init          # Create new repository
git status        # Check what's changed (use constantly!)
git add filename  # Stage specific file
git add .         # Stage all changes
git commit -m "message"  # Save changes permanently
git log --oneline # View commit history
```

### The Basic Workflow
```bash
# 1. Make changes to files
# 2. Check what changed
git status

# 3. Stage changes
git add filename

# 4. Commit changes
git commit -m "Descriptive message"

# 5. Repeat!
```

---

*Remember: Git is like riding a bike - it seems complicated at first, but once you get the basic workflow down, it becomes second nature!*