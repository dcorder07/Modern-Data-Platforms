"""A simple command-line to-do list app that lets users add, view, and remove tasks."""
from src.todo import todo_list

def test_todo():
    #arrange
    input_list = ["1", "Buy Milk", "2", "3", "1", "4"]
    expected_output = """1. Add Task
    2. View Tasks
    3. Mark Task as Done
    4. Exit
    ==================================================
    Enter your choice: 1
    Enter task: Buy Milk
    --------------------------------------------------
    1. Add Task
    2. View Tasks
    3. Mark Task as Done
    4. Exit
    ==================================================
    Enter your choice: 2
    Tasks:
    1. Buy Milk
    --------------------------------------------------
    1. Add Task
    2. View Tasks
    3. Mark Task as Done
    4. Exit
    ==================================================
    Enter your choice: 3
    Enter task number to mark as done: 1
    Task marked as done.
    1. Add Task
    2. View Tasks
    3. Mark Task as Done
    4. Exit
    ==================================================
    Enter your choice: 4
    Exiting.
    --------------------------------------------------"""
    #act
    actual_output = todo_list(input_list)
    #assert
    assert actual_output == expected_output
