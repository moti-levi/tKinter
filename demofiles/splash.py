from tkinter import *


def show_splash():
    splash = Toplevel()
    splash.geometry('500x300')
    splash.overrideredirect(True) # To disable the default Window decoration
    splash.after(2000, splash.destroy) # This window destroys after being on screen for 5 seconds
    splash.wait_window()

root = Tk()
root.withdraw()
show_splash()
root.deiconify()
root.mainloop()