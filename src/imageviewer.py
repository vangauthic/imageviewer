import os
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
from pathlib import Path
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

def forward(img_no):
    global label
    label.pack_forget()

    label = Label(image_frame, image=list_images[img_no - 1], bg="#2c2c2c")
    label.pack(pady=20, expand=True)

    button_forward.config(command=lambda: forward(img_no + 1))
    button_back.config(command=lambda: back(img_no - 1))

    if img_no == len(list_images):
        button_forward.config(state=DISABLED)
    else:
        button_forward.config(state=NORMAL)

    if img_no == 1:
        button_back.config(state=DISABLED)
    else:
        button_back.config(state=NORMAL)

def back(img_no):
    global label
    label.pack_forget()

    label = Label(image_frame, image=list_images[img_no - 1], bg="#2c2c2c")
    label.pack(pady=20, expand=True)

    button_forward.config(command=lambda: forward(img_no + 1))
    button_back.config(command=lambda: back(img_no - 1))

    if img_no == len(list_images):
        button_forward.config(state=DISABLED)
    else:
        button_forward.config(state=NORMAL)

    if img_no == 1:
        button_back.config(state=DISABLED)
    else:
        button_back.config(state=NORMAL)

root = ttk.Window(themename="darkly")
root.title("Image Viewer")

root.attributes('-fullscreen', True)

root.configure(bg="#2c2c2c")

default_path = Path.home() / "Pictures"
folder_selected = filedialog.askdirectory(title="Select Folder") or default_path

max_width = 1600
max_height = 900

list_images = []
valid_images = [".jpg", ".gif", ".png", ".tga"]

for f in os.listdir(folder_selected):
    ext = os.path.splitext(f)[1]
    if ext.lower() not in valid_images:
        continue

    opened = Image.open(os.path.join(folder_selected, f))
    opened.thumbnail((max_width, max_height))
    list_images.append(ImageTk.PhotoImage(opened))

image_frame = Frame(root, bg="#2c2c2c")
image_frame.pack(expand=True, fill=BOTH)

button_frame = Frame(root, bg="#2c2c2c")
button_frame.pack(side=BOTTOM, pady=20, expand=False)

button_inner_frame = Frame(button_frame, bg="#2c2c2c")
button_inner_frame.pack(anchor=CENTER)

label = Label(image_frame, image=list_images[0], bg="#2c2c2c")
label.pack(pady=20, expand=True)

def modern_button(text, command, state=NORMAL):
    return ttk.Button(button_inner_frame, text=text, command=command, state=state, bootstyle='primary', 
                      width=15, style='TButton')

button_back = modern_button("Back", back, state=DISABLED)
button_exit = modern_button("Exit", root.quit)
button_forward = modern_button("Forward", lambda: forward(2))

button_back.pack(side=LEFT, padx=40, pady=10, expand=True, fill=X)
button_exit.pack(side=LEFT, padx=40, pady=10, expand=True, fill=X)
button_forward.pack(side=LEFT, padx=40, pady=10, expand=True, fill=X)

root.mainloop()
