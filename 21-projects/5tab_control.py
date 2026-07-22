import tkinter as tk
from tkinter import ttk
win = tk.Tk()
win.title("Tab control")
nb = ttk.Notebook(win)
# page 1 , page 2 ================> frames
page1 = ttk.Frame(nb)
page2 = ttk.Frame(nb)
nb.add(page1, text='One') # add method
nb.add(page2, text='Two')
nb.pack(expand=True, fill='both')
#labels....
label1 = ttk.Label(page1, text='The label one ')
label1.grid(row=0, column=0)

#entry
entry1 = ttk.Entry(page1, width=30)
entry1.grid(row=0, column=1)

label2 = ttk.Label(page2, text='The label Two ')
label2.grid(row=0, column=0)

win.mainloop()