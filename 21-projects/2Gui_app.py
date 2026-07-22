""" STARTING IN THE NAME OF ALLAH, THE MOST KIND,BENEFICENT AND MOST MERCRIFUL """
# GUI APPLICATION WITH TKINTER (PYTHON-3.8.0)
#================= STARTER CODE =======================#
# import tkinter # module
# from tkinter import *
import tkinter as tk
from tkinter import ttk
win = tk.Tk()
win.title("GUI APP")

# create Labels,
name_label = ttk.Label(win, text="Enter your name : ") # name label
name_label.grid(row=0, column=0, sticky=tk.W) # capital W
# two layout managers pack, grid  method | {grid} better
email_label = ttk.Label(win, text="Enter your email : ") # email label
email_label.grid(row=1, column=0, sticky=tk.W)

age_label = ttk.Label(win, text="Enter your age : ") # age label
age_label.grid(row=2, column=0, sticky=tk.W) # w for west,
gender_label = ttk.Label(win, text="Select your gender : ")
gender_label.grid(row=3, column=0, sticky=tk.W) # gender label : combobox
# create Entrybox with Tkinter
#==========name entry box ==============
name_variable = tk.StringVar()
name_entrybox = ttk.Entry(win, width=25, textvariable = name_variable)
name_entrybox.grid(row=0, column=1)
name_entrybox.focus()
# ============ email entry box ==============
email_variable = tk.StringVar()
email_entrybox = ttk.Entry(win, width=25, textvariable = email_variable)
email_entrybox.grid(row=1, column=1)
#============= Age entry box ===============\
age_variable = tk.StringVar()
age_entrybox = ttk.Entry(win, width=25, textvariable = age_variable)
age_entrybox.grid(row=2, column=1)

# Create ComboBox
gender_variable = tk.StringVar()
gender_combobox = ttk.Combobox(win, width=23, textvariable = gender_variable, state = 'readonly')
gender_combobox['values'] = ('Male', 'Female', 'Other')
gender_combobox.current(0)
gender_combobox.grid(row=3, column=1)

#create Radio Button
radio_variable = tk.StringVar()
radio_button_one = ttk.Radiobutton(win, text='Student', value='Student', variable = radio_variable)
radio_button_one.grid(row=4, column=0)
radio_button_two = ttk.Radiobutton(win, text='Teacher', value='Teacher', variable = radio_variable)
radio_button_two.grid(row=4, column=1)

# Check button
check_variable = tk.IntVar()
check_button = ttk.Checkbutton(win, text='check here for subscribe our newslatter',variable=check_variable)
check_button.grid(row=5, columnspan=3) # span for extend


# Create Submit Button
def Action():
    user_name = name_variable.get()
    user_age = age_variable.get()
    user_email = email_variable.get()
    print(f"{user_name} {user_age} {user_email}")
    user_gender = gender_variable.get()
    user_button = radio_variable.get()
    if check_variable.get() == 0:
        subscribed = "NO"
    else:
        subscribed = "YES"
    print(user_gender, user_button, subscribed)
    with open('Gui_data.txt', 'a') as f:
        f.write(f"{user_name},{user_age},{user_email},{user_gender},{user_button},{subscribed}\n")
    # Configuration and coloring 
    name_entrybox.delete(0, tk.END) # configuration
    age_entrybox.delete(0, tk.END)
    email_entrybox.delete(0, tk.END)
    name_label.configure(foreground='Blue')
    #submit_button.configure(foreground="Red")

submit_button = ttk.Button(win, text='Submit', command=Action) # write button with tkinter
submit_button.grid(row=6, column=0)


win.mainloop()