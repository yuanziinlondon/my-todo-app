FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """Read a text file and return a list of to-do items."""
    with open(filepath, "r") as f:
        todos = f.readlines()
    return todos


def write_todos(todos, filepath=FILEPATH):
    """write the to-do list items into the text file."""
    with open(filepath, "w") as f:
        f.writelines(todos)
