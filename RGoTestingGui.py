import tkinter as tk
from tkinter import ttk
from PIL import ImageTk,Image
from readJson import JsonReader as Rj


_gcmbPaddy=10
_BtnWidth=8
# Creating tkinter main window
mw = tk.Tk()
mw.geometry('400x400')
mw.title('R-Go Housing testing (v1.0)')
#To Do Add R-go icon
# mw.iconbitmap('Rgo.icon')
   
mw.resizable(0, 0) #Don't allow resizing in the x or y direction

txtCameraOpt = tk.Label(mw, anchor='w',justify='left',borderwidth=2, relief="groove",width = 27,
		font = ("Times New Roman", 10))
txtCameraOpt.grid(row=3, column=1,padx=10, pady=_gcmbPaddy)

txtHousting = tk.Label(mw, anchor='w',justify='left',borderwidth=2, relief="groove",width = 27,
		font = ("Times New Roman", 10))
txtHousting.grid(row=5, column=1,padx=10, pady=_gcmbPaddy)

txtTlvSn = tk.Label(mw, anchor='w',justify='left',borderwidth=2, relief="groove",width = 27,
		font = ("Times New Roman", 10))
txtTlvSn.grid(row=6, column=1,padx=10, pady=_gcmbPaddy)

txtSomsn = tk.Label(mw, anchor='w',justify='left',borderwidth=2, relief="groove",width = 27,
		font = ("Times New Roman", 10))
txtSomsn.grid(row=7, column=1,padx=10, pady=_gcmbPaddy)

def Button_Clicker1(newnum):
	# new_number = e.get() + str(number)
	txtCameraOpt.delete(0, tk.END)
	txtCameraOpt.insert(0, str(newnum))

def Button_Clicker(newnum):
	txtCameraOpt.config(text="changed text!")


def fillCameraOPt():
    txtCameraOpt.insert(tk.END, 'camera opt')






# Label's
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

ttk.Label(mw, text = "Compute Type :",justify='left',
		font = ("Times New Roman", 10)).grid(sticky = 'W',column = 0,
		row = 4, padx = 10, pady = _gcmbPaddy)


ttk.Label(mw, text = "Housing S/N :",justify='left',
		font = ("Times New Roman", 10)).grid(sticky = 'W',column = 0,
		row = 5, padx = 10, pady = _gcmbPaddy)



ttk.Label(mw, text = "TLV S/N :",justify='left',
		font = ("Times New Roman", 10)).grid(sticky = 'W',column = 0,
		row = 6, padx = 10, pady = _gcmbPaddy)


ttk.Label(mw, text = "SOM S/N:",justify='left',
		font = ("Times New Roman", 10)).grid(sticky = 'W',column = 0,
		row = 7, padx = 10, pady = _gcmbPaddy)

SiteCmb = tk.StringVar()
st = ttk.Combobox(mw, width = 27,textvariable = SiteCmb)
st['values'] = ('Hausvarna','Haifa','Holon')
st.grid(column = 1, row = 0)

StationCmb = tk.StringVar()
stn = ttk.Combobox(mw, width = 27,textvariable = StationCmb)
stn['values'] = ('1','2','3')
stn.grid(column = 1, row = 1)

ModuleTypeCmb = tk.StringVar()
module = ttk.Combobox(mw, width = 27,textvariable = ModuleTypeCmb)
module['values'] = ('1','2','3')
module.grid(column = 1, row = 2)

ComputeTypeCmb = tk.StringVar()
ComputeType = ttk.Combobox(mw, width = 27,textvariable = ModuleTypeCmb)
ComputeType['values'] = ('1','2','3')
ComputeType.grid(column = 1, row = 4)





#button opperation

btnRead = tk.Button(mw, text='Read', command=lambda: Button_Clicker(1),bg='blue', fg='white',width=_BtnWidth).grid(column = 2, row = 3)

btnBarcode = tk.Button(mw, text='Barcode', command=lambda: Button_Clicker(1),bg='blue', fg='white',width=_BtnWidth).grid(column = 2, row =5)

btnReadTlvSn = tk.Button(mw, text='Read', command=lambda: Button_Clicker(1),bg='blue', fg='white',width=_BtnWidth).grid(column = 2, row = 6)

btnReadSomSn = tk.Button(mw, text='Read', command=lambda: Button_Clicker(1),bg='blue', fg='white',width=_BtnWidth).grid(column = 2, row = 7)

btnRDOnly = tk.Button(mw, text='R & D Only', command=lambda: Button_Clicker(1),bg='#009999', fg='white',width=_BtnWidth).grid(column = 0, row = 9)

btnTestStart = tk.Button(mw, text='Test', command=lambda: Button_Clicker(1),bg='green', fg='white',width = 15).grid(row=9, column=1, columnspan=2)



# Shows default value
st.current(1)
stn.current(1)
module.current(1)

data=Rj.ReadJson('DataFiles\data.json')

mw.mainloop()
