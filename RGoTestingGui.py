#region Using
from os import truncate
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk,Image
from readJson import JsonReader as Rj
from PyClass import readTestSuiteDefinition as Rjdefinition
# from PyClass import raedLanguageDef as RjLanguageReader
from PyClass import getTestScriptFiles as gTscr
#endregion

#region global Var
_gcmbPaddy=10
_BtnWidth=8
_row_num=0
_TestType=""
_Version=""
_generaldate=any
_showRDBtn:bool
_ShowRetryFailuresbtn:bool
_SelectModuleType:bool
_SelectRobotType:bool
_ReadCameraOTP:bool
_ReadTLVSN:bool
_ReadSOMSN:bool
_RetrieveHousingSN:bool
_Language:str
_Tests:any
_Eta:int=0
# global _CamerOTP
_lay=[]
#endregion


#region Read setting Json
data=Rj.ReadJson('DataFiles\Setting.json')
_generaldate=data.get("General")
_TestType=_generaldate.get("Tester Type")
_Version=_generaldate.get("Version")
_showRDBtn=1 if _generaldate.get("Show R&D button")=="yes"  else 0
_ShowRetryFailuresbtn=1 if _generaldate.get("Show Retry Failures button")=="yes" else 0
_Language=_generaldate.get("Language")
#endregion

#region Languege Json
# definitionData=RjLanguageReader.JsonDefinitionLanguage.ReadJsonLanguage('Lang\Language_definitions.json',_Language)
#endregion

#region Read SuiteDefinition Json


definitionData=Rjdefinition.JsonDefinitionReader.ReadJsonDefinition('DataFiles\Test_Suite_definition.json',_TestType)
_SelectModuleType=1 if definitionData.get("Select Module Type")=="yes" else 0
_SelectRobotType=1 if definitionData.get("Select Robot Type")=="yes" else 0
_ReadCameraOTP=1 if definitionData.get("Read Camera OTP")=="yes" else 0
_ReadTLVSN=1 if definitionData.get("Read TLV SN")=="yes" else 0
_RetrieveHousingSN=1 if definitionData.get("Retrieve Housing SN")=="yes" else 0
_ReadSOMSN=1 if definitionData.get("Read SOM SN")=="yes" else 0
_Tests=definitionData.get("Tests")
#endregion
#region get test python script from Test_definition.json
scriptDataSrc=gTscr.JsonGetTestScriptFiles.ReadTestScriptFiles('DataFiles\Test_definition.json',_Tests)
#endregion
#region CalcTime
for t in _Tests:
  _Eta=_Eta+int(t)
#endregion

#region Creating tkinter main window
mw = tk.Tk()
if(_TestType=="Housing Tests"):
	mw.geometry('400x400')
else:
	mw.geometry('400x260')
mw.title('R-Go ' + _TestType+ ' ' + _Version)

#To Do Add R-go icon
# mw.iconbitmap('Rgo.icon')

mw.resizable(0, 0) #Don't allow resizing in the x or y direction



#endregion

#region Site
ttk.Label(mw, text = "Site:",anchor='w',justify='left',
		font = ("Times New Roman", 10)).grid(sticky = 'W',column = 0,
		row = _row_num, padx = 10, pady = _gcmbPaddy)
SiteCmb = tk.StringVar()
st = ttk.Combobox(mw, width = 27,textvariable = SiteCmb)
st['values'] = ('Hausvarna','Haifa','Holon')
st.grid(column = 1, row = _row_num)
_row_num=_row_num+1
#endregion Site

#region Station
StationCmb = tk.StringVar()
stn = ttk.Combobox(mw, width = 27,textvariable = StationCmb)
stn['values'] = ('1','2','3')
stn.grid(column = 1, row = _row_num)

ttk.Label(mw, text = "station :",justify='left',
		font = ("Times New Roman", 10)).grid(sticky = 'W',column = 0,
		row = _row_num, padx = 10, pady = _gcmbPaddy)

_row_num=_row_num+1
#endregion

#region ModuleType
if(_SelectModuleType):
	ttk.Label(mw, text = "Module Type :",
		font = ("Times New Roman", 10)).grid(sticky = 'W',column = 0,
		row = _row_num, padx = 10, pady = _gcmbPaddy)

	ModuleTypeCmb = tk.StringVar()
	module = ttk.Combobox(mw, width = 27,textvariable = ModuleTypeCmb)
	module['values'] = ('1','2','3')
	module.grid(column = 1, row = _row_num)
	module.current(1)
	_row_num=_row_num+1
#endregion

#region Compute Type
if(_TestType=="Housing Tests"):
	ttk.Label(mw, text = "Compute Type :",justify='left',
			font = ("Times New Roman", 10)).grid(sticky = 'W',column = 0,
			row = _row_num, padx = 10, pady = _gcmbPaddy)

	ComputeTypeCmb = tk.StringVar()
	ComputeType = ttk.Combobox(mw, width = 27,textvariable = ComputeTypeCmb)
	ComputeType['values'] = ('1','2','3')
	ComputeType.grid(column = 1, row = _row_num)
	_row_num=_row_num+1
#endregion

#region Housing
if(_RetrieveHousingSN):

	ttk.Label(mw, text = "Housing S/N :",justify='left',
		font = ("Times New Roman", 10)).grid(sticky = 'W',column = 0,
		row = _row_num, padx = 10, pady = _gcmbPaddy)

	txtHousting = tk.Label(mw, anchor='w',justify='left',borderwidth=2, relief="groove",width = 27,
		font = ("Times New Roman", 10))
	txtHousting.grid(row=_row_num, column=1,padx=10, pady=_gcmbPaddy)

	btnBarcode = tk.Button(mw, text='Barcode', command=lambda: Button_Clicker(1),bg='blue', fg='white',width=_BtnWidth).grid(column = 2, row =_row_num)
	_row_num=_row_num+1
#endregion

#region TLV SN
if(_ReadTLVSN):
	ttk.Label(mw, text = "TLV S/N :",justify='left',
		font = ("Times New Roman", 10)).grid(sticky = 'W',column = 0,
		row = _row_num, padx = 10, pady = _gcmbPaddy)
	txtTlvSn = tk.Label(mw, anchor='w',justify='left',borderwidth=2, relief="groove",width = 27,
		font = ("Times New Roman", 10))
	txtTlvSn.grid(row=_row_num, column=1,padx=10, pady=_gcmbPaddy)
	btnReadTlvSn = tk.Button(mw, text='Read', command=lambda: Button_Clicker(1),bg='blue', fg='white',width=_BtnWidth).grid(column = 2, row = _row_num)
	_row_num=_row_num+1
#endregion

#region SOM S/N
if(_ReadSOMSN):
	txtSomsn = tk.Label(mw, anchor='w',justify='left',borderwidth=2, relief="groove",width = 27,
		font = ("Times New Roman", 10))
	txtSomsn.grid(row=_row_num, column=1,padx=10, pady=_gcmbPaddy)
	ttk.Label(mw, text = "SOM S/N:",justify='left',
		font = ("Times New Roman", 10)).grid(sticky = 'W',column = 0,
		row = _row_num, padx = 10, pady = _gcmbPaddy)
	btnReadSomSn = tk.Button(mw, text='Read', command=lambda: Button_Clicker(1),bg='blue', fg='white',width=_BtnWidth).grid(column = 2, row = _row_num)
	_row_num=_row_num+1
#endregion

#region CameraOTP
ttk.Label(mw, text = "Camera Opt :",justify='left',
		font = ("Times New Roman", 10)).grid(sticky = 'W',column = 0,
		row = _row_num, padx = 10, pady = _gcmbPaddy)
btnReadCamOtp = tk.Button(mw, text='Read', command=lambda: Button_Clicker(1),bg='blue', fg='white',width=_BtnWidth).grid(column = 2, row = _row_num)

txtCameraOpt = tk.Label(mw, anchor='w',justify='left',borderwidth=2, relief="groove",width = 27,
		font = ("Times New Roman", 10))
txtCameraOpt.grid(row=_row_num, column=1,padx=10, pady=_gcmbPaddy)
_row_num=_row_num+1
#endregion

#region fuction

def StartTesting():
	top = tk.Toplevel()
	_lay.append(top)

	top.title("Calibration in progress...")
	
	top.geometry('320x300')
	
	Headerlbl=ttk.Label(top, text = "Calibration in progress...",anchor='w',justify='left',
		font = ("Times New Roman", 20)).grid(sticky = 'W',column = 0,
		row = 0, padx = 10, pady = _gcmbPaddy,columnspan=2)
	
	CameraOTPlbl=ttk.Label(top, text = "Camera OTP :"+_CameraOTP,anchor='w',justify='left',
		font = ("Times New Roman", 15)).grid(sticky = 'W',column = 0,
		row = 1, padx = 10, pady = _gcmbPaddy,columnspan=2)
	
	progress = ttk.Progressbar(top, orient = tk.HORIZONTAL,
			length = 300, mode = 'determinate')
	progress.grid(column = 0,
			row = 2, padx = 10, pady = 10,columnspan=2)

	ETAlbl=ttk.Label(top, text = "ETA",justify='center',
		font = ("Times New Roman", 20))

	ETAlbl.grid(sticky = 'W',column = 0,
		row = 3, padx = 10, pady = _gcmbPaddy,columnspan=2)
	
	btn = tk.Button(top,text='Cancel',command=exit_btn,bg='red', fg='white',width = 8,anchor="c")
	btn.grid(row = 4,column = 0, sticky="nsew",padx = 10)
	btn2 = tk.Button(top,text='Done',command=lambda:bar(top,progress),bg='green', fg='white',width = 8,anchor="c")
	btn2.grid(row = 4,column = 1,sticky="nsew",padx = 10)
	
	mw.withdraw()
#region progress
def bar(top,progress):
		import time
		exec(open('CallibrationFile\Acc_Calibration.py'))
		progress['value'] = 20
		top.update_idletasks()
		time.sleep(1)

		progress['value'] = 40
		top.update_idletasks()
		time.sleep(1)

		progress['value'] = 50
		top.update_idletasks()
		time.sleep(1)

		progress['value'] = 60
		top.update_idletasks()
		time.sleep(1)

		progress['value'] = 80
		top.update_idletasks()
		time.sleep(1)
		progress['value'] = 100
		# progress.pack()
#endregion

#region close calibration progress
def exit_btn():
    top = _lay[0]
    top.destroy()
    _lay.pop(0)
    #remove the other window entirely
    #make root visible again
    mw.iconify()
    mw.deiconify()
#endregion

def Button_Clicker(newnum):
	global _CameraOTP	
	txtCameraOpt.config(text="changed text!")	
	_CameraOTP='1234'


#endregion

#region button opperation
if(_showRDBtn):
	btnRDOnly = tk.Button(mw, text='R & D Only', command=lambda: Button_Clicker(1),bg='#009999', fg='white',width=_BtnWidth).grid(column = 0, row = _row_num)

btnTestStart = tk.Button(mw, text='Calibrate', command=lambda: StartTesting(),bg='green', fg='white',width = 15).grid(row=_row_num, column=1, columnspan=2)

_row_num=_row_num+1
#endregion

# Shows default value
st.current(1)
stn.current(1)




mw.mainloop()
