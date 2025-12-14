import os
import tkinter as tk
from tkinter import filedialog, messagebox



def remove_zips():
    root = tk.Tk()
    root.withdraw()

    folder_path = filedialog.askdirectory(title="Select Folder")

    if not folder_path:
        print("No folder selected. Exiting.")
        return

    zip_files_found = []

    for root_dir, dirs, files in os.walk(folder_path):
        for file in files:
            if file.lower().endswith(".zip"):
                full_path = os.path.join(root_dir, file)
                zip_files_found.append(full_path)

    if not zip_files_found:
        messagebox.showinfo("Result", "No .zip files found in the selected directory.")
        return

    max_display = 25

    if len(zip_files_found) > max_display:
        displayed_files = zip_files_found[:max_display]
        file_list_str = "\n".join(displayed_files)
        file_list_str += f"\n\n...and {len(zip_files_found) - max_display} more files."
    else:
        file_list_str = "\n".join(zip_files_found)

    confirm_msg = (
        f"Found {len(zip_files_found)} .zip files in:\n{folder_path}\n\n"
        f"Files to be deleted:\n-------------------\n"
        f"{file_list_str}\n\n"
        f"Are you sure you want to delete them permanently?"
    )
    user_response = messagebox.askyesno("Confirm Deletion", confirm_msg, icon='warning')

    if user_response:
        deleted_count = 0
        errors = 0

        for file_path in zip_files_found:
            try:
                os.remove(file_path)
                print(f"Deleted: {file_path}")
                deleted_count += 1
            except Exception as e:
                print(f"Error deleting {file_path}: {e}")
                errors += 1

        result_msg = f"Operation complete.\n\nDeleted: {deleted_count}\nErrors: {errors}"
        messagebox.showinfo("Done", result_msg)
    else:
        print("Operation cancelled by user.")


if __name__ == "__main__":
    remove_zips()