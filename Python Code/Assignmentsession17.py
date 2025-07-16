from tkinter import *
screen1=Tk()
screen1.title("Log In")
screen1.geometry("700x600")
screen1.configure(bg="White")
a=StringVar()
b1=Label(screen1, text="Username", fg="Dark Gray", font=("Roboto", 25))
b1.grid(row=0, column=0)
a=Entry(screen1, width=30, bg="Light Gray", font=("Roboto", 20))
a.grid(row=0, column=1, ipady=20)

b2=Label(screen1, text="Password", fg="Dark Gray", font=("Roboto", 25))
b2.grid(row=1, column=0)
b=Entry(screen1, width=30, bg="light gray", font=("Roboto", 20))
b.grid(row=1, column=1, ipady=20)

b4=Label(screen1, text="Confirm Password", fg="Dark Gray", font=("Roboto", 25))
b4.grid(row=2, column=0)
c=Entry(screen1, width=30, bg="Light Gray", font=("roboto", 20))
c.grid(row=2, column=1, ipady=20)

b5=Label(screen1, text="Email ID", fg="Dark Gray", font=("roboto", 25))
b5.grid(row=3, column=0)
d=Entry(screen1, width=30, bg="light gray", font=("roboto", 20))
d.grid(row=3, column=1, ipady=20)

b3=Button(screen1, text="Sign In", fg="White", bg="Royal Blue", font=("Roboto", 20), width=30)
b3.grid(row=4, column=0, columnspan=2)
mainloop()