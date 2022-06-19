import tkinter as tk

class Feedback(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Feedback")
        self.geometry("300x200")
        self.create_widgets()

    def create_widgets(self):
        self.very_bad = tk.Button(self, text="Very Bad", command=self.very_bad)
        self.very_bad.pack(side="top")
        self.bad = tk.Button(self, text="Bad", command=self.bad)
        self.bad.pack(side="top")
        self.ok = tk.Button(self, text="Ok", command=self.ok)
        self.ok.pack(side="top")
        self.good = tk.Button(self, text="Good", command=self.good)
        self.good.pack(side="top")
        self.excellent = tk.Button(self, text="Excellent", command=self.excellent)
        self.excellent.pack(side="top")

    def very_bad(self):
        print("very bad")

    def bad(self):
        print("bad")

    def ok(self):
        print("ok")

    def good(self):
        print("good")

    def excellent(self):
        print("excellent")


if __name__ == "__main__":
    app = Feedback()
    app.mainloop()
