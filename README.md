# 🗂️ Image Organizer using Python

A Python automation project that organizes image files into separate folders based on their file extensions.

The project uses Python's file-handling capabilities to automatically identify and move JPG, JPEG and PNG images.

## 📌 Project Overview

Manually organizing large numbers of images can be time-consuming.

This script automates the process by scanning a specified source directory, identifying supported image formats and moving them into their respective folders.

## ✨ Features

- Scans files recursively using `pathlib`.
- Supports `.jpg`, `.jpeg` and `.png` extensions.
- Handles uppercase and lowercase extensions.
- Automatically creates destination folders.
- Moves files using `shutil`.
- Checks for duplicate filenames before moving.
- Skips files when the destination filename already exists.
- Handles file-operation errors using `try-except`.
- Displays a summary of successful, skipped and failed operations.

## 📁 Folder Organization

After execution, the folder structure looks like this:

```text
MY PICS/
│
├── photo1.jpg
├── photo2.jpeg
├── wallpaper.png
│
├── JPG/
│   └── photo1.jpg
│
├── JPEG/
│   └── photo2.jpeg
│
└── PNG/
    └── wallpaper.png
```

## 🛠️ Technologies Used

- Python 3
- `pathlib`
- `shutil`
- Dictionaries
- Loops and conditional statements
- Exception handling

## 📊 Output Summary

The program displays a summary containing:

- Successfully moved files.
- Skipped files (duplicate filenames).
- Failed file operations.
