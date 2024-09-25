import argparse
import sys

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(dest='action')


add_parser = subparsers.add_parser('add')
add_parser.add_argument('task')

delete_parser = subparsers.add_parser('delete')
delete_parser.add_argument('id', type=int)

update_parser = subparsers.add_parser('update')
update_parser.add_argument('id', type=int)
update_parser.add_argument('task')

mark_in_progress = subparsers.add_parser('mark-in-progress')
mark_in_progress.add_argument('id', type=int)

mark_done = subparsers.add_parser('mark-done')
mark_done.add_argument('id', type=int)

list_parser = subparsers.add_parser('list')
list_parser.add_argument('stage', nargs='?',default=None, choices=['done', 'todo', 'in-progress'])

args = parser.parse_args()

# Example of handling actions based on input
if args.action == 'add':
    print(f"Task added successfully: {args.task}")
elif args.action == 'delete':
    print(f"Task {args.id} deleted successfully.")
elif args.action == 'update':
    print(f"Task {args.id} updated to: {args.task}")
elif args.action == 'mark-in-progress':
    print(f"Task {args.id} marked as in-progress.")
elif args.action == 'mark-done':
    print(f"Task {args.id} marked as done.")
elif args.action == 'list':
    if args.stage:
        print(f"Listing tasks with stage: {args.stage}")
    else:
        print("Listing all tasks")