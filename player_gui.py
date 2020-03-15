from tkinter import *

def player():
    a=Tk()
    a.title("                             MUSIC PLAYER")
    a.geometry('428x446')
    r = PhotoImage(file=r"C:\Users\Samiksha\PycharmProjects\dem\n1.png")
    l1 = Label(a, image=r)
    l1.place(x=0, y=0)
    l=Label(a,text='Song list',fg='black',bg='black',height=15,width=35)
    c1 = Button(a, text="pause", font='Courier 16 bold', bg='white', fg='red', width=8, bd=1, relief='ridge',
                height=2)
    c2 = Button(a, text="play", font='Courier 16 bold', bg='white', fg='palevioletred2', width=8, bd=1,
                relief='ridge',height=2)
    c3 = Button(a, text="stop", font='Courier 16 bold', bg='white', fg='green', width=8, bd=1, relief='ridge',
                height=2)
    c4 = Button(a, text="previous", font='Courier 16 bold', bg='white', fg='deep sky blue2', width=8, bd=1,
                relief='ridge',height=2)
    c5 = Button(a, text="Back", font='Courier 12 bold', bg='white', fg='deep pink', width=6,
                bd=1,relief='ridge', height=1)
    c6 = Button(a, text="next", font='Courier 16 bold', bg='white', fg='deep sky blue2', width=8, bd=1,
                relief='ridge', height=2)

    l.place(x=35,y=53)
    c5.place(x=10, y=10)
    c1.place(x=170, y=300)
    c2.place(x=50, y=300)
    c3.place(x=130, y=370)
    c4.place(x=10, y=370)
    c6.place(x=250, y=370)
    c2.bind('<Button-1>')
    c1.bind('<Button-1>')
    c3.bind('<Button-1>')
    c4.bind('<Button-1>')
    c5.bind('<Button-1>')
    a.mainloop()

player()

