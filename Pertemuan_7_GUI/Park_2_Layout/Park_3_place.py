import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("Contoh Layout place")
window.geometry("400x500") #besar dari windows yang temen-temen punya
tombol_satu = ttk.Button(window,text="Tombol di posisi kordinat (x = 30 , y = 50)")
tombol_satu.place(x=30,y=50)
tombol_dua = ttk.Button(window,text="Tombol di posisi kordinat (x = 150 , y = 150)")
tombol_dua.place(x=150,y=150)
window.mainloop()