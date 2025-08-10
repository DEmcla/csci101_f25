# Git Version Control Tutorial
*For Computer Science Students - CSCI 101*

---

## Table of Contents
1. [What is Version Control?](#what-is-version-control)
2. [Why Do We Need Git?](#why-do-we-need-git)
3. [Installing and Setting Up Git](#installing-and-setting-up-git)
4. [Your First Git Repository](#your-first-git-repository)
5. [The Git Workflow](#the-git-workflow)
6. [Working with Remote Repositories](#working-with-remote-repositories)
7. [Best Practices](#best-practices)
8. [Common Commands Reference](#common-commands-reference)
9. [Troubleshooting](#troubleshooting)
10. [What's Next?](#whats-next)

---

## What is Version Control?

Imagine you're writing a research paper. You start with `paper.docx`, then make changes and save it as `paper_v2.docx`, then `paper_final.docx`, then `paper_final_ACTUALLY_FINAL.docx`. Sound familiar?

**Version control** is a system that automatically tracks changes to your files over time. Instead of creating multiple copies with confusing names, version control:

- Saves every version of your work automatically
- Shows you exactly what changed between versions
- Lets you go back to any previous version
- Allows multiple people to work on the same project without conflicts

Think of it like a "time machine" for your files - you can travel back to see what your project looked like at any point in history.

### Real-World Analogy
Version control is like Google Docs' "Version history" feature, but much more powerful and designed for code and technical projects.

---

## Why Do We Need Git?

Git is the most popular version control system in the world. Here's why it matters for computer science students:

### 🎯 **For Your Studies**
- **Track your coding assignments**: See how your programs evolve from first draft to final submission
- **Recover from mistakes**: Accidentally deleted important code? Git can restore it
- **Experiment safely**: Try new approaches without fear of breaking working code
- **Document your learning**: Your Git history becomes a portfolio of your progress

### 🏢 **For Your Career**
- **Industry standard**: 99% of software companies use Git
- **Collaboration**: Essential for team projects and internships
- **Open source**: Contribute to projects on GitHub, GitLab, etc.
- **Portfolio**: Employers look at your Git history to understand your coding skills

### 📚 **Looking Ahead**
In your upcoming courses (Java I, Web Development, Database), you'll use Git to:
- Submit assignments through GitHub
- Collaborate on group projects
- Manage complex codebases
- Deploy applications

---

## Installing and Setting Up Git

### Step 1: Install Git

**Windows:**
- Download from [git-scm.com](https://git-scm.com/)
- Run installer with default options
- Open "Git Bash" for command line access

**Mac:**
- Git is often pre-installed. Check by opening Terminal and typing: `git --version`
- If not installed, download from [git-scm.com](https://git-scm.com/) or use Homebrew: `brew install git`

**Linux:**
```bash
# Ubuntu/Debian
sudo apt update && sudo apt install git

# CentOS/RHEL
sudo yum install git
```

### Step 2: Configure Git

Tell Git who you are (replace with your information):

```bash
git config --global user.name "Your Full Name"
git config --global user.email "your.email@example.com"
```

### Step 3: Verify Installation

```bash
git --version
git config --list
```

---

## Your First Git Repository

Let's create your first Git repository with a simple project.

### Step 1: Create Project Directory

```bash
# Create a new folder for your project
mkdir my-first-repo
cd my-first-repo
```

### Step 2: Initialize Git Repository

```bash
git init
```

This creates a hidden `.git` folder that stores all version control information.

### Step 3: Create Your First File

Create a simple text file with your favorite programming language:

```bash
echo "My favorite programming language is Python because it's beginner-friendly." > favorites.txt
```

### Step 4: Check Repository Status

```bash
git status
```

You'll see something like:
```
On branch main

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
    favorites.txt

nothing added to commit but untracked files present (use "git add" to track)
```

**What this means:**
- `Untracked files`: Git sees the file but isn't tracking changes yet
- `No commits yet`: You haven't saved any versions yet

### Step 5: Add File to Staging Area

```bash
git add favorites.txt
```

Now check status again:
```bash
git status
```

### Step 6: Make Your First Commit

```bash
git commit -m "Add my favorite programming language"
```

**Congratulations!** 🎉 You've made your first commit!

### Step 7: View Your History

```bash
git log
```

---

## The Git Workflow

Understanding the Git workflow is crucial. Here's how it works:

```
Working Directory → Staging Area → Repository
      ↑                ↑              ↑
   (edit files)    (git add)    (git commit)
```

### The Three States

1. **Working Directory**: Where you edit files
2. **Staging Area**: Files prepared for the next commit (like a shopping cart)
3. **Repository**: Permanent storage of versions

### Hands-On Practice

Let's practice the workflow:

#### 1. Make Changes
```bash
echo "I'm learning Git in CSCI 101!" >> favorites.txt
echo "Git helps me track changes to my code." >> favorites.txt
```

#### 2. See What Changed
```bash
git status
git diff
```

The `diff` command shows exactly what changed:
- Lines starting with `+` are additions
- Lines starting with `-` are deletions

#### 3. Stage Changes
```bash
git add favorites.txt
```

#### 4. Commit Changes
```bash
git commit -m "Add thoughts about learning Git"
```

#### 5. View History
```bash
git log --oneline
```

This shows a compact view of your commits.

### Practice Exercise

Create a file called `goals.txt` with your computer science goals:

```bash
echo "My CS Goals:" > goals.txt
echo "1. Learn programming fundamentals" >> goals.txt
echo "2. Build my first web application" >> goals.txt
echo "3. Contribute to open source projects" >> goals.txt
```

Now practice the workflow:
1. Check status
2. Add the file
3. Commit with message "Add my computer science goals"
4. View your commit history

---

## Working with Remote Repositories

So far, everything has been local (on your computer). **Remote repositories** let you:
- Back up your work to the cloud
- Share projects with others
- Access your code from anywhere
- Build a public portfolio

### GitHub Setup

[GitHub](https://github.com) is the most popular Git hosting service.

#### Step 1: Create GitHub Account
- Go to [github.com](https://github.com) and sign up
- Choose a professional username (employers will see this!)
- Verify your email address

#### Step 2: Create Repository on GitHub
- Click "New repository" (green button)
- Name it "csci101-git-practice"
- Keep it public (for portfolio purposes)
- Don't initialize with README (we already have files)
- Click "Create repository"

#### Step 3: Connect Local to Remote
GitHub will show you commands like these (use your actual username):

```bash
git remote add origin https://github.com/yourusername/csci101-git-practice.git
git branch -M main
git push -u origin main
```

**What these commands do:**
- `remote add origin`: Links your local repo to GitHub
- `branch -M main`: Ensures you're on the main branch
- `push -u origin main`: Uploads your commits to GitHub

### The Push/Pull Workflow

```bash
# Make changes locally
echo "Remote repositories are awesome!" >> favorites.txt

# Stage and commit
git add favorites.txt
git commit -m "Add comment about remote repositories"

# Push to GitHub
git push
```

#### Viewing on GitHub
- Go to your repository page on GitHub
- Browse your files and commit history
- See how the web interface visualizes your work

#### Making Changes on GitHub
1. Click on `favorites.txt` in your GitHub repository
2. Click the pencil icon (Edit)
3. Add a line: "I can edit files directly on GitHub too!"
4. Scroll down and commit the change with a message
5. Go back to your local terminal

#### Pulling Changes
```bash
git pull
```

This downloads the change you made on GitHub to your local repository.

---

## Best Practices

### 1. Write Good Commit Messages

**Bad examples:**
- "fixed stuff"
- "changes"
- "asdfgh"

**Good examples:**
- "Add user registration form"
- "Fix calculation error in grade average"
- "Update README with installation instructions"

**Format:**
- Start with a verb (Add, Fix, Update, Remove)
- Keep first line under 50 characters
- Use present tense ("Add feature" not "Added feature")

### 2. Commit Early and Often

- Commit whenever you complete a logical unit of work
- Don't wait until everything is "perfect"
- Better to have many small commits than one giant commit

### 3. Use .gitignore Files

Some files shouldn't be tracked by Git:

Create `.gitignore` file:
```bash
# Ignore system files
.DS_Store
Thumbs.db

# Ignore editor files
.vscode/
.idea/

# Ignore temporary files
*.tmp
*.log
```

### 4. Check Status Frequently

Get in the habit of running `git status` often - it's your best friend!

---

## Common Commands Reference

### Basic Workflow
```bash
git init                    # Initialize repository
git status                  # Check status (use this A LOT!)
git add <file>             # Stage specific file
git add .                  # Stage all changes
git commit -m "message"    # Commit with message
git log                    # View commit history
git log --oneline          # Compact history view
```

### Viewing Changes
```bash
git diff                   # Show unstaged changes
git diff --staged          # Show staged changes
git show                   # Show last commit details
```

### Remote Repositories
```bash
git remote add origin <url>  # Add remote repository
git push -u origin main      # First push (sets upstream)
git push                     # Push changes
git pull                     # Pull changes from remote
```

### Getting Help
```bash
git help <command>         # Get help for specific command
git <command> --help       # Alternative help syntax
```

---

## Troubleshooting

### Common Issues and Solutions

#### "I forgot to add my name/email"
```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

#### "I made a typo in my commit message"
```bash
git commit --amend -m "Corrected commit message"
```
⚠️ Only use this if you haven't pushed yet!

#### "I want to undo my last commit but keep the changes"
```bash
git reset --soft HEAD~1
```

#### "I want to see what changed in a specific commit"
```bash
git show <commit-hash>
```

#### "Git says 'fatal: not a git repository'"
Make sure you're in the right directory and have run `git init`.

#### "I can't push to GitHub"
- Check your internet connection
- Verify the remote URL: `git remote -v`
- Make sure you're logged into GitHub

---

## What's Next?

Congratulations! You now understand the fundamentals of Git. Here's what to explore next:

### Immediate Next Steps
1. **Practice**: Create a few more repositories for your assignments
2. **Explore GitHub**: Browse popular repositories in your areas of interest
3. **Build Your Profile**: Use GitHub as a portfolio platform

### In Your Future Courses
- **Java I**: You'll submit assignments via GitHub
- **Web Development**: Deploy websites using Git
- **Database**: Version control database schemas and queries
- **Software Engineering**: Collaborate on team projects

### Advanced Git Concepts (for later)
- **Branching**: Work on features in isolation
- **Merging**: Combine different lines of development
- **Pull Requests**: Code review and collaboration workflow
- **Git GUI Tools**: Visual interfaces for complex operations

### Resources for Continued Learning
- [GitHub's Git Handbook](https://guides.github.com/introduction/git-handbook/)
- [Interactive Git Tutorial](https://learngitbranching.js.org/)
- [Pro Git Book](https://git-scm.com/book) (free online)
- [GitHub Skills](https://skills.github.com/) (interactive courses)

---

## Practice Project Ideas

To reinforce your learning, try these projects:

### Project 1: Personal Learning Journal
- Create a repository called "csci101-journal"
- Add weekly reflection files
- Track your progress through the course

### Project 2: Code Snippet Collection
- Create a repository for useful code snippets
- Add examples as you learn new programming concepts
- Organize by topic/language

### Project 3: Assignment Portfolio
- Create repositories for major assignments
- Practice good commit habits
- Build a showcase of your work

---

## Final Tips for Success

1. **Practice Regularly**: Use Git for all your assignments, even small ones
2. **Read Error Messages**: Git's error messages are usually helpful
3. **Don't Be Afraid**: You can't "break" Git easily - experiment!
4. **Ask for Help**: Your instructors and classmates are resources
5. **Build Your Portfolio**: Treat GitHub as your professional presence

Remember: Every professional developer uses version control. Starting now gives you a huge advantage in your computer science journey!

---

*This tutorial was created for CSCI 101 students. For questions or clarifications, reach out to your instructor or visit office hours.*