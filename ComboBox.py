import tkinter as tk
from tkinter import ttk

_gcmbPaddy=10
# Creating tkinter window
window = tk.Tk()
window.geometry('350x250')
window.title('R Go Testing Platform')
window.resizable(0, 0) #Don't allow resizing in the x or y direction
# Label
ttk.Label(window, text = "Site:",anchor='w',
		font = ("Times New Roman", 10)).grid(column = 0,
		row = 0, padx = 10, pady = _gcmbPaddy)


ttk.Label(window, text = "station :",
		font = ("Times New Roman", 10)).grid(column = 0,
		row = 1, padx = 10, pady = _gcmbPaddy)

ttk.Label(window, text = "Module Type :",
		font = ("Times New Roman", 10)).grid(column = 0,
		row = 2, padx = 10, pady = _gcmbPaddy)


n = tk.StringVar()
st = ttk.Combobox(window, width = 27,textvariable = n)
st['values'] = ('Hausvarna','Haifa','Holon')
st.grid(column = 1, row = 0)

n1 = tk.StringVar()
stn = ttk.Combobox(window, width = 27,textvariable = n1)
stn['values'] = ('1','2','3')
stn.grid(column = 1, row = 1)

n2 = tk.StringVar()
module = ttk.Combobox(window, width = 27,textvariable = n2)
module['values'] = ('1','2','3')
module.grid(column = 1, row = 2)

# Shows default value
st.current(1)
stn.current(1)
module.current(1)


window.mainloop()
