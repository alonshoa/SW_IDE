import sys
import tkinter as tk
import pdb

from text_areas_with_linenumber import LinedText


class DebuggerAdapter(object):
    def __init__(self, textarea):
        self.textarea = textarea

    def set_breakpoint(self, line_number):
        self.textarea.breakpoints.add(line_number)
        self.textarea.draw_breakpoints()

    def clear_breakpoint(self, line_number):
        self.textarea.breakpoints.remove(line_number)
        self.textarea.draw_breakpoints()

    def clear_all_breakpoints(self):
        self.textarea.breakpoints.clear()
        self.textarea.draw_breakpoints()


class BreakableTextarea(tk.Frame):
    def __init__(self, master, **kwargs):
        tk.Frame.__init__(self, master, **kwargs)
        self.text = tk.Text(self, **kwargs)
        # self.breakpoint_area = tk.Canvas(self, width=100, **kwargs)
        # width_ = self.text.cget("width") / 10
        # print(width_)
        self.breakpoint_area = tk.Canvas(self, width=10, **kwargs)
        # self.breakpoint_area.tag_raise()
        self.breakpoint_area.pack(side=tk.LEFT,ipadx=5, fill=tk.BOTH,expand=True)
        self.breakpoint_area.bind("<Button-1>", self.toggle_breakpoint)
        self.text.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        self.breakpoints = set()
        self.text.bind("<F8>", self.step_over)

    def step_over(self, event):
        self.text.event_generate("<<step-over>>")

    def toggle_breakpoint(self, event):
        line_number = self.text.index("@%s,%s linestart" % (event.x, event.y)).split(".")[0]
        if line_number in self.breakpoints:
            self.breakpoints.remove(line_number)
        else:
            self.breakpoints.add(line_number)
        self.draw_breakpoints()

    def draw_breakpoints(self):
        self.breakpoint_area.delete("all")
        for line_number in self.breakpoints:
            y = self.text.bbox(line_number + ".0")[1]
            self.breakpoint_area.create_oval(2, y + 2, 18, y + 18, fill="red")

    def insert(self, *args, **kwargs):
        self.text.insert(*args, **kwargs)
        self.draw_breakpoints()

    def delete(self, *args, **kwargs):
        self.text.delete(*args, **kwargs)
        self.draw_breakpoints()

    def see(self, *args, **kwargs):
        self.text.see(*args, **kwargs)
        self.draw_breakpoints()

    def update(self, *args, **kwargs):
        self.text.update(*args, **kwargs)
        self.draw_breakpoints()

    def get(self, *args, **kwargs):
        return self.text.get(*args, **kwargs)

    def index(self, *args, **kwargs):
        return self.text.index(*args, **kwargs)

    def bbox(self, *args, **kwargs):
        return self.text.bbox(*args, **kwargs)

    def mark_set(self, *args, **kwargs):
        return self.text.mark_set(*args, **kwargs)

    def mark_unset(self, *args, **kwargs):
        return self.text.mark_unset(*args, **kwargs)

    def mark_names(self, *args, **kwargs):
        return self.text.mark_names(*args, **kwargs)

    def tag_add(self, *args, **kwargs):
        return self.text.tag_add(*args, **kwargs)

    def tag_remove(self, *args, **kwargs):
        return self.text.tag_remove(*args, **kwargs)

    def tag_configure(self, *args, **kwargs):
        return self.text.tag_configure(*args, **kwargs)

    def tag_names(self, *args, **kwargs):
        return self.text.tag_names(*args, **kwargs)

    def tag_ranges(self, *args, **kwargs):
        return self.text.tag_ranges(*args, **kwargs)

    def tag_nextrange(self, *args, **kwargs):
        return self.text.tag_nextrange(*args, **kwargs)

    def tag_prevrange(self, *args, **kwargs):
        return self.text.tag_prevrange(*args, **kwargs)

    def tag_bind(self, *args, **kwargs):
        return self.text.tag_bind(*args, **kwargs)

    def tag_unbind(self, *args, **kwargs):
        return self.text.tag_unbind(*args, **kwargs)

    def tag_raise(self, *args, **kwargs):
        return self.text.tag_raise(*args, **kwargs)

    def tag_lower(self, *args, **kwargs):
        return self.text.tag_lower(*args, **kwargs)

    def tag_cget(self, *args, **kwargs):
        return self.text.tag_cget(*args, **kwargs)

    def tag_config(self, *args, **kwargs):
        return self.text.tag_config(*args, **kwargs)

    # def tag_names(self, *args, **kwargs):
    #     return self.text.tag_names(*args, **kwargs)

    def tag_delete(self, *args, **kwargs):
        return self.text.tag_delete(*args, **kwargs)

    def tag_has(self, *args, **kwargs):
        return self.text.tag_has(*args, **kwargs)

class BreakableTextareaWithLinenumbers(tk.Frame):
    def __init__(self, master, **kwargs):
        tk.Frame.__init__(self, master, **kwargs)
        self.text = LinedText(self, **kwargs)
        self.breakpoint_area = tk.Canvas(self, width=10, **kwargs)
        self.breakpoint_area.pack(side=tk.LEFT, ipadx=5, fill=tk.BOTH, expand=True)
        self.breakpoint_area.bind("<Button-1>", self.toggle_breakpoint)
        self.text.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        self.breakpoints = set()
        self.text.text.bind("<F8>", self.step_over)

    def step_over(self, event):
        self.text.text.event_generate("<<step-over>>")

    def toggle_breakpoint(self, event):
        line_number = self.text.text.index("@%s,%s linestart" % (event.x, event.y)).split(".")[0]
        if line_number in self.breakpoints:
            self.breakpoints.remove(line_number)
        else:
            self.breakpoints.add(line_number)
        self.draw_breakpoints()

    def draw_breakpoints(self):
        self.breakpoint_area.delete("all")
        for line_number in self.breakpoints:
            y = self.text.text.bbox(line_number + ".0")[1]
            self.breakpoint_area.create_oval(2, y + 2, 18, y + 18, fill="red")

    def insert(self, *args, **kwargs):
        self.text.insert(*args, **kwargs)
        self.draw_breakpoints()

    def delete(self, *args, **kwargs):
        self.text.delete(*args, **kwargs)
        self.draw_breakpoints()

    def see(self, *args, **kwargs):
        self.text.see(*args, **kwargs)
        self.draw_breakpoints()

    def update(self, *args, **kwargs):
        self.text.update(*args, **kwargs)
        self.draw_breakpoints()

    def get(self, *args, **kwargs):
        return self.text.get(*args, **kwargs)

    def index(self, *args, **kwargs):
        return self.text.index(*args, **kwargs)

    def bbox(self, *args, **kwargs):
        return self.text.bbox(*args, **kwargs)

    def mark_set(self, *args, **kwargs):
        return self.text.mark_set(*args, **kwargs)

    def mark_unset(self, *args, **kwargs):
        return self.text.mark_unset(*args, **kwargs)

    def mark_names(self, *args, **kwargs):
        return self.text.mark_names(*args, **kwargs)

    def tag_add(self, *args, **kwargs):
        return self.text.tag_add(*args, **kwargs)

    def tag_remove(self, *args, **kwargs):
        return self.text.tag_remove(*args, **kwargs)

    def tag_configure(self, *args, **kwargs):
        return self.text.tag_configure(*args, **kwargs)

    def tag_names(self, *args, **kwargs):
        return self.text.tag_names(*args, **kwargs)

    def tag_ranges(self, *args, **kwargs):
        return self.text.tag_ranges(*args, **kwargs)

    def tag_nextrange(self, *args, **kwargs):
        return self.text.tag_nextrange(*args, **kwargs)

    def tag_prevrange(self, *args, **kwargs):
        return self.text.tag_prevrange(*args, **kwargs)

    def tag_bind(self, *args, **kwargs):
        return self.text.tag_bind(*args, **kwargs)

    def tag_unbind(self, *args, **kwargs):
        return self.text.tag_unbind(*args, **kwargs)

    def tag_raise(self, *args, **kwargs):
        return self.text.tag_raise(*args, **kwargs)

    def tag_lower(self, *args, **kwargs):
        return self.text.tag_lower(*args, **kwargs)

    def tag_cget(self, *args, **kwargs):
        return self.text.tag_cget(*args, **kwargs)

    def tag_config(self, *args, **kwargs):
        return self.text.tag_config(*args, **kwargs)

    def tag_delete(self, *args, **kwargs):
        return self.text.tag_delete(*args, **kwargs)

    # def tag_has(self, *args, **kwargs):
    #     return self.text.tag_has(*args, **kwargs)


if __name__ == "__main__":
    v=""""
    print("Hi ! this is a test")
    """
    root = tk.Tk()
    text = BreakableTextareaWithLinenumbers(root)
    text.pack(fill=tk.BOTH, expand=True)
    debugger = DebuggerAdapter(text)
    pdb.Pdb(stdin=v, stdout=None).set_trace(sys._getframe().f_back)
    root.mainloop()
