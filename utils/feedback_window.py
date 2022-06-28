import tkinter as tk
from .mylogger import MyLogger

class Feedback(tk.Toplevel):
    def __init__(self):
        tk.Toplevel.__init__(self)
        self.title("Feedback")
        self.geometry("300x200")
        self.create_widgets()
        self.logger = MyLogger()

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
        self.logger.info("very bad")

    def bad(self):
        print("bad")
        self.logger.info(" bad")

    def ok(self):
        print("ok")
        self.logger.info("ok")

    def good(self):
        print("good")
        self.logger.info("good")

    def excellent(self):
        print("excellent")
        self.logger.info("excellent")

class Main(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Main")
        self.geometry("300x200")
        self.create_widgets()

    def create_widgets(self):
        self.feedback = tk.Button(self, text="Feedback", command=self.feedback)
        self.feedback.pack(side="top")

    def feedback(self):
        feedback = Feedback()


if __name__ == "__main__":
    app = Main()
    app.mainloop()