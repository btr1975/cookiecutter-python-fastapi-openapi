"""
post generation hooks for cookiecutter to remove unneeded files
"""
from typing import List
import os
import shutil

REMOVE_PATHS_NO_WEBPAGES = [
    '{% if cookiecutter.include_webpages != "y" %}{{cookiecutter.__app_name}}/routers/hello_world.py{% endif %}',
    '{% if cookiecutter.include_webpages != "y" %}{{cookiecutter.__app_name}}/static{% endif %}',
    '{% if cookiecutter.include_webpages != "y" %}{{cookiecutter.__app_name}}/templates{% endif %}',
]


def remove_paths(paths_to_remove: List[str]) -> None:
    """Remove files and directories

    :rtype: None
    :returns: Nothing it removes files and directories
    """
    for remove_path in paths_to_remove:
        path = remove_path.strip()
        if path and os.path.exists(path):
            if os.path.isfile(path):
                os.remove(path)

            elif os.path.isdir(path):
                shutil.rmtree(path)


if __name__ == '__main__':
    remove_paths(REMOVE_PATHS_NO_WEBPAGES)
