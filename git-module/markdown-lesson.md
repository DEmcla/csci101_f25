# Markdown Tutorial for Computer Science Students
*CSCI 101 - Git Module*

---

## Table of Contents
1. [What is Markdown?](#what-is-markdown)
2. [Why Use Markdown in Computer Science?](#why-use-markdown-in-computer-science)
3. [Basic Markdown Syntax](#basic-markdown-syntax)
4. [Advanced Formatting](#advanced-formatting)
5. [Code and Technical Writing](#code-and-technical-writing)
6. [Creating Professional Documentation](#creating-professional-documentation)
7. [Markdown Tools and Editors](#markdown-tools-and-editors)
8. [Practice Exercises](#practice-exercises)

---

## What is Markdown?

**Markdown** is a lightweight markup language that lets you format text using simple, readable syntax. You write in plain text with special characters, and it gets converted to formatted HTML.

### Example:
**You write this:**
```markdown
# My Project
This is **bold text** and this is *italic text*.

- Item 1
- Item 2
- Item 3
```

**It becomes this:**
# My Project
This is **bold text** and this is *italic text*.

- Item 1
- Item 2  
- Item 3

### Key Benefits
- **Simple**: Easy to learn and write
- **Readable**: Looks good even as plain text
- **Portable**: Works everywhere (GitHub, websites, documentation)
- **Version Control Friendly**: Perfect with Git (unlike Word docs!)

---

## Why Use Markdown in Computer Science?

### 📚 **Academic Uses**
- **README files**: Explain what your code does
- **Assignment documentation**: Write clear project reports
- **Study notes**: Format technical concepts clearly
- **Lab reports**: Include code, explanations, and results

### 💼 **Professional Uses**
- **GitHub repositories**: Every project needs a good README
- **Technical documentation**: API docs, user guides, tutorials
- **Project proposals**: Clean, professional formatting
- **Blog posts**: Many tech blogs use Markdown

### 🔧 **Why It's Perfect for Programmers**
- **Plain text**: Works with any editor, version control systems
- **Code-friendly**: Built-in syntax highlighting for code blocks
- **Fast**: No clicking through menus like in Word
- **Consistent**: Looks the same everywhere

---

## Basic Markdown Syntax

### Headers
```markdown
# Header 1 (Biggest)
## Header 2
### Header 3
#### Header 4
##### Header 5
###### Header 6 (Smallest)
```

### Text Formatting
```markdown
**Bold text**
*Italic text*
***Bold and italic***
~~Strikethrough~~
```

**Result:**
**Bold text**
*Italic text*
***Bold and italic***
~~Strikethrough~~

### Lists

**Unordered Lists:**
```markdown
- First item
- Second item
  - Nested item
  - Another nested item
- Third item
```

**Ordered Lists:**
```markdown
1. First step
2. Second step
3. Third step
   1. Sub-step
   2. Another sub-step
```

### Links and Images
```markdown
[Link text](https://example.com)
[Link to file](./path/to/file.md)

![Alt text for image](https://example.com/image.jpg)
![Local image](./images/screenshot.png)
```

### Paragraphs and Line Breaks
- Separate paragraphs with empty lines
- For line breaks within a paragraph, end line with two spaces

```markdown
This is paragraph one.

This is paragraph two.

This line ends with two spaces  
This creates a line break in the same paragraph.
```

---

## Advanced Formatting

### Tables
```markdown
| Column 1 | Column 2 | Column 3 |
|----------|----------|----------|
| Row 1    | Data     | More data|
| Row 2    | Info     | Details  |
```

**Result:**
| Column 1 | Column 2 | Column 3 |
|----------|----------|----------|
| Row 1    | Data     | More data|
| Row 2    | Info     | Details  |

### Blockquotes
```markdown
> This is a quote.
> It can span multiple lines.
> 
> - You can even include lists
> - Inside quotes
```

**Result:**
> This is a quote.
> It can span multiple lines.
> 
> - You can even include lists
> - Inside quotes

### Horizontal Rules
```markdown
Three or more dashes:
---

Three or more asterisks:
***
```

### Escape Characters
Use backslash `\` to display special characters literally:
```markdown
\*This won't be italic\*
\# This won't be a header
```

---

## Code and Technical Writing

### Inline Code
```markdown
Use `backticks` for inline code like `print("Hello")` or `git status`.
```

**Result:** Use `backticks` for inline code like `print("Hello")` or `git status`.

### Code Blocks

**Basic code block:**
````markdown
```
def hello():
    print("Hello, World!")
```
````

**With syntax highlighting:**
````markdown
```python
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)
```
````

**Result:**
```python
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)
```

### Popular Languages for Syntax Highlighting
- `python` - Python code
- `java` - Java code  
- `javascript` - JavaScript code
- `html` - HTML markup
- `css` - CSS styles
- `sql` - Database queries
- `bash` - Terminal commands
- `json` - JSON data

### Terminal Commands
````markdown
```bash
git init
git add .
git commit -m "Initial commit"
```
````

---

## Creating Professional Documentation

### Project README Template
```markdown
# Project Name

Brief description of what your project does.

## Features
- Feature 1
- Feature 2
- Feature 3

## Installation
```bash
# Installation commands here
```

## Usage
```python
# Code example here
```

## Contributing
Instructions for contributors.

## License
License information.
```

### Assignment Report Template
```markdown
# Assignment 1: [Title]
**Student:** Your Name  
**Course:** CSCI 101  
**Date:** [Date]

## Overview
Brief description of the assignment.

## Approach
Explain your approach to solving the problem.

## Implementation
```python
# Your code here
```

## Results
Describe what happened when you ran your code.

## Challenges
What problems did you encounter?

## Conclusion
What did you learn?
```

---

## Markdown Tools and Editors

### Text Editors with Markdown Support
- **VS Code**: Excellent Markdown preview and extensions
- **Sublime Text**: Clean interface with Markdown packages
- **Atom**: GitHub's editor with built-in Markdown support
- **Typora**: WYSIWYG Markdown editor (beginner-friendly)

### Online Editors
- **GitHub**: Edit Markdown files directly in browser
- **StackEdit**: Online Markdown editor with live preview
- **Dillinger**: Simple online Markdown editor

### Preview in VS Code
1. Open a `.md` file
2. Press `Ctrl+Shift+V` (Windows) or `Cmd+Shift+V` (Mac)
3. Split view: `Ctrl+K V` (Windows) or `Cmd+K V` (Mac)

---

## Practice Exercises

### Exercise 1: Personal Profile
Create a `profile.md` file with:
- Your name as a main header
- Brief introduction about yourself
- List of your interests
- Your goals in computer science
- A table with your favorite programming languages (even if you're just starting!)

### Exercise 2: Course Notes
Create `csci101-notes.md` with:
- Headers for different topics
- Code examples you've learned
- Important concepts in blockquotes
- Links to useful resources

### Exercise 3: Project Documentation
Create documentation for a hypothetical project:
- Project title and description
- Installation instructions
- Code examples with syntax highlighting
- Screenshots (use placeholder links)

---

## Common Mistakes to Avoid

1. **Missing spaces**: Headers need space after `#`
   - ❌ `#Header`
   - ✅ `# Header`

2. **No empty lines**: Separate different elements
   - ❌ Mixing headers and lists without spacing
   - ✅ Use empty lines between different sections

3. **Inconsistent list formatting**:
   - ❌ Mixing `-` and `*` for bullets
   - ✅ Pick one style and stick with it

4. **Code block syntax**: Use three backticks, not one
   - ❌ Single backticks for multi-line code
   - ✅ Triple backticks for code blocks

---

## Markdown Cheat Sheet

| Element | Syntax | Example |
|---------|--------|---------|
| Header | `# H1` | # Header 1 |
| Bold | `**text**` | **bold** |
| Italic | `*text*` | *italic* |
| Code | `` `code` `` | `inline code` |
| Link | `[text](url)` | [GitHub](https://github.com) |
| List | `- item` | - bullet point |
| Quote | `> text` | > quoted text |
| Table | `\| col \| col \|` | \| data \| data \| |

---

## What's Next?

After mastering Markdown:

1. **Practice with Git**: Use Markdown files in your repositories
2. **Explore GitHub**: See how open source projects use Markdown
3. **Documentation**: Start documenting your code projects
4. **Technical Writing**: Use Markdown for lab reports and assignments

### Advanced Topics to Explore Later
- **GitHub Flavored Markdown**: Extra features specific to GitHub
- **Math Equations**: LaTeX-style math in Markdown
- **Diagrams**: Mermaid diagrams in Markdown
- **Custom HTML**: Mixing HTML with Markdown for advanced formatting

---

## Resources

- [Markdown Guide](https://www.markdownguide.org/) - Comprehensive reference
- [GitHub Markdown Documentation](https://docs.github.com/en/get-started/writing-on-github)
- [CommonMark Spec](https://commonmark.org/) - Standard Markdown specification
- [Markdown Cheat Sheet](https://www.markdownguide.org/cheat-sheet/)

---

*Remember: The best way to learn Markdown is to use it! Start writing your documentation in Markdown today.*