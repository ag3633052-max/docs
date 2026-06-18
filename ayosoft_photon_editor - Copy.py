import tkinter as tk
from tkinter import filedialog, messagebox

class AyosoftPhoton:
    def __init__(self, root):
        self.root = root
        self.root.title("Ayosoft.Photon - The New Text Editor")
        self.root.geometry("800x600")

        self.filename = None

        # Create Text Widget
        self.text_area = tk.Text(self.root, undo=True)
        self.text_area.pack(fill=tk.BOTH, expand=1)

        # Create Menu
        self.menu = tk.Menu(self.root)
        self.root.config(menu=self.menu)

        # File Menu
        file_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="New", command=self.new_file)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.exit_app)

        # Edit Menu
        edit_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Edit", menu=edit_menu)
        edit_menu.add_command(label="Undo", command=self.text_area.edit_undo)
        edit_menu.add_command(label="Redo", command=self.text_area.edit_redo)
        edit_menu.add_separator()
        edit_menu.add_command(label="Cut", command=lambda: self.root.focus_get().event_generate('<<Cut>>'))
        edit_menu.add_command(label="Copy", command=lambda: self.root.focus_get().event_generate('<<Copy>>'))
        edit_menu.add_command(label="Paste", command=lambda: self.root.focus_get().event_generate('<<Paste>>'))

    def new_file(self):
        self.text_area.delete(1.0, tk.END)
        self.filename = None
        self.root.title("Ayosoft.Photon - New Document")

    def open_file(self):
        file_path = filedialog.askopenfilename(title="Open File", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file_path:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
            self.text_area.delete(1.0, tk.END)
            self.text_area.insert(tk.END, content)
            self.filename = file_path
            self.root.title(f"Ayosoft.Photon - {self.filename}")

    def save_file(self):
        if self.filename:
            content = self.text_area.get(1.0, tk.END)
            with open(self.filename, 'w', encoding='utf-8') as file:
                file.write(content)
        else:
            self.save_as()

    def save_as(self):
        file_path = filedialog.asksaveasfilename(title="Save As", defaultextension=".txt",
                                                     filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file_path:
            self.filename = file_path
            self.save_file()
            self.root.title(f"Ayosoft.Photon - {self.filename}")

    def exit_app(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = AyosoftPhoton(root)
    root.mainloop()