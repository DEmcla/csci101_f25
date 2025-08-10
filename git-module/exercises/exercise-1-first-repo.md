# Exercise 1: Creating Your First Repository

## Objective
Learn to initialize a Git repository and make your first commit.

## Steps

### Step 1: Create a project directory

**All Platforms:**
```bash
mkdir my-first-project
cd my-first-project
```

### Step 2: Initialize Git repository
```bash
git init
```

**Expected output:**
```
Initialized empty Git repository in /path/to/my-first-project/.git/
```

### Step 3: Create a simple file

**Git Bash (Windows) or Terminal (Mac/Linux):**
```bash
echo "Hello, Git!" > hello.txt
```

**Alternative (All Platforms) - Using Text Editor:**
1. Open your preferred text editor (Notepad, TextEdit, VS Code, etc.)
2. Type: `Hello, Git!`
3. Save as `hello.txt` in your `my-first-project` folder

### Step 4: Check repository status
```bash
git status
```

**Expected output:**
```
On branch main

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
    hello.txt

nothing added to commit but untracked files present (use "git add" to track)
```

### Step 5: Add file to staging area
```bash
git add hello.txt
```

**Verify it worked:**
```bash
git status
```

**Expected output:**
```
On branch main

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
    new file:   hello.txt
```

### Step 6: Make your first commit
```bash
git commit -m "Add hello.txt with greeting message"
```

**Expected output:**
```
[main (root-commit) a1b2c3d] Add hello.txt with greeting message
 1 file changed, 1 insertion(+)
 create mode 100644 hello.txt
```

### Step 7: View commit history
```bash
git log --oneline
```

**Expected output:**
```
a1b2c3d Add hello.txt with greeting message
```

## Questions to Consider
- What did `git status` show before and after adding the file?
- Why do we need to add files to the staging area before committing?
- What information does `git log` provide?

## Challenge: Practice the Workflow

**Goal:** Create and commit a second file to reinforce the workflow.

### Your Task:
1. **Create `about.txt`** with 2-3 lines about yourself (name, major, why you're learning Git)

2. **Follow the complete workflow:**
   - Check status
   - Stage the file
   - Check status again
   - Commit with a good message
   - View your updated history

### Platform-Specific File Creation:

**Git Bash/Terminal:**
```bash
echo "Name: Your Name" > about.txt
echo "Major: Computer Science" >> about.txt
echo "Learning Git to prepare for future CS courses" >> about.txt
```

**Text Editor (All Platforms):**
1. Create new file called `about.txt`
2. Add your information
3. Save in the `my-first-project` folder

### Success Check:
When done, `git log --oneline` should show two commits!

### Troubleshooting:
- **File not found**: Make sure you're in the `my-first-project` directory
- **Command not recognized**: Windows users should use Git Bash
- **Nothing to commit**: Check that you used `git add` before `git commit`