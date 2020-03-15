from tkinter import *


class main:
    def __init__(self):
        self.fpage()

    def art_list(self):
        t.destroy()
        global a
        a = Tk()
        a.title("                             MUSIC PLAYER")
        a.geometry('428x446')
        r = PhotoImage(file=r"C:\Users\Samiksha\PycharmProjects\dem\n1.png")
        l = Label(a, image=r)
        l.place(x=0, y=0)
        e = Entry(a, width=50)
        a.resizable(False, False)

        c1 = Button(a, text="ARIJIT SINGH", font='Courier 16 bold', bg='white', fg='red', width=17,bd=1,relief='ridge',
                   height=2)
        c2 = Button(a, text="SONU NIGAM", font='Courier 16 bold', bg='white', fg='palevioletred2', width=17,bd=1,relief='ridge',
                     height=2)
        c3 = Button(a, text="ARMAAN MALIK", font='Courier 16 bold', bg='white', fg='green', width=17,bd=1,relief='ridge',
                  height=2)
        c4 = Button(a, text="SHREYA GHOSHAL", font='Courier 16 bold', bg='white', fg='deep sky blue2', width=17,bd=1,relief='ridge',
                     height=2)
        c5 = Button(a, text="Back", font='Courier 12 bold', bg='white', fg='deep pink',command=self.go_back,width=12,bd=1,
                     relief='ridge',height=1)
        c5.place(x=10,y=10)
        e.place(x=10,y=60)
        c1.place(x=10,y=110)
        c2.place(x=10,y=190)
        c3.place(x=10,y=270)
        c4.place(x=10,y=360)


        a.mainloop()

    def song_list(self):
        t.destroy()
        global a
        a = Tk()
        a.title("                             MUSIC PLAYER")
        a.geometry('428x446')
        r = PhotoImage(file=r"C:\Users\Samiksha\PycharmProjects\dem\n1.png")
        l = Label(a, image=r)
        l.place(x=0, y=0)
        e = Entry(a, width=50)
        a.resizable(False, False)

        c1 = Button(a, text="BOLLYWOOD", font='Courier 16 bold', bg='white', fg='red', width=17,bd=1,relief='ridge',
                   height=2)
        c2 = Button(a, text="ENGLISH", font='Courier 16 bold', bg='white', fg='palevioletred2', width=17,bd=1,relief='ridge',
                     height=2)
        c3 = Button(a, text="PUNJABI", font='Courier 16 bold', bg='white', fg='green', width=17,bd=1,relief='ridge',
                  height=2)
        c4 = Button(a, text="SPANISH", font='Courier 16 bold', bg='white', fg='deep sky blue2', width=17,bd=1,relief='ridge',
                     height=2)
        c5 = Button(a, text="Back", font='Courier 12 bold', bg='white', fg='deep pink',command=self.go_back,width=12,bd=1,
                     relief='ridge',height=1)
        c5.place(x=10,y=10)
        e.place(x=10,y=60)
        c1.place(x=10,y=110)
        c2.place(x=10,y=190)
        c3.place(x=10,y=270)
        c4.place(x=10,y=360)

        a.mainloop()

    def alb_list(self):
        t.destroy()
        global a
        a = Tk()
        a.title("                             MUSIC PLAYER")
        a.geometry('428x446')
        r = PhotoImage(file=r"C:\Users\Samiksha\PycharmProjects\dem\n1.png")
        l = Label(a, image=r)
        l.place(x=0, y=0)
        e = Entry(a, width=50)
        a.resizable(False, False)

        c1 = Button(a, text="YJHD", font='Courier 16 bold', bg='white', fg='red', width=17,bd=1,relief='ridge',
                   height=2)
        c2 = Button(a, text="AASHIQI 2", font='Courier 16 bold', bg='white', fg='deep sky blue2', width=17,bd=1,relief='ridge',
                     height=2)
        c3 = Button(a, text="SOTY", font='Courier 16 bold', bg='white', fg='orchid3', width=17,bd=1,relief='ridge',
                  height=2)
        c4 = Button(a, text="ROCKSTAR", font='Courier 16 bold', bg='white', fg='palevioletred3', width=17,bd=1,relief='ridge',
                     height=2)
        c5 = Button(a, text="Back", font='Courier 12 bold', bg='white', fg='deep pink',command=self.go_back,width=12,bd=1,
                     relief='ridge',height=1)
        c5.place(x=10,y=10)
        e.place(x=10,y=60)
        c1.place(x=10,y=110)
        c2.place(x=10,y=190)
        c3.place(x=10,y=270)
        c4.place(x=10,y=360)

        a.mainloop()


    def mood_list(self):
        t.destroy()
        global a
        a = Tk()
        a.title("                             MUSIC PLAYER")
        a.geometry('428x446')
        r = PhotoImage(file=r"C:\Users\Samiksha\PycharmProjects\dem\n1.png")
        l = Label(a, image=r)
        l.place(x=0, y=0)
        e = Entry(a, width=50)
        a.resizable(False, False)

        c1 = Button(a, text="HAPPY", font='Courier 16 bold', bg='white', fg='red2', width=17,bd=1,relief='ridge',
                   height=2)
        c2 = Button(a, text="SAD", font='Courier 16 bold', bg='white', fg='palevioletred2', width=17,bd=1,relief='ridge',
                     height=2)
        c3 = Button(a, text="ROMANTIC", font='Courier 16 bold', bg='white', fg='deep sky blue2', width=17,bd=1,relief='ridge',
                  height=2)
        c4 = Button(a, text="LONG DRIVE", font='Courier 16 bold', bg='white', fg='coral', width=17,bd=1,relief='ridge',
                     height=2)
        c5 = Button(a, text="Back", font='Courier 12 bold', bg='white', fg='deep pink',command=self.go_back,width=12,bd=1,
                     relief='ridge',height=1)
        c6 = Button(a, text="PARTY", font='Courier 16 bold', bg='white', fg='indianred2', width=17,bd=1,relief='ridge',
                     height=2)
        c5.place(x=10,y=10)
        e.place(x=10,y=60)
        c1.place(x=10,y=90)
        c2.place(x=10,y=160)
        c3.place(x=10,y=230)
        c4.place(x=10,y=300)
        c6.place(x=10,y=370)

        a.mainloop()

    def go_back(self):
        a.destroy()
        self.fpage()

    def fpage(self):
        global t
        t = Tk()
        t.title("                             MUSIC PLAYER")
        t.geometry('428x446')
        a = PhotoImage(file=r"C:\Users\Samiksha\PycharmProjects\dem\n1.png")
        l=Label(t,image=a)
        l.place(x=0,y=0)

        t.resizable(False, False)
        b1 = Button(t, text="ALBUM", font='Courier 22 bold', bg='white',fg='pale violet red', width=7,bd=1,relief='ridge',
                    height=5,command=self.alb_list)
        b2 = Button(t, text="SONG", font='Courier 22 bold', bg='white', fg='steelblue4',width=7, height=5,bd=1,relief='ridge',
                    command=self.song_list)
        b3 = Button(t, text="MOOD", font='Courier 22 bold', bg='white', fg='sky blue2', width=7, height=5,bd=1,relief='ridge',
                    command=self.mood_list)
        b4 = Button(t, text="ARTIST", font='Courier 22 bold', bg='white', fg='indian red2', width=7, height=5,bd=1,relief='ridge',
                    command=self.art_list)

        b1.place(x=10,y=10)
        b2.place(x=150,y=10)
        b4.place(x=10,y=230)
        b3.place(x=150,y=230)

        t.mainloop()


o = main()
