# Git Version Control & Portfolio Assignment
**CSCI 101 - Introduction to Computer Science**

---

## Assignment Overview

This assignment combines Git version control with Markdown formatting to give you hands-on experience with two essential tools for computer science. You'll create a personal portfolio repository that showcases your learning journey and demonstrates mastery of professional development tools.

**Learning Objectives:**
- Master the complete Git workflow (init, add, commit, push)
- Understand version control fundamentals and best practices
- Learn Markdown formatting for technical documentation  
- Create a professional GitHub repository and profile
- Develop habits essential for future CS courses and career success

---

## Why Git and GitHub Matter

### For Your Studies
- **Track your progress**: See how your coding skills develop over time
- **Recover from mistakes**: Never lose important work again
- **Submit assignments**: Many CS courses use GitHub for assignment submission
- **Collaborate safely**: Work on group projects without conflicts

### For Your Career
- **Industry standard**: 99% of software companies use Git
- **Professional portfolio**: GitHub serves as your coding resume
- **Open source contribution**: Contribute to projects used by millions
- **Job interviews**: Employers review GitHub profiles during hiring

---

## Part 1: Git Fundamentals Tutorial

### What is Version Control?

Imagine you're writing a research paper. You create `paper.docx`, then `paper_v2.docx`, then `paper_final.docx`, then `paper_final_ACTUALLY_FINAL.docx`. Sound familiar?

**Version control** automatically tracks every change to your files over time, allowing you to:
- Save every version automatically
- See exactly what changed between versions  
- Go back to any previous version instantly
- Work with others without file conflicts

### Installing Git

**Windows:**
- Download from [git-scm.com](https://git-scm.com/)
- Run installer with default options
- Use "Git Bash" for command line access

**Mac:**  
- Git is often pre-installed. Check: `git --version`
- If needed, download from [git-scm.com](https://git-scm.com/)

**Linux:**
```bash
# Ubuntu/Debian
sudo apt update && sudo apt install git
```

### Configure Git
```bash
git config --global user.name "Your Full Name"
git config --global user.email "your.email@example.com"
```

### The Git Workflow

Understanding Git's three-stage workflow is essential:

```
Working Directory → Staging Area → Repository
      ↑                ↑              ↑
   (edit files)    (git add)    (git commit)
```

1. **Working Directory**: Where you edit files
2. **Staging Area**: Files prepared for commit (like a shopping cart)
3. **Repository**: Permanent storage of versions

### Essential Git Commands

```bash
# Repository setup
git init                    # Initialize repository
git status                  # Check status (use frequently!)
git log                     # View commit history

# Basic workflow
git add filename            # Stage specific file
git add .                   # Stage all changes
git commit -m "message"     # Save changes with description
git diff                    # Show what changed

# Remote repositories
git remote add origin <url> # Connect to GitHub
git push -u origin main     # Upload commits (first time)
git push                    # Upload commits (subsequent)
git pull                    # Download changes from GitHub
```

---

## Part 2: Assignment Requirements

### Repository Setup (25 points)

1. **Create Local Repository**
   ```bash
   mkdir csci101-portfolio
   cd csci101-portfolio
   git init
   ```

2. **GitHub Setup**
   - Create account at [github.com](https://github.com)
   - Create new public repository: `csci101-portfolio`
   - Connect local repository to GitHub

3. **Required Structure**
   ```
   csci101-portfolio/
   ├── README.md
   ├── about/
   │   ├── profile.md
   │   └── goals.md
   ├── learning/
   │   ├── week1-notes.md
   │   ├── week2-notes.md
   │   └── resources.md
   └── projects/
       └── project-ideas.md
   ```

### Markdown Documentation (40 points)

Create the following files using proper Markdown syntax:

#### README.md (Repository Homepage)
```markdown
# [Your Name]'s CSCI 101 Portfolio

Welcome to my Computer Science learning journey! This repository documents my progress in CSCI 101.

## About Me
[2-3 sentence introduction about yourself]

## Repository Structure
- **about/**: Personal information and academic goals
- **learning/**: Course notes and helpful resources
- **projects/**: Future project ideas and concepts

## Contact Information
- Email: your.email@example.com
- GitHub: [@yourusername](https://github.com/yourusername)

---
*Last updated: [Current Date]*
```

#### about/profile.md
**Required sections:**
- Personal introduction and background
- Academic journey and interests
- Why you chose Computer Science
- Programming languages (table format):
  
| Language | Experience Level | Interest Level |
|----------|------------------|----------------|
| Python   | Beginner        | High          |
| Java     | None            | Medium        |

- Fun fact about yourself

#### about/goals.md
**Required sections:**
- **Short-term goals** (this semester)
- **Long-term goals** (career/academic)
- **Skills to develop**
- **Courses you're excited about**
- **Industry interests**

#### learning/week1-notes.md & week2-notes.md
For each week:
- **Key concepts learned**
- **Important commands** (use code blocks)
- **Challenges faced**
- **Questions for exploration**
- **Helpful resources discovered**

#### learning/resources.md
Organize by category:
- **Websites and tutorials**
- **YouTube channels**
- **Books and documentation**
- **Tools and software**
- **Study tips**

#### projects/project-ideas.md
List 5+ project ideas with:
- **Description** of each project
- **Technologies** you'd use
- **Difficulty level** (Beginner/Intermediate/Advanced)
- **Why it interests you**

### Git Version Control Demonstration (25 points)

**Commit Requirements:**
- Minimum **8 meaningful commits**
- Each file committed separately when first created
- Show progression through commit history
- Use proper commit message format

**Good Commit Messages:**
- ✅ "Add personal profile with academic background"
- ✅ "Create week 1 notes covering Git fundamentals"
- ✅ "Update project ideas with web development concepts"

**Poor Examples:**
- ❌ "stuff"
- ❌ "changes"  
- ❌ "fix"

### Professional Presentation (10 points)

Your repository should demonstrate:
- **Consistent formatting** throughout all files
- **Professional tone** suitable for employers
- **Complete information** in all required sections
- **Clean organization** and logical structure
- **Working links** (test all internal references)

---

## Technical Requirements Checklist

### Markdown Elements to Use:
- [ ] Headers (multiple levels: #, ##, ###)
- [ ] **Bold** and *italic* text formatting
- [ ] Ordered and unordered lists
- [ ] [External links](https://example.com) and internal links
- [ ] Code blocks with syntax highlighting
- [ ] Tables for organized data
- [ ] > Blockquotes for emphasis
- [ ] Horizontal rules (---)

### Git Skills to Demonstrate:
- [ ] Repository initialization (`git init`)
- [ ] File staging (`git add`)
- [ ] Committing changes (`git commit`)
- [ ] Remote connection (`git remote add`)
- [ ] Pushing to GitHub (`git push`)
- [ ] Status checking (`git status`)
- [ ] History viewing (`git log`)
- [ ] Professional commit messages

---

## Submission Instructions

### Step 1: Final Quality Check
Before submission ensure:
- [ ] All required files present and complete
- [ ] Repository is public on GitHub
- [ ] All commits pushed to GitHub
- [ ] Links work correctly
- [ ] Markdown renders properly on GitHub

### Step 2: Canvas Submission
Submit to Canvas:
1. **GitHub Repository URL** (ensure public access)
2. **Self-Assessment** using provided rubric
3. **Reflection Essay** (2-3 paragraphs):
   - What you learned about Git and Markdown
   - Challenges you overcame
   - How these skills will help in future courses

---

## Grading Rubric

| Component | Excellent (A) | Good (B) | Satisfactory (C) | Needs Work (D-F) |
|-----------|---------------|----------|------------------|------------------|
| **Repository Setup** (25 pts) | Perfect setup, clean structure, proper GitHub connection | Minor setup issues, mostly correct | Basic requirements met, some problems | Major setup issues, incomplete |
| **Markdown Documentation** (40 pts) | All files complete, perfect formatting, professional content | Minor formatting issues, mostly complete | Basic requirements met, some formatting problems | Incomplete content, poor formatting |
| **Git Workflow** (25 pts) | 8+ meaningful commits, excellent workflow | 6-7 good commits, solid workflow | 4-5 commits, basic workflow | Poor commit history, workflow issues |
| **Professional Presentation** (10 pts) | Portfolio-ready, employer-viewable | Minor presentation issues | Acceptable but not polished | Unprofessional or sloppy |

**Total: 100 points**

---

## Tips for Success

### Git Best Practices
1. **Commit frequently** - Don't wait for perfection
2. **Write descriptive messages** - Explain the "why" not just "what"
3. **Check `git status` often** - Know your repository state
4. **Test before committing** - Make sure everything works

### Markdown Tips
1. **Preview your work** - Use VS Code preview or GitHub preview
2. **Keep formatting consistent** - Choose a style and maintain it
3. **Test all links** - Verify internal and external links work
4. **Use whitespace effectively** - Proper spacing improves readability

### Professional Portfolio Advice
1. **Write for your audience** - Future employers may see this
2. **Show personality professionally** - Be authentic but appropriate
3. **Keep it updated** - This can grow throughout your CS career
4. **Proofread carefully** - Grammar and spelling matter professionally

---

## Getting Help

### Available Resources
- **Office Hours**: [Schedule with instructor]
- **Tutoring Center**: [Campus tutoring information]
- **Study Groups**: Form study groups with classmates
- **Online Documentation**: 
  - [GitHub Git Handbook](https://guides.github.com/introduction/git-handbook/)
  - [Markdown Guide](https://www.markdownguide.org/)

### Common Issues & Solutions
- **Can't push to GitHub**: Check repository URL and permissions
- **Markdown not displaying properly**: Verify syntax, especially spacing around elements
- **Git says "not a repository"**: Ensure you ran `git init` in correct directory
- **Commit message editor opens**: Type message, save and close (`:wq` in Vim)

---

## Extension Opportunities

### Extra Credit Options (5 points each)
- **Git Branching**: Create feature branches and merge them
- **Advanced Markdown**: Add badges, images, or complex tables  
- **GitHub Pages**: Set up a live website from your repository
- **Contributing Guidelines**: Add CONTRIBUTING.md and CHANGELOG.md files

### Portfolio Enhancement Ideas
- Add screenshots of your work
- Include links to live project demos
- Create issue templates for feedback
- Add a Code of Conduct for professional presentation

---

## Looking Ahead

This assignment establishes foundation skills for your entire CS career:

### Immediate Applications
- **Future CSCI courses**: All will use Git for assignments
- **Group projects**: Essential collaboration tool
- **Internship applications**: Portfolio demonstrates professionalism
- **Technical interviews**: Shows development workflow understanding

### Professional Preparation
- **Industry standard**: Git is used universally in software development
- **Open source contribution**: Gateway to contributing to major projects
- **Career advancement**: GitHub profiles influence hiring decisions
- **Lifelong learning**: Version control supports continuous skill development

---

**Due Date**: [Insert specific due date]  
**Late Policy**: [Insert course late policy]

*This assignment begins your journey as a professional developer. The habits and skills you develop here will serve you throughout your computer science career. Invest the time to do it well!*