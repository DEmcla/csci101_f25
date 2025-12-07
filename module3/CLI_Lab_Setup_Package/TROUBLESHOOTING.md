# Troubleshooting Guide
## CLI Lab Setup - Windows 11

---

## Common Setup Issues

### Problem: "Windows protected your PC" message

**Solution:**
1. Click "More info"
2. Click "Run anyway"
3. Or use `setup_lab.bat` instead of `.ps1`

### Problem: PowerShell execution policy error

**Error message:** `cannot be loaded because running scripts is disabled`

**Solution:**
- Use `setup_lab.bat` instead (just double-click it)
- Batch files work on all locked-down systems

### Problem: Setup script doesn't run at all

**Solution - Manual Setup:**
1. Open Command Prompt (Windows Key → type `cmd`)
2. Type these commands one at a time:
```cmd
cd Desktop
mkdir cli_lab
cd cli_lab
mkdir myproject
mkdir myproject\src
mkdir myproject\docs
mkdir myproject\tests
mkdir system_report
```

3. Copy `server.log` file manually to `Desktop\cli_lab\`

---

## Common Lab Issues

### Problem: "The system cannot find the path specified"

**Cause:** You're not in the correct directory

**Solution:**
```cmd
cd %USERPROFILE%\Desktop\cli_lab
```

Or:
```cmd
cd Desktop\cli_lab
```

### Problem: Commands show "'command' is not recognized"

**Examples:**
- `'ls' is not recognized`
- `'grep' is not recognized`

**Solution:**
Use Windows equivalents:

| Unix/Mac Command | Windows Command Prompt | PowerShell |
|-----------------|----------------------|------------|
| `ls` | `dir` | `ls` or `dir` |
| `ls -la` | `dir` | `ls` or `dir` |
| `cat file.txt` | `type file.txt` | `cat file.txt` or `type` |
| `grep "text" file` | `findstr "text" file` | `Select-String "text" file` |
| `rm file` | `del file` | `del file` or `Remove-Item` |

### Problem: "Access is denied" when creating files

**Cause:** Trying to create files outside your user directory

**Solution:**
- Always work in `Desktop\cli_lab`
- Never try to create files in `C:\` or `C:\Program Files`
- Check current location: `cd`

### Problem: Can't see file extensions (.txt, .log, etc.)

**Solution:**
In File Explorer:
1. Click "View" tab
2. Check "File name extensions"

Or use Command Prompt - it always shows extensions:
```cmd
dir
```

### Problem: "mkdir" creates directory but shows error

**Example:** `A subdirectory or file myproject already exists.`

**Solution:**
- This is normal if directory already exists
- Not actually an error - just a warning
- Continue with next command

---

## Network Command Issues

### Problem: "ping" command hangs forever

**Cause:** Default ping in Windows continues until stopped

**Solution:**
- Use `-n` to limit: `ping -n 4 google.com`
- Or press `Ctrl+C` to stop

### Problem: "Request timed out" when pinging

**Possible causes:**
1. No internet connection
2. Firewall blocking ping
3. Website blocking ICMP

**Solution:**
- Try different site: `ping -n 4 8.8.8.8`
- Check with instructor if campus network blocks ping
- This is expected on some networks

### Problem: "tracert" shows only asterisks (* * *)

**Cause:** Routers not responding or firewall blocking

**Solution:**
- This is normal for some network segments
- Look for rows that DO show IP addresses
- Focus on first few hops (your network)

---

## File Operation Issues

### Problem: Can't delete file - "file is being used"

**Solution:**
1. Close any programs that might have the file open
2. Close and reopen Command Prompt
3. Try again

### Problem: "del" deletes without confirmation

**Note:** This is normal Windows behavior

**Solution:**
- Double-check filename before pressing Enter
- Use `dir` to verify file exists first
- There is no "undo" for command line deletion

### Problem: Copy/paste doesn't work in Command Prompt

**Solution:**

**To paste in Command Prompt:**
- Right-click in Command Prompt window
- Or: Enable Ctrl+V in Properties

**To copy from Command Prompt:**
- Right-click and drag to select text
- Press Enter to copy
- Or: Enable Ctrl+C in Properties (under "Edit Options")

---

## Path and Navigation Issues

### Problem: "cd" command doesn't change drive

**Example:** You're on C:\ and want to go to D:\

**Solution:**
Use `/d` flag:
```cmd
cd /d D:\folder
```

Or just type the drive letter:
```cmd
D:
```

### Problem: Space in path name causes error

**Example:** `cd C:\Program Files` doesn't work

**Solution:**
Use quotes:
```cmd
cd "C:\Program Files"
```

### Problem: Lost - don't know where I am

**Solution:**
```cmd
cd
```
Shows your current directory

### Problem: Want to go back to previous directory

**Solution:**
```cmd
cd ..
```
Goes up one level

---

## Text File Issues

### Problem: Text file shows weird characters

**Cause:** Wrong encoding or line endings

**Solution:**
- Use `type` command instead of opening in Notepad
- File content should still be readable
- Use PowerShell: `Get-Content file.txt`

### Problem: Can't find text with findstr

**Example:** `findstr "ERROR" server.log` shows nothing

**Solution:**
- Check spelling (case matters by default)
- Use `/i` for case-insensitive: `findstr /i "error" server.log`
- Verify file exists: `dir server.log`
- Make sure you're in right directory: `cd`

---

## Quick Diagnostic Commands

If something isn't working, try these:

```cmd
REM Where am I?
cd

REM What's in this folder?
dir

REM Is the file really here?
dir server.log

REM What's in the file?
type server.log

REM Can I access network?
ping -n 2 8.8.8.8

REM Start fresh in lab folder
cd %USERPROFILE%\Desktop\cli_lab
```

---

## Still Having Problems?

### Quick Fixes:

1. **Close and reopen Command Prompt**
   - Fixes many weird issues

2. **Verify you're in lab folder**
   ```cmd
   cd Desktop\cli_lab
   ```

3. **Re-run setup script**
   - Closes all programs
   - Double-click `setup_lab.bat`
   - Creates fresh environment

4. **Check with instructor**
   - Show them exact error message
   - Show them output of: `cd` command

---

## Emergency Reset

If everything is broken:

```cmd
REM Delete everything (be careful!)
cd Desktop
rmdir /s cli_lab

REM Start over
(Double-click setup_lab.bat again)
```

---

## Contact Information

**During Class:**
- Raise your hand
- Ask instructor or TA

**After Class:**
- Email instructor with:
  - Screenshot of error
  - Output of `cd` command
  - What command you were trying

---

**Remember:** The command line is picky about:
- Spelling (case matters sometimes)
- Spaces (use quotes for paths with spaces)
- Location (make sure you're in the right directory)

**Most problems are solved by:**
1. Checking where you are: `cd`
2. Checking what's there: `dir`
3. Starting fresh: Close and reopen Command Prompt
