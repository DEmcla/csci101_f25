# Command Line Interface Mastery
## CSCI 101 - Essential System Administration Skills

**Class Duration:** 75 minutes
- **Lecture:** 30 minutes
- **Hands-On Labs:** 45 minutes

**Prerequisites:** Basic computer literacy, terminal access
**Required:** Computer with terminal (Windows PowerShell, Mac Terminal, or Linux Shell)

---

## Learning Objectives

By the end of this class, you will be able to:

- ✓ Navigate file systems using command-line tools
- ✓ Create, copy, move, and delete files/directories
- ✓ Diagnose basic network issues using CLI commands
- ✓ Combine commands using pipes and redirection
- ✓ Apply safety practices to avoid data loss

---

# LECTURE (30 Minutes)

## Part 1: Why CLI Matters (3 minutes)

### The Hidden Power
While GUIs dominate daily computing, CLI is essential for:
- **Server administration** - Most servers have no GUI
- **Network troubleshooting** - Fastest diagnostic tools
- **Automation** - Scripts can repeat complex tasks
- **Speed** - Expert users are 3-5x faster

### CLI vs GUI Quick Comparison

| Task | GUI Time | CLI Time |
|------|----------|----------|
| Find files modified today | 2-3 min | 5 seconds |
| Rename 100 files | 15-20 min | 10 seconds |
| Check network connectivity | 1-2 min | 5 seconds |

**Professional Reality:** System admins, developers, and network engineers spend 40-60% of their time in CLI environments.

---

## Part 2: Command Line Fundamentals (5 minutes)

### Command Anatomy
```bash
command -options arguments
│       │       │
│       │       └── What to act upon
│       └── How to modify behavior
└── What to do
```

**Examples:**
```bash
ls -la /home          # List all files in long format
ping -c 4 google.com  # Ping Google 4 times
```

### Your Shell
- **Windows:** PowerShell or Command Prompt
- **Mac/Linux:** Bash or Zsh (Terminal app)

### Essential Keyboard Shortcuts
| Key | Action |
|-----|--------|
| **Tab** | Auto-complete |
| **Ctrl+C** | Stop current command |
| **↑/↓** | Previous commands |
| **Ctrl+L** | Clear screen |

---

## Part 3: File System Navigation (8 minutes)

### Core Navigation Commands

```bash
pwd                    # Where am I?
ls                     # What's here?
ls -la                 # Detailed list with hidden files
cd /path/to/directory  # Go somewhere
cd ..                  # Go up one level
cd ~                   # Go home
cd -                   # Go to previous location
```

### Understanding Paths

**Absolute Path** (from root):
```bash
/home/username/documents/file.txt     # Linux/Mac
C:\Users\Username\Documents\file.txt  # Windows
```

**Relative Path** (from current location):
```bash
./file.txt            # Current directory
../file.txt           # Parent directory
../../other/file.txt  # Two levels up
```

### File Management Essentials

```bash
# Creating
mkdir project                    # Create directory
mkdir -p project/src/main        # Create nested directories
touch file.txt                   # Create empty file

# Copying and Moving
cp file.txt backup.txt           # Copy file
cp -r directory/ backup/         # Copy directory (recursive)
mv oldname.txt newname.txt       # Rename
mv file.txt /new/location/       # Move

# Deleting (⚠️ NO UNDO!)
rm file.txt                      # Delete file
rm -r directory/                 # Delete directory
```

### Viewing Files

```bash
cat file.txt                     # Display entire file
less file.txt                    # Page through (q to quit)
head file.txt                    # First 10 lines
tail file.txt                    # Last 10 lines
tail -f log.txt                  # Follow file changes (live)
```

### Searching

```bash
grep "search term" file.txt      # Find in file
grep -i "term" file.txt          # Case-insensitive
grep -r "term" directory/        # Search all files
find . -name "*.txt"             # Find files by name
```

---

## Part 4: Network Diagnostics (8 minutes)

### Testing Connectivity

```bash
# Basic ping
ping google.com                  # Test connectivity (Ctrl+C to stop)
ping -c 4 google.com             # Ping 4 times (Linux/Mac)
ping -n 4 google.com             # Ping 4 times (Windows)
```

**Understanding Ping Output:**
```
64 bytes from 172.217.164.110: icmp_seq=0 ttl=117 time=12.3 ms
                               │          │      └── Response time (latency)
                               │          └── Hops remaining
                               └── Packet number
```

### Route Tracing

```bash
traceroute google.com            # Show path to destination (Mac/Linux)
tracert google.com               # Show path (Windows)
```

**Each line = one router hop:**
```
1    192.168.1.1        2.0 ms    # Your router
2    10.0.0.1           8.1 ms    # ISP router
3    * * *                        # Filtered/timeout
```

### DNS and Configuration

```bash
# DNS lookup
nslookup google.com              # Resolve domain to IP

# Network configuration
ifconfig                         # Mac/Linux: Show network info
ipconfig                         # Windows: Show network info
ipconfig /all                    # Windows: Detailed info
```

### Systematic Troubleshooting

When "internet doesn't work":
1. **Test local:** `ping 127.0.0.1` (am I alive?)
2. **Test gateway:** `ping 192.168.1.1` (can I reach my router?)
3. **Test DNS:** `nslookup google.com` (can I resolve names?)
4. **Test external:** `ping 8.8.8.8` (can I reach internet?)
5. **Trace route:** `traceroute google.com` (where does it fail?)

---

## Part 5: Command Combinations & Safety (6 minutes)

### Pipes and Redirection

**Pipe (|)** - Send output to another command:
```bash
ls -la | grep ".txt"             # Filter for .txt files
ps aux | grep firefox            # Find Firefox process
cat log.txt | grep error | wc -l # Count error lines
```

**Redirect (>, >>)** - Save output to file:
```bash
ls -la > filelist.txt            # Save to file (overwrite)
echo "text" >> file.txt          # Append to file
command 2> errors.txt            # Save errors only
```

### Powerful Combinations

```bash
# Find large files
find . -type f -size +100M

# Delete old temporary files
find . -name "*.tmp" -mtime +7 -delete

# Monitor system
ps aux | sort -k 3 -nr | head -5  # Top 5 CPU users
```

### Safety Rules ⚠️

```bash
# DANGEROUS - No undo!
rm -rf /                         # Deletes EVERYTHING
rm -rf *                         # Deletes current directory

# SAFER - Be specific
rm specific_file.txt
rm -r specific_directory/

# TEST FIRST
find . -name "*.tmp" -print      # Preview
find . -name "*.tmp" -delete     # Then delete
```

**Golden Rules:**
1. ✓ **Tab-complete** to avoid typos
2. ✓ **Test with `echo`** before executing
3. ✓ **Backup before major changes**
4. ✓ **Double-check paths** before delete

---

# HANDS-ON LABS (45 Minutes)

## Lab Setup (3 minutes)

### Open Your Terminal
- **Windows:** Search "PowerShell" or "Command Prompt"
- **Mac:** Applications → Utilities → Terminal
- **Linux:** Ctrl+Alt+T

### Create Lab Directory
```bash
cd ~
mkdir cli_lab
cd cli_lab
pwd    # Verify you're in the right place
```

---

## Lab 1: File System Mastery (12 minutes)

### Exercise 1A: Create Project Structure (4 min)

**Scenario:** You're starting a web development project.

**Tasks:**
```bash
# 1. Create this directory structure:
#    myproject/
#    ├── src/
#    │   ├── css/
#    │   ├── js/
#    │   └── images/
#    ├── docs/
#    └── tests/

mkdir -p myproject/{src/{css,js,images},docs,tests}

# 2. Navigate and verify
cd myproject
ls -la
ls -la src/

# 3. Create files
touch src/index.html
touch src/js/main.js
touch src/css/style.css
touch docs/README.md
touch tests/test.js

# 4. Verify files created
find . -type f
```

### Exercise 1B: File Operations (4 min)

**Tasks:**
```bash
# 1. Create sample content
echo "# My Project" > docs/README.md
echo "console.log('Hello');" > src/js/main.js

# 2. View the files
cat docs/README.md
cat src/js/main.js

# 3. Copy files
cp docs/README.md docs/README_backup.md

# 4. Create archive directory
mkdir archive

# 5. Move backup to archive
mv docs/README_backup.md archive/

# 6. Verify structure
ls -la docs/
ls -la archive/
```

### Exercise 1C: Search and Filter (4 min)

**Tasks:**
```bash
# 1. Find all JavaScript files
find . -name "*.js"

# 2. Find all files in src directory
find src -type f

# 3. List all directories
find . -type d

# 4. Create some .tmp files
touch temp1.tmp temp2.tmp src/temp3.tmp

# 5. Find all .tmp files
find . -name "*.tmp"

# 6. Preview deletion (DON'T DELETE YET)
find . -name "*.tmp" -print

# 7. Now delete them
find . -name "*.tmp" -delete

# 8. Verify they're gone
find . -name "*.tmp"
```

**✓ Checkpoint:** You should have a complete project structure with HTML, CSS, JS files, and no .tmp files.

---

## Lab 2: Log Analysis & Text Processing (10 minutes)

### Exercise 2A: Create Sample Log File (3 min)

**Create a simulated log file:**
```bash
# Return to lab directory
cd ~/cli_lab

# Create log entries
cat > server.log << 'EOF'
2024-11-20 10:15:23 INFO Server started on port 8080
2024-11-20 10:15:45 INFO User login: alice
2024-11-20 10:16:12 WARNING High memory usage: 85%
2024-11-20 10:16:34 INFO User login: bob
2024-11-20 10:17:01 ERROR Database connection failed
2024-11-20 10:17:23 INFO Retrying database connection
2024-11-20 10:17:45 ERROR Database connection failed
2024-11-20 10:18:12 CRITICAL System overload detected
2024-11-20 10:18:34 INFO User logout: alice
2024-11-20 10:19:01 WARNING Disk space low: 90% used
2024-11-20 10:19:23 INFO User login: charlie
2024-11-20 10:19:45 ERROR Failed to load configuration
2024-11-20 10:20:12 INFO Configuration loaded from backup
2024-11-20 10:20:34 INFO User logout: bob
2024-11-20 10:21:01 WARNING CPU usage high: 92%
EOF

# Verify file was created
cat server.log
```

### Exercise 2B: Analyze the Log (7 min)

**Tasks:**
```bash
# 1. Count total lines
wc -l server.log

# 2. View first 5 entries
head -n 5 server.log

# 3. View last 5 entries
tail -n 5 server.log

# 4. Find all ERROR entries
grep "ERROR" server.log

# 5. Count how many errors
grep "ERROR" server.log | wc -l

# 6. Find all WARNING and CRITICAL entries
grep -E "WARNING|CRITICAL" server.log

# 7. Find entries for user 'alice'
grep "alice" server.log

# 8. Extract just the timestamps of errors
grep "ERROR" server.log | cut -d' ' -f1-2

# 9. Save all errors to separate file
grep "ERROR" server.log > errors.txt
cat errors.txt

# 10. Append warnings to errors file
grep "WARNING" server.log >> errors.txt
cat errors.txt

# 11. Find all unique log levels
cat server.log | awk '{print $3}' | sort | uniq

# 12. Count entries by log level
cat server.log | awk '{print $3}' | sort | uniq -c
```

**✓ Checkpoint:** You should be able to explain:
- How many total log entries exist
- How many errors occurred
- Which users logged in/out
- What critical issues happened

---

## Lab 3: Network Troubleshooting (12 minutes)

### Exercise 3A: Basic Connectivity Tests (5 min)

**Scenario:** Test your network connectivity.

**Tasks:**
```bash
# 1. Test loopback (am I working?)
ping -c 4 127.0.0.1        # Mac/Linux
ping -n 4 127.0.0.1        # Windows

# 2. Test your gateway (check your actual gateway IP first)
# Find your gateway:
# Mac/Linux:
route -n | grep "^0.0.0.0" | awk '{print $2}'
# Windows:
ipconfig | findstr /i "Gateway"

# Then ping it (replace with YOUR gateway):
ping -c 4 192.168.1.1      # Mac/Linux
ping -n 4 192.168.1.1      # Windows

# 3. Test DNS resolution
nslookup google.com
nslookup github.com
nslookup stackoverflow.com

# 4. Test external connectivity
ping -c 4 8.8.8.8          # Google DNS (Mac/Linux)
ping -n 4 8.8.8.8          # Google DNS (Windows)

# 5. Ping actual website
ping -c 4 google.com       # Mac/Linux
ping -n 4 google.com       # Windows
```

### Exercise 3B: Route Tracing (4 min)

**Tasks:**
```bash
# 1. Trace route to Google (THIS TAKES ~30 SECONDS)
traceroute google.com      # Mac/Linux
tracert google.com         # Windows

# 2. Trace route to another site
traceroute github.com      # Mac/Linux
tracert github.com         # Windows

# 3. Compare the routes - are there common hops?
```

**Analyze the output:**
- First hop = your router
- Second hop = ISP equipment
- Asterisks (*) = filtered/no response
- Final hop = destination

### Exercise 3C: Network Configuration (3 min)

**Tasks:**
```bash
# 1. View your network configuration
# Mac/Linux:
ifconfig                   # Or: ip addr show

# Windows:
ipconfig /all

# 2. Identify your:
#    - IP address
#    - Subnet mask
#    - Default gateway
#    - DNS servers

# 3. Save configuration to file
# Mac/Linux:
ifconfig > my_network_config.txt

# Windows:
ipconfig /all > my_network_config.txt

# 4. View the saved file
cat my_network_config.txt  # Mac/Linux/PowerShell
type my_network_config.txt # Windows cmd
```

**✓ Checkpoint:** You should know:
- Your computer's IP address
- Your default gateway
- Your DNS servers
- How many hops to google.com

---

## Lab 4: Real-World Scenario - System Check (8 minutes)

### Exercise 4: Complete System Diagnostic

**Scenario:** You're asked to document the current state of a system.

**Create a system report:**

```bash
# Navigate to lab directory
cd ~/cli_lab

# Create report directory
mkdir system_report
cd system_report

# 1. System identification
echo "=== System Report ===" > report.txt
echo "Generated: $(date)" >> report.txt
echo "" >> report.txt

# 2. Current location
echo "=== Current Directory ===" >> report.txt
pwd >> report.txt
echo "" >> report.txt

# 3. Disk space
echo "=== Disk Space ===" >> report.txt
df -h >> report.txt 2>&1       # Mac/Linux
# OR
# wmic logicaldisk get size,freespace,caption  # Windows

echo "" >> report.txt

# 4. Current directory contents
echo "=== Directory Contents ===" >> report.txt
ls -la >> report.txt
echo "" >> report.txt

# 5. Network configuration
echo "=== Network Configuration ===" >> report.txt
ifconfig >> report.txt 2>&1     # Mac/Linux
# OR
# ipconfig /all >> report.txt   # Windows

echo "" >> report.txt

# 6. DNS test
echo "=== DNS Test ===" >> report.txt
nslookup google.com >> report.txt 2>&1
echo "" >> report.txt

# 7. Connectivity test
echo "=== Connectivity Test ===" >> report.txt
ping -c 4 google.com >> report.txt 2>&1        # Mac/Linux
# OR
# ping -n 4 google.com >> report.txt           # Windows

# 8. View the report
cat report.txt

# 9. Count lines in report
wc -l report.txt

# 10. Search for specific info
grep -i "inet" report.txt       # Find IP addresses (Mac/Linux)
```

**Advanced: Create a reusable script**

```bash
# Create a script file
cat > system_check.sh << 'EOF'
#!/bin/bash
# System Check Script
DATE=$(date +%Y%m%d_%H%M%S)
REPORT="system_report_$DATE.txt"

echo "Generating system report: $REPORT"

{
    echo "=== System Report ==="
    echo "Generated: $(date)"
    echo ""
    echo "=== Current Location ==="
    pwd
    echo ""
    echo "=== Disk Space ==="
    df -h
    echo ""
    echo "=== Network Config ==="
    ifconfig
    echo ""
    echo "=== DNS Test ==="
    nslookup google.com
    echo ""
    echo "=== Connectivity ==="
    ping -c 4 google.com
} > "$REPORT" 2>&1

echo "Report saved to: $REPORT"
cat "$REPORT"
EOF

# Make it executable (Mac/Linux only)
chmod +x system_check.sh

# Run it
./system_check.sh
```

**✓ Checkpoint:** You should have:
- A complete system report in a text file
- Documentation of your network configuration
- Proof of internet connectivity
- A reusable script (optional)

---

## Wrap-Up & Assessment (5 minutes)

### Quick Challenge

Without looking at notes, try to:

```bash
# 1. Go to your home directory
cd ~

# 2. Create this structure:
#    challenge/
#    ├── data/
#    └── output/

mkdir -p challenge/{data,output}

# 3. Create a file with your name
echo "Your Name" > challenge/data/student.txt

# 4. Copy it to output
cp challenge/data/student.txt challenge/output/

# 5. List all files in challenge
find challenge -type f

# 6. Test network and save result
ping -c 2 google.com > challenge/output/network_test.txt

# 7. View the result
cat challenge/output/network_test.txt
```

### Self-Assessment Checklist

Can you do these WITHOUT looking at notes?

- [ ] Navigate to any directory using `cd`
- [ ] List files with details using `ls -la`
- [ ] Create files and directories
- [ ] Copy and move files
- [ ] Search for text in files with `grep`
- [ ] Test network connectivity with `ping`
- [ ] Look up domain names with `nslookup`
- [ ] Combine commands with `|` and `>`
- [ ] Safely delete files

**If you checked 7+:** You're ready for basic CLI work!
**If you checked 5-6:** Review the labs and practice more
**If you checked <5:** Schedule office hours for additional help

---

## Take-Home Practice

### Daily Practice (Week 1)
Do ALL your file operations via CLI for one week:
- Navigate folders
- Create files/folders
- Copy and move files
- Search for files

### Network Troubleshooting Practice
When internet seems slow:
1. Run `ping google.com` - check latency
2. Run `traceroute google.com` - find slow hops
3. Run `nslookup google.com` - test DNS

### Muscle Memory Commands
Practice these until automatic:
```bash
pwd              # Where am I?
ls -la           # What's here?
cd ..            # Go up
grep "x" file    # Find text
find . -name "x" # Find file
ping google.com  # Test network
```

---

## Reference Card (Save This!)

### Essential Commands

```bash
# Navigation
pwd                          # Print working directory
ls -la                       # List all files with details
cd /path                     # Change directory
cd ~ or cd                   # Go home
cd ..                        # Go up one level

# File Management
mkdir dirname                # Create directory
mkdir -p path/to/dir         # Create nested directories
touch file.txt               # Create empty file
cp source dest               # Copy file
cp -r source dest            # Copy directory
mv old new                   # Rename/move
rm file                      # Delete file
rm -r dir                    # Delete directory

# Viewing Files
cat file.txt                 # Display file
less file.txt                # Page through (q to quit)
head file.txt                # First 10 lines
tail file.txt                # Last 10 lines
tail -f file.txt             # Follow file changes

# Searching
grep "text" file             # Find in file
grep -i "text" file          # Case-insensitive
find . -name "*.txt"         # Find files by name

# Network
ping host                    # Test connectivity
traceroute host              # Trace route (Mac/Linux)
tracert host                 # Trace route (Windows)
nslookup domain              # DNS lookup
ifconfig                     # Network config (Mac/Linux)
ipconfig                     # Network config (Windows)

# Combining Commands
command1 | command2          # Pipe output
command > file               # Save output (overwrite)
command >> file              # Append output
```

### Keyboard Shortcuts

```bash
Tab                          # Auto-complete
Ctrl+C                       # Stop command
Ctrl+L                       # Clear screen
↑/↓                         # Command history
Ctrl+A                       # Beginning of line
Ctrl+E                       # End of line
```

---

## Next Steps

### Immediate Practice
- Complete all 4 labs on your own machine
- Repeat until you can do without notes
- Try the take-home challenges

### This Week
- Use CLI for ALL file operations
- Troubleshoot network issues with CLI tools
- Create a habit of using terminal daily

### Advanced Topics (Future)
- Bash scripting and automation
- SSH and remote access
- Git version control
- Text processing with awk/sed
- System administration tasks

---

**Remember:** CLI mastery is like learning to type - awkward at first, then indispensable. Practice daily for two weeks and it becomes second nature.

**Questions?** Review the labs, check the reference card, and practice!

---

**End of Class Materials**
