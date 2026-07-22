import tkinter as tk
from tkinter import ttk
win = tk.Tk()
win.title("menu baar")

#func
def my_function():
    ''' this function is for command '''
    print('command my_function called')
#menu  =================================> Object
#menubar = tk.Menu(win)
#*********************************Simple menubar*******************************
# menubar.add_command(label='Save', command=my_function)
# menubar.add_command(label='Save as', command=my_function)
# menubar.add_command(label='Copy', command=my_function)
# menubar.add_command(label='Paste', command=my_function)

#drop down menubar
main_menu = tk.Menu(win)
file_menu = tk.Menu(main_menu, tearoff=0)

#dropdown
file_menu.add_command(label='New File', command=my_function)
file_menu.add_separator()
file_menu.add_command(label='Save', command=my_function)
file_menu.add_command(label='Save as', command=my_function)
# edit menu
edit_menu = tk.Menu(main_menu, tearoff=0)
edit_menu.add_command(label='undo', command=my_function)
edit_menu.add_command(label='redo', command=my_function)
# case cade
main_menu.add_cascade(label='File', menu=file_menu)
edit_menu.add_cascade(label='Edit', menu=edit_menu)



win.config(menu=main_menu) # no grid no pack method here


win.mainloop()