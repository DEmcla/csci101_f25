# CLI Lab Setup Script for Windows 11 (PowerShell)
# CSCI 101 - Command Line Interface Mastery
# This script creates the practice environment for CLI labs

Write-Host "============================================" -ForegroundColor Cyan
Write-Host "CLI Lab Environment Setup" -ForegroundColor Cyan
Write-Host "CSCI 101 - Command Line Interface Mastery" -ForegroundColor Cyan
Write-Host "============================================" -ForegroundColor Cyan
Write-Host ""

# Create main lab directory on Desktop
Write-Host "Creating lab directory structure..." -ForegroundColor Yellow
$labPath = "$env:USERPROFILE\Desktop\cli_lab"
New-Item -ItemType Directory -Force -Path $labPath | Out-Null
Set-Location $labPath

# Create Lab 1 structure (web project)
Write-Host "Setting up Lab 1: File System Mastery..." -ForegroundColor Yellow
$dirs = @(
    "myproject",
    "myproject\src",
    "myproject\src\css",
    "myproject\src\js",
    "myproject\src\images",
    "myproject\docs",
    "myproject\tests"
)

foreach ($dir in $dirs) {
    New-Item -ItemType Directory -Force -Path $dir | Out-Null
}

# Create sample files for Lab 1
"# My Project" | Out-File -FilePath "myproject\docs\README.md" -Encoding UTF8
"console.log('Hello World');" | Out-File -FilePath "myproject\src\js\main.js" -Encoding UTF8
"body { margin: 0; }" | Out-File -FilePath "myproject\src\css\style.css" -Encoding UTF8
@"
<!DOCTYPE html>
<html>
<head>
    <title>My Project</title>
</head>
<body>
    <h1>Hello World</h1>
</body>
</html>
"@ | Out-File -FilePath "myproject\src\index.html" -Encoding UTF8

# Create Lab 2 structure and log file
Write-Host "Setting up Lab 2: Log Analysis..." -ForegroundColor Yellow
$logEntries = @"
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
2024-11-20 10:21:23 INFO User login: alice
2024-11-20 10:21:45 ERROR Network timeout after 30 seconds
2024-11-20 10:22:12 WARNING Memory usage critical: 95%
2024-11-20 10:22:34 INFO System maintenance started
2024-11-20 10:23:01 ERROR Failed to write to disk
"@

$logEntries | Out-File -FilePath "server.log" -Encoding UTF8

# Create additional sample files for practice
Write-Host "Creating practice files..." -ForegroundColor Yellow

@"
This is a sample text file for searching.
Error: File not found
Info: Process completed successfully
Warning: Low disk space
"@ | Out-File -FilePath "sample1.txt" -Encoding UTF8

@"
Another sample file with different content.
Error: Connection timeout
Debug: Variable value is 42
"@ | Out-File -FilePath "sample2.txt" -Encoding UTF8

@"
Network configuration details
IP Address: 192.168.1.100
Subnet Mask: 255.255.255.0
Gateway: 192.168.1.1
DNS Server: 8.8.8.8
"@ | Out-File -FilePath "network_info.txt" -Encoding UTF8

# Create directories for Lab 3 and Lab 4
Write-Host "Setting up Lab 3 and Lab 4 directories..." -ForegroundColor Yellow
New-Item -ItemType Directory -Force -Path "system_report" | Out-Null

# Create a README file
Write-Host "Creating README..." -ForegroundColor Yellow
@"
CLI Lab Environment
===================

This directory contains your CLI lab environment.

Directory Structure:
  myproject/       - Web project structure (Lab 1)
  server.log       - Sample log file (Lab 2)
  sample*.txt      - Practice text files
  network_info.txt - Network configuration sample
  system_report/   - Lab 4 working directory

To start labs, open Command Prompt or PowerShell and navigate to:
  cd Desktop\cli_lab

Then type: dir
  (or 'ls' in PowerShell)

Good luck with your labs!
"@ | Out-File -FilePath "README.txt" -Encoding UTF8

Write-Host ""
Write-Host "============================================" -ForegroundColor Green
Write-Host "Setup Complete!" -ForegroundColor Green
Write-Host "============================================" -ForegroundColor Green
Write-Host ""
Write-Host "Your lab environment is ready at:" -ForegroundColor White
Write-Host "  $labPath" -ForegroundColor Cyan
Write-Host ""
Write-Host "To begin labs:" -ForegroundColor White
Write-Host "  1. Open Command Prompt or PowerShell" -ForegroundColor Gray
Write-Host "  2. Type: cd Desktop\cli_lab" -ForegroundColor Gray
Write-Host "  3. Type: dir  (or 'ls' in PowerShell)" -ForegroundColor Gray
Write-Host ""
Write-Host "Press any key to open the lab folder..." -ForegroundColor Yellow
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")

# Open the folder in Explorer
Start-Process explorer.exe $labPath
