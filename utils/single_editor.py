import tkinter as tk
from tkinter import ttk


class SingleEditor(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.instruction = tk.Text(self, height=10, width=50, wrap=tk.WORD)
        self.instruction.grid(row=0, column=0, columnspan=2)
        self.pw = ttk.PanedWindow(self, orient=tk.HORIZONTAL)
        self.pw.grid(row=1, column=0, columnspan=2)
        self.input_code = tk.Text(self.pw, height=10, width=50, wrap=tk.WORD, state=tk.DISABLED)
        self.output_code = tk.Text(self.pw, height=10, width=50, wrap=tk.WORD, state=tk.DISABLED)
        self.pw.add(self.output_code)
        self.input_code.bind('<Key>', self.key_pressed)
        self.input_code.bind('<Button-1>', self.mouse_pressed)
        self.input_code.bind('<ButtonRelease-1>', self.mouse_released)
        self.input_code.bind('<B1-Motion>', self.mouse_dragged)
        self.input_code.bind('<Button-3>', self.right_mouse_pressed)
        self.input_code.bind('<ButtonRelease-3>', self.right_mouse_released)
        self.input_code.bind('<B3-Motion>', self.right_mouse_dragged)
        self.input_code.bind('<Control-Key-a>', self.select_all)
        self.input_code.bind('<Control-Key-c>', self.copy)
        self.input_code.bind('<Control-Key-x>', self.cut)
        self.input_code.bind('<Control-Key-v>', self.paste)
        self.input_code.bind('<Control-Key-z>', self.undo)
        self.input_code.bind('<Control-Key-y>', self.redo)
        self.input_code.bind('<Control-Key-s>', self.save)
        self.input_code.bind('<Control-Key-o>', self.open)
        self.input_code.bind('<Control-Key-n>', self.new)
        self.input_code.bind('<Control-Key-q>', self.quit)
        self.input_code.bind('<Control-Key-h>', self.help)
        self.input_code.bind('<Control-Key-r>', self.run)
        self.input_code.bind('<Control-Key-d>', self.debug)
        self.input_code.bind('<Control-Key-p>', self.profile)
        self.input_code.bind('<Control-Key-t>', self.test)
        self.input_code.bind('<Control-Key-e>', self.export)
        self.input_code.bind('<Control-Key-i>', self.import_file)
        self.input_code.bind('<Control-Key-b>', self.build)
        self.input_code.bind('<Control-Key-l>', self.load)
        self.input_code.bind('<Control-Key-u>', self.unload)
        self.input_code.bind('<Control-Key-m>', self.merge)
        self.input_code.bind('<Control-Key-f>', self.find)
        self.input_code.bind('<Control-Key-g>', self.find_next)
        self.input_code.bind('<Control-Key-j>', self.jump)
        self.input_code.bind('<Control-Key-k>', self.jump_back)
        self.input_code.bind('<Control-Key-w>', self.wrap)
        self.input_code.bind('<Control-Key-y>', self.redo)
        self.input_code.bind('<Control-Key-s>', self.save)
        self.input_code.bind('<Control-Key-o>', self.open)
        self.input_code.bind('<Control-Key-n>', self.new)
        self.input_code.bind('<Control-Key-q>', self.quit)
        self.input_code.bind('<Control-Key-h>', self.help)
        self.input_code.bind('<Control-Key-r>', self.run)
        self.input_code.bind('<Control-Key-d>', self.debug)
        self.input_code.bind('<Control-Key-p>', self.profile)
        self.input_code.bind('<Control-Key-t>', self.test)
        self.input_code.bind('<Control-Key-e>', self.export)
        self.input_code.bind('<Control-Key-i>', self.import_file)
        self.input_code.bind('<Control-Key-b>', self.build)
        self.input_code.bind('<Control-Key-l>', self.load)
        self.input_code.bind('<Control-Key-u>', self.unload)
        self.input_code.bind('<Control-Key-m>', self.merge)
        self.input_code.bind('<Control-Key-f>', self.find)
        self.input_code.bind('<Control-Key-g>', self.find_next)
        self.input_code.bind('<Control-Key-j>', self.jump)
        self.input_code.bind('<Control-Key-k>', self.jump_back)
        self.input_code.bind('<Control-Key-w>', self.wrap)

    def key_pressed(self, event):
        print('key pressed')

    def mouse_pressed(self, event):
        print('mouse pressed')

    def mouse_released(self, event):
        print('mouse released')

    def mouse_dragged(self, event):
        print('mouse dragged')

    def right_mouse_pressed(self, event):
        print('right mouse pressed')

    def right_mouse_released(self, event):
        print('right mouse released')

    def right_mouse_dragged(self, event):
        print('right mouse dragged')

    def select_all(self, event):
        print('select all')

    def copy(self, event):
        print('copy')

    def cut(self, event):
        print('cut')

    def paste(self, event):
        print('paste')

    def undo(self, event):
        print('undo')

    def redo(self, event):
        print('redo')

    def save(self, event):
        print('save')

    def open(self, event):
        print('open')

    def new(self, event):
        print('new')

    def quit(self, event):
        print('quit')

    def help(self, event):
        print('help')

    def run(self, event):
        print('run')

    def debug(self, event):
        print('debug')

    def profile(self, event):
        print('profile')

    def test(self, event):
        print('test')

    def export(self, event):
        print('export')

    def import_file(self, event):
        print('import')

    def build(self, event):
        print('build')

    def load(self, event):
        print('load')

    def unload(self, event):
        print('unload')

    def merge(self, event):
        print('merge')

    def find(self, event):
        print('find')

    def find_next(self, event):
        print('find next')

    def jump(self, event):
        print('jump')

    def jump_back(self, event):
        print('jump back')

    def wrap(self, event):
        self.pw.add(self.input_code)
        self.pw.add(self.output_code)


if __name__ == '__main__':
    root = tk.Tk()
    app = SingleEditor(master=root)
    app.mainloop()
