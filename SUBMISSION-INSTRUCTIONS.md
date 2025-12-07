# Course Submission Instructions

## 🚀 First Time Here?
**Start with the [GitHub Tutorial](GIT-SETUP-TUTORIAL.md)** - A complete walk-through that will:
- Help you install Git
- Set up your GitHub account
- Practice making a submission
- Create your first Pull Request

## Overview
This tutorial has five pull requests. Each pull request is a separate, isolated submission containing only the materials for that specific assignment.

**Important:** Each pull request should only include files from its corresponding folder:
- PR 01 → only `pullrequest_01/` files
- PR 02 → only `pullrequest_02/` files
- PR 03 → only `pullrequest_03/` files
- PR 04 → only `pullrequest_04/` files
- PR 05 → only `pullrequest_05/` files

**We will use the professional Fork & Pull Request workflow - the same process used by software developers worldwide!**

## Initial Setup (Do This Once)

### Step 1: Fork the Repository
1. Go to the main course repository on GitHub
2. Click the "Fork" button in the top-right corner
3. This creates YOUR own copy of the repository

### Step 2: Clone Your Fork
```bash
# Clone your fork (not the original!)
# Replace YOUR_USERNAME with your GitHub username
git clone https://github.com/YOUR_USERNAME/csci101_f25.git
cd csci101_f25
```

### Step 3: Set Up the Upstream Remote
```bash
# Connect to the course repository for updates
git remote add upstream https://github.com/csci101_f25/csci101_f25.git

# Verify your remotes
git remote -v
# You should see:
# origin = your fork
# upstream = course repository
```

## Submission Process for Each Pull Request

### 1. Update Your Fork
Before starting each assignment, get the latest updates:
```bash
# Get updates from the course repository
git fetch upstream
git checkout main
git merge upstream/main
git push origin main
```

### 2. Create a Branch for Your Work
```bash
# Create a new branch for your submission
# Format: pr0#_firstname_lastname
git checkout -b pr01_john_smith
```

### 3. Add Your Assignment File
- **File name**: `Assignment_FirstName_LastName.docx`
- **Location**: Place in the appropriate pullrequest folder
- **Example**: `pullrequest_01/Assignment_John_Smith.docx`

### 4. Commit Your Work
```bash
# Add your file
git add pullrequest_01/Assignment_John_Smith.docx

# Commit with a clear message
git commit -m "Add PR 01 submission - John Smith"

# Push to YOUR fork
git push origin pr01_john_smith
```

### 5. Create a Pull Request
1. Go to YOUR fork on GitHub
2. Click "Pull requests" → "New pull request"
3. Make sure:
   - Base repository: Course repository (csci101_f25/csci101_f25)
   - Base branch: main
   - Head repository: Your fork
   - Compare branch: Your PR branch (e.g., pr01_john_smith)
4. Click "Create pull request"
5. **Title your PR**: `PR 01 Submission - FirstName LastName`
6. Add any comments about your submission
7. Click "Create pull request"

## Important Guidelines

### File Naming Convention
**MUST follow this format exactly:**
```
Assignment_FirstName_LastName.docx
```
Examples:
- ✅ `Assignment_John_Smith.docx`
- ✅ `Assignment_Maria_Garcia.docx`
- ❌ `assignment-john-smith.docx` (wrong format)
- ❌ `John Smith Assignment.docx` (wrong format)

### Branch Naming Convention
**MUST follow this format:**
```
pr0#_firstname_lastname
```
Examples:
- ✅ `pr01_john_smith`
- ✅ `pr02_maria_garcia`
- ❌ `PR01-John-Smith` (wrong format)
- ❌ `john_pr01` (wrong format)

### Pull Request Title Convention
**MUST follow this format:**
```
PR 0# Submission - FirstName LastName
```
Examples:
- ✅ `PR 01 Submission - John Smith`
- ✅ `PR 02 Submission - Maria Garcia`

## Common Issues and Solutions

### "Permission Denied" When Pushing
- Make sure you're pushing to YOUR fork, not the course repository
- Check with: `git remote -v`

### Need to Update Your Submission
1. Make changes to your file
2. On the same branch:
```bash
git add pullrequest_01/Assignment_FirstName_LastName.docx
git commit -m "Update PR 01 submission - FirstName LastName"
git push origin pr01_firstname_lastname
```
3. The PR will automatically update

### Merge Conflicts
If you see merge conflicts:
```bash
# Update from instructor's repo
git fetch upstream
git merge upstream/main
# Resolve any conflicts
git add .
git commit -m "Resolve merge conflicts"
git push origin your-branch-name
```

## Grading Notes
- ✅ Correct file naming = Full points
- ✅ Proper PR title = Easy identification
- ✅ Clean commit history = Professional practice
- ❌ Wrong format = Point deductions
- ❌ Direct push attempts = Submission not accepted

## Why This Workflow?
This is **exactly** how professional developers work:
- **Fork**: Create your own workspace
- **Branch**: Isolate your changes
- **Pull Request**: Submit work for review
- **Code Review**: Get feedback (instructor comments)

You're learning real industry practices that you'll use in internships and jobs!

## Questions?
1. Review these instructions carefully
2. Check the Git module materials
3. Ask during office hours
4. Post in the course discussion forum

Remember: This workflow might seem complex at first, but it's preparing you for real software development. Every tech company uses this process!