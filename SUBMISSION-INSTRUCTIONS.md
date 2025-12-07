# Submission Instructions

## Prerequisites
Complete **Session 1 (github-setup-guide.html)** before starting this tutorial.

## Overview
This tutorial has three pull requests. Each pull request is a separate, isolated submission containing only the materials for that specific assignment.

**Important:** Each pull request should only include files from its corresponding folder:
- PR 01 → only `pullrequest_01/` files
- PR 02 → only `pullrequest_02/` files
- PR 03 → only `pullrequest_03/` files

---

## The Three Pull Request Assignments

Each submission requires a `README.md` file plus the assigned file type.

### PR 01: Word Document
**Files required in your subfolder:**
- `README.md` - Describes your submission
- `Assignment.docx` - A Word document

**Purpose:** Learn the basic submission workflow with a familiar file type.

**Example folder structure:**
```
pullrequest_01/john_smith/
  README.md
  Assignment.docx
```

---

### PR 02: Python Program
**Files required in your subfolder:**
- `README.md` - Describes what your program does
- `helloWorld.py` - A simple Python program

**Purpose:** Submit your first code file! Your Python program should print "Hello, World!" when run.

**Example folder structure:**
```
pullrequest_02/john_smith/
  README.md
  helloWorld.py
```

**Example helloWorld.py:**
```python
# My first Python program
# Author: John Smith

print("Hello, World!")
```

---

### PR 03: Markdown File
**Files required in your subfolder:**
- `README.md` - Describes your submission
- `markdown_demo.md` - A Markdown file demonstrating formatting

**Purpose:** Learn Markdown syntax by creating a formatted document. This reinforces why README.md files are powerful!

**Example folder structure:**
```
pullrequest_03/john_smith/
  README.md
  markdown_demo.md
```

**Your markdown_demo.md must demonstrate:**
- A heading (`#`)
- A subheading (`##`)
- A bulleted list (`-`)
- **Bold** text (`**bold**`)
- *Italic* text (`*italic*`)

**Example markdown_demo.md:**
```markdown
# Markdown Demo - John Smith

## What is Markdown?
Markdown is a **lightweight** markup language for creating *formatted* text.

## Common Uses
- README files
- Documentation
- Notes
```

---

## README.md Template

Every submission needs a README.md file. Use this template:

```markdown
# PR 0X Submission - Your Name

## Description
Brief description of what you're submitting.

## Files Included
- `filename.ext` - Description of this file

## Author
Your Name
CSCI 101 - Fall 2025
```

---

## Submission Process

### 1. Update Your Fork
Before starting each assignment:
```bash
git fetch upstream
git checkout main
git merge upstream/main
git push origin main
```

### 2. Create a Branch
```bash
git checkout -b pr01_firstname_lastname
```

### 3. Create Your Subfolder
```bash
mkdir pullrequest_01/firstname_lastname
```

### 4. Add Your Files
Add your `README.md` and assignment file to your subfolder.

### 5. Commit and Push
```bash
git add pullrequest_01/firstname_lastname/
git commit -m "Add PR 01 submission - FirstName LastName"
git push origin pr01_firstname_lastname
```

### 6. Create Pull Request on GitHub
1. Go to your fork on GitHub
2. Click "Compare & pull request"
3. **Set base branch to `submissions`** (not main!)
4. Title: `PR 01 Submission - FirstName LastName`
5. Click "Create pull request"

---

## Important Guidelines

### Subfolder Naming
```
firstname_lastname
```
- Use lowercase
- Use underscore between names
- Example: `john_smith`

### Branch Naming
```
pr0#_firstname_lastname
```
- Example: `pr01_john_smith`, `pr02_john_smith`

### Pull Request Title
```
PR 0# Submission - FirstName LastName
```
- Example: `PR 01 Submission - John Smith`

---

## Common Issues

### "Permission Denied" When Pushing
- Make sure you're pushing to YOUR fork
- Check with: `git remote -v`

### Need to Update Your Submission
```bash
git add pullrequest_01/firstname_lastname/
git commit -m "Update PR 01 submission"
git push origin pr01_firstname_lastname
```
The PR will automatically update.

### Pull Request Going to Wrong Branch
- Change base branch to `submissions`, not `main`

---

## Branch Structure

- `main` - Course materials (sync from here)
- `submissions` - Where PRs get merged (submit PRs here)

---

*Questions? Ask during office hours!*
