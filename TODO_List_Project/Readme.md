# To-Do List Manager (OOP) — README

## Overview

This project is a simple **Console-Based To-Do List Manager** written in Python using **Object-Oriented Programming (OOP)**. It stores tasks in a JSON file (`tasks.json`)

---

## Features

* Add tasks (title + description)
* View tasks with completed/incomplete status
* Delete tasks by number
* Mark tasks as complete
* Persistent storage using `tasks.json`
* Clean OOP structure using `Task` and `TaskManager` classes

---

## Requirements

* Python 3.8 or higher
* No external libraries required (uses built-in `json` and `os`)

---

## Project Structure

```
ToDoManager/
├─ main.py          # Main program (OOP version)
├─ tasks.json       # JSON file to store tasks (initial content: [])
└─ README.md        # This file
```

---

## Setup Instructions

### Step 1: Create Project Folder

Create a folder named `ToDoManager`.

### Step 2: Add Files

Inside that folder:

* Save the provided `main.py` file.
* Create a `tasks.json` file with the following initial content:

  ```json
  []
  ```

### Step 3: Run the Project

Open a terminal (or PowerShell on Windows), navigate to your project folder and run:

```bash
python main.py
```

Follow the on-screen menu to add, view, delete, or mark tasks complete.

---

## Example Usage

* Choose `2` → Add a new task (enter title and description).
* Choose `1` → View all tasks with their status.
* Choose `4` → Mark a task as complete by entering its number.
* Choose `3` → Delete a task by entering its number.
* Choose `5` → Exit the program.

---

## Common Issue & Fix

**Error:** `json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)`

**Cause:** `tasks.json` is empty or has invalid JSON.

**Fix:** Open `tasks.json` and ensure it contains:

```json
[]
```

Alternatively, the `load_tasks()` function in the provided code automatically handles this by returning an empty list if the file is invalid.

---

## Explanation: `if __name__ == "__main__":`

This line ensures that `main()` runs **only when you execute this file directly** (for example, using `python main.py`).
If you import this file into another Python script, the menu won’t run automatically.

---

## Next Improvements (Future Enhancements)

* Add **due date** and **priority** fields.
* Add **search** by title/keyword.
* Add **sorting** (e.g., incomplete first, then completed).
* Use **SQLite** for larger datasets.
* Build a **GUI** using `tkinter` or a web app using Flask.

---

## License

You can add any license you prefer (MIT is common for small projects). Example: `MIT License`.

---

## Summary

This project demonstrates practical use of **Python OOP**, **file handling**, and **JSON** while building a real-world mini application. It’s an excellent beginner-friendly project for interviews and portfolios.
