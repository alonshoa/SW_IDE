import tkinter as tk
from functools import wraps


# @undo
class MyText(tk.Text):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.bind('<Control-u>', self.undo_event)
        self.bind('<Control-U>', self.undo_event)
        self.bind('<Control-a>', self.select_all)
        self.bind('<Control-A>', self.select_all)

    def undo_event(self, event=None):
        try:
            return self._undo_event(event)
        except AttributeError:
            pass
        self._undo_event = self._undo_event(self)
        return self._undo_event(event)

    def _undo_event(self, event=None):
        func_name, args, kwargs = self.undo_stack.pop()
        if func_name == 'insert':
            self.delete(*args)
        elif func_name == 'delete':
            self.insert(*args, **kwargs)
        else:
            raise ValueError('Unknown function name: {}'.format(func_name))

    def undo(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            self.undo_stack.append((func.__name__, args, kwargs))
            return func(self, *args, **kwargs)

        return wrapper
    @property
    def undo_stack(self):
        try:
            return self._undo_stack
        except AttributeError:
            self._undo_stack = []
            return self._undo_stack

    @undo
    def insert(self, index, chars, tags=None):
        super().insert(index, chars, tags)

    def select_all(self, event=None):
        self.tag_add('sel', '1.0', 'end')
        return 'break'

    @undo
    def delete(self, index1, index2=None):
        super().delete(index1, index2)


if __name__ == '__main__':
    root = tk.Tk()
    text = MyText(root)
    text.pack()
    root.mainloop()
