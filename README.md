# To Do List CLI:

## Tools Used:
- Python3
- pip3
- SQLite3
- argsparse
- datetime
- tabulate

## Installation of requirements:
```
# Navigate to project directory
pip3 install -r requirements.txt
```
## How to use:

```
# Adding a new task
python3 tasktracker add <task>

# Updating and deleting tasks
python3 tasktracker.py update <id> <updated_task>
python3 tasktracker.py delete <id>

# Marking a task as in progress or done
python3 tasktracker.py mark-in-progress <id>
python3 tasktracker.py mark-done <id>

# Listing all tasks
python3 tasktracker.py list

# Listing tasks by status
python3 tasktracker.py list done
python3 tasktracker.py list todo
python3 tasktracker.py list in-progress
```
