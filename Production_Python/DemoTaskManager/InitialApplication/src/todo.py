"""A simple command-line to-do list app that lets users add, view, and remove tasks.

This version keeps your original formatting but adds a 'commands' argument so tests
can run without input()/print(). In tests, call todo_list(listo=[], commands=[...])
and it returns one big output string. If commands is None, you can optionally add
an interactive wrapper later.
"""

MENU = (
    "1. Add Task\n"
    "2. View Tasks\n"
    "3. Mark Task as Done\n"
    "4. Exit\n"
    "==================================================\n"
)

DASH = "--------------------------------------------------\n"


def _list_block(listo) -> str:
    lines = ["Tasks:"]
    for i, t in enumerate(listo, start=1):
        lines.append(f"{i}. {t}")
    lines.append(DASH.rstrip("\n"))
    return "\n".join(lines) + "\n"


def todo_list(listo: list = None, commands: list | None = None):
    """
    Test mode (no I/O): todo_list(listo=[], commands=[...]) -> str
    Builds and returns the full output string that mirrors the interactive version.

    Interactive mode is intentionally omitted here for clean unit testing.
    """
    if listo is None:
        listo = []

    if commands is None:
        raise RuntimeError(
            "todo_list() is running in testable mode only. "
            "Pass commands=[...] for unit tests."
        )

    it = iter(commands)
    out = []

    while True:
        out.append(MENU)

        # Get choice (default to '4' if commands end)
        try:
            x = next(it)
        except StopIteration:
            x = "4"

        out.append(f"Enter your choice: {x}\n")

        if x == "1":
            # Add task: needs next item
            try:
                tsk = next(it)
            except StopIteration:
                tsk = ""
            out.append(f"Enter task: {tsk}\n")
            if tsk:
                listo.append(tsk)
            out.append(DASH)

        elif x == "2":
            out.append(_list_block(listo))

        elif x == "3":
            # Mark done: needs next item (1-based index)
            try:
                n = next(it)
            except StopIteration:
                n = "0"
            out.append(f"Enter task number to mark as done: {n}\n")
            try:
                idx = int(n) - 1
            except ValueError:
                idx = -1
            if 0 <= idx < len(listo):
                listo.pop(idx)
                out.append("Task marked as done.\n")
            else:
                out.append("Invalid task number.\n")

        elif x == "4":
            out.append("Exiting.\n")
            out.append(DASH)
            break

        else:
            out.append("Invalid choice.\n")
            out.append(DASH)

    return "".join(out)
