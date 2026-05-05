# ⚙️ Advanced Automation Projects

This folder contains Python automation scripts built to solve real-world problems using file handling and system operations.

---

## 📁 File Organizer Tool

A Python script that automatically organizes files into folders based on their type.

---

## 🔹 Version 1 (v1)

Basic implementation of file organizer.

### ✨ Features:

* Creates folders: Movies, Documents, Images
* Moves files based on file type
* Skips unsupported files
* Prevents overwriting existing files

### ⚠️ Limitations:

* No "Others" folder
* Skips unknown file types
* Less structured output

---

## 🔹 Version 2 (v2)

Improved and more robust version of the file organizer.

### 🚀 Improvements over v1:

* Added **"Others" folder** for unsupported files
* Better file categorization
* Cleaner and more readable code
* Improved user feedback with clear messages
* Handles more edge cases

---

## ▶️ How to Use

1. Run the script:

   ```bash
   python file_organizer_tool_v2.py
   ```
2. Enter the full folder path
3. Files will be automatically organized

---

## 🧠 Learning Outcomes

* Working with `os` module (file & directory handling)
* Using `shutil` for file operations
* Building real-world automation scripts
* Improving code from v1 → v2 (iteration & optimization)

---

## 📌 Future Improvements

* Add support for more file types
* CLI-based arguments (no manual input)
* GUI version using Tkinter
* Duplicate file renaming system

---
## 🖥️ System Monitoring Tools

### 🌐 Network Health Checker

Checks whether websites are online or offline using system ping commands.

#### ✨ Features:

* Uses subprocess to run ping command
* Checks multiple websites
* Displays online/offline status

---

### 📊 Active App Monitor

Monitors whether a specific application is running on the system.

#### ✨ Features:

* Uses system process list (`tasklist`)
* Detects if a target app (e.g., Notepad) is active
* Simple real-time monitoring logic

---


