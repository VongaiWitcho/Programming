import tkinter as tk
from tkinter import filedialog, messagebox
from backup import BackupManager
from logger import Logger

class BackupGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("File Backup Logger")

        self.logger = Logger()
        self.manager = BackupManager(self.logger)

        self.source_dir = tk.StringVar()
        self.dest_dir = tk.StringVar()
        self.version = tk.StringVar(value="1.0")
        self.zip_option = tk.BooleanVar()

        self.build_gui()

    def build_gui(self):
        tk.Label(self.window, text="Source Folder").grid(row=0, column=0)
        tk.Entry(self.window, textvariable=self.source_dir, width=50).grid(row=0, column=1)
        tk.Button(self.window, text="Browse", command=self.browse_source).grid(row=0, column=2)

        tk.Label(self.window, text="Destination Folder").grid(row=1, column=0)
        tk.Entry(self.window, textvariable=self.dest_dir, width=50).grid(row=1, column=1)
        tk.Button(self.window, text="Browse", command=self.browse_dest).grid(row=1, column=2)

        tk.Checkbutton(self.window, text="ZIP Backup", variable=self.zip_option).grid(row=2, column=1)

        tk.Label(self.window, text="Version").grid(row=3, column=0)
        tk.Entry(self.window, textvariable=self.version).grid(row=3, column=1)

        tk.Button(self.window, text="Backup Now", command=self.backup).grid(row=4, column=1)

        self.window.mainloop()

    def browse_source(self):
        self.source_dir.set(filedialog.askdirectory())

    def browse_dest(self):
        self.dest_dir.set(filedialog.askdirectory())

    def backup(self):
        success = self.manager.backup_folder(
            self.source_dir.get(),
            self.dest_dir.get(),
            self.version.get(),
            zip_backup=self.zip_option.get()
        )
        messagebox.showinfo("Backup", "Backup completed." if success else "Backup failed.")

if __name__ == "__main__":
    BackupGUI()
