import tkinter as tk
from tkinter import ttk
_gcmbPaddy=10
# Creating tkinter window
window = tk.Tk()
window.geometry('350x250')
# Label
ttk.Label(window, text = "Site:",
		font = ("Times New Roman", 10)).grid(column = 0,
		row = 0, padx = 10, pady = _gcmbPaddy)


ttk.Label(window, text = "station :",
		font = ("Times New Roman", 10)).grid(column = 0,
		row = 1, padx = 10, pady = _gcmbPaddy)

ttk.Label(window, text = "Module Type :",
		font = ("Times New Roman", 10)).grid(column = 0,
		row = 2, padx = 10, pady = _gcmbPaddy)


n = tk.StringVar()
station = ttk.Combobox(window, width = 27,
							textvariable = n)

n1 = tk.StringVar()
st = ttk.Combobox(window, width = 27,
							textvariable = n1)

n2 = tk.StringVar()
module = ttk.Combobox(window, width = 27,
							textvariable = n1)

# Adding combobox drop down list
station['values'] = (' 1',
						' 2',
						' 3')						)

st['values'] = (' 1',
'2','3')

module['values'] = (' 1',
'2','3')

st.grid(column = 1, row = 0)
station.grid(column = 1, row = 1)
module.grid(column = 1, row = 2)

# Shows february as a default value
st.current(1)
station.current(1)
module.current(1)
window.mainloop()
