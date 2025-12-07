@echo off
REM CLI Lab Setup Script for Windows 11
REM CSCI 101 - Command Line Interface Mastery
REM This script creates the practice environment for CLI labs

echo ============================================
echo CLI Lab Environment Setup
echo CSCI 101 - Command Line Interface Mastery
echo ============================================
echo.

REM Create main lab directory
echo Creating lab directory structure...
cd %USERPROFILE%\Desktop
mkdir cli_lab 2>nul
cd cli_lab

REM Create Lab 1 structure (web project)
echo Setting up Lab 1: File System Mastery...
mkdir myproject 2>nul
mkdir myproject\src 2>nul
mkdir myproject\src\css 2>nul
mkdir myproject\src\js 2>nul
mkdir myproject\src\images 2>nul
mkdir myproject\docs 2>nul
mkdir myproject\tests 2>nul

REM Create sample files for Lab 1
echo # My Project > myproject\docs\README.md
echo console.log('Hello World'); > myproject\src\js\main.js
echo body { margin: 0; } > myproject\src\css\style.css
echo ^<!DOCTYPE html^>^<html^>^<head^>^<title^>My Project^</title^>^</head^>^<body^>^<h1^>Hello^</h1^>^</body^>^</html^> > myproject\src\index.html

REM Create Lab 2 structure and log file
echo Setting up Lab 2: Log Analysis...
echo 2024-11-20 10:15:23 INFO Server started on port 8080 > server.log
echo 2024-11-20 10:15:45 INFO User login: alice >> server.log
echo 2024-11-20 10:16:12 WARNING High memory usage: 85%% >> server.log
echo 2024-11-20 10:16:34 INFO User login: bob >> server.log
echo 2024-11-20 10:17:01 ERROR Database connection failed >> server.log
echo 2024-11-20 10:17:23 INFO Retrying database connection >> server.log
echo 2024-11-20 10:17:45 ERROR Database connection failed >> server.log
echo 2024-11-20 10:18:12 CRITICAL System overload detected >> server.log
echo 2024-11-20 10:18:34 INFO User logout: alice >> server.log
echo 2024-11-20 10:19:01 WARNING Disk space low: 90%% used >> server.log
echo 2024-11-20 10:19:23 INFO User login: charlie >> server.log
echo 2024-11-20 10:19:45 ERROR Failed to load configuration >> server.log
echo 2024-11-20 10:20:12 INFO Configuration loaded from backup >> server.log
echo 2024-11-20 10:20:34 INFO User logout: bob >> server.log
echo 2024-11-20 10:21:01 WARNING CPU usage high: 92%% >> server.log
echo 2024-11-20 10:21:23 INFO User login: alice >> server.log
echo 2024-11-20 10:21:45 ERROR Network timeout after 30 seconds >> server.log
echo 2024-11-20 10:22:12 WARNING Memory usage critical: 95%% >> server.log
echo 2024-11-20 10:22:34 INFO System maintenance started >> server.log
echo 2024-11-20 10:23:01 ERROR Failed to write to disk >> server.log

REM Create additional sample files for practice
echo Creating practice files...
echo This is a sample text file for searching. > sample1.txt
echo Error: File not found >> sample1.txt
echo Info: Process completed successfully >> sample1.txt
echo Warning: Low disk space >> sample1.txt

echo Another sample file with different content. > sample2.txt
echo Error: Connection timeout >> sample2.txt
echo Debug: Variable value is 42 >> sample2.txt

echo Network configuration details > network_info.txt
echo IP Address: 192.168.1.100 >> network_info.txt
echo Subnet Mask: 255.255.255.0 >> network_info.txt
echo Gateway: 192.168.1.1 >> network_info.txt

REM Create directories for Lab 3 and Lab 4
echo Setting up Lab 3 and Lab 4 directories...
mkdir system_report 2>nul

REM Create a README file
echo Creating README...
echo CLI Lab Environment > README.txt
echo =================== >> README.txt
echo. >> README.txt
echo This directory contains your CLI lab environment. >> README.txt
echo. >> README.txt
echo Directory Structure: >> README.txt
echo   myproject/       - Web project structure (Lab 1) >> README.txt
echo   server.log       - Sample log file (Lab 2) >> README.txt
echo   sample*.txt      - Practice text files >> README.txt
echo   network_info.txt - Network configuration sample >> README.txt
echo   system_report/   - Lab 4 working directory >> README.txt
echo. >> README.txt
echo To start labs, open Command Prompt or PowerShell and navigate to: >> README.txt
echo   cd Desktop\cli_lab >> README.txt
echo. >> README.txt

echo.
echo ============================================
echo Setup Complete!
echo ============================================
echo.
echo Your lab environment is ready at:
echo   %USERPROFILE%\Desktop\cli_lab
echo.
echo To begin labs:
echo   1. Open Command Prompt or PowerShell
echo   2. Type: cd Desktop\cli_lab
echo   3. Type: dir
echo.
echo Press any key to open the lab folder...
pause >nul

REM Open the folder in Explorer
explorer "%USERPROFILE%\Desktop\cli_lab"
