from tkinter import *
import getpass
window = Tk()
window.title="Login"
cu="Mikey"
cp="1234"
lbl3 = lbl3 =Label(window, text="")
lbl3.place(x=100,y=250)

txt = Entry(window,width=20)
txt.grid(column=2,row=0)
lbl = Label(window, text="Username")
lbl.grid(column=1,row=0)
lbl2 = Label(window, text="Password")
lbl2.grid(column=1,row=1)
txt2 = Entry(window,width=20, show="*")
txt2.grid(column=2,row=1)



def clear():
    print("clear all entries triggered")
    txt.delete(0, END)
    txt2.delete(0, END)



btn2 = Button(window, text="Clear",height=2, bg="white", width= 5, command=clear)
btn2.grid(column=2,row=3)





def login():
    print("Login attempt")
    user=txt.get()
    psw=txt2.get()
    print(user, "tried to login as ", cu, ".Password they entered: ",psw,"Correct password: ",cp)


    if user==cu:

        if psw ==cp:
            print("correct")
            lbl3.configure(text="Logged in as Mikey", bg="green")
        else:
            print("incorrect")
            lbl3.configure(text="Incorrect Username or password", bg="red")
    else:
        print("incorrect")
        lbl3.configure(text="Incorrect Username or password", bg="red")
window.geometry('275x275')
btn = Button(window, text="Login", bg="green",height=2, width= 5, command=login)
btn.grid(column=2,row=2)
window.mainloop()
