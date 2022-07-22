from tkinter import *
import  random

class Manager(Tk):
    def __init__(self):      #root=self
        super().__init__()
        self.geometry("744x377")

    L=["0","1","2","3","4"," 5","6","7","8","9",
       "A", "B", "C", "D", "E", 'F', 'G', 'H', 'I',
       'J', 'K', 'M', 'N', 'O', 'p', 'Q', 'R',
       'S', 'T', 'U', 'V', 'W', 'X', 'Y','Z',
       '@', '#', '$','a', 'b', 'c', 'd', 'e', 'f',
       'g', 'h','i', 'j', 'k', 'm', 'n', 'o', 'p',
       'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y','z']
    pd=""
    na=""
    ph=""
    em=""
    pa=""
    def create(self):
        n = int(input("enter length of password="))
        for i in range(0, n) :
          a=random.choice(self.L)
          self.pd=self.pd+a
        print(self.pd)

    def saver(self):
        print(self.na)
        print(self.em)
        print(self.pa)
        print(self.ph)


    def Next(self):

        root1=Toplevel()
        name = Label(root1, text="First name")
        phone = Label(root1, text="Roll Number")
        email = Label(root1, text="Email")
        Password = Label(root1, text="Password")

        name.grid(row=1, column=2)
        phone.grid(row=2, column=2)
        email.grid(row=3, column=2)
        Password.grid(row=4, column=2)



        # entries
        Entry(root1, textvariable=namevalue).grid(row=1, column=3)
        phoneentry = Entry(root1, textvariable=phonevalue)
        emailentry = Entry(root1, textvariable=emailvalue)
        Passwordentry = Entry(root1, textvariable=Passwordvalue)

        # packing

        phoneentry.grid(row=2, column=3)
        emailentry.grid(row=3, column=3)
        Passwordentry.grid(row=4, column=3)

        # check box
        che1 = Checkbutton(root1,text="Numeric ", variable=numvalue)
        che2 = Checkbutton(root1,text="Upper case")
        che3 = Checkbutton(root1,text="Lower case")
        che4 = Checkbutton(root1,text="Special Character")

        che1.grid(row=6, column=2)
        che2.grid(row=6, column=3)
        che3.grid(row=6, column=4)
        che4.grid(row=6, column=5)
        self.na=namevalue.get()
        self.ph=phonevalue.get()
        self.em=emailvalue.get()
        self.pa=Passwordvalue.get()
        # print("hello", namevalue.get(), phonevalue.get())
        Button(root1, text="save", command=self.saver).grid(row=7, column=4)
        root1.mainloop()




    def reset(self):
        p=int(input("enter your Password="))
        guess=""
        while(guess!=p):
            guess=""
            for letter in range(len(p)):
                guess_pass=random.choice(self.L)
                guess=guess+guess_pass
        print(guess)



    def strength(self):
        def upper(check) :
            u="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            for i in u:
              for j in check:
                if i==j:
                    return 1

        def lower(check):
            low="abcdefghijklmnopqrstuvwxyz"
            for i in low:
                for j in check:
                    if i==j:
                        return 1

        def num(check):
            val="0123456789"
            for i in val:
                for j in check:
                    if i==j:
                        return 1

        def special(check):
            z="@#&$"
            for i in z:
                for j in check:
                    if i==j:
                        return 1

        def length(check):
            c=0
            for i in check:
                c=c+1
            if c>6 and c<16:
                return 1

       # self.pd=check
        g= upper(self.pd)
        h= lower(self.pd)
        e=num(self.pd)
        j= special(self.pd)
        k= length(self.pd)
        if g==1 and  h==1 and e==1 and j==1 and k==1:
            print("valid password")
        else:
            if g!=1:
                print("upper case is not available")
            elif h!=1:
                print("lower case is not available")
            elif e!=1:
                print("Integer is not available")
            elif j!=1:
                print("special case is not available")
            elif k!=1:
                print("Minimum length 6 characters.Maximum length 16 characters.")


#main
pas=Manager()

# root.geometry("644x388")

Label(pas,text="This is password manager",font="comicsansms 13 bold",pady=15).grid(row=0, column=3)
# variable for storing
namevalue = StringVar()
phonevalue = StringVar()
emailvalue = StringVar()
Passwordvalue = StringVar()
numvalue = IntVar()
Button(pas,text="Create Password",command=pas.create).grid(row=7,column=3)
Button(pas,text="next",command=pas.Next).grid(row=7,column=4)

pas.mainloop()

