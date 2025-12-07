# GitHub Tutorial: Your First Pull Request
## CSCI 101 - Session 2 of 2

---

## Prerequisites

**Before starting this tutorial, complete Session 1 (github-setup-guide.html):**
- GitHub account created
- Git installed on your computer
- Git configured with your name and email

**Time needed**: 20-30 minutes

---

## What We'll Accomplish

By the end of this tutorial, you will have:
- Forked the course repository
- Cloned it to your computer
- Created your first Pull Request

---

## Part 1: Fork the Course Repository

### Step 1.1: Find the Course Repository
1. Go to the course repository:
   ```
   https://github.com/csci101_f25/csci101_f25
   ```
2. You should see the repository with pullrequest folders and a README

### Step 1.2: Fork It!
1. Click the **"Fork"** button (top-right of the page)
2. If asked "Where should we fork?", click your username
3. Wait a few seconds...
4. You now have YOUR OWN COPY! The URL will be:
   ```
   https://github.com/YOUR_USERNAME/csci101_f25
   ```

**Important:** You're now on YOUR fork, not the course repository!

---

## Part 2: Clone to Your Computer

### Step 2.1: Get Your Fork's URL
1. On YOUR fork (check the URL has your username)
2. Click the green **"Code"** button
3. Make sure **"HTTPS"** is selected
4. Click the copy button to copy the URL

### Step 2.2: Clone It
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

### Step 2.3: Verify You're in the Right Place
```bash
ls
```
You should see:
```
pullrequest_01/
pullrequest_02/
pullrequest_03/
README.md
SUBMISSION-INSTRUCTIONS.md
```

---

## Part 3: Connect to Course Repository

### Step 3.1: Add Upstream Remote
```bash
git remote add upstream https://github.com/csci101_f25/csci101_f25.git
```

### Step 3.2: Verify Your Remotes
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

## Part 4: Create Your First Pull Request

Now let's submit PR 01! You'll create a Word document with a README.md file.

### Step 4.1: Create a Branch
```bash
git checkout -b pr01_firstname_lastname
```
Replace with your actual name:
```bash
git checkout -b pr01_john_smith
```

### Step 4.2: Create Your Subfolder
```bash
mkdir pullrequest_01/john_smith
```
(Use YOUR name, lowercase, with underscore)

### Step 4.3: Create Your Files

You need two files in your subfolder:

**1. Create README.md**

Create a file called `README.md` in your subfolder with this content:

```markdown
# PR 01 Submission - John Smith

## Description
My first pull request submission for CSCI 101.

## Files Included
- `Assignment.docx` - My Word document assignment

## Author
John Smith
CSCI 101 - Fall 2025
```

**2. Create Assignment.docx**

Create a simple Word document called `Assignment.docx` with any content (e.g., "This is my first GitHub submission!").

**Your folder should now contain:**
```
pullrequest_01/john_smith/
  README.md
  Assignment.docx
```

### Step 4.4: Add and Commit
```bash
# See what changed
git status

# Add your subfolder
git add pullrequest_01/john_smith/

# Commit with message
git commit -m "Add PR 01 submission - John Smith"
```

### Step 4.5: Push to Your Fork
```bash
git push origin pr01_john_smith
```

You might be prompted for your GitHub username and password:
- Username: Your GitHub username
- Password: You need a **Personal Access Token** (not your password!)
  - Go to GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic)
  - Generate new token (classic)
  - Select "repo" scope
  - Copy and use this as your password

---

## Part 5: Create the Pull Request on GitHub

### Step 5.1: Go to GitHub
1. Go to YOUR fork on GitHub
2. You should see a yellow banner: "pr01_john_smith had recent pushes"
3. Click **"Compare & pull request"**
4. **Change the base branch from `main` to `submissions`**

**If you don't see the banner:**
1. Click "Pull requests"
2. Click "New pull request"
3. Make sure the settings are:
   - Base repository: `csci101_f25/csci101_f25`
   - Base: `submissions` (not main!)
   - Head repository: `YOUR_USERNAME/csci101_f25`
   - Compare: `pr01_john_smith`

**Important:** Always change the base branch to `submissions`!

### Step 5.2: Create the Pull Request
1. Title: `PR 01 Submission - John Smith`
2. Description (optional): "My first pull request for CSCI 101"
3. Click **"Create pull request"**

### Step 5.3: Success!
You should see your pull request created! The URL will be something like:
```
https://github.com/csci101_f25/csci101_f25/pull/1
```

---

## Congratulations!

You've just completed your first Pull Request using the same workflow professional developers use worldwide!

**The Three Pull Requests:**

| PR | What to Submit |
|----|----------------|
| PR 01 | README.md + Word document (.docx) |
| PR 02 | README.md + Python program (helloWorld.py) |
| PR 03 | README.md + Markdown file (about_me.md) |

See `SUBMISSION-INSTRUCTIONS.md` for detailed requirements for each PR.

---

## Workflow for Future PRs

### Before Each PR:
```bash
# Get any updates from course repo
git fetch upstream
git checkout main
git merge upstream/main
git push origin main
```

### For Each PR:
```bash
# 1. Create a new branch
git checkout -b pr02_firstname_lastname

# 2. Create your subfolder
mkdir pullrequest_02/firstname_lastname

# 3. Add your README.md + assignment file to the subfolder

# 4. Stage, commit, and push
git add pullrequest_02/firstname_lastname/
git commit -m "Add PR 02 submission - FirstName LastName"
git push origin pr02_firstname_lastname

# 5. Go to GitHub and create Pull Request (base branch: submissions)
```

---

## Quick Reference Card

```bash
# Sync with course repo
git fetch upstream
git checkout main
git merge upstream/main
git push origin main

# Create branch for PR
git checkout -b pr0#_firstname_lastname

# Create subfolder, add README.md + assignment file

# Stage, commit, push
git add pullrequest_0#/firstname_lastname/
git commit -m "Add PR 0# submission - FirstName LastName"
git push origin pr0#_firstname_lastname

# Then create PR on GitHub (base: submissions)
```

---

## Troubleshooting

### "Permission denied" when pushing
- **Cause**: Trying to push to course repo instead of your fork
- **Fix**: Check your remotes with `git remote -v`

### "Fatal: not a git repository"
- **Cause**: You're not in the right folder
- **Fix**: `cd` into your csci101_f25 folder

### Can't find Git Bash (Windows)
- **Fix**: Search "Git Bash" in Start Menu

### Password authentication was removed
- **Fix**: Use a Personal Access Token instead of password
- Create at: GitHub → Settings → Developer settings → Personal access tokens

### Pull request going to wrong branch
- **Fix**: Make sure base branch is `submissions`, not `main`

---

## Branch Structure

- `main` - Course materials (sync from here)
- `submissions` - Where your PRs get merged (submit PRs here)

Students sync from `main` but submit PRs to `submissions`. This keeps your work separate from other students.

---

*Questions? Check SUBMISSION-INSTRUCTIONS.md or ask during office hours!*
