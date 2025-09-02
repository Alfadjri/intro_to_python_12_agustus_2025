import tkinter as tk
from tkinter import ttk


# function
def sapaan():
    data_input = input_username.get() #get nilai dari inputan
    print(f"username {data_input}")

# Jendela
window = tk.Tk()
window.title("Contoh penggunaan Entry")

# Isi Content
label_sapaan = ttk.Label(
    window,
    text="Username",
    font=("Helvetica",10)
)
button_click = ttk.Button(
    window,
    text="Login",
    command=sapaan
)
input_username = ttk.Entry(
    window,
    width=30
) # tampilan

# Tampilkan Gui loop
label_sapaan.pack(pady=20,padx=20)
input_username.pack(padx=20,pady=20)
button_click.pack(pady=20,padx=20)
window.mainloop()
