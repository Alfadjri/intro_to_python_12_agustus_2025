import tkinter as tk
from tkinter import ttk

# function
def sapaan():
    print("Button berhasil di click!")

# Jendela
window = tk.Tk()
window.title("Contoh penggunaan button")

# Isi Content
label_sapaan = ttk.Label(
    window,
    text="Click Here!!!",
    font=("Helvetica",10)
)
button_click = ttk.Button(
    window,
    text="Click",
    command=sapaan
)

# Tampilkan Gui loop
label_sapaan.pack(pady=20,padx=20)
button_click.pack(pady=20,padx=20)
window.mainloop()
