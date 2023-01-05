"""Utility script for auto populating __init__.py for proper package management."""

import sys
import os
import re

def populate_init(path: str):
    """Help to auto populate the init to manage packages properly."""
    init_path = os.path.join(path, "__init__.py")
    file_names = os.listdir(path)
    py_check = re.compile(r'.*\.py')
    filter_check = re.compile('__init__.py|__pycache__|venv|.vscode|.git|.pytest_cache|logs|flaskr')
    all = []

    # Remove the old init if it exists
    if os.path.exists(init_path):
        os.remove(init_path)

    # Find out what to list for the package
    for name in file_names:
        # Pass if its not filtered
        if filter_check.search(name):
            continue

        file_path = os.path.join(path, name)

        # If a submodule, populate subpackage recursively
        if os.path.isdir(file_path):
            if os.listdir(file_path):
                populate_init(file_path)
                all.append(name)
        # Otherwise add to all
        elif py_check.search(name):
            all.append(re.sub('.py', '', name))

    with open(init_path, 'w') as init_file:
        # Write the docstring
        init_file.write(f'"""Auto-generate init for package {os.path.basename(path)}."""\n')

        # Write the all section
        init_file.write('__all__ = [ ')
        for module in all:
            init_file.write(f"'{module}', ")
        init_file.write(']')

if __name__ == '__main__':
    # E.G.
    populate_init(sys.argv[1])

