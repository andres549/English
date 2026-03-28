# Persistence Log

## Overview
This project implements a simple Python script to record and manage daily blockers for a team.  
It demonstrates file handling (`r`, `w`, `a` modes), the use of the `with` statement for automatic file closing, and basic terminal navigation.  
At the end of the file, English reflections are included to practice professional communication protocols.

## Features
- Add a new blocker and save it persistently in `database.txt`.
- Fetch and display all blockers in a clear, numbered list.
- Show a warning before overwriting existing data.
- Interactive menu that repeats until the user chooses to exit.

## File Structure
- `persistence_log.py` → Main Python script with logic and reflections.
- `database.txt` → Text file where blockers are stored (created automatically if not present).

## Requirements
To run this project you need:

- **Python 3.8 or higher** installed on your system.
- Access to the **Terminal or command line** to execute the script.
- A text editor or IDE (for example, VS Code, PyCharm, or even Notepad).
- Internet connection only if you plan to clone the repository from GitHub.
- Write permissions in the directory where the program is executed (to create and modify `database.txt`).

## How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/persistence-log.git
   cd persistence-log
   
2. Run the script:
python persistence_log.py

# Example Usage

Team Daily Status Menu
1. Add Blocker
2. Fetch Blockers
3. Overwrite Warning
4. Exit

by: @andres549

