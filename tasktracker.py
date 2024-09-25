#!/usr/local/bin/python3.12

import argparse
import datetime
import sqlite3
from tabulate import tabulate

def connect_db(db_name="tracker.db"):
    """Connect to the SQLite database."""
    return sqlite3.connect(db_name)

def execute_query(query, params=()):
    """Execute a query and return the results."""
    with con:
        cur.execute(query, params)
        return cur.fetchall()

def print_tasks(rows):
    """Print the tasks in a formatted table."""
    print(tabulate(rows, headers=['ID', 'Description', 'Status', 'Time Created', 'Time Updated'], tablefmt='grid'))

def add_task(description):
    current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    execute_query(
        "INSERT INTO tasks (description, status, time_created, time_updated) VALUES (?, ?, ?, ?)",
        (description, 'todo', current_time, current_time)
    )
    print_tasks(execute_query("SELECT * FROM tasks"))

def remove_task(task_id):
    execute_query("DELETE FROM tasks WHERE id = ?", (task_id,))
    print_tasks(execute_query("SELECT * FROM tasks"))

def update_task(task_id, description):
    time_updated = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    execute_query(
        "UPDATE tasks SET description = ?, time_updated = ? WHERE id = ?",
        (description, time_updated, task_id)
    )
    print_tasks(execute_query("SELECT * FROM tasks"))

def mark_task_status(task_id, status):
    time_updated = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    execute_query(
        "UPDATE tasks SET status = ?, time_updated = ? WHERE id = ?",
        (status, time_updated, task_id)
    )
    print_tasks(execute_query("SELECT * FROM tasks"))

def list_tasks(status=None):
    if status:
        rows = execute_query("SELECT * FROM tasks WHERE status = ?", (status,))
    else:
        rows = execute_query("SELECT * FROM tasks")
    print_tasks(rows)

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(dest='action')

add_parser = subparsers.add_parser('add')
add_parser.add_argument('description')

delete_parser = subparsers.add_parser('delete')
delete_parser.add_argument('id', type=int)

update_parser = subparsers.add_parser('update')
update_parser.add_argument('id', type=int)
update_parser.add_argument('description')

mark_in_progress_parser = subparsers.add_parser('mark-in-progress')
mark_in_progress_parser.add_argument('id', type=int)

mark_done_parser = subparsers.add_parser('mark-done')
mark_done_parser.add_argument('id', type=int)

list_parser = subparsers.add_parser('list')
list_parser.add_argument('status', nargs='?', default=None, choices=['done', 'todo', 'in-progress'])

args = parser.parse_args()

con = connect_db()
cur = con.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS tasks(
    id INTEGER PRIMARY KEY AUTOINCREMENT,    
    description TEXT NOT NULL,
    status TEXT,
    time_created TIME,
    time_updated TIME)
''')

action_map = {
    "add": lambda: add_task(args.description),
    "delete": lambda: remove_task(args.id),
    "update": lambda: update_task(args.id, args.description),
    "mark-in-progress": lambda: mark_task_status(args.id, 'in-progress'),
    "mark-done": lambda: mark_task_status(args.id, 'done'),
    "list": lambda: list_tasks(args.status)
}

action = action_map.get(args.action)
if action:
    action()

con.close()
