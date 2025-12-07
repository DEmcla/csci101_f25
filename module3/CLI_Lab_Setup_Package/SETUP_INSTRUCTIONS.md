# CLI Lab Setup Package
## CSCI 101 - Command Line Interface Mastery

This package contains all the files you need for the CLI labs on locked-down Windows 11 systems.

---

## Quick Start

### Option 1: Automatic Setup (Recommended)

1. **Download this entire folder** to your Desktop
2. **Double-click** `setup_lab.bat`
3. Wait for "Setup Complete!" message
4. Lab environment will open automatically

### Option 2: PowerShell Setup (Alternative)

1. Right-click `setup_lab.ps1`
2. Select "Run with PowerShell"
3. If you see a security warning, type `Y` and press Enter
4. Wait for completion

### Option 3: Manual Setup (If scripts are blocked)

If administrative restrictions prevent running scripts:

1. Create folder on Desktop: `Desktop\cli_lab`
2. Copy all files from this package into `cli_lab`
3. Open Command Prompt or PowerShell
4. Navigate to: `cd Desktop\cli_lab`

---

## What Gets Created

The setup script creates this structure on your Desktop:

```
Desktop\cli_lab\
├── README.txt              # Lab information
├── server.log              # Sample log file for Lab 2
├── sample1.txt             # Practice text file
├── sample2.txt             # Practice text file
├── network_info.txt        # Sample network data
├── system_report\          # Lab 4 working directory
└── myproject\              # Lab 1 web project
    ├── src\
    │   ├── css\
    │   │   └── style.css
    │   ├── js\
    │   │   └── main.js
    │   ├── images\
    │   └── index.html
    ├── docs\
    │   └── README.md
    └── tests\
```

---

## Files Included in This Package

| File | Purpose |
|------|---------|
| `setup_lab.bat` | Automatic setup script (Batch) |
| `setup_lab.ps1` | Automatic setup script (PowerShell) |
| `server.log` | Sample log file with 20 entries |
| `SETUP_INSTRUCTIONS.md` | This file |
| `TROUBLESHOOTING.md` | Help if things go wrong |

---

## Verifying Setup

After running setup, open Command Prompt and type:

```cmd
cd Desktop\cli_lab
dir
```

You should see:
- myproject folder
- server.log file
- sample1.txt and sample2.txt
- network_info.txt
- system_report folder
- README.txt

---

## Starting Your Labs

### Open Command Prompt:
1. Press `Windows Key`
2. Type `cmd`
3. Press Enter

### Navigate to lab folder:
```cmd
cd Desktop\cli_lab
```

### Verify you're in the right place:
```cmd
cd
```
Should show: `C:\Users\YourName\Desktop\cli_lab`

---

## Important Notes for Locked-Down Systems

✓ **Works without admin rights** - All commands use your user directory
✓ **No installations required** - Uses built-in Windows commands
✓ **Safe to practice** - All operations are in your Desktop\cli_lab folder
✓ **Can delete anytime** - Just delete the cli_lab folder when done

---

## Troubleshooting

### "Cannot run script" error
- Use `setup_lab.bat` instead of `.ps1`
- Or follow Option 3 (Manual Setup)

### "Access denied" error
- Make sure you're saving to Desktop (not C:\ or Program Files)
- Check with instructor if issues persist

### "File not found" error
- Make sure you extracted ALL files from the zip
- Verify you're in Desktop\cli_lab folder

### Commands not working
- Make sure you're using Command Prompt or PowerShell
- Don't use Windows Explorer for commands
- Check spelling carefully

---

## Need Help?

1. Check `TROUBLESHOOTING.md` in this folder
2. Ask your instructor or TA
3. Verify you're in the correct directory: `cd Desktop\cli_lab`
4. Try closing and reopening Command Prompt

---

## After Class

You can:
- Keep practicing in this folder
- Delete the cli_lab folder when done
- Re-run setup script anytime to start fresh

---

**Ready to start?** Run the setup script and open Command Prompt!
