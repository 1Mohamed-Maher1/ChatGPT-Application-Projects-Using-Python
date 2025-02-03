import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

def open_file():
    """Open a text file and load its content into the text area."""
    filepath = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if not filepath:
        return
    txt_edit.delete("1.0", tk.END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END, text)
    root.title(f"Text Editor - {filepath}")

def save_file():
    """Save the current content of the text area to a text file."""
    filepath = filedialog.asksaveasfilename(defaultextension="txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        text = txt_edit.get("1.0", tk.END)
        output_file.write(text)
    root.title(f"Text Editor - {filepath}")

# Set up the main application window
root = tk.Tk()
root.title("Text Editor")
root.geometry("600x400")

# Create a text widget for editing content
txt_edit = tk.Text(root, wrap="word")
txt_edit.pack(expand=True, fill="both")

# Create a menu bar with File menu
menu_bar = tk.Menu(root)
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)
menu_bar.add_cascade(label="File", menu=file_menu)

# Add the menu bar to the window
root.config(menu=menu_bar)

# Run the application
root.mainloop()

################################################################

# import tkinter as tk
# from tkinter import filedialog

# def open_file():
#     """Open a text file and load its content into the text area."""
#     filepath = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
#     if not filepath:
#         return
#     txt_edit.delete("1.0", tk.END)
#     with open(filepath, "r") as input_file:
#         text = input_file.read()
#         txt_edit.insert(tk.END, text)
#     root.title(f"Text Editor - {filepath}")

# def save_file():
#     """Save the current content of the text area to a text file."""
#     filepath = filedialog.asksaveasfilename(defaultextension="txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
#     if not filepath:
#         return
#     with open(filepath, "w") as output_file:
#         text = txt_edit.get("1.0", tk.END)
#         output_file.write(text)
#     root.title(f"Text Editor - {filepath}")

# # Set up the main application window
# root = tk.Tk()
# root.title("Text Editor")
# root.geometry("600x400")

# # Configure the grid layout
# root.rowconfigure(0, weight=1)
# root.columnconfigure(0, weight=1)

# # Create a text widget for editing content
# txt_edit = tk.Text(root, wrap="word")
# txt_edit.grid(row=0, column=0, sticky="nsew")

# # Create a scroll bar for the text widget
# scrollbar = tk.Scrollbar(root, command=txt_edit.yview)
# scrollbar.grid(row=0, column=1, sticky="ns")
# txt_edit.config(yscrollcommand=scrollbar.set)

# # Create a menu bar with File menu
# menu_bar = tk.Menu(root)
# file_menu = tk.Menu(menu_bar, tearoff=0)
# file_menu.add_command(label="Open", command=open_file)
# file_menu.add_command(label="Save", command=save_file)
# file_menu.add_separator()
# file_menu.add_command(label="Exit", command=root.quit)
# menu_bar.add_cascade(label="File", menu=file_menu)

# # Add the menu bar to the window
# root.config(menu=menu_bar)

# # Run the application
# root.mainloop()

####################################################

# import tkinter as tk
# from tkinter import filedialog

# def open_file():
#     """Open a text file and load its content into the text area."""
#     filepath = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
#     if not filepath:
#         return
#     txt_edit.delete("1.0", tk.END)
#     with open(filepath, "r") as input_file:
#         text = input_file.read()
#         txt_edit.insert(tk.END, text)
#     root.title(f"Text Editor - {filepath}")

# def save_file():
#     """Save the current content of the text area to a text file."""
#     filepath = filedialog.asksaveasfilename(defaultextension="txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
#     if not filepath:
#         return
#     with open(filepath, "w") as output_file:
#         text = txt_edit.get("1.0", tk.END)
#         output_file.write(text)
#     root.title(f"Text Editor - {filepath}")

# # Set up the main application window
# root = tk.Tk()
# root.title("Text Editor")
# root.geometry("600x400")

# # Configure the grid layout for the main window
# root.rowconfigure(0, weight=1)
# root.columnconfigure(0, weight=1)

# # Create a text widget for editing content
# txt_edit = tk.Text(root, wrap="word")
# txt_edit.grid(row=0, column=0, sticky="nsew")

# # Create a scroll bar for the text widget
# scrollbar = tk.Scrollbar(root, command=txt_edit.yview)
# scrollbar.grid(row=0, column=1, sticky="ns")
# txt_edit.config(yscrollcommand=scrollbar.set)

# # Create a frame to hold the buttons
# button_frame = tk.Frame(root)
# button_frame.grid(row=0, column=2, sticky="ns", padx=5, pady=5)

# # Add buttons to the button frame
# open_button = tk.Button(button_frame, text="Open", command=open_file)
# open_button.grid(row=0, column=0, sticky="ew", padx=5, pady=5)

# save_button = tk.Button(button_frame, text="Save", command=save_file)
# save_button.grid(row=1, column=0, sticky="ew", padx=5, pady=5)

# exit_button = tk.Button(button_frame, text="Exit", command=root.quit)
# exit_button.grid(row=2, column=0, sticky="ew", padx=5, pady=5)

# # Expand the button frame to take the required height
# button_frame.rowconfigure([0, 1, 2], weight=1)
# button_frame.columnconfigure(0, weight=1)

# # Create a menu bar with File menu
# menu_bar = tk.Menu(root)
# file_menu = tk.Menu(menu_bar, tearoff=0)
# file_menu.add_command(label="Open", command=open_file)
# file_menu.add_command(label="Save", command=save_file)
# file_menu.add_separator()
# file_menu.add_command(label="Exit", command=root.quit)
# menu_bar.add_cascade(label="File", menu=file_menu)

# # Add the menu bar to the window
# root.config(menu=menu_bar)

# # Run the application
# root.mainloop()
