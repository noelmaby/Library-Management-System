import time
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk, Image
import pyttsx3

#voice
engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
engine.setProperty('rate',165)
engine.runAndWait()

def speak(str):
    engine.say(str)
    engine.runAndWait()

#admin
def admin():
    adm = Toplevel()

    adm.title("ADMIN CORNER")
    adm.geometry("1200x700")
    adm.resizable(False, False)

    adm.configure(bg="grey")

    adm.bg = ImageTk.PhotoImage(Image.open("C:\\Users\\Admin\\Desktop\\python project\\admwall.png"))
    adm.bg_image = Label(adm, image=adm.bg).place(x=0, y=0, relwidth=1, relheight=1)


#returnbook
def returnb():
    import mysql.connector as con
    mydb = con.connect(host="localhost", user="root", password="1234", database="library")
    myr = mydb.cursor()
    mycur = mydb.cursor()
    list8 = []
    list6 = []

    stt = "available"
    flag = False

    bn = int(bokid.get())
    dt = dat.get()
    snam = stname.get()
    clss= click.get()

    mycur.execute("select * from book where BOOK_ID='{}'".format(bn))
    dta = mycur.fetchall()
    if dta == []:
        messagebox.showerror("error", "BOOK ID NOT EXIST \n ENTER VALID BOOK ID", parent=win)
    else:
        mycur.execute("select BOOK_ID from book where STATUS='available'")
        for x in mycur:
            list8.append(x[0])
        if bn in list8:
            messagebox.showerror("error", "BOOK RETURNED ALREADY \n ENTER ANOTHER BOOK ID")
        else:
            myr.execute("select BOOK_NAME from book where BOOK_ID='{}' ".format(bn))
            for d in myr:
                list6.append(d[0])
            mycur.execute("insert into returnbook values('{}','{}','{}','{}','{}') ".format(bn, list6[0], snam, dt,clss))
            mycur.execute("update book set STATUS='{}' where BOOK_ID='{}' ".format(stt, bn))
            speak("BOOK RETURNED SUCCESSFULLY")
            messagebox.showinfo("NOTE", "BOOK RETURNED SUCCESSFULLY",parent=win)
            mydb.commit()

#returnbook
def shows():
    sec = clicked.get()
    import mysql.connector as con
    mydb = con.connect(host="localhost", user="root", password="1234", database="library")
    mycur = mydb.cursor()
    mycr = mydb.cursor()
    mycur.execute("select * from book where BOOK_GENRES ='{}' ".format(sec))
    data = mycur.fetchall()

    box = ttk.Treeview(win)

    box['columns'] = ("BOOK_ID", "BOOK_NAME", "AUTHOR", "BOOK_GENRES", "STATUS")

    box.column("#0", width=0, stretch=NO)
    box.column("BOOK_ID", width=150)
    box.column("BOOK_NAME", width=150)
    box.column("AUTHOR", width=150)
    box.column("BOOK_GENRES", width=150)
    box.column("STATUS", width=150)

    box.heading("#0", text=" ", anchor=W)
    box.heading("BOOK_ID", text="BOOK_ID", anchor=W)
    box.heading("BOOK_NAME", text="BOOK_NAME", anchor=W)
    box.heading("AUTHOR", text="AUTHOR", anchor=W)
    box.heading("BOOK_GENRES", text="BOOK_GENRES", anchor=W)
    box.heading("STATUS", text="STATUS", anchor=W)

    count = 0
    for t in data:
        box.insert('', 0, values=(t[0], t[1], t[2], t[3], t[4]))
        count = count + 1

    box.place(x=243, y=270)




#ISSUE_BOOK
def issue():
    import mysql.connector as con
    mydb = con.connect(host="localhost", user="root", password="1234", database="library")
    myr = mydb.cursor()
    mycurs = mydb.cursor()
    mycur = mydb.cursor()
    list1=[]
    list5 = []
    sts = "issued"


    bno = int(bokid.get())
    date = dat.get()
    stuname = stname.get()
    cls =click.get()
    mycur.execute("select * from book where BOOK_ID='{}'".format(bno))
    dta = mycur.fetchall()
    if dta == []:
        messagebox.showerror("error", "BOOK ID NOT EXIST \n ENTER VALID BOOK ID", parent=win)
    else:
        mycur.execute("select BOOK_ID from book where STATUS='issued'")
        for x in mycur:
            list1.append(x[0])
        if bno in list1:
            messagebox.showerror("error", "BOOK ALREADY ISSUED \n ENTER ANOTHER BOOK ID", parent=win)
        else:
            myr.execute("select BOOK_NAME from book where BOOK_ID='{}' ".format(bno))
            for d in myr:
                list5.append(d[0])
            mycur.execute("insert into issuebook values('{}','{}','{}','{}','{}') ".format(bno, list5[0], stuname, date,cls))
            mycur.execute("update book set STATUS='{}' where BOOK_ID='{}' ".format(sts, bno))
            speak("BOOK ISSUED SUCCESSFULLY")
            messagebox.showinfo("NOTE", "BOOK ISSUED SUCCESSFULLY", parent=win)
            mydb.commit()


#ISSUE_BOOK
def show():
    sec = clicked.get()
    import mysql.connector as con
    mydb = con.connect(host="localhost", user="root", password="1234", database="library")
    mycur = mydb.cursor()
    mycr = mydb.cursor()
    mycur.execute("select * from book where BOOK_GENRES ='{}' ".format(sec))
    data = mycur.fetchall()

    box = ttk.Treeview(win)

    box['columns'] = ("BOOK_ID", "BOOK_NAME", "AUTHOR", "BOOK_GENRES", "STATUS")

    box.column("#0", width=0, stretch=NO)
    box.column("BOOK_ID", width=150)
    box.column("BOOK_NAME", width=150)
    box.column("AUTHOR", width=150)
    box.column("BOOK_GENRES", width=150)
    box.column("STATUS", width=150)

    box.heading("#0", text=" ", anchor=W)
    box.heading("BOOK_ID", text="BOOK_ID", anchor=W)
    box.heading("BOOK_NAME", text="BOOK_NAME", anchor=W)
    box.heading("AUTHOR", text="AUTHOR", anchor=W)
    box.heading("BOOK_GENRES", text="BOOK_GENRES", anchor=W)
    box.heading("STATUS", text="STATUS", anchor=W)

    count = 0
    for t in data:
        box.insert('', 0, values=(t[0], t[1], t[2], t[3], t[4]))
        count = count + 1

    box.place(x=235, y=260)

#ISSUE_BOOK
def issuebook():
    lis = []
    lis1= [1,2,3,4,5,6,7,8,9,10,11,12]
    global bokid, stname, dat, win, clicked,click

    import mysql.connector as con
    mydb = con.connect(host="localhost", user="root", password="1234", database="library")
    mycr = mydb.cursor()
    mycr.execute("select distinct(BOOK_GENRES) from book;")
    for i in mycr:
        lis.append(i[0])

    win = Toplevel()

    win.title("STUDENT CORNER")
    win.geometry("1000x500")
    win.resizable(False, False)

    win.configure(bg="grey")

    win.bg = ImageTk.PhotoImage(Image.open("C:\\Users\\Admin\\Desktop\\python project\\stuwall.png"))
    win.bg_image = Label(win, image=win.bg).place(x=0, y=0, relwidth=1, relheight=1)


    #title
    s = Label(win, text="STUDENT CORNER", font=("jokerman", 20,"bold"), fg="lightblue")
    s.place(x=400,y=0)



    # book id
    frm1 = Frame(win, bg="lightgrey")
    frm1.place(relwidth=0.60, relheight=0.07, x=20, y=50)
    s1 = Label(frm1, text="BOOK ID :", font=("verdana", 15), fg="black")
    s1.place(relx=0.09, relwidth=0.30, relheight=1)
    bokid = Entry(frm1, bg="lightgrey", font=("verdana", 15))
    bokid.place(relx=0.45, relwidth=0.39, relheight=1)

    # student name
    frm2 = Frame(win, bg="lightgrey")
    frm2.place(relwidth=0.60, relheight=0.07, x=20, y=100)
    s2 = Label(frm2, text="STUDENT NAME :", font=("verdana", 15), fg="black")
    s2.place(relx=0.09, relwidth=0.30, relheight=1)
    stname = Entry(frm2, bg="lightgrey", font=("verdana", 15))
    stname.place(relx=0.45, relwidth=0.39, relheight=1)

    # date
    frm3 = Frame(win, bg="lightgrey")
    frm3.place(relwidth=0.60, relheight=0.07, x=20, y=145)
    s3 = Label(frm3, text="DATE :", font=("verdana", 15), fg="black")
    s3.place(relx=0.09, relwidth=0.30, relheight=1)
    dat = Entry(frm3, bg="lightgrey", font=("verdana", 15))
    dat.place(relx=0.45, relwidth=0.39, relheight=1)
    dat.insert(0, "YYYY/MM/DD")

    frm4 = Frame(win, bg="lightgrey")
    frm4.place(relwidth=0.60, relheight=0.07, x=20, y=189)
    s4 = Label(frm4, text="CLASS:", font=("verdana", 15), fg="black")
    s4.place(relx=0.09, relwidth=0.30, relheight=1)
    click = StringVar()
    click.set("CHOOSE CLASS")
    drop = OptionMenu(win, click, *lis1)
    drop.place(x=400, y=190)


    issuebtn=ImageTk.PhotoImage(Image.open("C:\\Users\\Admin\\Desktop\\python project\\issuebtn.png"))
    isubtn = Button(win,command=issue,image=issuebtn,bd=0,bg="black")
    isubtn.image=issuebtn
    isubtn.place(x=800, y=75)

    cancelbtn = ImageTk.PhotoImage(Image.open("C:\\Users\\Admin\\Desktop\\python project\\cance.png"))
    canl = Button(win, image=cancelbtn,command=win.destroy,bd=0,bg="black")
    canl.image=cancelbtn
    canl.place(x=850, y=125)

    returnbtn = ImageTk.PhotoImage(Image.open("C:\\Users\\Admin\\Desktop\\python project\\returnbtn.png"))
    retbtn = Button(win, image=returnbtn, bd=0,bg="black",command=returnb)
    retbtn.image = returnbtn
    retbtn.place(x=800, y=176)

    clicked = StringVar()
    clicked.set("CHOOSE BOOK GENRES")

    drop = OptionMenu(win, clicked, *lis)
    drop.place(x=50, y=295)

    sbl = Button(win, text="SHOW BOOK LIST", bg="lightgrey", font=("verdana", 10), command=show).place(x=50, y=330)

    def clock():
        hour = time.strftime("%I")
        minute = time.strftime("%M")
        second = time.strftime("%S")
        am_pm = time.strftime("%p")
        day = time.strftime("%A")

        mylabel.config(text=hour + ":" + minute + ":" + second + " " + am_pm)
        mylabel.after(1000, clock)

    mylabel = Label(win, text=" ", font=("Helvetica", 20, "bold"), fg="lightblue", bg="white")
    mylabel.place(x=10, y=380)

    clock()

    win.mainloop()








#LOGIN_MAIN
class Login:
    def __init__ (self,root):
        self.root = root
        self.root.title("Login System")
        self.root.geometry("626x417+100+50")
        self.root.resizable(False,False)
        #image
        self.bg=ImageTk.PhotoImage(Image.open("C:\\Users\\Admin\\Desktop\\python project\\sara.png"))
        self.bg_image=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)


        #login frame
        Frame_login=Frame(self.root,bg="white")
        Frame_login.place(x=25,y=40,height=320,width=400)

        #TIMEzzz
        def clock():
            hour = time.strftime("%I")
            minute = time.strftime("%M")
            second = time.strftime("%S")
            am_pm=time.strftime("%p")
            day=time.strftime("%A")

            mylabel.config(text=hour + ":" + minute + ":" + second+" "+am_pm)
            mylabel.after(1000, clock)
            mylabel1.config(text=day)

        def update():
            mylabel.config(text="NEW TEXT")

        mylabel = Label(self.root, text=" ", font=("Helvetica", 20,"bold"), fg="darkorange", bg="white")
        mylabel.place(x=466,y=0)

        mylabel1 = Label(self.root, text=" ", font=("Helvetica", 18,"bold"), fg="darkorange", bg="white")
        mylabel1.place(x=466,y=35)



        clock()

        title=Label(Frame_login,text="LOGIN",font=("Impact",30,"bold"),fg="orange",bg="white").place(x=50,y=10)
        desc=Label(Frame_login, text="LIBRARY LOGIN ", font=("Goudy old style", 15, "bold"), fg="orange", bg="white").place(x=50, y=55)

        lab_user = Label(Frame_login, text="USERNAME", font=("Goudy old style", 25, "bold"), fg="gray", bg="white").place(x=50, y=85)
        self.user=Entry(Frame_login,font=("times new roman",15),bg="lightgray")
        self.user.place(x=50,y=120,width=200,height=30)

        lab_user = Label(Frame_login,text="PASSWORD",font=("Goudy old style",25, "bold"),fg="gray",bg="white").place(x=50, y=160)
        self.passw = Entry(Frame_login, font=("times new roman", 15), bg="lightgray")
        self.passw.place(x=50, y=195, width=200, height=30)

        login = ImageTk.PhotoImage(Image.open("C:\\Users\\Admin\\Desktop\\python project\\login.png"))
        Login_btn=Button(Frame_login,command=self.login_function,image=login,bd=0)
        Login_btn.image=login
        Login_btn.place(x=50,y=240)

        cancel = ImageTk.PhotoImage(Image.open("C:\\Users\\Admin\\Desktop\\python project\\cancel.png"))
        exit=Button(Frame_login,command=self.root.quit,image=cancel,bd=0)
        exit.image=cancel
        exit.place(x=190,y=245)

    def login_function(self):
        if self.passw.get()=="" or self.user.get()=="":
            messagebox.showerror("ERROR","All Fields Are Required",parent=self.root)
        elif "1234" != self.passw.get() or self.user.get()!= "admin":
            messagebox.showerror("error","Invalid Username/Password",parent=self.root)
        else:
            messagebox.showinfo("LOGED IN","WELCOME TO LIBRARY",parent=self.root)
            speak("LOGIN SUCCESSFULL")
            top = Toplevel()
            top.title("LIBRARY")
            top.geometry("626x417")
            top.resizable(False, False)
            top.bg = ImageTk.PhotoImage(Image.open("C:\\Users\\Admin\\Desktop\\python project\\sara.png"))
            top.bg_image = Label(top, image=top.bg).place(x=0, y=0)

            wt = Label(top, text="LIBRARY MANAGEMENT", fg="white", bg="black", font=("jokerman", 13, "bold"), width=100,
                       height=3)
            wt.pack()

            stubtn = ImageTk.PhotoImage(Image.open("C:\\Users\\Admin\\Desktop\\python project\\studentbtn.png"))
            bt1 = Button(top,image=stubtn,bd=0,command=issuebook,bg="black")
            bt1.image=stubtn
            bt1.place(x=210, y=100)

            adbtn = ImageTk.PhotoImage(Image.open("C:\\Users\\Admin\\Desktop\\python project\\adminbtn.png"))
            bt2 = Button(top,image=adbtn,bd=0,command=admin,bg="black")
            bt2.image=adbtn
            bt2.place(x=225, y=230)

            logout = ImageTk.PhotoImage(Image.open("C:\\Users\\Admin\\Desktop\\python project\\logout.jpg"))
            bt3 = Button(top,command=self.root.quit,image=logout,bd=0,bg="black")
            bt3.image=logout
            bt3.place(x=7,y=365)

            def clock():
                hour = time.strftime("%I")
                minute = time.strftime("%M")
                second = time.strftime("%S")
                am_pm = time.strftime("%p")
                day = time.strftime("%A")

                mylabel.config(text=hour + ":" + minute + ":" + second + " " + am_pm)
                mylabel.after(1000, clock)
            mylabel = Label(top, text=" ", font=("Helvetica", 20, "bold"), fg="darkorange", bg="white")
            mylabel.place(x=460, y=366)

            clock()



root = Tk()
obj = Login(root)
root.mainloop()

