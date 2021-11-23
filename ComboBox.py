import tkinter as tk
from tkinter import ttk
  
# Creating tkinter window
window = tk.Tk()
window.title('Rgo Testing Program')
window.geometry('500x350')
  
# label text for title
ttk.Label(window, text = "RGo Testing", 
          background = 'green', foreground ="white", 
          font = ("Times New Roman", 15)).grid(row = 0, column = 1)
  
# label
ttk.Label(window, text = "Site :",
          font = ("Times New Roman", 10)).grid(column = 0,
          row = 1,  column = 0,padx = 10, pady = 25)


# label
ttk.Label(window, text = "Station :",
          font = ("Times New Roman", 10)).grid(column = 0,
          row = 2, column = 0,padx = 10, pady = 25)
  
# Combobox creation
site = tk.StringVar()
sitechoosen = ttk.Combobox(window, width = 27, textvariable = site)

# Combobox creation
station = tk.StringVar()
stationChoosen = ttk.Combobox(window, width = 27, textvariable = station)
  
# Adding combobox drop down list
sitechoosen['values'] = (' January', 
                          ' February',
                          ' March',
                          ' April',
                          ' May',
                          ' June',
                          ' July',
                          ' August',
                          ' September',
                          ' October',
                          ' November',
                          ' December')
stationChoosen['values'] = (' 1', 
                          ' 2',
                          ' 3')  


sitechoosen.grid(column = 1, row = 2)
sitechoosen.current()

stationChoosen.grid(column = 2, row = 2)
stationChoosen.current()


window.mainloop()