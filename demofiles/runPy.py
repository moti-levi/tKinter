import runpy
# Python 3.x code
# Imports
import tkinter
from tkinter import messagebox

root = tkinter.Tk()
root.withdraw()

# Message Box

runpy.run_path(path_name='CallibrationFile\Acc_Calibration.py')
runpy.run_path(path_name='CallibrationFile\Test_CANbus_comm.py')


messagebox.showinfo("Title", "Done")
