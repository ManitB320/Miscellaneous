import tkinter as tk
from tkinter import ttk

#window
window = tk.Tk()
window.title('Trial')
window.geometry('800x400')


#title
title_label = ttk.Label(master = window, text = 'Miles to Kilo', font= 'Calibri 24 bold')
title_label.pack()

#run
window.mainloop()