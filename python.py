import os
import subprocess
import tkinter as tk
import tkinter.filedialog as filedialog
from tkinter import ttk

class FileGenerator:
    @staticmethod
    def create_python_file(file_name, code, directory=""):
        try:
            file_path = os.path.join(directory, file_name) if directory else file_name
            with open(file_path, "w") as file:
                file.write(code)
            print(f"Successfully created a Python file: {file_path}")
            print(f"File saved at: {file_path}")
        except Exception as e:
            print(f"Error while creating the file: {e}")

    @staticmethod
    def fix_error(file_name, error_description, solution):
        try:
            with open(file_name, "r") as file:
                file_content = file.read()
        except Exception as e:
            print(f"Error while reading the file: {e}")
            return

        fixed_lines = file_content.split("\n")

        for line_index, line_content in enumerate(fixed_lines):
            if error_description in line_content:
                fixed_lines[line_index] = solution

        with open(file_name, "w") as file:
            file.write("\n".join(fixed_lines))

        print(f"Successfully fixed the error in the file: {file_name}")

def create_file():
    file_name = fileNameEntry.get()
    code = codeEntry.get("1.0", "end-1c")

    directory = filedialog.askdirectory()
    if directory:
        FileGenerator.create_python_file(file_name, code, directory)

def fix_error():
    file_name = fileNameEntry2.get()
    error_description = errorEntry.get()
    solution = solutionEntry.get()

    file_path = filedialog.askopenfilename()
    if file_path:
        with open(file_path, "r") as file:
            file_content = file.read()

        fixed_lines = file_content.split("\n")

        for line_index, line_content in enumerate(fixed_lines):
            if error_description in line_content:
                fixed_lines[line_index] = solution

        with open(file_path, "w") as file:
            file.write("\n".join(fixed_lines))

        print(f"Successfully fixed the error in the file: {file_path}")

# Create the main window
root = tk.Tk()
root.title("File Generator")

# Set up the GUI style
style = ttk.Style()
style.configure("Custom.TLabel", font=("Arial", 12), foreground="white")
style.configure("Custom.TEntry", font=("Arial", 12), foreground="white")
style.configure("Custom.TButton", font=("Arial", 12), foreground="white", background="dodgerblue", padding=(5, 2, 5, 2))

# Create a frame
frame = ttk.Frame(root, style="Custom.TFrame")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), padx=10, pady=10)

# Configuration for the widgets

fileNameLabel = ttk.Label(frame, text="File Name:", style="Custom.TLabel")
fileNameLabel.grid(row=0, column=0, sticky=tk.W, padx=(0, 10))

fileNameEntry = ttk.Entry(frame, style="Custom.TEntry", width=30)
fileNameEntry.grid(row=0, column=1, sticky=(tk.W, tk.E))

codeLabel = ttk.Label(frame, text="Code:", style="Custom.TLabel")
codeLabel.grid(row=1, column=0, sticky=tk.W, padx=(0, 10))

codeEntry = tk.Text(frame, height=10, width=50)
codeEntry.grid(row=1, column=1, sticky=(tk.W, tk.E, tk.N, tk.S), padx=(0, 10))

directoryLabel = ttk.Label(frame, text="Directory:", style="Custom.TLabel")
directoryLabel.grid(row=2, column=0, sticky=tk.W, padx=(0, 10))

dirEntry = ttk.Entry(frame, style="Custom.TEntry", width=30)
dirEntry.grid(row=2, column=1, sticky=(tk.W, tk.E))

ttk.Button(frame, text="Create File", style="Custom.TButton", command=create_file).grid(row=3, column=0, columnspan=2, pady=(10, 0))

fileNameLabel2 = ttk.Label(frame, text="File Name:", style="Custom.TLabel")
fileNameLabel2.grid(row=4, column=0, sticky=tk.W, padx=(0, 10))

fileNameEntry2 = ttk.Entry(frame, style="Custom.TEntry", width=30)
fileNameEntry2.grid(row=4, column=1, sticky=(tk.W, tk.E))

errorLabel = ttk.Label(frame, text="Error Description:", style="Custom.TLabel")
errorLabel.grid(row=5, column=0, sticky=tk.W, padx=(0, 10))

errorEntry = ttk.Entry(frame, style="Custom.TEntry", width=30)
errorEntry.grid(row=5, column=1, sticky=(tk.W, tk.E))

solutionLabel = ttk.Label(frame, text="Solution:", style="Custom.TLabel")
solutionLabel.grid(row=6, column=0, sticky=tk.W, padx=(0, 10))

solutionEntry = ttk.Entry(frame, style="Custom.TEntry", width=30)
solutionEntry.grid(row=6, column=1, sticky=(tk.W, tk.E))

ttk.Button(frame, text="Fix Error", style="Custom.TButton", command=fix_error).grid(row=7, column=0, columnspan=2, pady=(10, 0))

root.mainloop()