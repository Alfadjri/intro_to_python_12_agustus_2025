import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("Contoh Layout Grid")
window.geometry("500x400") #besar dari windows yang temen-temen punya
ttk.Label(window,text="Username :").grid(row=0,column=0,sticky="w",padx=5,pady=5)
ttk.Entry(window).grid(row=0,column=1,sticky="w",padx=5,pady=5)
ttk.Label(window,text="Password :").grid(row=1,column=0,sticky="w",padx=5,pady=5)
ttk.Entry(window).grid(row=1,column=1,sticky="w",padx=5,pady=5)
window.mainloop()