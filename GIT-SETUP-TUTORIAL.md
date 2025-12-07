# GitHub Tutorial: Your First Submission
## A Complete Walk-Through for CSCI 101 Students

---

## 🎯 What We'll Accomplish
By the end of this tutorial, you will have:
- ✅ Created your GitHub account
- ✅ Installed Git on your computer
- ✅ Forked the course repository
- ✅ Made a practice submission
- ✅ Created your first Pull Request

**Time needed**: 30-45 minutes

---

## Part 1: GitHub Account Setup

### Step 1.1: Create Your GitHub Account
1. Go to [https://github.com](https://github.com)
2. Click the "Sign up" button
3. Choose a username (Tip: Use something professional like `firstname-lastname` or `firstinitiallastname`)
   - ✅ Good: `john-smith`, `jsmith2025`, `johnsmith`
   - ❌ Avoid: `coolgamer123`, `dragonslayer99`
4. Use your school email if possible
5. Verify your email address

### Step 1.2: Complete Your Profile
1. Click your avatar (top-right) → "Your profile"
2. Click "Edit profile"
3. Add:
   - Your real name
   - A brief bio: "Computer Science student at [University]"
   - Your school/location

---

## Part 2: Git Installation

### For Windows Users

#### Step 2.1W: Download Git
1. Go to [https://git-scm.com/download/windows](https://git-scm.com/download/windows)
2. Download the installer
3. Run the installer

#### Step 2.2W: Installation Settings
Click "Next" for most screens, but pay attention to these:
- **Default editor**: Choose "Use Notepad as Git's default editor" (easier for beginners)
- **PATH environment**: Choose "Git from the command line and also from 3rd-party software"
- **Line ending conversions**: Choose "Checkout Windows-style, commit Unix-style"

#### Step 2.3W: Verify Installation
1. Open "Git Bash" (search for it in Start Menu)
2. Type: `git --version`
3. You should see something like: `git version 2.42.0`

### For Mac Users

#### Step 2.1M: Check if Git is Installed
1. Open Terminal (find it in Applications → Utilities)
2. Type: `git --version`
3. If you see a version number, skip to Part 3
4. If prompted to install, click "Install"

#### Alternative Mac Installation:
1. Go to [https://git-scm.com/download/mac](https://git-scm.com/download/mac)
2. Download and run the installer

### For Linux Users
Open terminal and run:
```bash
# Ubuntu/Debian:
sudo apt update && sudo apt install git

# Fedora:
sudo dnf install git
```

---

## Part 3: Configure Git

### Step 3.1: Open Your Terminal
- **Windows**: Open "Git Bash"
- **Mac/Linux**: Open Terminal

### Step 3.2: Set Your Identity
Replace with YOUR information:
```bash
git config --global user.name "John Smith"
git config --global user.email "jsmith@university.edu"
```

### Step 3.3: Verify Configuration
```bash
git config --list
```
You should see your name and email in the output.

---

## Part 4: Fork the Course Repository

### Step 4.1: Find the Course Repository
1. Go to the course repository:
   ```
   https://github.com/csci101_f25/csci101_f25
   ```
2. You should see the course repository with pullrequest folders

### Step 4.2: Fork It!
1. Click the "Fork" button (top-right of the page)
2. If asked "Where should we fork?", click your username
3. Wait a few seconds...
4. You now have YOUR OWN COPY! The URL will be:
   ```
   https://github.com/YOUR_USERNAME/csci101_f25
   ```

**⚠️ IMPORTANT**: You're now on YOUR fork, not the instructor's repository!

---

## Part 5: Clone to Your Computer

### Step 5.1: Get Your Fork's URL
1. On YOUR fork (check the URL has your username)
2. Click the green "Code" button
3. Make sure "HTTPS" is selected
4. Click the copy button to copy the URL

### Step 5.2: Clone It
1. Open your terminal/Git Bash
2. Navigate to where you want to store your coursework:
   ```bash
   # Windows example:
   cd /c/Users/YourName/Documents
   
   # Mac example:
   cd ~/Documents
   ```
3. Clone your repository:
   ```bash
   git clone https://github.com/YOUR_USERNAME/csci101_f25.git
   ```
4. Enter the folder:
   ```bash
   cd csci101_f25
   ```

### Step 5.3: Verify You're in the Right Place
```bash
ls
```
You should see:
```
pullrequest_01/
pullrequest_02/
pullrequest_03/
pullrequest_04/
pullrequest_05/
README.md
SUBMISSION-INSTRUCTIONS.md
```

---

## Part 6: Connect to Course Repository

### Step 6.1: Add Upstream Remote
```bash
git remote add upstream https://github.com/csci101_f25/csci101_f25.git
```

### Step 6.2: Verify Your Remotes
```bash
git remote -v
```
You should see:
```
origin    https://github.com/YOUR_USERNAME/csci101_f25.git (fetch)
origin    https://github.com/YOUR_USERNAME/csci101_f25.git (push)
upstream  https://github.com/csci101_f25/csci101_f25.git (fetch)
upstream  https://github.com/csci101_f25/csci101_f25.git (push)
```

**What this means:**
- `origin` = Your fork (where you push your work)
- `upstream` = Course repository (where you submit via Pull Request)

---

## Part 7: Practice Submission

Let's do a practice run with a simple text file before your real assignment!

### Step 7.1: Create a Practice Branch
```bash
git checkout -b practice_firstname_lastname
```
Replace with your actual name, for example:
```bash
git checkout -b practice_john_smith
```

### Step 7.2: Create a Practice File
1. Create a simple text file:
   ```bash
   # Windows (Git Bash):
   echo "This is my practice submission" > practice/Practice_John_Smith.txt
   
   # Mac/Linux:
   echo "This is my practice submission" > practice/Practice_John_Smith.txt
   ```

2. Verify it was created:
   ```bash
   ls practice/
   ```

### Step 7.3: Add and Commit
```bash
# See what changed
git status

# Add your file
git add practice/Practice_John_Smith.txt

# Commit with message
git commit -m "Add practice submission - John Smith"
```

### Step 7.4: Push to Your Fork
```bash
git push origin practice_john_smith
```

You might be prompted for your GitHub username and password:
- Username: Your GitHub username
- Password: You need a Personal Access Token (not your password!)
  - Go to GitHub → Settings → Developer settings → Personal access tokens
  - Generate new token (classic)
  - Select "repo" scope
  - Copy and use this as your password

---

## Part 8: Create Your First Pull Request

### Step 8.1: Go to GitHub
1. Go to YOUR fork on GitHub
2. You should see a yellow banner: "practice_john_smith had recent pushes"
3. Click "Compare & pull request"

**If you don't see the banner:**
1. Click "Pull requests"
2. Click "New pull request"
3. Make sure the settings are:
   - Base repository: `csci101_f25/csci101_f25`
   - Base: `main`
   - Head repository: `YOUR_USERNAME/csci101_f25`
   - Compare: `practice_john_smith`

### Step 8.2: Create the Pull Request
1. Title: `Practice Submission - John Smith`
2. Description (optional): "This is my practice submission for the Git tutorial"
3. Click "Create pull request"

### Step 8.3: Success!
You should see your pull request created! The URL will be something like:
```
https://github.com/csci101_f25/csci101_f25/pull/1
```

---

## Part 9: Your Real Assignment Workflow

Now you're ready for actual assignments! Here's the workflow:

### Before Each Assignment:
```bash
# Get any updates from instructor
git fetch upstream
git checkout main
git merge upstream/main
git push origin main
```

### For Each Assignment:
```bash
# 1. Create a new branch
git checkout -b pr01_john_smith

# 2. Add your assignment file to the correct folder
# (Put your file in the pullrequest_01/ folder)

# 3. Add and commit
git add pullrequest_01/Assignment_John_Smith.docx
git commit -m "Add PR 01 submission - John Smith"

# 4. Push
git push origin pr01_john_smith

# 5. Go to GitHub and create Pull Request
```

---

## 🚨 Common Problems and Solutions

### "Permission denied" when pushing
- **Cause**: Trying to push to instructor's repo instead of your fork
- **Fix**: Check your remotes with `git remote -v`

### "Fatal: not a git repository"
- **Cause**: You're not in the right folder
- **Fix**: `cd` into your csci101_f25 folder

### Can't find Git Bash (Windows)
- **Fix**: Search "Git Bash" in Start Menu, or reinstall Git

### "Please tell me who you are" error
- **Fix**: Run the config commands from Part 3

### Password authentication was removed
- **Fix**: Use a Personal Access Token instead of password
- Create at: GitHub → Settings → Developer settings → Personal access tokens

---

## ✅ Checklist: Are You Ready?

Before starting real assignments, confirm:

- [ ] I have a GitHub account with my real name
- [ ] Git is installed on my computer
- [ ] I've forked the course repository
- [ ] I've cloned MY fork to my computer
- [ ] I've added the upstream remote
- [ ] I successfully created a practice PR
- [ ] I understand the difference between:
  - My fork (origin) vs Course repo (upstream)
  - Branches vs Main
  - Local vs Remote

---

## 🎉 Congratulations!

You've just learned the professional Git workflow used by millions of developers worldwide! This is a real skill that you'll use throughout your career.

**Next Steps:**
1. Delete your practice branch locally:
   ```bash
   git checkout main
   git branch -d practice_john_smith
   ```
2. Review the SUBMISSION-INSTRUCTIONS.md for assignment details
3. Start your first real assignment!

**Remember:** It's normal to feel confused at first. Every professional developer went through this learning curve. Don't hesitate to ask for help!

---

## Quick Reference Card

Keep this handy for assignments:

```bash
# Before starting assignment
git fetch upstream
git checkout main
git merge upstream/main
git push origin main

# Create branch for work
git checkout -b pr01_firstname_lastname

# After adding your file
git add pullrequest_01/Assignment_FirstName_LastName.docx
git commit -m "Add PR 01 submission - FirstName LastName"
git push origin pr01_firstname_lastname

# Then create PR on GitHub
```

---

*Questions? Check SUBMISSION-INSTRUCTIONS.md or ask during office hours!*