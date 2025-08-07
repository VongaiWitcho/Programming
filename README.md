# 📁 File Backup Logger

A file and directory backup tool with versioning, ZIP support, and logging — all wrapped in a clean, user-friendly GUI. Easily copy or compress folders, log backup activity with timestamps, file counts, durations, and more. Configurable via a JSON settings file.

---
# File Backup Logger - User Guide

## Main Interface

![Main GUI](https://github.com/VongaiWitcho/Programming/blob/main/filelogger.PNG))

## Log Output Example

![Log Output](https://github.com/VongaiWitcho/Programming/file_backup_logger/fileloggerlogs.png)


## ✅ Features

- 🔄 Backup entire folders with versioning
- 🗜️ Choose between ZIP compression or plain copy
- 📋 Log backups with:
  - Timestamp
  - File count
  - Duration
  - Backup size
- 🖥️ Intuitive GUI built with Tkinter
- ⚙️ Save your preferences in a JSON config file
- 🧱 Object-Oriented Design for easy extension

---

## 🏁 Getting Started

### 📦 Prerequisites

- Python 3.8 or later
- Required packages (only built-ins used: `tkinter`, `shutil`, `zipfile`, etc.)

> _No third-party dependencies required._

---

### 🚀 Installation

1. Clone this repository:

```bash
git clone https://github.com/VongaiWitcho/file_backup_logger.git
cd file_backup_logger

2. Run the program:
python main.py

🖱️ Usage Instructions
Launch the app with python main.py.

Select the source folder you want to back up.

Choose a destination folder for the backup.

Enter a version number (e.g., 1.2.3).

Check the ZIP Backup box if you want a compressed backup.

Click "Backup Now".

Your backup will be created with a timestamped folder name like:
backup_2025-08-01_14-22-35_v1.2.3

 A log entry will be saved in:
logs/backup.log

