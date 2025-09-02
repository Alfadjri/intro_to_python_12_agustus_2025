import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("Contoh bind command")

def panggilan():
    print("Hello World!!!")
    
tombol = ttk.Button(window,text="Click Here!!",command=panggilan)
tombol.pack(padx=10,pady=10)

window.mainloop()