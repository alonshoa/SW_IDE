import tkinter as tk
import re
import os

from devince_codex_1.SW_IDE.utils.shortcuts_window import ShortcutKeyBinder


def read_shortcut_keys(app_filename):
    """
    This method gets a tk.Frame class file and parse put all the key bindings.
    It returns a list of tuples of the key and the command
    :param app_filename:
    :return:
    """
    with open(app_filename, 'r') as f:
        lines = f.readlines()

    key_bindings = {}
    for line in lines:
        if '.bind' in line:
            print(line)
            key_bindings.update(parse_line(line))
    return key_bindings


def parse_line(line):
    """
    This method gets a line and parse it to return a tuple of the key and the command
    :param line:
    :return:
    """
    key_match = re.search(r'<(.*)>', line)
    command_match = re.search(r'\(.*,(.*)\)', line)
    if key_match and command_match:
        key = key_match.group(1)
        command = command_match.group(1)
        return {key: command}
    else:
        return {}


def read_shortcut_keys_from_folder(folder_path):
    """
    This method gets a folder path and iterate over all the files in the folder and subfolders
    and parse the shortcut keys and add them to a ShortcutKeyBinder
    :param folder_path:
    :return:
    """
    shortcut_key_binder = ShortcutKeyBinder(os.path.join(folder_path, 'shortcuts.yaml'))
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                shortcut_keys = read_shortcut_keys(file_path)
                for shortcut, command in shortcut_keys.items():
                    shortcut_key_binder.add_shortcut(shortcut, command)


if __name__ == '__main__':
    read_shortcut_keys_from_folder(os.getcwd())
