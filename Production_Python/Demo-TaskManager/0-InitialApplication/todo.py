"""A simple command-line to-do list app that lets users add, view, and remove tasks."""
from log_todo import logger

def todo(listo: list = None) -> None:

    if listo is None:
        listo = []

    while True:
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Done")
        print("4. Exit")
        print("=" * 50)
        x = input("Enter your choice: ")
        if x == "1":
            tsk = input("Enter task: ")
            listo.append(tsk)
            logger.info(f'Task added: {tsk}')
            print("-" * 50)
        elif x == "2":
            print("Tasks:")
            for i, t in enumerate(listo):
                print(f"{i+1}. {t}")
                logger.info(f'Tasks viewed')
            print("-" * 50)
        elif x == "3":
            usr_input = input("Enter task number to mark as done: ")
            if 0 <= int(usr_input) - 1 < len(listo):
                listo.pop(int(usr_input) - 1)
                logger.info(f'Task number {usr_input} marked as done')
                print("Task marked as done.")
            else:
                print("Invalid task number.")
                logger.warning(f'{usr_input} is an invalid task number so cant be marked as done')
        elif x == "4":
            print("Exiting.")
            logger.info('Exiting the application')
            print("-" * 50)
            break
        else:
            print("Invalid choice.")
            logger.error(f'Invalid number entry: {x}')
            print("-" * 50)

todo()
