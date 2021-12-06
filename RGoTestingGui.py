#region Using
from os import truncate
import time
import runpy
import threading
import tkinter as tk
import importlib
import importlib.util
import queue
from tkinter import IntVar, ttk
# from PIL import ImageTk,Image
from PyClass import readJson as Rj
from PyClass import readTestSuiteDefinition as Rjdefinition
from PyClass import raedLanguageDef as RjLanguageReader
from PyClass import getTestScriptFiles as gTscr
#endregion

#region global Var
_gcmbPaddy=10
_PadX=5
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
_BigFontSize:int=0
_SmallFontSize:int=0
# global _CamerOTP
_lay=[]
_scriptDataSrc=[]
_scriptRunTime=[]
_RetryOnFailyre:bool
_RandDTestDict=[]
_LangdefinitionDataDic:any
_BigFontSizeFamily:str=""
_SmallFontFamily:str=""
#for r & D only tests if the user select the option to create on the fly R&D check
_RAndDOnlyFlagTest:bool
_chkBoxvar = dict()
_lblWidth:int=15
_cmbWidth:int=25
#endregion



#region Read setting Json
data=Rj.JsonReader.ReadJson('DataFiles\Setting.json')
_generaldate=data.get("General")
_TestType=_generaldate.get("Tester Type")
_Version=_generaldate.get("Version")
_showRDBtn=1 if _generaldate.get("Show R&D button")=="yes"  else 0
_ShowRetryFailuresbtn=1 if _generaldate.get("Show Retry Failures button")=="yes" else 0
_Language=_generaldate.get("Language")
_RetryOnFailyre=1 if(_generaldate.get("Retry On Failure"))=="Yes" else 0
_BigFontSize=int(_generaldate.get("BigFontSize"))
_SmallFontSize=int(_generaldate.get("SmallFontSize"))
_BigFontFamily=str(_generaldate.get("BigFontFamily"))
_SmallFontFamily=str(_generaldate.get("SmallFontFamily"))
#endregion

#region Languege Json
_LangdefinitionDataDic=RjLanguageReader.JsonDefinitionLanguage.ReadJsonLanguage('Lang\Language_definitions.json',_Language)
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
_scriptDataSrc=gTscr.JsonGetTestScriptFiles.ReadTestScriptFiles('DataFiles\Test_definition.json',_Tests)
#endregion
#region Calc all script Time
_scriptRunTime=gTscr.JsonGetTestScriptFiles.ReadTestScriptFilesRunTime('DataFiles\Test_definition.json',_Tests)
for t in _scriptRunTime:
	_Eta+=int(t)
#endregion

#region Creating tkinter main window
mw = tk.Tk()
if(_TestType=="Module Calibration"):
	mw.title(_LangdefinitionDataDic['Module Calibration Title'] + ' ' + _Version)
	mw.geometry('450x260')
elif _TestType=="Housing Tests":
	mw.geometry('450x450')
	mw.title(_LangdefinitionDataDic['Housing Test Title'] + ' ' + _Version)
elif _TestType=="Robot Tests":
	mw.geometry('450x400')
	mw.title(_LangdefinitionDataDic['Robot Test Title'] + ' ' + _Version)

#To Do Add R-go icon
# mw.iconbitmap('Rgo.icon')

mw.resizable(0, 0) #Don't allow resizing in the x or y direction



#endregion

#region Site

ttk.Label(mw, text = str(_LangdefinitionDataDic['Site Label']) +":",anchor='w',justify='left',
		font = (_BigFontFamily, _BigFontSize)).grid(sticky = 'W',column = 0,
		row = _row_num, padx = _PadX, pady = _gcmbPaddy)
SiteCmb = tk.StringVar()

st = ttk.Combobox(mw, width = _cmbWidth,textvariable = SiteCmb)
st['values'] = ('Hausvarna','Haifa','Holon')
st.grid(column = 1, row = _row_num,sticky = 'W')
_row_num=_row_num+1
#endregion Site

#region Station

ttk.Label(mw, text = _LangdefinitionDataDic['Station Label'],justify='left',
		font = (_BigFontFamily, _BigFontSize),width=_lblWidth).grid(sticky = 'W',column = 0,
		row = _row_num, padx = _PadX, pady = _gcmbPaddy)

StationCmb = tk.StringVar()
stn = ttk.Combobox(mw, width = _cmbWidth,textvariable = StationCmb)
stn['values'] = ('1','2','3')
stn.grid(column = 1, row = _row_num,sticky = 'W')


_row_num=_row_num+1
#endregion

#region ModuleType
if(_SelectModuleType):
	ttk.Label(mw, text = _LangdefinitionDataDic['Module Type Label'],
		font = (_BigFontFamily, _BigFontSize)).grid(sticky = 'W',column = 0,
		row = _row_num, padx = _PadX, pady = _gcmbPaddy)

	ModuleTypeCmb = tk.StringVar()
	module = ttk.Combobox(mw, width = _cmbWidth,textvariable = ModuleTypeCmb)
	module['values'] = ('5','2','3')
	module.grid(column = 1, row = _row_num,sticky = 'W')
	module.current(1)
	_row_num=_row_num+1
#endregion

#region Compute Type
if(_TestType=="Housing Tests"):
	ttk.Label(mw, text = _LangdefinitionDataDic['Compute Type'],justify='left',
			font = (_BigFontFamily, _BigFontSize)).grid(sticky = 'W',column = 0,
			row = _row_num, padx = _PadX, pady = _gcmbPaddy)

	ComputeTypeCmb = tk.StringVar()
	ComputeType = ttk.Combobox(mw, width = _cmbWidth,textvariable = ComputeTypeCmb)
	ComputeType['values'] = ('1','2','9')
	ComputeType.grid(column = 1, row = _row_num,sticky = 'W')
	_row_num=_row_num+1
#endregion

#region Housing
if(_RetrieveHousingSN):

	ttk.Label(mw, text = _LangdefinitionDataDic['Housing SN'],justify='left',
		font = (_BigFontFamily, _BigFontSize)).grid(sticky = 'W',column = 0,
		row = _row_num, padx = _PadX, pady = _gcmbPaddy)

	txtHousting = tk.Label(mw, anchor='w',justify='left',borderwidth=2, relief="groove",width = _lblWidth,
		font = (_BigFontFamily, _BigFontSize))
	txtHousting.grid(row=_row_num, column=1, pady=_gcmbPaddy,sticky = 'W')

	btnBarcode = tk.Button(mw, text=_LangdefinitionDataDic['Barcode'],justify='left', 
			command=lambda: Button_Clicker(1),bg='blue', fg='white',
			font = (_SmallFontFamily, _SmallFontSize),
			width=_BtnWidth).grid(column = 2, row =_row_num,sticky = 'W')
	_row_num=_row_num+1
#endregion

#region TLV SN
if(_ReadTLVSN):
	ttk.Label(mw, text = _LangdefinitionDataDic['TLVSN'],justify='left',
		font = (_BigFontFamily, _BigFontSize)).grid(sticky = 'W',column = 0,
		row = _row_num, padx = _PadX, pady = _gcmbPaddy)
	txtTlvSn = tk.Label(mw, anchor='w',justify='left',borderwidth=2, relief="groove",width = _lblWidth,
		font = (_BigFontFamily, _BigFontSize))
	txtTlvSn.grid(row=_row_num, column=1, pady=_gcmbPaddy)
	btnReadTlvSn = tk.Button(mw, text=_LangdefinitionDataDic['Read'], 
	font = (_SmallFontFamily, _SmallFontSize),
	command=lambda: Button_Clicker(1),bg='blue', fg='white',width=_BtnWidth).grid(column = 2, 
		row = _row_num,sticky = 'W')
	_row_num=_row_num+1
#endregion

#region SOM S/N
if(_ReadSOMSN):
	ttk.Label(mw, text = _LangdefinitionDataDic['SOMSN'],justify='left',
		font = (_BigFontFamily, _BigFontSize)).grid(sticky = 'W',column = 0,
		row = _row_num, padx = _PadX, pady = _gcmbPaddy)

	txtSomsn = tk.Label(mw, anchor='w',justify='left',borderwidth=2, relief="groove",width = _lblWidth,
		font = (_BigFontFamily, _BigFontSize))
	txtSomsn.grid(row=_row_num, column=1,padx=0, pady=_gcmbPaddy)
	
	btnReadSomSn = tk.Button(mw, text=_LangdefinitionDataDic['Read'],
	font = (_SmallFontFamily, _SmallFontSize),
	command=lambda: Button_Clicker(1),
	bg='blue', fg='white',width=_BtnWidth).grid(column = 2, row = _row_num,sticky = 'W')
	_row_num=_row_num+1
#endregion

#region Robot S/N
if (_SelectRobotType):

	tk.Label(mw, text = _LangdefinitionDataDic['RobotSN'],justify='left',
			font = (_BigFontFamily, _BigFontSize)).grid(sticky = 'W',column = 0,
			row = _row_num, padx = _PadX, pady = _gcmbPaddy)

	RobotSN = tk.StringVar()
	RobotSNCmb = ttk.Combobox(mw, width = _cmbWidth,textvariable = RobotSN)
	RobotSNCmb['values'] = ('1','2','3')
	RobotSNCmb.grid(column = 1, row = _row_num,sticky = 'W')
	_row_num=_row_num+1
#endregion

#region CameraOTP
ttk.Label(mw, text = _LangdefinitionDataDic['Camera OTP Label'],justify='left',
		font = (_BigFontFamily, _BigFontSize)).grid(sticky = 'W',column = 0,
		row = _row_num, padx = _PadX, pady = _gcmbPaddy)
		
btnReadCamOtp = tk.Button(mw, text=_LangdefinitionDataDic['Read'], 
	font = (_SmallFontFamily, _SmallFontSize),
	command=lambda: Button_Clicker(1),bg='blue', 
	fg='white',width=_BtnWidth).grid(column = 2, row = _row_num,sticky = 'W')

txtCameraOpt = tk.Label(mw, anchor='w',justify='left',borderwidth=2, relief="groove",width = _lblWidth,
		font = (_BigFontFamily, _BigFontSize))
txtCameraOpt.grid(row=_row_num, column=1,padx=0, pady=_gcmbPaddy)
_row_num=_row_num+1
#endregion

#region fuction
def RAndDOnlyTest():
	top = tk.Toplevel()
	mw.withdraw()
	_lay.append(top)

	if(_TestType=="Module Calibration"):
		top.title(_LangdefinitionDataDic['Module Calibration Title'] + ' ' + _Version)
	elif _TestType=="Housing Tests":
		top.title(_LangdefinitionDataDic['Housing Test Title'] + ' ' + _Version)
	elif _TestType=="Robot Tests":	
		top.title(_LangdefinitionDataDic['Robot Test Title'] + ' ' + _Version)
	
	#top.geometry(mw.winfo_geometry().width,660)
	top.geometry('450x660')
	
	_scriptNameAndNumber=gTscr.JsonGetTestScriptFiles.ReadDefinisionFileNameAndNumber('DataFiles\Test_definition.json')
	rowNum:int=0
	ColNum:int=0
	# var = dict()
	# count=1
	for i in _scriptNameAndNumber:
		_chkBoxvar[i]= _scriptNameAndNumber[i]
		
		if ColNum==2:
			ColNum=0
			rowNum+=1

		checkButton = tk.Checkbutton(top, text=i, variable=_chkBoxvar[i], 
                      command=lambda key=i: SelectRAndDTesting(key))    			

		checkButton.grid(sticky = 'W',column = ColNum,
					row=rowNum, padx = 10, pady = _gcmbPaddy)
		ColNum=ColNum+1
		checkButton.deselect()
		# checkButton.select()
		if _scriptNameAndNumber[i] in _Tests:
			_RandDTestDict.append(_scriptNameAndNumber[i])
			checkButton.select()
		
		# count += 1	

	btnTestStart = tk.Button(top, text=_LangdefinitionDataDic['Save'], command=lambda: SaveRAndDTesting()
	,bg='blue', fg='white',width = 15)
	btnTestStart.grid(row=rowNum+1, column=0)

	btnTestStart = tk.Button(top, text=_LangdefinitionDataDic['Cancel'], command=lambda:exit_btn()
	,bg='Red', fg='white',width = 15)
	btnTestStart.grid(row=rowNum+1, column=1)


#region craete on the fly test list for R&D Only
def SelectRAndDTesting(key):
	global _RandDTestDict
	global _RAndDOnlyFlagTest
	_RAndDOnlyFlagTest=True	
	# print(_chkBoxvar.get(key))
	if _chkBoxvar.get(key) in  _RandDTestDict:
		_RandDTestDict.remove(_chkBoxvar.get(key))
		# print(_chkBoxvar.get(key))
	else:
		_RandDTestDict.append(_chkBoxvar.get(key))
#endregion

#region Save R&D esting
def SaveRAndDTesting():
	global _Eta
	global _scriptDataSrc
	global _Tests		
	if len(_RandDTestDict)>0:	
		gTscr.JsonGetTestScriptFiles.UpdateJsonDefinitionFile('DataFiles\Test_Suite_definition.json',
		'Tests',_RandDTestDict,_TestType)
	#region get test python script from Test_definition.json
	definitionData=Rjdefinition.JsonDefinitionReader.ReadJsonDefinition('DataFiles\Test_Suite_definition.json',_TestType)
	_Tests=definitionData.get("Tests")
	_scriptDataSrc=gTscr.JsonGetTestScriptFiles.ReadTestScriptFiles('DataFiles\Test_definition.json',_Tests)
	#endregion
	#region Calc all script Time
	_scriptRunTime=gTscr.JsonGetTestScriptFiles.ReadTestScriptFilesRunTime('DataFiles\Test_definition.json',_Tests)
	_Eta=0
	for t in _scriptRunTime:
		_Eta+=int(t)
	#endregion
	exit_btn()
#endregion

def StartTesting():

	top = tk.Toplevel()
	
	_lay.append(top)
	_row_num:int=0
	rootHeight = mw.winfo_height()+20
	rootWidth = mw.winfo_width()
	mw.withdraw()
	lv_x = mw.winfo_rootx()
	lv_y = mw.winfo_rooty()
	top.geometry(str(mw.winfo_width()) +'x' + str(mw.winfo_height()+20))
	top.resizable(False, False)

	top.columnconfigure(0, weight=1)
	top.columnconfigure(1, weight=3)
	if _TestType=="Module Calibration":
		top.title(_LangdefinitionDataDic['Module Calibration Title'])
		Headerlbl=ttk.Label(top, text = _LangdefinitionDataDic['CalibreationInprogress'],
		anchor='w',justify='left',
			font = ("Times New Roman", 20))
	elif _TestType=="Housing Tests":
		top.title(_LangdefinitionDataDic['Housing Test Title'])
		Headerlbl=ttk.Label(top, text = _LangdefinitionDataDic['Testing in progress'],anchor='w',justify='left',
			font = ("Times New Roman", 20))
	elif _TestType=="Robot Tests":
		top.title(_LangdefinitionDataDic['Robot Test Title'])
		Headerlbl=ttk.Label(top, text = _LangdefinitionDataDic['Testing in progress'],anchor='w',justify='left',
			font = ("Times New Roman", 20))
	# top.geometry('320x300')

	# configure the grid
	top.columnconfigure(0, weight=1)
	top.columnconfigure(1, weight=1)
	top.columnconfigure(2, weight=1)
	top.columnconfigure(3, weight=1)

	Headerlbl.grid(sticky = 'W',column = 0,row = _row_num, padx = 10, pady = _gcmbPaddy,columnspan=4)

	_row_num+=1

	#Frame
	
	
	lf = ttk.LabelFrame(top)
	lf.grid(sticky = 'EW',column=0, row=_row_num, ipadx=10, ipady=10,columnspan=4)
	
	#end farame
	if(_RetrieveHousingSN):
		Housinglbl=ttk.Label(lf, text = _LangdefinitionDataDic['Housing SN']+":",justify='left',
			font = (_BigFontFamily, _BigFontSize))
			
		Housinglbl.grid(sticky = 'w',column = 0,
			row = _row_num, padx = 1, pady = _gcmbPaddy)		

		HousinglblData=ttk.Label(lf, text = _CameraOTP,justify='left',anchor='c',
			font = (_BigFontFamily, _BigFontSize),borderwidth=4, relief="solid")
		
		HousinglblData.grid(column = 1,
			row = _row_num, padx = 10, pady = 5,ipadx=5)
	
	if(_ReadTLVSN):
		ReadTLVSNlbl=ttk.Label(lf, text = _LangdefinitionDataDic['TLVSN'] +":",justify='left',
		font = (_BigFontFamily, _BigFontSize))

		ReadTLVSNlbl.grid(sticky = 'W',column = 2,
		row = _row_num, padx = 1, pady = _gcmbPaddy)

		ReadTLVSNlblData=ttk.Label(lf, text = _CameraOTP,justify='left',anchor='c',
		font = (_BigFontFamily, _BigFontSize),borderwidth=2, relief="solid")
		
		ReadTLVSNlblData.grid(sticky = 'W',column = 3,
		row = _row_num, padx = 0, pady = 5,ipadx=5)

		_row_num+=1

	

	if(_ReadSOMSN):
		txtSomsn = ttk.Label(lf, text = _LangdefinitionDataDic['SOMSN'] +":",anchor='w',
			justify='left',
		font = (_BigFontFamily, _BigFontSize))		
		txtSomsn.grid(sticky = 'W',row=_row_num, column=2,padx=0, pady=5)

		txtSomsnData = ttk.Label(lf, text = _CameraOTP,anchor='c',
			justify='left',
		font = (_BigFontFamily, _BigFontSize),borderwidth=2, relief="solid")	

		txtSomsnData.grid(sticky = 'W',row=_row_num, column=3,padx=0, pady=5,ipadx=5)

	CameraOTPlbl=ttk.Label(lf, text = _LangdefinitionDataDic['Camera OTP Label'] +":"
	,anchor='c',justify='left',
		font = (_BigFontFamily, _BigFontSize))

	CameraOTPlbl.grid(sticky = 'W',column = 0,
		row = _row_num, padx = 0, pady = 0)

	CameraOTPlblData=ttk.Label(lf, text = _CameraOTP 
	,anchor='c',justify='left',
		font = (_BigFontFamily, _BigFontSize),borderwidth=2, relief="solid")

	CameraOTPlblData.grid(sticky = 'W',column = 1,
		row = _row_num, padx = 10, pady = 0,ipadx=5)



	_row_num+=1
	

	#region progress bar Style
	style = ttk.Style(top)
	style.layout('text.Horizontal.TProgressbar',
             [('Horizontal.Progressbar.trough',
               {'children': [('Horizontal.Progressbar.pbar',
                              {'side': 'left', 'sticky': 'ns'})],
                'sticky': 'nswe'}),
              ('Horizontal.Progressbar.label', {'sticky': ''})])
	style.configure('text.Horizontal.TProgressbar', text='0 %')
	#endregion progress bar Style
	
	progress = ttk.Progressbar(top, style='text.Horizontal.TProgressbar', length=400,
                               maximum=_Eta, value=0)

	progress.grid(column = 0,row = _row_num, padx = 10, pady = 10,columnspan=4)						   

	_row_num+=1

	ETAlbl=ttk.Label(top, text =_LangdefinitionDataDic['ETA'] + ":",justify='center',
		font = (_BigFontFamily, _BigFontSize))	

	ETAlbl.grid(sticky = 'EW',column = 2,
		row = _row_num, padx = 0, pady = 0)
	
	ElapsetTimelbl=ttk.Label(top, text = str(_Eta)  ,anchor='w',justify='left',
		font = (_BigFontFamily, _BigFontSize))
	ElapsetTimelbl.grid(sticky = 'EW',column = 3,
		row = _row_num, padx = 0, pady = 0)
	
	_row_num+=1

	ETAlblMinSecWarning=ttk.Label(top, text = "",justify='center',
	font = (_BigFontFamily, _BigFontSize),wraplength=400)

	ETAlblMinSecWarning.grid(sticky = 'EW',column = 0,
	row = _row_num, padx = 10, pady = _gcmbPaddy,columnspan=4)

	_row_num+=1

	btnCancel = tk.Button(top,text =_LangdefinitionDataDic['Cancel'],command=exit_btn,bg='red', 
			fg='white',anchor="c",width = 10,height=1,font = (_BigFontFamily, _BigFontSize))

	btnCancel.grid(row = _row_num,column = 0, padx = 10,columnspan=2,sticky = 'W')

	btnDone = tk.Button(top,text = _LangdefinitionDataDic['Done'],bg='gray', fg='white',
		anchor="c",command=exit_btn,state='disabled',
		width = 10,height=1,font = (_BigFontFamily, _BigFontSize))

	btnDone.grid(row = _row_num,column = 2,padx = 10,columnspan=2,sticky = 'E')

	th = threading.Thread(target=bar, args=(top,progress,ElapsetTimelbl,style,Headerlbl,ETAlbl,btnDone,
	ETAlblMinSecWarning,btnCancel))
	th.start()
	#bar(top,progress)

#region progress
def bar(top,progress,ElapsetTimelbl,style,Headerlbl,ETAlbl,
		btn2,ETAlblMinSecWarning,btn):
	# import queue
	global _Eta
	TestPass:bool=True
	PopFlag:bool=True
	dotindex:int=0
	runthreads = []	
	elapsedTime=0
	inetvalPB=_Eta		
	TestIndex=0	
	#region Run all Test Scripts
	for script in _scriptDataSrc:
		if PopFlag==True:
			PopFlag=False				
			specName =script.split('.')
			print(script)		
			#region load class Dynamic by Reflection
			test_spec = importlib.util.spec_from_file_location(specName[0], 'CallibrationTestScriptFile\\' + script)
			test_module = importlib.util.module_from_spec(test_spec)		
			test_spec.loader.exec_module(test_module)
			print(test_module.RetVal)
			#create instance of the class
			ScriptClass = test_module.Test()		
			#endregion		
			#region Thread run
			sThrd = threading.Thread(target=ScriptClass.RunTest)	
			sThrd.start()		
			runthreads.append(sThrd)
			#endregion
			CurrentTestTime=0
			StartEtaTime=elapsedTime
			StartinetvalPB=inetvalPB
			# print(str(_scriptRunTime[TestIndex]))
		#region Thread Loop 
		while len(runthreads) >0:	
			CurrentTestTime+=1		
			elapsedTime=elapsedTime+1
			inetvalPB=inetvalPB-1
			#print(str(CurrentTestTime))			
			if(CurrentTestTime<=_scriptRunTime[TestIndex]):
				newTime=str(int(inetvalPB/60))+ " " + _LangdefinitionDataDic['MinuteLabel'] +" :"
				# 'calc time str'
				if (int((inetvalPB%60)))>0:
					newTime+=str((int((inetvalPB%60)))) + " " + _LangdefinitionDataDic['SecondsLabel']			  
				else:
					newTime+="0" + str((int((inetvalPB%60))))

				if inetvalPB>59:
					ElapsetTimelbl['text'] =str(newTime)
					# ElapsetTimelbl['text'] =str(inetvalPB) + 'sec or '  + str(int(inetvalPB/60)) + ' Minutes'
				else:
					if inetvalPB>0:
						ElapsetTimelbl['text'] = str(inetvalPB) + " " + _LangdefinitionDataDic['SecondsLabel']
				if(elapsedTime<=_Eta-2):
					percentage = round(elapsedTime/_Eta * 100)  # Calculate percentage.
					progress.config(value=elapsedTime)
					style.configure('text.Horizontal.TProgressbar', text='{:g} %'.format(percentage))
					# print(str(elapsedTime))
				else:
					progress.config(value=100)
					style.configure('text.Horizontal.TProgressbar', text='{:g} %'.format(100))	
				
			else:#'test time taking longer than expected'				
				if(dotindex==0):
					ETAlblMinSecWarning.config(text=_LangdefinitionDataDic['LongTetsTime'],foreground='red')
					dotindex+=1
				else:
					ETAlblMinSecWarning.config(text=ETAlblMinSecWarning["text"]+'.')					
					if(dotindex>3):
						dotindex=0
					else:
						dotindex+=1
					
			time.sleep(1)
			for thread in runthreads:
				if not thread.is_alive():				
					runthreads.pop(0)
					PopFlag=True
			#endregion
		if(test_module.RetVal!='Pass'):
			TestPass=False			
			if(_RetryOnFailyre==False):
				break
		else:
			gTscr.JsonGetTestScriptFiles.UpdateJsonDefinitionSuccessTime('DataFiles\Test_definition.json',
				CurrentTestTime,script)
			
		print(test_module.RetVal)				
		#in case that the test take longer from that expected
		#or case that the test was  shorter from that expected
		if(CurrentTestTime>_scriptRunTime[TestIndex] or 
			CurrentTestTime<_scriptRunTime[TestIndex]):
			dotindex=0
			ETAlblMinSecWarning.config(text='')
			elapsedTime=StartEtaTime+int(_scriptRunTime[TestIndex])
			inetvalPB=StartinetvalPB-int(_scriptRunTime[TestIndex])
		TestIndex=TestIndex+1
	#endregion
	if(TestPass):
		ElapsetTimelbl.config(text=_LangdefinitionDataDic['Pass'],foreground='green')
	else:
		ElapsetTimelbl.config(text=_LangdefinitionDataDic['Fail'],foreground='red')
	ETAlbl.config(text=_LangdefinitionDataDic['Result'])
	Headerlbl.config(text=_LangdefinitionDataDic['Calibration completed'])
	btn2.config(state='normal',bg='green')
	btn.config(state='disabled',bg='gray')
#endregion
#region run Py test Script
def RunTestScript(path_name:str):
	runpy.run_path(path_name=path_name)#'CallibrationTestScriptFile\Acc_Calibration.py'
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
	btnRDOnly = tk.Button(mw, 
	command=lambda: RAndDOnlyTest(),bg='#009999',
	 fg='white',width = 10,height=1,font = (_BigFontFamily, _BigFontSize))
	btnRDOnly.grid(column = 0, row = _row_num,sticky = 'W',padx=10)
	btnRDOnly.config(text=_LangdefinitionDataDic['RAndDOnly'])
	


btnTestStart = tk.Button(mw, text=_LangdefinitionDataDic['Calibrate'], 
 command=lambda: StartTesting(),bg='green',
 fg='white',width = 12,height=1,font = (_BigFontFamily, _BigFontSize)).grid(row=_row_num, column=1, 
 	columnspan=2,sticky = 'SE')

_row_num=_row_num+1
#endregion

# Shows default value
st.current(1)
stn.current(1)




mw.mainloop()
