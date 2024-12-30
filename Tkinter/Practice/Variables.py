import tkinter as tk
from tkinter import ttk

def button_func():
    print(string_var.get())
    string_var.set('button pressed')

#window
window = tk.Tk()
window.title('Getting and setting widgets')
window.geometry('400x200')

#tkinter variable

string_var = tk.StringVar() 

#widgets

label = ttk.Label(master = window, text = 'sum', font = 'calibri 20', textvariable = string_var )

entry = ttk.Entry(master = window,textvariable = string_var )

button = ttk.Button(master = window, text = 'button', command = button_func)

label.pack()
entry.pack()
button.pack()

#run
window.mainloop()
