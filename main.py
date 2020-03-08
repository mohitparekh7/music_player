from tkinter import *
class main:
    def __init__(self):
        self.fpage()

    def art_list(self):
        print("artist")
        t.destroy()
        global a
        a = Tk()
        e = Entry(a)
        e.pack(side=TOP)
        f1 = Frame(a)
        f1.pack(side=LEFT)
        f2 = Frame(a)
        f2.pack(side=RIGHT)
        c1 = Button(f1, text="Arijit Singh", fg='red', width=12)
        c2 = Button(f2, text="Sonu Nigam", fg='black', width=12)
        c3 = Button(f1, text="Armaan Malik", fg='green', width=12)
        c4 = Button(f2, text="Shreya Ghoshal", fg='blue', width=12)
        c5 = Button(f2, text="<-", fg='black', width=12,command = self.go_back)
        c5.pack()
        c1.pack(side=TOP)
        c2.pack(side=TOP)
        c3.pack(side=BOTTOM)
        c4.pack(side=BOTTOM)


    def song_list(self):
        print("song")
        t.destroy()
        a = Tk()
        e = Entry(a)
        e.pack(side=TOP)
        f1 = Frame(a)
        f1.pack(side=LEFT)
        f2 = Frame(a)
        f2.pack(side=RIGHT)
        c1 = Button(f1, text="Hindi Bollywood", fg='red', width=12)
        c2 = Button(f2, text="English", fg='black', width=12)
        c3 = Button(f1, text="Punjabi", fg='green', width=12)
        c4 = Button(f2, text="Spanish", fg='blue', width=12)
        c1.pack(side=TOP)
        c2.pack(side=TOP)
        c3.pack(side=BOTTOM)
        c4.pack(side=BOTTOM)


    def alb_list(self):
        print("album")
        t.destroy()
        a = Tk()
        e = Entry(a)
        e.pack(side=TOP)
        f1 = Frame(a)
        f1.pack(side=LEFT)
        f2 = Frame(a)
        f2.pack(side=RIGHT)
        c1 = Button(f1, text="Purpose", fg='red', width=12)
        c2 = Button(f2, text="Believe", fg='black', width=12)
        c3 = Button(f1, text="Divide", fg='green', width=12)
        c4 = Button(f2, text="Illuminate", fg='blue', width=12)
        c1.pack(side=TOP)
        c2.pack(side=TOP)
        c3.pack(side=BOTTOM)
        c4.pack(side=BOTTOM)


    def mood_list(self):
        print("mood")
        t.destroy()
        a = Tk()
        e = Entry(a)
        e.pack(side=TOP)
        f1 = Frame(a)
        f1.pack(side=LEFT)
        f2 = Frame(a)
        f2.pack(side=RIGHT)
        c1 = Button(f1, text="Happy", fg='red', width=12)
        c2 = Button(f2, text="Heart Broken", fg='black', width=12)
        c3 = Button(f1, text="In Love", fg='green', width=12)
        c4 = Button(f2, text="Party Mode", fg='blue', width=12)
        c5 = Button(f1, text="Dark", fg='pink', width=12)
        c6 = Button(f2, text="Dreamy", fg='orange', width=12)
        c7 = Button(f1, text="Meditative", fg='purple', width=12)
        c8 = Button(f2, text="Workout", fg='cyan', width=12)
        c1.pack(side=TOP)
        c2.pack(side=TOP)
        c3.pack(side=BOTTOM)
        c4.pack(side=BOTTOM)
        c5.pack(side=BOTTOM)
        c6.pack(side=BOTTOM)
        c7.pack(side=BOTTOM)
        c8.pack(side=BOTTOM)

    def go_back(self):
        a.destroy()
        self.fpage()

    def fpage(self):
        global t
        t =Tk()
        b1 = Button(t, text="Album", fg='red', width=10, height=10, command=self.alb_list)
        b2 = Button(t, text="Song", fg='black', width=10, height=10, command=self.song_list)
        b3 = Button(t, text="Mood", fg='green', width=10, height=10, command=self.mood_list)
        b4 = Button(t, text="Artist", fg='blue', width=10, height=10, command=self.art_list)

        b1.grid(row=0, column=0)
        b2.grid(row=0, column=3)
        #b5.grid(row=1,column=2)
        b4.grid(row=2, column=0)
        b3.grid(row=2, column=3)

        t.mainloop()

o = main()