import tkinter as tk
from tkinter import ttk

def button_func():
    
    #get content of entry

    entry_text = entry.get()

    #update label

    entry['state'] = 'disabled' #disables entry widget from working further

    #label.configure(text = 'some other text')
    #label['text'] = 'some other text' #same as above
    label['text'] = entry_text

def button_func_2():

    label['text'] = 'sum'
    entry['state'] = 'enabled'

#window
window = tk.Tk()
window.title('Getting and setting widgets')
window.geometry('400x200')

#widgets

label = ttk.Label(master = window, text = 'sum', font = 'calibri 20' )

entry = ttk.Entry(master = window, )

button = ttk.Button(text = 'submit', command = button_func)
button_2 = ttk.Button(text = 'revert', command = button_func_2)

label.pack()
entry.pack()
button.pack()
button_2.pack()

#run
window.mainloop()
