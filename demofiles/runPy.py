import runpy
# Python 3.x code
# Imports
import tkinter
from tkinter import messagebox

root = tkinter.Tk()
root.withdraw()

# Message Box

runpy.run_path(path_name='CallibrationTestScriptFile\Acc_Calibration.py')
runpy.run_path(path_name='CallibrationTestScriptFile\Test_CANbus_comm.py')


messagebox.showinfo("Title", "Done")


# #region runScripts
# def runScript(_scriptDataSrc,ElapsetTimelbl):
# 	runpy.run_path(path_name='CallibrationTestScriptFile\Acc_Calibration.py')
# 	ElapsetTimelbl.config(text="5")
# 	runpy.run_path(path_name='CallibrationTestScriptFile\Test_CANbus_comm.py')
# 	ElapsetTimelbl.config(text="10")
# #endregion
