import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

def open_file():
    filepath = askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.txt")])

    if not filepath:
        return
    txt_edit.delete(1.0, tk.END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END, text)
    Window.title(f"AlmdrasaTextEditor - {filepath}")


def save_file():
    filepath = asksaveasfilename(defaultextension="txt",filetypes=[("Text Files", "*.txt"), ("All Files", "*.txt")])
    
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        text = txt_edit.get(1.0, tk.END)
        output_file.write(text)
    Window.title(f"AlmdrasaTextEditor - {filepath}")

Window = tk.Tk()
Window.title('Almdrasa Text Editor')
Window.rowconfigure(0, minsize=600)
Window.columnconfigure(1, minsize=800)


txt_edit = tk.Text(Window)
frame_buttons = tk.Frame(Window, relief=tk.RAISED)
btn_open = tk.Button(frame_buttons, text="Open File", command=open_file)
btn_save = tk.Button(frame_buttons, text="Save As", command=save_file)

btn_open.grid(column=0, row=0, sticky="ew",padx=5, pady=5)
btn_save.grid(column=0, row=1,sticky="ew", padx=5)

frame_buttons.grid(column=0 , row=0, sticky="ns")
txt_edit.grid(column=1 , row=0, sticky="nsew")

Window.mainloop()