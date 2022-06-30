import os
import sys
import subprocess

class Shortcut:
    def __init__(self, name, command, shortcut):
        self.name = name
        self.command = command
        self.shortcut = shortcut

    def create(self):
        if os.name == 'nt':
            self.create_windows()
        elif os.name == 'posix':
            self.create_linux()
        else:
            print('Unsupported OS')

    def create_windows(self):
        import win32com.client
        shell = win32com.client.Dispatch("WScript.Shell")
        shortcut = shell.CreateShortCut(os.path.join(os.environ['USERPROFILE'], 'Desktop', self.name + '.lnk'))
        shortcut.Targetpath = sys.executable
        shortcut.Arguments = self.command
        shortcut.Hotkey = self.shortcut
        shortcut.IconLocation = sys.executable
        shortcut.save()

    def create_linux(self):
        subprocess.call(['gnome-terminal', '-e', self.command])


if __name__ == '__main__':
    shortcut = Shortcut('test', 'python test.py', 'Ctrl+Alt+T')
    shortcut.create()
