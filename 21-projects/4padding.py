import tkinter as tk
from tkinter import ttk
win = tk.Tk()
win.title("Loop")

labels = ['what is your name  : ', 'what is your age  : ', 'your Gender']

for i in range(len(labels)): # loop on labels with len function
    current_label = 'label' + str(i) #label0, label1
    current_label = ttk.Label(win, text=labels[i])
    current_label.grid(row=i, column=0, sticky=tk.W, padx=40, pady=0) # padx pady

# Entrybox
name_var = tk.StringVar()
user_data = {
    'name' : tk.StringVar(),
    'age' : tk.StringVar(),
    'gender' : tk.StringVar()
}
counter = 0
for i in user_data:
    current_entrybox = 'entry' + i # entryname # entryage # entrygndr
    current_entrybox = ttk.Entry(win, width=16, textvariable=user_data[i])
    current_entrybox.grid(column=1, row=counter, padx=40, pady=0) #50, etx
    counter += 1

#submit button
def Action_button():
    print(user_data['name'].get())
    print(user_data['age'].get())
    print(user_data['gender'].get())

submit_btn = ttk.Button(win, text='Submit', command=Action_button)
submit_btn.grid(row=3, columnspan=2)

win.mainloop()