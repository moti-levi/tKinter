import tkinter as tk
from tkinter import ttk
from PIL import ImageTk,Image


# function to open a new window
# on a button click
def openNewWindow():
     
    # Toplevel object which will
    # be treated as a new window
    newWindow = Toplevel(master)
 
    # sets the title of the
    # Toplevel widget
    newWindow.title("New Window")
 
    # sets the geometry of toplevel
    newWindow.geometry("200x200")
 
    # A Label widget to show in toplevel
    Label(newWindow,
          text ="This is a new window").pack()



_gcmbPaddy=10
# Creating tkinter main window
mw = tk.Tk()
mw.geometry('350x280')
mw.title('R Go Testing Platform')
mw.resizable(0, 0) #Don't allow resizing in the x or y direction

# e = Entry(root, width=35, borderwidth=5)
# e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


e = tk.Label(mw, anchor='w',justify='left',borderwidth=2, relief="groove",width = 27,
		font = ("Times New Roman", 10))
e.grid(row=3, column=1,padx=10, pady=_gcmbPaddy)

def Button_Clicker1(newnum):
	# new_number = e.get() + str(number)
	e.delete(0, tk.END)
	e.insert(0, str(newnum))

def Button_Clicker(newnum):
	e.config(text="changed text!")

# text=tk.Text(mw, height = 1, width = 23,state='disabled').grid(sticky = 'w',column = 1,
# 		row = 3, padx = 10, pady = _gcmbPaddy)

def fillCameraOPt():
    e.insert(tk.END, 'camera opt')

# text = tk.Text(mw, height = 2, width = 30)
# # text.pack()
# text.insert(tk.END, '-')

# def apress():
#     text.insert(tk.END, 'a')

# btn = tk.Button(mw, text = 'a', width = 5, command = apress) 
# # btn.pack()

# back = tk.Frame(master=mw, width=500, height=500, bg='black')
# back.pack()

# Label
ttk.Label(mw, text = "Site:",anchor='w',justify='left',
		font = ("Times New Roman", 10)).grid(sticky = 'W',column = 0,
		row = 0, padx = 10, pady = _gcmbPaddy)


ttk.Label(mw, text = "station :",justify='left',
		font = ("Times New Roman", 10)).grid(sticky = 'W',column = 0,
		row = 1, padx = 10, pady = _gcmbPaddy)

ttk.Label(mw, text = "Module Type :",
		font = ("Times New Roman", 10)).grid(sticky = 'W',column = 0,
		row = 2, padx = 10, pady = _gcmbPaddy)

ttk.Label(mw, text = "Camera Opt :",justify='left',
		font = ("Times New Roman", 10)).grid(sticky = 'W',column = 0,
		row = 3, padx = 10, pady = _gcmbPaddy)



n = tk.StringVar()
st = ttk.Combobox(mw, width = 27,textvariable = n)
st['values'] = ('Hausvarna','Haifa','Holon')
st.grid(column = 1, row = 0)

n1 = tk.StringVar()
stn = ttk.Combobox(mw, width = 27,textvariable = n1)
stn['values'] = ('1','2','3')
stn.grid(column = 1, row = 1)

n2 = tk.StringVar()
module = ttk.Combobox(mw, width = 27,textvariable = n2)
module['values'] = ('1','2','3')
module.grid(column = 1, row = 2)


# button_1 = tk.Button(root, text="1", padx=40, pady=20, command=lambda: Button_Clicker(1))


close = tk.Button(mw, text='Read', command=lambda: Button_Clicker(1),bg='blue', fg='white').grid(column = 2, row = 3)

# Shows default value
st.current(1)
stn.current(1)
module.current(1)


mw.mainloop()
