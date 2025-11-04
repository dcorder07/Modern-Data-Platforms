"""Unit test for todo_list using class-based, command-driven mode (no input/print)."""
from src.todo import todo_list

def test_todo():
    # arrange
    commands = ["1", "Buy Milk", "2", "3", "1", "4"]
    expected_output = (
        "1. Add Task\n"
        "2. View Tasks\n"
        "3. Mark Task as Done\n"
        "4. Exit\n"
        "==================================================\n"
        "Enter your choice: 1\n"
        "Enter task: Buy Milk\n"
        "--------------------------------------------------\n"
        "1. Add Task\n"
        "2. View Tasks\n"
        "3. Mark Task as Done\n"
        "4. Exit\n"
        "==================================================\n"
        "Enter your choice: 2\n"
        "Tasks:\n"
        "1. Buy Milk\n"
        "--------------------------------------------------\n"
        "1. Add Task\n"
        "2. View Tasks\n"
        "3. Mark Task as Done\n"
        "4. Exit\n"
        "==================================================\n"
        "Enter your choice: 3\n"
        "Enter task number to mark as done: 1\n"
        "Task marked as done.\n"
        "1. Add Task\n"
        "2. View Tasks\n"
        "3. Mark Task as Done\n"
        "4. Exit\n"
        "==================================================\n"
        "Enter your choice: 4\n"
        "Exiting.\n"
        "--------------------------------------------------\n"
    )

    # act
    actual_output = todo_list(listo=[], commands=commands)

    # assert
    assert actual_output == expected_output
