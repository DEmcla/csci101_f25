# [Module 4] GitHub: An Overview and Introduction
## Version Control and Collaborative Development

### Class Overview (75 minutes)

This lecture provides an introduction to version control and GitHub. You'll use these tools in future courses and projects.

| Segment | Topic | Time |
|---------|-------|------|
| 1 | Introduction: Why Version Control? | 10 min |
| 2 | Git vs GitHub: Understanding the Difference | 10 min |
| 3 | Core Concepts: Repositories, Commits, Branches | 20 min |
| 4 | Hands-On: Creating Your First Repository | 15 min |
| 5 | Collaboration Features: Pull Requests & Issues | 15 min |
| 6 | Wrap-up & Exit Ticket | 5 min |

---

## Learning Objectives

By the end of this lesson, you will be able to:

1. **Explain** the purpose and benefits of version control systems
2. **Distinguish** between Git (the tool) and GitHub (the platform)
3. **Identify** the core components of a Git repository
4. **Create** a new repository on GitHub
5. **Describe** the workflow of commits, branches, and pull requests
6. **Recognize** how GitHub enables collaborative software development

---

## Key Terms for Today

| Term | Definition |
|------|------------|
| **Version Control** | A system that tracks changes to files over time, allowing you to recall specific versions later |
| **Git** | A distributed version control system created by Linus Torvalds in 2005 |
| **GitHub** | A web-based platform that hosts Git repositories and provides collaboration tools |
| **Repository (Repo)** | A storage location containing all files, folders, and version history for a project |
| **Commit** | A snapshot of your project at a specific point in time, with a message describing the changes |
| **Branch** | An independent line of development that allows work on features without affecting the main code |
| **Pull Request (PR)** | A proposal to merge changes from one branch into another, enabling code review |
| **Clone** | Creating a local copy of a remote repository on your computer |

---

## 1. Introduction: Why Version Control?

### The Problem Without Version Control

Imagine you're writing a research paper. Without version control, you might end up with files like:

```
essay_draft1.docx
essay_draft2.docx
essay_final.docx
essay_final_REAL.docx
essay_final_REAL_v2.docx
essay_final_REAL_v2_SUBMITTED.docx
```

**Sound familiar?**

This approach has serious problems:
- Which version has the changes your professor requested?
- What exactly changed between draft1 and draft2?
- How do you collaborate with a partner without overwriting each other's work?
- What if you need to undo a change from three versions ago?

### The Solution: Version Control

Version control systems solve these problems by:

| Problem | Solution |
|---------|----------|
| Multiple confusing file copies | Single file with complete history |
| Unknown changes between versions | Detailed change tracking with messages |
| Collaboration conflicts | Merge tools and conflict resolution |
| Undoing changes is difficult | Easy rollback to any previous state |
| No backup if computer fails | Remote storage and synchronization |

### Real-World Importance

Version control is **essential** in professional software development:

- **Linux kernel**: Over 27 million lines of code, thousands of contributors
- **Microsoft Windows**: Uses Git internally for development
- **Every major tech company**: Google, Meta, Amazon, Netflix all use version control

> "If you're not using version control, you're not a professional programmer."
> — Every senior developer, ever

---

## 2. Git vs GitHub: Understanding the Difference

### A Common Point of Confusion

Many beginners confuse Git and GitHub. Let's clarify:

| Aspect | Git | GitHub |
|--------|-----|--------|
| **What is it?** | Software tool | Web platform/service |
| **Where does it run?** | On your computer | On the internet |
| **Created by** | Linus Torvalds (2005) | Tom Preston-Werner (2008) |
| **Cost** | Free, open source | Free tier + paid plans |
| **Primary function** | Track file changes locally | Host repositories, enable collaboration |
| **Can work without the other?** | Yes | Needs Git to function |

### The Relationship: An Analogy

Think of it like **email**:

- **Git** is like your email application (Outlook, Apple Mail, Gmail app)
  - It's the tool you use to write, send, and organize messages
  - It works on your computer

- **GitHub** is like Gmail's servers (or your email provider)
  - It stores your messages in the cloud
  - It lets you access your email from anywhere
  - It enables you to communicate with others

You can write emails offline with your email app (Git works locally), but to send them to others, you need a server (GitHub provides remote hosting).

### Other Git Hosting Platforms

GitHub isn't the only option for hosting Git repositories:

| Platform | Key Features |
|----------|--------------|
| **GitHub** | Largest community, extensive integrations, GitHub Actions |
| **GitLab** | Built-in CI/CD, self-hosted option, DevOps focus |
| **Bitbucket** | Atlassian integration (Jira, Trello), free private repos |
| **Azure DevOps** | Microsoft ecosystem, enterprise features |

We focus on **GitHub** because:
- Largest developer community (100+ million users)
- Industry standard for open-source projects
- Excellent learning resources
- Free for students (GitHub Education)

---

## Checkpoint #1: Git vs GitHub

**Answer these questions before continuing:**

1. If your internet goes down, can you still make commits with Git?
2. True or False: GitHub invented Git.
3. What's the main thing GitHub adds that Git alone doesn't provide?

<details>
<summary>Click for Answers</summary>

1. **Yes!** Git works entirely on your local computer. You only need internet to push/pull from remote repositories.
2. **False.** Linus Torvalds created Git in 2005. GitHub was created 3 years later in 2008 by different people.
3. **Remote hosting and collaboration features.** GitHub stores your code in the cloud and provides tools like pull requests, issues, and project boards.

</details>

---

## 3. Core Concepts: Repositories, Commits, and Branches

### 3.1 Repositories

A **repository** (or "repo") is like a project folder with superpowers.

**What's inside a repository:**
```
my-project/
├── .git/              # Hidden folder - Git's brain (stores all history)
├── src/               # Your source code
│   ├── main.py
│   └── utils.py
├── docs/              # Documentation
│   └── README.md
├── tests/             # Test files
│   └── test_main.py
└── README.md          # Project description (shown on GitHub)
```

**Key point:** The `.git/` folder is what makes a regular folder into a Git repository. It contains the entire history of your project.

### 3.2 Commits: Snapshots in Time

A **commit** is a snapshot of your entire project at a moment in time.

Think of commits like **save points in a video game**:
- You can always go back to a previous save
- Each save has a note about what you accomplished
- The game keeps track of all your saves in order

**Anatomy of a commit:**

```
commit 7a3b9f2e1d4c5f6g8h9i0j1k2l3m4n5o6p7q8r9s
Author: Jane Developer <jane@example.com>
Date:   Mon Nov 25 14:30:00 2024

    Add user login functionality

    - Created login form component
    - Added password validation
    - Connected to authentication API
```

**Each commit includes:**
- **Unique ID (hash)**: 40-character identifier (like `7a3b9f2...`)
- **Author**: Who made the change
- **Timestamp**: When it was made
- **Message**: Description of what changed
- **Changes**: The actual file modifications

### 3.3 Commit Messages Matter!

Good commit messages are **essential** for understanding project history.

| Bad Message | Good Message |
|-------------|--------------|
| "fixed stuff" | "Fix login button not responding on mobile" |
| "updates" | "Add email validation to registration form" |
| "asdfgh" | "Remove deprecated API endpoint" |
| "final changes" | "Implement password reset functionality" |

**A good commit message:**
- Starts with a verb (Add, Fix, Update, Remove, Refactor)
- Is specific about what changed
- Explains *why* if the change isn't obvious

### 3.4 Branches: Parallel Universes

A **branch** is an independent line of development.

**The Timeline Analogy:**

Imagine you're working on a time travel movie script:

```
main branch (the "official" timeline):

    *---*---*---*---*  (main storyline)
         \
          *---*---*    (feature/alternate-ending)
              \
               *---*   (experiment/robot-twist)
```

- **Main branch**: The official, stable version
- **Feature branches**: Experimental work that doesn't affect the main version
- You can merge branches back together when ready

**Why branches matter:**
- Work on new features without breaking working code
- Multiple team members can work simultaneously
- Easy to abandon failed experiments
- Keep the main branch always deployable

---

## Checkpoint #2: Core Concepts

**Quick check - True or False:**

1. A commit message should be as short as possible, even if it's vague.
2. The `.git` folder stores the entire history of your project.
3. Creating a new branch automatically deletes your work on the main branch.
4. Each commit has a unique identifier called a hash.

<details>
<summary>Click for Answers</summary>

1. **False.** Commit messages should be clear and descriptive, not vague. "Fix login bug on mobile Safari" is much better than "fix."
2. **True.** The `.git` folder contains all commits, branches, and history. That's why you should never manually edit it!
3. **False.** Branches are completely independent. Creating a new branch doesn't affect other branches at all.
4. **True.** Every commit has a unique 40-character SHA-1 hash that identifies it.

</details>

---

## 4. Hands-On: Creating Your First Repository

### Step 1: Sign Up for GitHub (if needed)

1. Go to [github.com](https://github.com)
2. Click "Sign up"
3. Use your school email for free student benefits
4. Choose a professional username (this becomes part of your developer identity!)

### Step 2: Create a New Repository

1. Click the **+** icon in the top right corner
2. Select **"New repository"**
3. Fill in the details:

| Field | What to Enter |
|-------|---------------|
| Repository name | `my-first-repo` (use lowercase, hyphens for spaces) |
| Description | "My first GitHub repository for CSCI 101" |
| Visibility | **Public** (visible to everyone) or **Private** (only you) |
| Initialize | Check "Add a README file" |

4. Click **"Create repository"**

**Congratulations!** You now have a GitHub repository!

### Step 3: Understanding the Repository Page

Your new repository page shows:

```
┌─────────────────────────────────────────────────────────────┐
│  username/my-first-repo                          [⭐ Star]  │
├─────────────────────────────────────────────────────────────┤
│  📁 Code   🔀 Pull Requests   ⚠️ Issues   📊 Actions   ...  │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  📄 README.md                    1 commit    main ▼         │
│                                                             │
│  ─────────────────────────────────────────────────────      │
│  # my-first-repo                                            │
│  My first GitHub repository for CSCI 101                    │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

**Key areas:**
- **Code tab**: View and browse files
- **Pull requests**: Proposed changes (covered later)
- **Issues**: Bug reports and feature requests
- **README.md**: Displayed as the "homepage" of your repo

### Step 4: Make Your First Edit on GitHub

1. Click on `README.md`
2. Click the **pencil icon** (Edit this file)
3. Add some content:

```markdown
# My First Repository

Welcome to my first GitHub repository!

## About This Project

I'm learning about:
- Version control with Git
- Collaboration with GitHub
- Professional development workflows

## Contact

Created by [Your Name] for CSCI 101
```

4. Scroll down to **"Commit changes"**
5. Write a commit message: "Update README with project description"
6. Click **"Commit changes"**

**You just made your first commit!**

---

## 5. Collaboration Features: Pull Requests & Issues

### 5.1 The Collaboration Workflow

In professional development, you rarely commit directly to the main branch. Instead:

```
1. Create a branch      →  2. Make changes      →  3. Open Pull Request
        ↓                         ↓                         ↓
   "feature/login"         commit, commit...        Request review
                                                          ↓
4. Code Review          →  5. Address Feedback  →  6. Merge!
        ↓                         ↓                         ↓
   Team reviews code       Fix issues, discuss      Changes go to main
```

### 5.2 Pull Requests (PRs)

A **Pull Request** is a proposal to merge changes from one branch into another.

**Why not just merge directly?**
- **Code review**: Others can check your work for bugs
- **Discussion**: Team can suggest improvements
- **Documentation**: Creates a record of why changes were made
- **Testing**: Automated tests can run before merging

**Anatomy of a Pull Request:**

```
┌─────────────────────────────────────────────────────────────┐
│  Add user authentication  #42                               │
│  feature/auth → main                                        │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  📝 Description:                                            │
│  This PR adds login and registration functionality          │
│  - Username/password authentication                         │
│  - Session management                                       │
│  - Logout feature                                           │
│                                                             │
│  ✅ All checks passed                                       │
│  👥 Reviewers: @teammate1, @teammate2                       │
│  💬 4 comments                                              │
│                                                             │
│  [Merge pull request]                                       │
└─────────────────────────────────────────────────────────────┘
```

### 5.3 Issues: Tracking Work

**Issues** are GitHub's way to track:
- Bugs that need fixing
- Features to implement
- Questions or discussions
- Documentation improvements

**Example Issue:**

```
┌─────────────────────────────────────────────────────────────┐
│  🐛 Login button doesn't work on Safari  #37               │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  When clicking the login button on Safari 16, nothing       │
│  happens. Works fine on Chrome and Firefox.                 │
│                                                             │
│  Steps to reproduce:                                        │
│  1. Open site in Safari                                     │
│  2. Enter credentials                                       │
│  3. Click "Login"                                           │
│  4. Nothing happens (expected: redirect to dashboard)       │
│                                                             │
│  Labels: bug, high-priority, browser-compatibility          │
│  Assignee: @developer1                                      │
└─────────────────────────────────────────────────────────────┘
```

### 5.4 Forking: Contributing to Others' Projects

**Forking** creates your own copy of someone else's repository.

**The Open Source Contribution Workflow:**

1. **Fork** the original repository (creates your copy)
2. **Clone** your fork to your computer
3. **Create a branch** for your changes
4. **Make changes** and commit them
5. **Push** to your fork
6. **Open a Pull Request** to the original repository
7. **Maintainers review** and potentially merge your contribution

This is how millions of developers contribute to open-source projects!

---

## Checkpoint #3: Collaboration

**Match the term to its purpose:**

| Term | Purpose |
|------|---------|
| 1. Pull Request | A. Track bugs and feature requests |
| 2. Issue | B. Create your own copy of someone's repo |
| 3. Fork | C. Propose merging changes with code review |
| 4. Branch | D. Work on features without affecting main code |

<details>
<summary>Click for Answers</summary>

1. **C** - Pull Request: Propose merging changes with code review
2. **A** - Issue: Track bugs and feature requests
3. **B** - Fork: Create your own copy of someone's repo
4. **D** - Branch: Work on features without affecting main code

</details>

---

## Summary: The GitHub Workflow

Here's how everything fits together:

```
┌─────────────────────────────────────────────────────────────┐
│                    GITHUB WORKFLOW                          │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│    LOCAL (your computer)          REMOTE (GitHub)           │
│                                                             │
│    ┌──────────────┐              ┌──────────────┐          │
│    │  Your Files  │              │  Repository  │          │
│    │              │    push →    │              │          │
│    │  Working     │              │   Branches   │          │
│    │  Directory   │   ← pull     │   Commits    │          │
│    │              │              │   History    │          │
│    └──────────────┘              └──────────────┘          │
│           │                             │                   │
│           ↓                             ↓                   │
│      git commit                   Pull Requests             │
│      (save snapshot)              (code review)             │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Key Takeaways

| Concept | Key Point |
|---------|-----------|
| **Version Control** | Tracks changes over time, enables collaboration, provides backup |
| **Git vs GitHub** | Git is the tool (local), GitHub is the platform (remote hosting) |
| **Repository** | A project folder with complete version history |
| **Commit** | A snapshot with a message describing what changed |
| **Branch** | Independent line of development for features/experiments |
| **Pull Request** | Proposal to merge changes, enables code review |
| **Issue** | Tracking system for bugs, features, and discussions |

---

## Exit Ticket

**Before you leave, answer these questions:**

1. You're working on a group project. Why would you use branches instead of everyone committing to main?

2. Your teammate asks: "I made some changes but I'm not sure if they'll break anything. What should I do?" What GitHub feature would you recommend?

3. In your own words, explain the difference between Git and GitHub using an analogy (different from the email one we used).

---

*Module 4, Lecture 1 | CSCI 101 | Fall 2025*
