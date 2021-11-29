# import tkinter as tk

# root = tk.Tk()

# #In order to hide main window
# root.withdraw()

# tk.Label(root, text="Main Window").pack()

# aWindow = tk.Toplevel(root)

# def change_window():
#     #remove the other window entirely
#     aWindow.destroy()

#     #make root visible again
#     root.iconify()
#     root.deiconify()


# tk.Button(aWindow, text="This is aWindow", command=change_window).pack()

# root.mainloop()

from tkinter import *

class TestApp:
    def __init__(self, master):
        self.master = master
        master.minsize(width=800, height=640)

        self.button = Button(master, text='Next', command=self.firstWindow)
        self.button.pack()

    def firstWindow(self):
        self.master.withdraw()
        self.newfirstWindow = Toplevel(self.master)
        self.newfirstWindow.minsize(width=800, height=640)

        self.button = Button(self.newfirstWindow, text='Next', command=self.secondWindow)
        self.button.pack()

    def secondWindow(self):
        self.newfirstWindow.destroy()
        self.newsecondWindow = Toplevel(self.master)
        self.newsecondWindow.minsize(width=800, height=640)

        self.button = Button(self.newsecondWindow, text='Quit', command=self.master.quit())
        self.button.pack()





if __name__ == "__main__":
    master = Tk()
    App = TestApp(master)
    master.mainloop()




