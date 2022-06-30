import tkinter as tk
# from utils import YAMLConfig
from devince_codex_1.SW_IDE.utils.YAMLconfig import YAMLConfig


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


class ShortcutsConfigWindow(tk.Frame):
   def __init__(self, master, shortcut_key_binder):
      super(ShortcutsConfigWindow, self).__init__()
      self.master = master
      self.shortcut_key_binder = shortcut_key_binder
      self.shortcuts = list(self.shortcut_key_binder.get_shortcuts())
      self.shortcut_entries = {}
      self.command_entries = {}
      self.init_window()

   def init_window(self):
      self.master.title("Shortcut Keys")
      self.pack(fill=tk.BOTH, expand=1)

      for i,shortcut in enumerate(self.shortcuts):
         shortcut_label = tk.Label(self, text=shortcut)
         shortcut_label.grid(row=i, column=0)

         shortcut_entry = tk.Entry(self, width=10)
         shortcut_entry.insert(0, shortcut)
         shortcut_entry.grid(row=i, column=1)
         self.shortcut_entries[shortcut] = shortcut_entry

         command_entry = tk.Entry(self, width=50)
         command_entry.insert(0, self.shortcut_key_binder.get_shortcut_command(shortcut))
         command_entry.grid(row=i, column=2)
         self.command_entries[shortcut] = command_entry

      save_button = tk.Button(self, text="Save", command=self.save_shortcuts)
      save_button.grid(row=len(self.shortcuts), column=0)

      add_button = tk.Button(self, text="Add", command=self.add_shortcut)
      add_button.grid(row=len(self.shortcuts), column=1)

      remove_button = tk.Button(self, text="Remove", command=self.remove_shortcut)
      remove_button.grid(row=len(self.shortcuts), column=2)

   def save_shortcuts(self):
      for shortcut in self.shortcuts:
         self.shortcut_key_binder.add_shortcut(self.shortcut_entries[shortcut].get(), self.command_entries[shortcut].get())

   def add_shortcut(self):
      self.shortcut_key_binder.add_shortcut("shortcut", "command")
      self.shortcuts = list(self.shortcut_key_binder.get_shortcuts())
      self.init_window()

   def remove_shortcut(self):
      self.shortcut_key_binder.remove_shortcut(self.shortcuts[-1])
      self.shortcuts.pop()
      self.init_window()

if __name__ == '__main__':
   root = tk.Tk()
   root.geometry("500x500")
   shortcut_key_binder = ShortcutKeyBinder('shortcuts.yaml')
   app = ShortcutsConfigWindow(root, shortcut_key_binder)
   root.mainloop()
