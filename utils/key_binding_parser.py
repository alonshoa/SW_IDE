import tkinter as tk
import re
import os

from utils.YAMLconfig import YAMLConfig


class ShortcutKeyBinder:
   def __init__(self, file_path):
      self.config = YAMLConfig(file_path, required_configs=['shortcuts'])
      self.config.load()

   def get_shortcut_command(self, shortcut):
      return self.config.get('shortcuts')[shortcut]

   def get_shortcuts(self):
      return self.config.get('shortcuts').keys()

   def add_shortcut(self, shortcut, command):
      shortcuts = self.config.get('shortcuts')
      shortcuts[shortcut] = command
      self.config.export({'shortcuts': shortcuts})

   def remove_shortcut(self, shortcut):
      shortcuts = self.config.get('shortcuts')
      del shortcuts[shortcut]
      self.config.export({'shortcuts': shortcuts})


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
        if 'bind' in line:
            key_bindings.update(parse_line(line))
    return key_bindings

def parse_line(line):
    """
    This method gets a line and parse it to return a tuple of the key and the command
    :param line:
    :return:
    """
    key = re.search(r'<(.*)>', line).group(1)
    command = re.search(r'\((.*)\)', line).group(1)
    return {key: command}

    return key_bindings
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
