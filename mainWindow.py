import tkinter as tk

def startgame():
    pass

mw = tk.Tk()              #Here I tried (1)
mw.title('The game')

back = tk.Frame(master=mw, width=500, height=500, bg='black')
back.pack()

go = tk.Button(master=back, text='Start Game', bg='black', fg='red',
                     command=lambda:startgame()).pack()
close = tk.Button(master=back, text='Quit', bg='black', fg='red',
                     command=lambda:quit()).pack()
info = tk.Label(master=back, text='Made by me!', bg='red',
                         fg='black').pack()

mw.mainloop()