# loop_project
Description
This project tests a Python program that performs a long-running task and creates a file after the task is completed.

Python Code
import time

print("Starting long task...")

time.sleep(120)

with open("task-completed.txt", "w") as f:
    f.write("Task completed successfully.")

print("Long task completed.")
How It Works
The program starts and prints Starting long task....
It waits for 120 seconds (2 minutes).
It creates a file named task-completed.txt.
It writes Task completed successfully. into the file.
Finally, it prints Long task completed..
Expected Output
Starting long task...
Long task completed.
Generated File
After the program finishes, the following file will be created:

task-completed.txt
The file will contain:

Task completed successfully.
Project Files
project/
├── README.md
├── long task.py
└── task-completed.txt
Purpose
The purpose of this test is to verify that a long-running Python task can complete successfully and create an output file.
