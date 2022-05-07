import tkinter as tk
import os
import openai
import tkinter.filedialog
import subprocess
import tkinter.ttk as ttk
import pygments
import pygments.lexers
import pygments.formatters

openai.api_key = os.getenv("OPENAI_KEY")

def get_response(instruction, code):
    response = openai.Edit.create(
        engine="code-davinci-edit-001",
        input=code,
        instruction=instruction,
        temperature=0,
        top_p=1
    )
    return response

def send_to_openai(app):
    instructions = app.instructions_text.get("1.0", "end-1c")
    code = app.code_text.get("1.0", "end-1c")
    response = get_response(instructions, code)
    app.output_code_textbox.config(state="normal")
    app.output_code_textbox.delete("1.0", "end")
    app.output_code_textbox.insert("1.0", response["choices"][0]["text"])
    app.output_code_textbox.config(state="disabled")

def save_result(app):
    file = tk.filedialog.asksaveasfile(mode="w", defaultextension=".txt")
    if file is None:
        return
    text = app.output_code_textbox.get("1.0", "end-1c")
    file.write(text)
    file.close()

def compare_code(app):
    input_code = app.code_text.get("1.0", "end-1c")
    output_code = app.output_code_textbox.get("1.0", "end-1c")
    input_code_lines = input_code.split("\n")
    output_code_lines = output_code.split("\n")
    if len(input_code_lines) != len(output_code_lines):
        print("The input and output code are not aligned")
        return
    app.output_code_textbox.tag_config("diff", background="red")
    for i in range(len(input_code_lines)):
        if input_code_lines[i] != output_code_lines[i]:
            app.output_code_textbox.tag_add("diff", str(i+1) + ".0", str(i+1) + ".end")

def run_output(app):
    file = tk.filedialog.asksaveasfile(mode="w", defaultextension=".py")
    if file is None:
        return
    text = app.output_code_textbox.get("1.0", "end-1c")
    file.write(text)
    file.close()
    subprocess.call(["python", file.name])

def load_script(app):
    file = tk.filedialog.askopenfile(mode="r")
    if file is None:
        return
    text = file.read()
    app.code_text.delete("1.0", "end")
    app.code_text.insert("1.0", text)

def highlight_code(app):
    code = app.code_text.get("1.0", "end-1c")
    lexer = pygments.lexers.guess_lexer(code)
    formatter = pygments.formatters.HtmlFormatter()
    app.code_text.tag_config("highlight", background="green")
    app.code_text.tag_remove("highlight", "1.0", "end")
    for token, content in lexer.get_tokens(code):
        app.code_text.tag_add("highlight", "1.0", "end")

def create_file_explorer(app):
    app.file_explorer = ttk.Treeview(app)
    app.file_explorer.grid(row=1, column=0)
    app.file_explorer.insert("", "end", ".", text=".", open=True)
    for file in os.listdir():
        app.file_explorer.insert("", "end", file, text=file)
    app.file_explorer.bind("<Double-1>", lambda event: load_script(app))
    app.code_text.bind("<KeyRelease>", lambda event: highlight_code(app))

def create_slide_menu(app):
    app.slide_menu = tk.Menu(app.master)
    app.master.config(menu=app.slide_menu)
    app.file_menu = tk.Menu(app.slide_menu)
    app.slide_menu.add_cascade(label="File", menu=app.file_menu)
    app.file_menu.add_command(label="Load Script", command=lambda: load_script(app))
    app.file_menu.add_command(label="Save Result to File", command=lambda: save_result(app))
    app.file_menu.add_command(label="Run Output", command=lambda: run_output(app))

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        self.file_explorer = None
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=1)
        self.grid_rowconfigure(1, weight=1)
        create_slide_menu(self)

    def create_widgets(self):
        self.instructions_label = tk.Label(self, text="Input Instructions:")
        self.code_label = tk.Label(self, text="Input Code:")
        self.instructions_text = tk.Text(self, width=100, height=10)
        self.code_text = tk.Text(self, width=100, height=30)
        self.output_code_textbox = tk.Text(self, width=100, height=30, state="disabled")
        self.output_code_label = tk.Label(self, text="Output Code:")
        self.submit_button = tk.Button(self, text="Submit", command=lambda: send_to_openai(self))
        self.save_result_button = tk.Button(self, text="Save Result to File", command=lambda: save_result(self))
        self.compare_code_button = tk.Button(self, text="Compare Code", command=lambda: compare_code(self))

        self.instructions_label.grid(row=0, column=0)
        self.code_label.grid(row=1, column=0)
        self.instructions_text.grid(row=0, column=1)
        self.code_text.grid(row=1, column=1)
        self.output_code_label.grid(row=0, column=2)
        self.output_code_textbox.grid(row=1, column=2)
        self.submit_button.grid(row=2, column=1)
        self.save_result_button.grid(row=2, column=2)
        create_file_explorer(self)
        self.compare_code_button.grid(row=2, column=3)

root = tk.Tk()
root.title("Code-Davinci")
app = Application(master=root)
app.mainloop()
