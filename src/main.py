import LittleDog as ld
import tkinter as tk
from tkinter import filedialog, messagebox
import os

class LittleDogEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("LittleDog 0.0.1")
        self.root.geometry("800x600")
        
        # Set the icon of the window
        self.root.iconbitmap("src/assets/LittleDog5727.ico")
        
        self.text_area = tk.Text(self.root, wrap='word', undo=True)
        self.text_area.pack(fill='both', expand=1)
        
        self.file_path = None
        
        self.create_menu()
        self.bind_shortcuts()
    
    def create_menu(self):
        menu_bar = tk.Menu(self.root)
        
        # File menu
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="New", command=self.new_file, accelerator="Ctrl+N")
        file_menu.add_command(label="Open", command=self.open_file, accelerator="Ctrl+O")
        file_menu.add_command(label="Save", command=self.save_file, accelerator="Ctrl+S")
        file_menu.add_command(label="Save As", command=self.save_as_file, accelerator="Ctrl+Shift+S")
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit, accelerator="Ctrl+Q")
        
        menu_bar.add_cascade(label="File", menu=file_menu)
        
        # Run menu
        run_menu = tk.Menu(menu_bar, tearoff=0)
        run_menu.add_command(label="Run", command=self.run_code, accelerator="Ctrl+R")
        
        menu_bar.add_cascade(label="Run", menu=run_menu)
        
        self.root.config(menu=menu_bar)
    
    def bind_shortcuts(self):
        self.root.bind('<Control-n>', lambda event: self.new_file())
        self.root.bind('<Control-o>', lambda event: self.open_file())
        self.root.bind('<Control-s>', lambda event: self.save_file())
        self.root.bind('<Control-S>', lambda event: self.save_as_file())
        self.root.bind('<Control-q>', lambda event: self.root.quit())
        self.root.bind('<Control-r>', lambda event: self.run_code())
    
    def new_file(self):
        self.text_area.delete(1.0, tk.END)
        self.file_path = None
        self.root.title("LittleDog Editor - New File")
    
    def open_file(self):
        self.file_path = filedialog.askopenfilename(
            defaultextension=".ld",
            filetypes=[("LittleDog Files", "*.ld"), ("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        if self.file_path:
            with open(self.file_path, "r", encoding="utf-8") as file:
                content = file.read()
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(tk.INSERT, content)
            self.root.title(f"LittleDog Editor - {os.path.basename(self.file_path)}")
    
    def save_file(self):
        if self.file_path:
            self._save_to_file(self.file_path)
        else:
            self.save_as_file()
    
    def save_as_file(self):
        self.file_path = filedialog.asksaveasfilename(
            defaultextension=".ld",
            filetypes=[("LittleDog Files", "*.ld"), ("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        if self.file_path:
            self._save_to_file(self.file_path)
    
    def _save_to_file(self, path):
        with open(path, "w", encoding="utf-8") as file:
            content = self.text_area.get(1.0, tk.END)
            file.write(content)
        self.root.title(f"LittleDog Editor - {os.path.basename(self.file_path)}")
        messagebox.showinfo("Saved", f"File saved as {self.file_path}")
    
    def run_code(self):
        try:
            # Get the code from the text area
            code = self.text_area.get(1.0, tk.END)
            # Execute the code
            ld.littledogai_lilfy(code, False, True)
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred:\n{e}")

if __name__ == "__main__":
    print("LittleDog 0.0.1 > \nTerminal >>>")
    root = tk.Tk()
    editor = LittleDogEditor(root)
    root.mainloop()
