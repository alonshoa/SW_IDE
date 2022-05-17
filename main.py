import tkinter as tk
import os
import openai

from utils.app_using_buton_panel import Application

openai.api_key = os.getenv("OPENAI_KEY")

def main():
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()

if __name__ == "__main__":
    main()
