import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("Contoh Layout Pack")
window.geometry("1680x1050") #besar dari windows yang temen-temen punya
ttk.Label(window,text="Label pertama").pack(padx=20,pady=20) #untuk mengatur layout 1 komponen
ttk.Label(window,text="Label dua").pack(padx=20,pady=20)
ttk.Label(window,text="Label tiga").pack(padx=20,pady=20)
window.mainloop()