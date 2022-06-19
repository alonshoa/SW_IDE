import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from devince_codex_1.SW_IDE.new_GUI.text_areas import ThreeTextAreas


class EditorNotebook(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.modified = []
        self.tab_name_child = {}
        self.notebook = ttk.Notebook(self)
        self.file_names = []
        self.notebook.pack(fill=tk.BOTH, expand=True)

    def add_file(self, file_name= None,content=None) :
        if file_name is None:
            file_name = filedialog.askopenfilename()
        if file_name in self.file_names:
            return
        self.file_names.append(file_name)
        frame = ThreeTextAreas(self.notebook, file_name)
        self.tab_name_child[file_name.split('/')[-1]] = frame
        self.modified.append(False)
        if content is not None:
            frame.set_code(content)
        frame.registerCodeModifiedEvent(lambda event: self.set_modified(frame))
        self.notebook.add(frame, text=file_name.split('/')[-1])
        self.notebook.select(frame)
        return frame

    def close(self, frame):
        if messagebox.askyesno("Save", "Do you want to save?"):
            self.save(frame)
        del self.tab_name_child[self.file_names[self.notebook.index(frame)].split('/')[-1]]
        self.modified[self.notebook.index(frame)] = False
        self.notebook.tab(frame, text=self.file_names[self.notebook.index(frame)].split('/')[-1])
        self.notebook.forget(frame)

    def set_modified(self, frame):
        self.modified[self.notebook.index(frame)] = True
        self.notebook.tab(frame, text=self.file_names[self.notebook.index(frame)].split('/')[-1] + '*')

    def save(self, frame):
        file_name = self.notebook.tab(frame, "text").replace('*','')
        if file_name == 'New File':
            file_name = filedialog.asksaveasfilename()
        with open(file_name, 'w') as f:
            f.write(self.get_output_code())


    def get_instructions(self):
        return self.tab_name_child[self.notebook.tab(self.notebook.select(), "text").replace('*','')].get_instructions()

    def get_code(self):
        return self.tab_name_child[self.notebook.tab(self.notebook.select(), "text").replace('*','')].get_code()

    def get_output_code(self):
        return self.tab_name_child[self.notebook.tab(self.notebook.select(), "text").replace('*','')].get_output_code()

    def set_output_code(self,output_code):
        self.tab_name_child[self.notebook.tab(self.notebook.select(), "text").replace('*', '')].set_output_code(output_code)
