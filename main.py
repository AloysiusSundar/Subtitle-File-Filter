import os
import tkinter as tk
from tkinter import filedialog

def clean_in_directory(target_dir):
    deleted_count = 0
    for filename in os.listdir(target_dir):
        if filename.lower().endswith(".vtt") and "english" not in filename.lower():
            file_path = os.path.join(target_dir, filename)
            try:
                os.remove(file_path)
                print(f"Deleted: {filename}")
                deleted_count += 1
            except Exception as e:
                print(f"Error deleting {filename}: {e}")
    return deleted_count

root = tk.Tk()
root.withdraw()

total_deleted = 0
while True:
    target_dir = filedialog.askdirectory(title="Select Folder (Cancel to stop)")
    if not target_dir:  
        break
    total_deleted += clean_in_directory(target_dir)

print(f"\nCleanup complete. {total_deleted} files deleted across all selected folders.")
