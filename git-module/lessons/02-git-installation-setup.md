# Installing and Setting Up Git
*CSCI 101 - Git Module - Lesson 2*

---

## Learning Objectives
By the end of this lesson, you will:
- Successfully install Git on your operating system
- Configure Git with your personal information  
- Access Git through your command line interface
- Verify your installation is working correctly

**Time Estimate:** 30 minutes (varies by platform)

---

## Before You Start

### What You'll Need
- **Administrator access** to your computer (ability to install software)
- **Internet connection** for downloads
- **About 30 minutes** (most of this is download time)

### Choose Your Path
This lesson provides instructions for three platforms. **Jump to your operating system:**
- [Windows 11 (or Windows 10)](#windows-11-installation)
- [macOS](#macos-installation) 
- [Linux](#linux-installation)

---

## Windows 11 Installation

### Step 1: Download Git for Windows

1. **Go to the official Git website**: [https://git-scm.com/](https://git-scm.com/)
2. **Click "Download for Windows"** - the site should automatically detect your OS
3. **Wait for download** - the file will be named something like `Git-2.42.0-64-bit.exe`

### Step 2: Run the Installer

1. **Find your downloaded file** (usually in Downloads folder)
2. **Right-click** and select "Run as administrator" (if prompted)
3. **Follow the installation wizard** - here are the recommended settings:

#### Important Settings (Choose These Options)
- **License**: Click "Next"
- **Installation Location**: Keep default (`C:\Program Files\Git`)
- **Components**: Keep all defaults selected
- **Start Menu Folder**: Keep default
- **Default Editor**: Choose "Use Visual Studio Code" if you have it, otherwise "Use Notepad"
- **Branch Name**: Choose "Override the default branch name for new repositories" → use "main"
- **PATH Environment**: Choose "Git from the command line and also from 3rd-party software"
- **SSH Executable**: Keep default "Use bundled OpenSSH"
- **HTTPS Transport**: Keep default "Use the OpenSSL library"
- **Line Endings**: Choose "Checkout Windows-style, commit Unix-style line endings"
- **Terminal Emulator**: Choose "Use Windows' default console window"
- **Git Pull Behavior**: Keep default "Default (fast-forward or merge)"
- **Credential Helper**: Keep default "Git Credential Manager"
- **Extra Options**: Keep all defaults
- **Experimental Options**: Don't check anything

4. **Click "Install"** and wait for completion

### Step 3: Access Git on Windows

You now have **three ways** to use Git on Windows:

#### Option 1: Git Bash (Recommended for Beginners)
- **How to open**: Start Menu → search "Git Bash" → click it
- **What it is**: Unix-style terminal that works consistently with tutorials
- **When to use**: Following along with lessons and exercises

#### Option 2: Command Prompt
- **How to open**: Start Menu → search "cmd" → click "Command Prompt"
- **What it is**: Traditional Windows command line
- **When to use**: If you prefer Windows-style commands

#### Option 3: PowerShell  
- **How to open**: Start Menu → search "PowerShell" → click it
- **What it is**: Modern Windows command line
- **When to use**: Advanced users or specific Windows integration

**For this course, we recommend Git Bash** because commands will match exactly what we show in lessons.

### Step 4: Verify Installation (Windows)

1. **Open Git Bash**
2. **Type this command and press Enter**:
   ```bash
   git --version
   ```
3. **You should see something like**:
   ```
   git version 2.42.0.windows.1
   ```

If you see a version number, **Git is installed correctly!** Skip to [Configuration](#configuration).

---

## macOS Installation

### Method 1: Check if Already Installed (Try This First)

Many Macs come with Git pre-installed. Let's check:

1. **Open Terminal**:
   - Press `Cmd + Space` to open Spotlight search
   - Type "Terminal" and press Enter
   - OR: Applications → Utilities → Terminal

2. **Check for Git**:
   ```bash
   git --version
   ```

3. **If you see a version number**, Git is already installed! Skip to [Configuration](#configuration).

4. **If you see "command not found"**, continue with Method 2 or 3 below.

### Method 2: Download from Git Website (Easiest)

1. **Go to**: [https://git-scm.com/download/mac](https://git-scm.com/download/mac)
2. **Click** the download link for macOS
3. **Open the downloaded `.dmg` file**
4. **Double-click** the installer and follow instructions
5. **Verify installation** using the command from Method 1

### Method 3: Install Xcode Command Line Tools

1. **Open Terminal** (see Method 1 for how)
2. **Run this command**:
   ```bash
   xcode-select --install
   ```
3. **Click "Install"** when prompted
4. **Wait for download and installation** (can take 10-30 minutes)
5. **Verify installation**:
   ```bash
   git --version
   ```

### Method 4: Using Homebrew (For Advanced Users)

If you already have Homebrew installed:
```bash
brew install git
```

**Don't have Homebrew?** Use Method 2 instead - it's simpler for beginners.

### macOS Troubleshooting

#### If Terminal says "command not found" after installation:
1. **Close and reopen Terminal**
2. **Try the version command again**
3. **If still not working**, restart your computer and try again

#### If you get a security warning:
1. **Go to**: System Preferences → Security & Privacy → General
2. **Click "Allow"** for the Git installer
3. **Try installation again**

---

## Linux Installation

### Ubuntu/Debian Systems

1. **Open Terminal** (`Ctrl + Alt + T`)
2. **Update package list**:
   ```bash
   sudo apt update
   ```
3. **Install Git**:
   ```bash
   sudo apt install git
   ```
4. **Verify installation**:
   ```bash
   git --version
   ```

### Fedora Systems

1. **Open Terminal**
2. **Install Git**:
   ```bash
   sudo dnf install git
   ```
3. **Verify installation**:
   ```bash
   git --version
   ```

### CentOS/RHEL Systems

1. **Open Terminal**
2. **Install Git**:
   ```bash
   sudo yum install git
   ```
3. **Verify installation**:
   ```bash
   git --version
   ```

### Arch Linux Systems

1. **Open Terminal**
2. **Install Git**:
   ```bash
   sudo pacman -S git
   ```
3. **Verify installation**:
   ```bash
   git --version
   ```

---

## Configuration

**After Git is installed on any platform, you need to configure it with your information.**

### Step 1: Set Your Name

Replace "Your Full Name" with your actual name:
```bash
git config --global user.name "Your Full Name"
```

**Example:**
```bash
git config --global user.name "Sarah Johnson"
```

### Step 2: Set Your Email

Replace with your school email or personal email:
```bash
git config --global user.email "your.email@example.com"
```

**Example:**
```bash
git config --global user.email "sarah.johnson@university.edu"
```

### Step 3: Verify Your Configuration

```bash
git config --list
```

You should see your name and email in the output:
```
user.name=Sarah Johnson
user.email=sarah.johnson@university.edu
```

### Why This Configuration Matters

- **Commits are signed** with your name and email
- **Collaboration requires identification** - teammates see who made changes
- **Professional appearance** - your commits look professional on GitHub
- **University requirements** - some professors require school email addresses

---

## Testing Your Installation

Let's make sure everything works correctly:

### Test 1: Version Check
```bash
git --version
```
**Expected result**: Version number (like `git version 2.42.0`)

### Test 2: Configuration Check
```bash
git config --global user.name
git config --global user.email
```
**Expected result**: Your name and email

### Test 3: Help System
```bash
git help
```
**Expected result**: List of common Git commands

### Test 4: Create Test Repository
```bash
mkdir git-test
cd git-test
git init
```
**Expected result**: Message like "Initialized empty Git repository"

**Clean up the test:**
```bash
cd ..
rm -rf git-test
```
(On Windows Command Prompt, use `rmdir /s git-test`)

---

## Troubleshooting Common Issues

### Problem: "git: command not found"

**On Windows:**
- Make sure you installed Git for Windows
- Try using Git Bash instead of Command Prompt
- Restart your computer and try again

**On macOS:**
- Make sure installation completed successfully
- Close and reopen Terminal
- Try installing Xcode Command Line Tools

**On Linux:**
- Make sure you used the correct package manager for your distribution
- Try running `which git` to see if it's installed in an unexpected location

### Problem: Permission denied during installation

**On Windows:**
- Right-click installer and "Run as administrator"
- Make sure you have admin rights on your computer

**On macOS:**
- Enter your password when prompted
- Make sure your account has admin privileges

**On Linux:**
- Make sure you're using `sudo` with installation commands
- Check that your account is in the sudoers group

### Problem: Configuration not saving

- Make sure you're using the `--global` flag
- Check that you have write permissions to your home directory
- Try running `git config --list` to see if settings are actually saved

---

## Platform-Specific Tips

### Windows Users
- **Use Git Bash** for consistency with tutorials
- **File paths** use forward slashes in Git Bash: `/c/Users/username/`
- **Copy/Paste** in Git Bash: Right-click to paste
- **Consider VS Code** as your text editor (works great with Git)

### macOS Users  
- **Terminal shortcuts**: `Cmd+T` for new tab, `Cmd+W` to close tab
- **File paths** start with `/Users/username/`
- **TextEdit warning**: Save as plain text, not rich text
- **Consider VS Code** or another programmer-friendly editor

### Linux Users
- **You probably know this already**, but `Ctrl+C` cancels commands
- **File paths** are case-sensitive (unlike Windows)
- **Package managers** keep Git updated automatically
- **Any text editor works** - nano, vim, emacs, VS Code, etc.

---

## What's Next?

**Congratulations!** 🎉 You now have Git installed and configured. You're ready to create your first repository.

### Before the Next Lesson
- [ ] Git is installed and shows a version number
- [ ] Your name and email are configured
- [ ] You can open your platform's command line interface
- [ ] You feel comfortable with basic command line navigation

### In the Next Lesson
We'll create your very first Git repository and learn the five essential commands every developer uses daily.

**Continue to:** `lessons/03-your-first-repository.md`

---

## Quick Reference

### Command Line Access by Platform
- **Windows**: Git Bash, Command Prompt, or PowerShell
- **macOS**: Terminal (Applications → Utilities → Terminal)
- **Linux**: Terminal (`Ctrl + Alt + T` on most distributions)

### Essential Configuration Commands
```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
git config --list  # View all settings
git --version      # Check Git version
```

---

*Having trouble? Don't hesitate to ask for help in class or office hours. Getting the setup right is crucial for everything that follows!*