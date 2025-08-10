# Git & Markdown Assignment
**CSCI 101 - Version Control Module**

---

## Assignment Overview

This assignment combines Git version control with Markdown formatting to give you hands-on experience with two essential tools for computer science. You'll create a personal portfolio repository that showcases your learning journey and technical skills.

**Learning Objectives:**
- Practice the complete Git workflow (init, add, commit, push)
- Master Markdown formatting for technical documentation
- Create a professional GitHub repository
- Develop good version control habits
- Build foundation skills for future CS courses

---

## Assignment Requirements

### Part 1: Repository Setup (20 points)

1. **Create Local Repository**
   - Create a new directory called `csci101-portfolio`
   - Initialize as a Git repository
   - Configure your Git identity (name and email)

2. **Create GitHub Repository**
   - Create a new public repository on GitHub named `csci101-portfolio`
   - Connect your local repository to GitHub
   - Make your initial push

3. **Repository Structure**
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

### Part 2: Markdown Documentation (40 points)

Create the following files using proper Markdown formatting:

#### 1. README.md (Main repository page)
```markdown
# [Your Name]'s CSCI 101 Portfolio

Welcome to my Computer Science journey! This repository documents my learning experience in CSCI 101.

## About Me
Brief introduction (2-3 sentences)

## Repository Structure
- **about/**: Personal information and goals
- **learning/**: Course notes and resources
- **projects/**: Project ideas and future work

## Contact
- Email: your.email@example.com
- GitHub: [@yourusername](https://github.com/yourusername)

---
*Last updated: [Date]*
```

#### 2. about/profile.md
**Required sections:**
- Personal introduction
- Academic background
- Interests (both technical and personal)
- Why you chose Computer Science
- Table of programming languages you know/want to learn
- Fun fact about yourself

#### 3. about/goals.md  
**Required sections:**
- Short-term goals (this semester)
- Long-term goals (career/academic)
- Skills you want to develop
- Courses you're excited about
- Industry areas of interest

#### 4. learning/week1-notes.md & week2-notes.md
**For each week, include:**
- Key concepts learned
- Important commands/syntax (use code blocks)
- Challenges faced
- Questions for further exploration
- Links to helpful resources

#### 5. learning/resources.md
**Organize resources by category:**
- Useful websites
- YouTube channels
- Books or tutorials
- Tools and software
- Study tips

#### 6. projects/project-ideas.md
**List 5+ project ideas:**
- Brief description of each project
- Technologies you'd use
- Difficulty level (beginner/intermediate/advanced)
- Why it interests you

### Part 3: Git Version Control (25 points)

**Commit Requirements:**
- Minimum 8 meaningful commits
- Each file should be committed separately when first created
- Show progression of work through commit history
- Use proper commit message format

**Commit Message Examples:**
- ✅ "Add personal profile with academic background"
- ✅ "Update week 1 notes with Git commands"
- ✅ "Create project ideas list with 6 potential projects"
- ❌ "stuff"
- ❌ "changes"
- ❌ "fixed"

**Branching (Optional Extra Credit - 5 points):**
- Create a branch for experimental features
- Make commits on the branch
- Merge back to main branch

### Part 4: Professional Presentation (15 points)

Your repository should demonstrate:
- **Consistent formatting**: Proper Markdown syntax throughout
- **Professional tone**: Appropriate for potential employers to view
- **Complete information**: All required sections filled out thoroughly
- **Clean organization**: Logical file structure and navigation
- **Working links**: All internal links should work correctly

---

## Technical Requirements

### Markdown Elements You Must Use:
- [ ] Headers (multiple levels)
- [ ] **Bold** and *italic* text
- [ ] Unordered and ordered lists
- [ ] Links (both external and internal)
- [ ] Code blocks with syntax highlighting
- [ ] Tables
- [ ] Blockquotes
- [ ] Horizontal rules

### Git Skills You Must Demonstrate:
- [ ] Repository initialization
- [ ] File staging (`git add`)
- [ ] Committing changes (`git commit`)
- [ ] Pushing to remote (`git push`)
- [ ] Viewing status and history (`git status`, `git log`)
- [ ] Meaningful commit messages
- [ ] Proper Git configuration

---

## Submission Instructions

### Step 1: Final Repository Check
Before submitting, ensure:
- All required files are present and complete
- Repository is public on GitHub
- All commits are pushed to GitHub
- Links work correctly
- Markdown renders properly on GitHub

### Step 2: Canvas Submission
Submit the following to Canvas:
1. **GitHub Repository URL** (make sure it's accessible)
2. **Self-Assessment** (see rubric below)
3. **Reflection** (2-3 paragraphs):
   - What did you learn about Git and Markdown?
   - What challenges did you face?
   - How will these skills help in future courses?

### Step 3: Peer Review (Optional)
Exchange repository URLs with a classmate and provide constructive feedback on:
- Markdown formatting
- Content organization
- Professional presentation
- Git commit quality

---

## Grading Rubric

### Repository Setup (20 points)
- **Excellent (18-20)**: Perfect setup, clean structure, proper remote connection
- **Good (15-17)**: Minor setup issues, mostly correct structure
- **Satisfactory (12-14)**: Basic setup complete, some organizational issues
- **Needs Improvement (0-11)**: Major setup problems, incomplete structure

### Markdown Documentation (40 points)
- **Excellent (36-40)**: All files complete, perfect formatting, professional content
- **Good (30-35)**: Minor formatting issues, mostly complete content
- **Satisfactory (24-29)**: Basic requirements met, some formatting problems
- **Needs Improvement (0-23)**: Incomplete content, poor formatting

### Git Version Control (25 points)
- **Excellent (23-25)**: 8+ meaningful commits, perfect workflow demonstrated
- **Good (19-22)**: 6-7 commits, good workflow with minor issues
- **Satisfactory (15-18)**: 4-5 commits, basic workflow understood
- **Needs Improvement (0-14)**: Poor commit history, workflow problems

### Professional Presentation (15 points)
- **Excellent (14-15)**: Repository ready for professional viewing
- **Good (11-13)**: Minor presentation issues
- **Satisfactory (8-10)**: Acceptable but not polished
- **Needs Improvement (0-7)**: Unprofessional or incomplete presentation

**Total: 100 points**

---

## Tips for Success

### Git Best Practices
1. **Commit early and often** - Don't wait until everything is perfect
2. **Write descriptive commit messages** - Your future self will thank you
3. **Check `git status` frequently** - Know what's staged and what isn't
4. **Use `.gitignore`** for files you don't want to track

### Markdown Tips  
1. **Preview your work** - Use VS Code's Markdown preview or GitHub's preview
2. **Keep it simple** - Don't over-complicate the formatting
3. **Test your links** - Make sure internal links work correctly
4. **Use consistent formatting** - Pick a style and stick with it

### Professional Portfolio Tips
1. **Write for your audience** - Assume potential employers might see this
2. **Be authentic** - Show your personality while remaining professional
3. **Keep it updated** - This repository can grow throughout your CS career
4. **Proofread everything** - Spelling and grammar matter

---

## Getting Help

### Resources
- **Git Tutorial**: See `git-tutorial.md` in this module
- **Markdown Lesson**: See `markdown-lesson.md` in this module
- **Office Hours**: [Instructor office hours]
- **Study Groups**: Collaborate with classmates

### Common Issues
- **Can't push to GitHub**: Check your repository URL and permissions
- **Markdown not rendering**: Check your syntax, especially spacing
- **Git says "not a repository"**: Make sure you ran `git init`
- **Merge conflicts**: Ask for help - we'll cover this later in the course

---

## Extension Opportunities

For students who finish early or want extra challenges:

### Advanced Git Features (Extra Credit)
- Create and work with branches
- Practice merging branches
- Use Git tags for versions

### Enhanced Documentation
- Add a `CONTRIBUTING.md` file
- Create a `CHANGELOG.md` to track updates
- Add badges to your README (build status, etc.)

### Portfolio Expansion
- Add screenshots of your work
- Include links to live demos (when you have projects)
- Create a personal website using GitHub Pages

---

**Due Date**: [Insert due date]  
**Late Policy**: [Insert late policy]

*This assignment serves as your introduction to the tools you'll use throughout your Computer Science career. Take time to do it well - these skills will serve you in every future course!*