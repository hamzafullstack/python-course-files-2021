import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as msg_box
win = tk.Tk()
win.title("msg box")

#label_frame
label_frame = ttk.LabelFrame(win, text='Contact Details')
label_frame.grid(row=0, column=0, padx=40, pady=10)

#labels
name_labels = ttk.Label(label_frame, text='Enter your name please : ')
age_labels = ttk.Label(label_frame, text='Enter your age please : ')

#entry box variables
name_var = tk.StringVar()
age_var = tk.StringVar()

#entry boxes
name_entrybox = ttk.Entry(label_frame, width=36, textvariable= name_var)
age_entrybox = ttk.Entry(label_frame, width=36, textvariable= age_var)

# grid
name_labels.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
age_labels.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)
name_entrybox.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
age_entrybox.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W)

# functionality for button and exception handling
def submit():
    name = name_var.get()
    age = age_var.get()
    if name == '' or age == '':
        msg_box.showerror("Error", "Please fill both Name & Age")
    else:
        try:
            # age = 'eriefefjfdf' /// default age = '19'
            age = int(age) # we will raise valueError for string input
        except ValueError:
            msg_box.showerror('Wrong input', 'Only integer allowed in age')
        else:
            print(f"{name} : {age}")

#button 
submit_btn = ttk.Button(win, text="Submit", command=submit)
submit_btn.grid(row=1, columnspan=2, padx=40)

win.mainloop()