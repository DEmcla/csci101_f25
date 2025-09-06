# Semester Project Submission Instructions

## 🚀 First Time Here?
**Start with the [Git Setup Tutorial](GIT-SETUP-TUTORIAL.md)** - A complete walk-through that will:
- Help you install Git
- Set up your GitHub account  
- Practice making a submission
- Create your first Pull Request

## Overview
This semester-long project will develop through 7 steps. Each step builds upon the previous one, demonstrating your growth in programming and problem-solving skills throughout CSCI 101.

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
# Connect to the original repository for updates
# Replace INSTRUCTOR_USERNAME with your instructor's GitHub username
git remote add upstream https://github.com/INSTRUCTOR_USERNAME/csci101_f25.git

# Verify your remotes
git remote -v
# You should see:
# origin = your fork
# upstream = instructor's original
```

## Submission Process for Each Project Step

### 1. Update Your Fork
Before starting each assignment, get the latest updates:
```bash
# Get updates from the instructor's repository
git fetch upstream
git checkout main
git merge upstream/main
git push origin main
```

### 2. Create a Branch for Your Work
```bash
# Create a new branch for your submission
# Format: step#_firstname_lastname
git checkout -b step1_john_smith
```

### 3. Add Your Project File
- **File name**: `Project_FirstName_LastName.docx`
- **Location**: Place in the appropriate project-step folder
- **Example**: `project-step-1/Project_John_Smith.docx`

### 4. Commit Your Work
```bash
# Add your file
git add project-step-1/Project_John_Smith.docx

# Commit with a clear message
git commit -m "Add Step 1 submission - John Smith"

# Push to YOUR fork
git push origin step1_john_smith
```

### 5. Create a Pull Request
1. Go to YOUR fork on GitHub
2. Click "Pull requests" → "New pull request"
3. Make sure:
   - Base repository: Instructor's repository
   - Base branch: main
   - Head repository: Your fork
   - Compare branch: Your step branch (e.g., step1_john_smith)
4. Click "Create pull request"
5. **Title your PR**: `Step 1 Submission - FirstName LastName`
6. Add any comments about your submission
7. Click "Create pull request"

## Important Guidelines

### File Naming Convention
**MUST follow this format exactly:**
```
Project_FirstName_LastName.docx
```
Examples:
- ✅ `Project_John_Smith.docx`
- ✅ `Project_Maria_Garcia.docx`
- ❌ `project-john-smith.docx` (wrong format)
- ❌ `John Smith Project.docx` (wrong format)

### Branch Naming Convention
**MUST follow this format:**
```
step#_firstname_lastname
```
Examples:
- ✅ `step1_john_smith`
- ✅ `step2_maria_garcia`
- ❌ `Step1-John-Smith` (wrong format)
- ❌ `john_step1` (wrong format)

### Pull Request Title Convention
**MUST follow this format:**
```
Step # Submission - FirstName LastName
```
Examples:
- ✅ `Step 1 Submission - John Smith`
- ✅ `Step 2 Submission - Maria Garcia`

## Common Issues and Solutions

### "Permission Denied" When Pushing
- Make sure you're pushing to YOUR fork, not the instructor's repository
- Check with: `git remote -v`

### Need to Update Your Submission
1. Make changes to your file
2. On the same branch:
```bash
git add project-step-1/Project_FirstName_LastName.docx
git commit -m "Update Step 1 submission - FirstName LastName"
git push origin step1_firstname_lastname
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