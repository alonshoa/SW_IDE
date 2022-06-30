import tkinter as tk
import yaml
import sys

from src.utils.YAMLconfig import YAMLConfig


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



class AppShortcuts:
   def __init__(self, app, file_path):
      self.app = app
      self.shortcut_key_binder = ShortcutKeyBinder(file_path)

   def bind_shortcuts(self):
      for shortcut in self.shortcut_key_binder.get_shortcuts():
         self.app.bind(shortcut, self.shortcut_key_binder.get_shortcut_command(shortcut))

   def unbind_shortcuts(self):
      for shortcut in self.shortcut_key_binder.get_shortcuts():
         self.app.unbind(shortcut)

   def add_shortcut(self, shortcut, command):
      self.shortcut_key_binder.add_shortcut(shortcut, command)
      self.app.bind(shortcut, command)

   def remove_shortcut(self, shortcut):
      self.shortcut_key_binder.remove_shortcut(shortcut)
      self.app.unbind(shortcut)
