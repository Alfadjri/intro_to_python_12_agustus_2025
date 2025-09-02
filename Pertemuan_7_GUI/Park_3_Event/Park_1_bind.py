import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("Contoh bind command")

def panggilan(event):
    print("Hello World!!!")
    
lable = ttk.Label(window,text="Arahakan kursor ke sini ada pesan yang akan muncul")
lable.bind("<Enter>",panggilan)
lable.pack(padx=10,pady=10)

window.mainloop()