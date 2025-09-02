import tkinter as tk
from tkinter import ttk

# Jendela
window = tk.Tk()
window.title("Contoh penggunaan lable")

# Isi Content
label_sapaan = ttk.Label(
    window,
    text="Selamat datang di gui baru",
    font=("Helvetica",10)
)

# Tampilkan Gui loop
label_sapaan.pack(pady=20,padx=20)
window.mainloop()
