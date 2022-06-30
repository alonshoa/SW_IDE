import tkinter as tk
import os
import openai

from src.old_GUI.app_using_buton_panel import Application
# from src.new_GUI.tk_notebook_app_button_panel import NotebookApplication as Application
# from devince_codex_1.SW_IDE.new_GUI.darkmode import DarkMode
openai.api_key = os.getenv("OPENAI_KEY")

def main():
    root = tk.Tk()
    app = Application(root)
    # ts = ThemedStyle(app,theme='equilux')
    # DarkMode(app)
    app.pack(fill=tk.BOTH, expand=True)
    app.mainloop()

if __name__ == "__main__":
    main()
