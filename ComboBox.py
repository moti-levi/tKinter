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
mw.geometry('350x250')
mw.title('R Go Testing Platform')
mw.resizable(0, 0) #Don't allow resizing in the x or y direction

back = tk.Frame(master=mw, width=500, height=500, bg='black')
# back.pack()

# Label
ttk.Label(mw, text = "Site:",anchor='w',
		font = ("Times New Roman", 10)).grid(column = 0,
		row = 0, padx = 10, pady = _gcmbPaddy)


ttk.Label(mw, text = "station :",
		font = ("Times New Roman", 10)).grid(column = 0,
		row = 1, padx = 10, pady = _gcmbPaddy)

ttk.Label(mw, text = "Module Type :",
		font = ("Times New Roman", 10)).grid(column = 0,
		row = 2, padx = 10, pady = _gcmbPaddy)

ttk.Label(mw, text = "Camera Opt :",
		font = ("Times New Roman", 10)).grid(column = 0,
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

close = tk.Button( text='Read', command=openNewWindow,bg='blue', fg='white').grid(column = 2, row = 3)

# Shows default value
st.current(1)
stn.current(1)
module.current(1)


mw.mainloop()
