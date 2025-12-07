# Command Line Interface Mastery
## CSCI 101 - Essential System Administration Skills

**Lecture Duration:** 90-120 minutes
**Prerequisites:** Basic computer literacy, familiarity with file systems
**Materials Needed:** Computer with terminal access (Windows/Mac/Linux)

---

## Learning Objectives

By the end of this lesson, students will be able to:

- ✓ Navigate file systems efficiently using command-line tools
- ✓ Manage files and directories with confidence
- ✓ Execute network diagnostic commands for troubleshooting
- ✓ Understand the philosophy and power of CLI-based computing
- ✓ Develop workflows that combine multiple commands effectively
- ✓ Troubleshoot common system and network issues from the command line

---

## Lecture Outline

### Part 1: Introduction and Philosophy (15 minutes)
- Why master the command line?
- CLI vs. GUI comparison
- Real-world applications

### Part 2: Command Line Fundamentals (20 minutes)
- Understanding the shell
- Command anatomy and structure
- Common shells across platforms

### Part 3: File System Navigation (25 minutes)
- Essential navigation commands
- Path concepts (absolute vs. relative)
- File and directory management
- File content operations

### Part 4: Network Diagnostics (20 minutes)
- Connectivity testing (ping, traceroute)
- Network configuration commands
- DNS operations
- Advanced diagnostics

### Part 5: System Information and Monitoring (15 minutes)
- Process management
- System resources
- Log file monitoring

### Part 6: Practical Applications and Workflows (15 minutes)
- Command combinations
- Pipes and redirection
- Real-world scenarios

### Part 7: Best Practices and Safety (10 minutes)
- Safety considerations
- Backup strategies
- Building fluency

---

# PART 1: Introduction and Philosophy

## Why Master the Command Line?

### The Hidden Power Behind Modern Computing

While graphical interfaces dominate daily computing, the command line interface (CLI) remains the backbone of:

- **Server administration** - Most servers run without GUIs
- **Network troubleshooting** - Fastest diagnostic tools available
- **Software development** - Version control, build systems, deployment
- **Data analysis** - Powerful text processing and automation
- **System automation** - Scripting repetitive tasks

### CLI vs. GUI: When Each Excels

#### GUI Advantages:
- Visual feedback and intuitive navigation
- Discovery of features through exploration
- Reduced learning curve for basic tasks
- Better for creative work (design, media editing)

#### CLI Advantages:
- **Speed:** Expert users work much faster
- **Precision:** Exact control over operations
- **Automation:** Scripts can repeat complex tasks
- **Remote access:** Works over network connections
- **Resource efficiency:** Minimal system overhead
- **Batch operations:** Process hundreds of files at once

> **Professional Reality:** System administrators, developers, and network engineers spend significant time in CLI environments. Mastering these tools is essential for IT careers.

---

# PART 2: Command Line Fundamentals

## Understanding the Shell

The **shell** is your command interpreter - it takes your typed commands and executes them.

### Common Shells:

| Shell | Platform | Description |
|-------|----------|-------------|
| **Bash** | Linux/Mac | Bourne Again Shell - most common, default on most systems |
| **PowerShell** | Windows | Modern shell with object-oriented approach |
| **Command Prompt** | Windows | Traditional Windows shell (cmd) |
| **Zsh** | Mac/Linux | Enhanced Bash with better auto-completion |
| **Fish** | Mac/Linux | User-friendly shell with syntax highlighting |

## Anatomy of a Command

```bash
command -options arguments
│       │       │
│       │       └── What to act upon
│       └── How to modify behavior
└── What to do
```

### Examples:

```bash
ls -la /home/user          # List all files in long format
ping -c 4 google.com       # Ping Google 4 times
cp -r source/ destination/ # Copy directory recursively
```

### Command Structure Patterns

1. **Basic Commands:** `ls`, `pwd`, `date`
2. **Commands with Arguments:** `cd /home`, `cat filename.txt`
3. **Commands with Options:** `ls -l`, `ping -c 4`
4. **Complex Commands:** `find /home -name "*.txt" -size +1M`

---

# PART 3: File System Navigation Mastery

## Essential Navigation Commands

### Current Location Commands

```bash
pwd                    # Print Working Directory - where am I?
ls                     # List contents of current directory
ls -l                  # Long format (permissions, size, date)
ls -la                 # Include hidden files (starting with .)
ls -lh                 # Human-readable file sizes
ls -lt                 # Sort by modification time
```

#### Understanding `ls -la` Output:

```
drwxr-xr-x  5 user  group   160 Nov 20 10:30 Documents
-rw-r--r--  1 user  group  1024 Nov 19 15:45 file.txt
│││││││││  │  │     │       │    │           └── Filename
│││││││││  │  │     │       │    └── Modification date/time
│││││││││  │  │     │       └── Size in bytes
│││││││││  │  │     └── Group owner
│││││││││  │  └── Owner
│││││││││  └── Number of links
└─┴─┴─┴─┴─┴─┴─┴─┴── Permissions (owner-group-others)
```

### Directory Navigation

```bash
cd /path/to/directory  # Change to specific directory
cd ~                   # Go to home directory
cd ..                  # Go up one directory level
cd -                   # Return to previous directory
cd                     # Go to home directory (same as cd ~)
```

### Path Understanding

#### Absolute Paths: Start from root directory

```bash
# Linux/Mac
/home/username/documents/file.txt

# Windows
C:\Users\Username\Documents\file.txt
```

#### Relative Paths: From current location

```bash
./file.txt            # File in current directory
../file.txt           # File in parent directory
../../other/file.txt  # Two levels up, then into 'other'
```

## File and Directory Management

### Creating Structure

```bash
mkdir project                    # Create single directory
mkdir -p project/src/main       # Create nested directories (-p creates parents)
mkdir project1 project2         # Create multiple directories
touch filename.txt               # Create empty file
touch file1.txt file2.txt       # Create multiple files
```

### Copying and Moving

```bash
cp file.txt backup.txt           # Copy file
cp -r directory/ backup/         # Copy directory recursively (-r required for directories)
mv oldname.txt newname.txt       # Rename/move file
mv file.txt /new/location/       # Move to different directory
mv *.txt documents/              # Move all .txt files (using wildcard)
```

### Deleting Files and Directories

```bash
rm filename.txt                  # Delete file
rm -r directory/                 # Delete directory and contents
rm -f filename.txt               # Force delete (no prompts)
rm -rf directory/                # Force delete directory (DANGEROUS!)
rm *.tmp                         # Delete all .tmp files
```

> ⚠️ **WARNING:** There's no "Recycle Bin" in CLI. Deleted files are typically gone forever!

## File Content Operations

### Viewing File Contents

```bash
cat filename.txt                 # Display entire file
less filename.txt                # Page through file (q to quit, / to search)
head filename.txt                # First 10 lines
head -n 20 filename.txt          # First 20 lines
tail filename.txt                # Last 10 lines
tail -f logfile.txt              # Follow file changes (great for logs)
```

### Searching Within Files

```bash
grep "search term" filename.txt              # Find lines containing term
grep -i "search term" filename.txt          # Case-insensitive search
grep -r "search term" directory/            # Search all files in directory
grep -n "search term" filename.txt          # Show line numbers
grep -v "search term" filename.txt          # Show lines NOT containing term
find /path -name "*.txt" -exec grep "term" {} \;  # Search in found files
```

### File Properties and Permissions

```bash
ls -l filename.txt               # Detailed file information
file filename.txt                # Determine file type
du -h filename.txt               # File size (human-readable)
du -sh directory/                # Directory size
chmod 755 filename.txt           # Change file permissions (Linux/Mac)
chown user:group filename.txt    # Change ownership (Linux/Mac)
```

---

# PART 4: Network Diagnostic Commands

## Connectivity Testing

### Basic Connectivity with Ping

```bash
# Linux/Mac
ping google.com                  # Test basic connectivity (continuous)
ping -c 4 google.com             # Ping 4 times then stop

# Windows
ping google.com                  # Ping 4 times by default
ping -n 4 google.com             # Explicitly ping 4 times
ping -t google.com               # Continuous ping (Ctrl+C to stop)

# IPv6
ping6 ipv6.google.com            # IPv6 ping (Linux/Mac)
```

#### Understanding Ping Output:

```
PING google.com (172.217.164.110): 56 data bytes
64 bytes from 172.217.164.110: icmp_seq=0 ttl=117 time=12.345 ms
│                               │          │      │        └── Round-trip time
│                               │          │      └── Time To Live (hops remaining)
│                               │          └── Packet sequence number
│                               └── IP address resolved from domain
```

**What each metric means:**
- **IP Address:** Resolved from domain name via DNS
- **icmp_seq:** Packet sequence number (detects packet loss/reordering)
- **ttl:** Time To Live - remaining router hops allowed
- **time:** Round-trip time in milliseconds (latency)

### Route Tracing

```bash
# Linux/Mac
traceroute google.com            # Trace route to destination
mtr google.com                   # Continuous trace route (better visualization)

# Windows
tracert google.com               # Trace route to destination
```

#### Interpreting Traceroute Output:

```
1    192.168.1.1 (gateway)       2.045 ms   1.987 ms   2.123 ms
2    10.0.0.1 (ISP router)       8.123 ms   7.899 ms   8.234 ms
3    * * *                       (timeout or filtered)
4    172.217.164.110             12.345 ms  11.987 ms  12.456 ms
```

Each line shows:
- **Hop number**
- **IP address/hostname** of router
- **Three round-trip times** (three packets sent per hop)
- **Asterisks (*)** indicate no response (firewall or timeout)

## Network Configuration

### Interface Information

```bash
# Linux/Mac
ifconfig                         # All network interfaces (older command)
ifconfig eth0                    # Specific interface
ip addr show                     # Modern Linux command (preferred)
ip link show                     # Show link layer information
ip route show                    # Display routing table

# Windows
ipconfig                         # Basic IP configuration
ipconfig /all                    # Detailed configuration
ipconfig /release                # Release DHCP lease
ipconfig /renew                  # Renew DHCP lease
route print                      # Display routing table
```

### DNS Operations

```bash
# Cross-platform
nslookup google.com              # Basic DNS lookup
nslookup google.com 8.8.8.8     # Use specific DNS server

# Linux/Mac (more detailed)
dig google.com                   # Detailed DNS information
dig @8.8.8.8 google.com          # Use specific DNS server
dig google.com +short            # Just show IP address
dig -x 8.8.8.8                   # Reverse DNS lookup

# Windows-specific
nslookup -type=MX google.com     # Mail exchange records
nslookup -type=NS google.com     # Name server records
```

## Advanced Network Diagnostics

### Port and Service Testing

```bash
# Test if specific port is open
telnet google.com 80             # Test HTTP port
nc -zv google.com 80             # Test with netcat (Linux/Mac)
nc -zv google.com 80-443         # Scan port range

# Show all network connections
netstat -an                      # All connections (numeric)
netstat -tulpn                   # TCP/UDP with process info (Linux)
ss -tulpn                        # Modern replacement for netstat (Linux)

# Windows
netstat -ano                     # All connections with PID
netstat -b                       # Show executable (requires admin)
```

### Network Statistics

```bash
# Linux/Mac
iftop                            # Real-time bandwidth usage (requires install)
netstat -i                       # Interface statistics
netstat -s                       # Protocol statistics

# Windows
netstat -e                       # Interface statistics
netstat -s                       # Protocol statistics
```

---

# PART 5: System Information and Monitoring

## Process Management

```bash
# Linux/Mac
ps aux                           # All running processes
ps -ef                           # Alternative format
ps aux | grep firefox            # Find specific process
top                              # Real-time process monitor (q to quit)
htop                             # Enhanced top (if installed)

# Process control
kill 1234                        # Terminate process by PID
kill -9 1234                     # Force kill (SIGKILL)
killall firefox                  # Terminate by process name
pkill firefox                    # Pattern-based kill

# Windows
tasklist                         # List running processes
tasklist /fi "STATUS eq running" # Filter running processes
taskkill /PID 1234               # Kill process by PID
taskkill /IM notepad.exe         # Kill by process name
taskkill /F /IM notepad.exe      # Force kill
```

## System Resources

```bash
# Linux/Mac
df -h                            # Disk space usage (human-readable)
df -h /home                      # Specific filesystem
free -h                          # Memory usage
uptime                           # System uptime and load average
uname -a                         # System information
lscpu                            # CPU information
lsblk                            # Block device information

# Windows
dir C:\ /s                       # Directory listing with subdirectories
systeminfo                       # Comprehensive system information
wmic cpu get name                # CPU information
wmic memorychip get capacity     # Memory information
```

## Log File Monitoring

```bash
# Linux/Mac
tail -f /var/log/syslog          # Follow system log in real-time
tail -n 100 /var/log/syslog      # Last 100 lines
journalctl -f                    # Follow systemd journal
journalctl -u ssh.service        # Logs for specific service
dmesg                            # Kernel ring buffer messages
dmesg | tail -50                 # Recent kernel messages

# Windows
# Most log viewing in Windows is GUI-based (Event Viewer)
wevtutil qe System /c:10 /rd:true /f:text  # Recent system events
wevtutil qe Application /c:20              # Application events
```

---

# PART 6: Command Combinations and Workflows

## Pipes and Redirection

### Pipes (|): Send output of one command to another

```bash
ls -la | grep ".txt"             # List only .txt files
ps aux | grep firefox            # Find Firefox processes
cat logfile.txt | grep error | wc -l  # Count error lines
history | grep ssh               # Search command history for ssh
df -h | sort -k 5 -n             # Sort disk usage by percentage
```

### Redirection (>, >>, <):

```bash
# Output redirection
ls -la > filelist.txt            # Save output to file (overwrite)
echo "new line" >> filelist.txt  # Append to file
command 2> errors.txt            # Save error output only
command &> all_output.txt        # Save both stdout and stderr
command > output.txt 2>&1        # Alternative: redirect both

# Input redirection
wc -l < file.txt                 # Count lines (input from file)
mysql -u user -p database < dump.sql  # Import SQL file
```

## Useful Command Combinations

### Find and Process Files

```bash
# Show last 10 lines of all log files
find . -name "*.log" -exec tail -n 10 {} \;

# Delete all temporary files
find . -name "*.tmp" -delete

# Find files larger than 100MB
find . -type f -size +100M

# Find and compress old log files
find /var/log -name "*.log" -mtime +30 -exec gzip {} \;

# Find files modified in last 24 hours
find . -type f -mtime -1
```

### System Monitoring Combinations

```bash
# Top 10 CPU users
ps aux | sort -k 3 -nr | head -10

# Top 10 memory users
ps aux | sort -k 4 -nr | head -10

# Disk usage without temporary filesystems
df -h | grep -v tmpfs

# Count web server connections
netstat -an | grep :80 | wc -l

# Monitor CPU usage every 2 seconds
while true; do uptime; sleep 2; done
```

### Text Processing

```bash
# Remove duplicate lines
cat file.txt | sort | uniq

# Count unique IP addresses in log
cat access.log | awk '{print $1}' | sort | uniq -c

# Find which log files contain errors
grep "ERROR" *.log | cut -d: -f1 | sort | uniq

# Extract email addresses from file
grep -Eo '\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b' file.txt

# Count word frequency
cat file.txt | tr ' ' '\n' | sort | uniq -c | sort -nr
```

---

# PART 7: Hands-On Activities and Practical Scenarios

## Activity 1: File System Organization

**Scenario:** Create a project structure for a web development project

### Tasks:

1. **Create directory structure:**
```bash
mkdir -p myproject/{src,docs,tests,assets/{images,css,js}}
```

2. **Navigate and explore:**
```bash
cd myproject
tree                             # Show directory tree (if available)
find . -type d                   # List all directories
ls -R                            # Recursive listing
```

3. **Create files:**
```bash
touch src/index.html src/main.js
touch docs/README.md docs/API.md
touch tests/test_main.js
touch assets/css/style.css
```

4. **Verify structure:**
```bash
ls -la
ls -la src/
find . -name "*.js"              # Find all JavaScript files
find . -type f                   # List all files
du -sh *                         # Size of each directory
```

## Activity 2: Log Analysis

**Scenario:** Analyze system logs to identify issues

### Tasks:

1. **View recent system activity:**
```bash
# Linux/Mac
tail -n 50 /var/log/syslog | grep -i error
journalctl --since "1 hour ago" | grep -i error
journalctl --since today | grep -i fail

# Windows
wevtutil qe System /c:50 /rd:true /f:text | findstr /i error
```

2. **Monitor live log activity:**
```bash
# Linux/Mac
tail -f /var/log/syslog

# Watch for specific patterns
tail -f /var/log/syslog | grep --line-buffered "error\|warning"

# Watch directory for changes
watch -n 2 'ls -la /tmp'
```

## Activity 3: Network Troubleshooting Workflow

**Scenario:** User reports "can't access websites"

### Systematic Troubleshooting:

1. **Test local connectivity:**
```bash
ping 127.0.0.1                  # Test loopback (verify TCP/IP stack)
ping 192.168.1.1                # Test gateway (adjust for your network)
```

2. **Test DNS resolution:**
```bash
nslookup google.com              # Can we resolve names?
ping 8.8.8.8                     # Test Google's DNS directly (bypasses DNS)
```

3. **Test external connectivity:**
```bash
ping google.com                  # Test external site
traceroute google.com            # Find where connection fails
```

4. **Check network configuration:**
```bash
# Linux/Mac
ifconfig                         # Check IP configuration
route -n                         # Check routing table
cat /etc/resolv.conf             # Check DNS servers

# Windows
ipconfig /all                    # Check IP configuration
route print                      # Check routing table
```

5. **Document findings:**
```bash
# Save diagnostic output
{
  echo "=== Network Diagnostics ==="
  date
  echo "=== IP Configuration ==="
  ifconfig
  echo "=== Routing Table ==="
  route -n
  echo "=== DNS Test ==="
  nslookup google.com
  echo "=== Ping Test ==="
  ping -c 4 google.com
} > network_diagnostics.txt
```

## Activity 4: System Performance Investigation

**Scenario:** System seems slow

### Investigation Steps:

1. **Check system load:**
```bash
# Linux/Mac
top                              # Interactive (press 1 to see all CPUs)
uptime                           # Load average
df -h                            # Disk space
free -h                          # Memory usage
iostat                           # I/O statistics (if available)

# Windows
tasklist                         # Running processes
systeminfo | findstr /C:"Total Physical Memory"
```

2. **Identify resource hogs:**
```bash
# Linux/Mac
ps aux --sort=-%cpu | head -10   # Top CPU users
ps aux --sort=-%mem | head -10   # Top memory users
lsof | wc -l                     # Count open files

# Windows
tasklist /fi "memusage gt 100000" # Processes using >100MB RAM
wmic process get name,workingsetsize | sort
```

3. **Check disk I/O:**
```bash
# Linux
iotop                            # Real-time disk I/O (requires install)
iostat -x 2                      # Extended I/O stats every 2 seconds

# Check which process is using disk
lsof | grep deleted              # Deleted but open files
```

4. **Check network usage:**
```bash
netstat -an | wc -l              # Count active connections
ss -s                            # Socket statistics (Linux)
lsof -i                          # Network connections by process
```

---

# PART 8: Platform-Specific Considerations

## Windows: Command Prompt vs. PowerShell

### Command Prompt (cmd) Basics:

```cmd
dir                              # List directory contents
dir /s                           # Recursive listing
cd C:\path\to\directory          # Change directory
copy file.txt backup.txt         # Copy file
xcopy /E source dest             # Copy directory tree
del file.txt                     # Delete file
type file.txt                    # Display file contents
find "text" file.txt             # Search in file
```

### PowerShell Advantages:

```powershell
Get-ChildItem                    # List directory (ls alias works)
Get-ChildItem -Recurse           # Recursive listing
Get-Process                      # List processes
Get-Service                      # List services
Get-NetAdapter                   # Network adapters
Test-NetConnection google.com    # Enhanced ping with port testing
Get-Content file.txt | Select-String "pattern"  # Search in file
Get-EventLog -LogName System -Newest 20  # Recent system events
```

## Linux/Mac Terminal Enhancements

### Bash Keyboard Shortcuts:

| Shortcut | Action |
|----------|--------|
| **Tab** | Auto-complete command/path |
| **Ctrl+C** | Interrupt current command |
| **Ctrl+Z** | Suspend current command |
| **Ctrl+D** | End input / Logout |
| **Ctrl+L** | Clear screen |
| **Ctrl+A** | Move to beginning of line |
| **Ctrl+E** | Move to end of line |
| **Ctrl+R** | Search command history |
| **↑/↓** | Navigate command history |
| **!!** | Repeat last command |
| **!$** | Last argument of previous command |

### Useful Aliases (add to ~/.bashrc or ~/.zshrc):

```bash
# Navigation
alias ll='ls -la'
alias la='ls -A'
alias l='ls -CF'
alias ..='cd ..'
alias ...='cd ../..'

# Safety
alias rm='rm -i'
alias cp='cp -i'
alias mv='mv -i'

# Utilities
alias grep='grep --color=auto'
alias h='history'
alias c='clear'
alias ports='netstat -tulanp'
alias myip='curl ifconfig.me'

# Git shortcuts (if using Git)
alias gs='git status'
alias ga='git add'
alias gc='git commit'
alias gp='git push'
```

---

# PART 9: Safety and Best Practices

## Command Line Safety Rules

### 1. Always Double-Check Dangerous Commands

```bash
# EXTREMELY DANGEROUS - can delete everything
rm -rf /
rm -rf /*

# DANGEROUS - deletes all files in current directory
rm -rf *

# SAFER - be specific
rm -rf /path/to/specific/directory
rm -f specific_file.txt
```

### 2. Use Tab Completion to Avoid Typos

- Type partial filename and press **Tab**
- Reduces risk of targeting wrong files
- Shell will complete or show options

### 3. Test Commands Safely First

```bash
# PREVIEW what would be deleted
find . -name "*.tmp" -print

# Then actually delete after verification
find . -name "*.tmp" -delete

# Test copy operation
cp -v source dest               # Verbose mode shows what's copied

# Dry run for rsync
rsync -av --dry-run source/ dest/
```

### 4. Use `echo` to Test Complex Commands

```bash
# Test before executing
echo rm *.txt                   # See what would be deleted
echo mv *.jpg ~/Pictures/       # See what would be moved

# Then execute
rm *.txt
```

## Backup Before Major Changes

```bash
# Create simple backup
cp -r important_directory/ important_directory_backup/

# Create timestamped backup
cp -r project/ project_backup_$(date +%Y%m%d_%H%M%S)/

# Create compressed archive
tar -czf backup_$(date +%Y%m%d).tar.gz important_directory/

# Create incremental backup with rsync
rsync -av --delete source/ backup/
```

## Emergency Recovery

### If a Command Hangs:

| Key | Action |
|-----|--------|
| **Ctrl+C** | Interrupt most commands |
| **Ctrl+Z** | Suspend command (resume with `fg`) |
| **Ctrl+D** | End input stream |
| **Ctrl+\** | Force quit (SIGQUIT) |

### If You Made a Mistake:

```bash
# If you just deleted something
# Linux/Mac: Check trash (if using GUI)
# Windows: Check Recycle Bin

# Restore from backup
cp -r backup/ original/

# Use version control if available
git checkout -- deleted_file.txt
```

---

# PART 10: Building CLI Fluency

## Daily Practice Recommendations

### Week 1: Basic Navigation
- ✓ Use CLI for all file operations
- ✓ Practice with `ls`, `cd`, `pwd`, `mkdir`
- ✓ Navigate without GUI file manager
- ✓ Goal: Navigate entire file system confidently

### Week 2: File Operations
- ✓ Copy, move, and organize files via CLI
- ✓ Practice with `cp`, `mv`, `rm`
- ✓ Use `find` to locate files
- ✓ Goal: Manage files faster than GUI

### Week 3: System Monitoring
- ✓ Check system status daily via CLI
- ✓ Use `top`, `ps`, `df`, `netstat`
- ✓ Monitor log files with `tail -f`
- ✓ Goal: Understand system health at a glance

### Week 4: Network Operations
- ✓ Troubleshoot network issues via CLI
- ✓ Practice `ping`, `traceroute`, `nslookup`
- ✓ Analyze network configuration
- ✓ Goal: Diagnose connectivity problems independently

## Advanced Skills Development

### 1. Scripting: Automate Repetitive Tasks

```bash
#!/bin/bash
# Simple backup script
DATE=$(date +%Y%m%d)
SOURCE=~/important_files
DEST=~/backups

# Create backup directory
mkdir -p $DEST

# Create compressed archive
tar -czf $DEST/backup_$DATE.tar.gz $SOURCE

# Keep only last 7 days of backups
find $DEST -name "backup_*.tar.gz" -mtime +7 -delete

echo "Backup completed: backup_$DATE.tar.gz"
```

### 2. Regular Expressions: Powerful Pattern Matching

```bash
# Find IP addresses in log file
grep -E '[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}' logfile.txt

# Lines starting with ERROR
grep '^ERROR' logfile.txt

# Email addresses
grep -Eo '\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b' file.txt

# Phone numbers (US format)
grep -E '\(?[0-9]{3}\)?[-. ]?[0-9]{3}[-. ]?[0-9]{4}' contacts.txt
```

### 3. Process Management: Control Running Programs

```bash
# Run command in background
long_running_command &

# Run command that persists after logout
nohup long_running_command &

# List background jobs
jobs

# Bring job to foreground
fg %1

# Send job to background
bg %1

# Disown job (won't receive SIGHUP)
disown %1
```

---

# PART 11: Career Relevance and Next Steps

## Industry Applications

### System Administration
- Server configuration and maintenance
- Log analysis and troubleshooting
- Automated deployment and monitoring
- Batch user account management
- Scheduled task automation

### Software Development
- Version control (Git commands)
- Build systems and CI/CD pipelines
- Database management and queries
- Code deployment and testing
- Development environment setup

### Cybersecurity
- Network scanning and analysis
- Log forensics and incident response
- Penetration testing tools
- Security monitoring and alerting
- Vulnerability assessment

### Data Science
- Large dataset processing
- Statistical analysis with command-line tools
- Automation of data pipelines
- Remote server data analysis
- Batch data transformation

## Advanced CLI Tools to Explore

### Text Processing
```bash
awk         # Pattern scanning and processing
sed         # Stream editor for filtering/transforming
jq          # JSON processor
cut         # Extract columns from files
paste       # Merge files side-by-side
```

### System Monitoring
```bash
htop        # Enhanced process viewer
iotop       # I/O monitoring by process
nethogs     # Network usage per process
atop        # Advanced system monitor
glances     # Cross-platform monitoring tool
```

### Productivity Tools
```bash
tmux        # Terminal multiplexer (multiple terminals in one)
screen      # Alternative terminal multiplexer
vim/emacs   # Powerful text editors
git         # Version control system
ssh         # Secure remote access
```

---

# PART 12: Mastery Checklist

## You have achieved CLI competency when you can:

- [ ] Navigate file systems efficiently without GUI
- [ ] Manage files and directories with confidence
- [ ] Diagnose network issues using command-line tools
- [ ] Monitor system performance and identify bottlenecks
- [ ] Combine commands effectively using pipes and redirection
- [ ] Troubleshoot problems systematically using CLI tools
- [ ] Work remotely via SSH or other terminal connections
- [ ] Automate repetitive tasks with basic scripting
- [ ] Read and understand command documentation (man pages)
- [ ] Recover gracefully from mistakes

---

## Key Takeaways

### The CLI Mindset
Think in terms of commands, not clicks. Consider how to accomplish tasks efficiently through text-based interfaces rather than graphical ones.

### Professional Impact
CLI mastery dramatically increases your effectiveness in technical roles. Tasks that might take minutes through GUI interfaces can often be accomplished in seconds via command line, especially when dealing with multiple files or repetitive operations.

### Continuous Learning
The command line is vast. Focus on:
1. **Core commands** you use daily
2. **Problem-solving patterns** that repeat
3. **Automation opportunities** in your workflow
4. **Documentation skills** (man pages, help commands)

> **Remember:** The command line is not just a tool—it's a way of thinking about computing that emphasizes precision, efficiency, and automation. These skills will serve you throughout your career in technology.

---

## Additional Resources

### Documentation
- `man command` - Manual pages (Linux/Mac)
- `command --help` - Help flag (most commands)
- `help command` - Built-in help (Windows cmd)
- `Get-Help command` - PowerShell help

### Online Resources
- **ExplainShell.com** - Breaks down complex commands
- **TLDR Pages** - Simplified man pages with examples
- **Stack Overflow** - Community Q&A
- **Command Line Challenge** - Practice exercises

### Practice Environments
- **Linux VM** - Install Ubuntu/Fedora in VirtualBox
- **Windows Subsystem for Linux (WSL)** - Linux on Windows
- **Online terminals** - Repl.it, JSLinux
- **Raspberry Pi** - Affordable Linux hardware

---

## Assessment Criteria

Students will be evaluated on their ability to:

1. **Execute fundamental commands** (30%)
   - Navigate file systems
   - Manage files and directories
   - View and search file contents

2. **Perform network diagnostics** (25%)
   - Test connectivity with ping
   - Trace routes with traceroute
   - Query DNS information
   - Interpret diagnostic output

3. **Monitor system resources** (20%)
   - Check process information
   - Analyze disk and memory usage
   - Monitor log files

4. **Combine commands effectively** (15%)
   - Use pipes and redirection
   - Create command workflows
   - Apply logical problem-solving

5. **Apply safety and best practices** (10%)
   - Verify commands before execution
   - Create backups appropriately
   - Recover from mistakes

---

**End of Lecture Notes**

*These notes are designed for flexible delivery - adapt timing and depth based on student experience level and available lab time.*
