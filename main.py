import tkinter as tk
import os
import openai

from devince_codex_1.utils.app import Application

openai.api_key = os.getenv("OPENAI_KEY")

root = tk.Tk()
app = Application(master=root)
app.mainloop()
