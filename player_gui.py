from tkinter import *

def player():
    a=Tk()
    a.config(bg='black')

    l=Label(a,text='Song list',fg='black',height=10,width=15)
    c1 = Button(a, text="pause", font='Courier 12 bold', bg='black', fg='deep pink', width=10)
    c2 = Button(a, text='play', font='Courier 12 bold', bg='black', fg='deep sky blue', width=10)
    c3 = Button(a, text="stop", font='Courier 12 bold', bg='black', fg='palevioletred2', width=10)
    c4 = Button(a, text="back", font='Courier 12 bold', bg='black', fg='indianred1', width=10)
    c5 = Button(a, text="next", font='Courier 12 bold', bg='black', fg='green', width=10)
    c6 = Button(a, text="prev", font='Courier 12 bold', bg='black', fg='yellow', width=10)
    c2.grid(row=3,column=1)
    c2.bind('<Button-1>')
    c1.grid(row=3,column=0)
    c1.bind('<Button-1>')
    c3.grid(row=3,column=2)
    c3.bind('<Button-1>')
    c4.grid(row=0,column=0)
    c4.bind('<Button-1>')
    l.grid(row=1,column=1)
    c5.grid(row=4,column=2)
    c5.bind('<Button-1>')
    c6.grid(row=4,column=0)
    a.mainloop()

player()