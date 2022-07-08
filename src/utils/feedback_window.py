import tkinter as tk
from .mylogger import MyLogger

class FeedbackWindow(tk.Toplevel):
    def __init__(self):
        tk.Toplevel.__init__(self)
        self.title("FeedbackWindow")
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
        self.destroy()

    def bad(self):
        print("bad")
        self.destroy()
        self.logger.info(" bad")
        self.destroy()

    def ok(self):
        print("ok")
        self.logger.info("ok")
        self.destroy()

    def good(self):
        print("good")
        self.logger.info("good")
        self.destroy()

    def excellent(self):
        print("excellent")
        self.logger.info("excellent")
        self.destroy()

class Main(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Main")
        self.geometry("300x200")
        self.create_widgets()

    def create_widgets(self):
        self.feedback = tk.Button(self, text="FeedbackWindow", command=self.feedback)
        self.feedback.pack(side="top")

    def feedback(self):
        feedback = FeedbackWindow()


if __name__ == "__main__":
    app = Main()
    app.mainloop()

