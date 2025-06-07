import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox
import subprocess
import platform
import os

DB_PATH = "memory.db"

# Helper function to open files cross-platform
def open_file(path):
    if not os.path.exists(path):
        messagebox.showerror("File Not Found", f"File does not exist:\n{path}")
        return
    system = platform.system()
    try:
        if system == "Darwin":  # macOS
            subprocess.run(["open", path])
        elif system == "Windows":
            os.startfile(path)
        else:  # Linux
            subprocess.run(["xdg-open", path])
    except Exception as e:
        messagebox.showerror("Error", f"Failed to open file:\n{e}")

class MemoryBrowser(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Memory Browser")
        self.geometry("900x400")
        self.resizable(True, True)

        # Connect to database
        self.conn = sqlite3.connect(DB_PATH)
        self.create_table_if_missing()
        self.create_widgets()
        self.load_memories()

    # Create the table if it doesn't exist
    def create_table_if_missing(self):
        cursor = self.conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS memories (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                prompt TEXT,
                enhanced_prompt TEXT,
                image_path TEXT,
                model_path TEXT
            )
        """)
        self.conn.commit()

    # Create GUI elements
    def create_widgets(self):
        self.tree = ttk.Treeview(
            self,
            columns=("Prompt", "Expanded Prompt", "Image", "3D Model"),
            show="headings"
        )
        self.tree.heading("Prompt", text="Prompt")
        self.tree.heading("Expanded Prompt", text="Expanded Prompt")
        self.tree.heading("Image", text="Image Path")
        self.tree.heading("3D Model", text="3D Model Path")
        self.tree.column("Prompt", width=200)
        self.tree.column("Expanded Prompt", width=350)
        self.tree.column("Image", width=150)
        self.tree.column("3D Model", width=150)
        self.tree.pack(fill=tk.BOTH, expand=True)

        self.tree.bind("<<TreeviewSelect>>", self.on_select)

    # Load data from the database into the Treeview
    def load_memories(self):
        self.tree.delete(*self.tree.get_children())  # Clear old entries
        cursor = self.conn.cursor()
        cursor.execute("SELECT id, prompt, enhanced_prompt, image_path, model_path FROM memories ORDER BY id DESC")
        rows = cursor.fetchall()
        for row in rows:
            self.tree.insert("", "end", iid=row[0], values=row[1:])

    # Handle row selection
    def on_select(self, event):
        selected = self.tree.selection()
        if not selected:
            return
        item_id = selected[0]
        values = self.tree.item(item_id, "values")
        image_path = values[2]
        model_path = values[3]

        # Open the image and model files if paths exist
        if image_path:
            open_file(image_path)
        if model_path:
            open_file(model_path)

if __name__ == "__main__":
    app = MemoryBrowser()
    app.mainloop()
