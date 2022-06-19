import tkinter as tk
from tkinter import ttk

# from devince_codex_1.SW_IDE.utils.button_functionality import highlight_code
from devince_codex_1.SW_IDE.utils.button_functionality_generelized import highlight_code


class ThreeTextAreas(tk.Frame):
    def __init__(self, parent, filename):
        tk.Frame.__init__(self, parent)
        self.filename = filename
        self.parent = parent
        self.onCodeModifiedEvents = []
        self.initUI()

    def registerCodeModifiedEvent(self, onCodeModifiedEvent):
        self.onCodeModifiedEvents.append(onCodeModifiedEvent)

    def initUI(self):
        self.pack(fill=tk.BOTH, expand=1)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)

        self.lblA = tk.Label(self, text="Instructions")
        self.lblB = tk.Label(self, text="Code")
        self.lblC = tk.Label(self, text="Output Code")

        self.areaA = tk.Text(self)
        self.areaB = tk.Text(self)
        self.areaC = tk.Text(self)

        highlight_code(self.areaB, self.areaC)
        self.areaB.bind("<<Modified>>", self.onCodeModified)

        self.lblA.grid(sticky=tk.W, pady=4, padx=5, row=0, column=0)
        self.lblB.grid(sticky=tk.W, pady=4, padx=5, row=0, column=1)
        self.lblC.grid(sticky=tk.W, pady=4, padx=5, row=0, column=2)

        self.areaA.grid(row=1, column=0, columnspan=1, rowspan=4, padx=5, sticky=tk.E + tk.W + tk.S + tk.N)
        self.areaB.grid(row=1, column=1, columnspan=1, rowspan=4, padx=5, sticky=tk.E + tk.W + tk.S + tk.N)
        self.areaC.grid(row=1, column=2, columnspan=1, rowspan=4, padx=5, sticky=tk.E + tk.W + tk.S + tk.N)

    def onCodeModified(self, event):
        for callback in self.onCodeModifiedEvents:
            callback(event)

    def set_code(self, content):
        self.areaB.insert(1.0, content)

    def get_code(self):
        return self.areaB.get(1.0, tk.END)

    def get_instructions(self):
        return self.areaA.get(1.0, tk.END)
    # def highlight_code(self):
    #     highlight_code()

    def set_output_code(self,content):
        self.areaC.insert(1.0, content)

    def get_output_code(self):
        return self.areaC.get(1.0, tk.END)

def main():
    root = tk.Tk()

    def onCodeModifiedEvent(event):
        print("modified")

    ex = ThreeTextAreas(root, "test", onCodeModifiedEvent)
    root.geometry("600x250+300+300")
    root.mainloop()


if __name__ == '__main__':
    main()