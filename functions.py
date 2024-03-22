FILEPATH = "todos.txt"


def getTodos(filepath=FILEPATH):
    """ opening file 'with context manager' """
    with open(filepath, 'r') as file:
        todos = file.readlines()
    return todos


def writeTodos(todos, filepath=FILEPATH):
    """writing the file"""
    with open(filepath, 'w') as file:
        file.writelines(todos)
