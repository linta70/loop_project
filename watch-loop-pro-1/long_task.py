import time

print("Starting long task...")

time.sleep(120)

with open("task-completed.txt", "w") as f:
    f.write("Task completed successfully.")

    print("long task completed.")