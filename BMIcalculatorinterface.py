from tkinter import *
screen=Tk()
screen.title("BMI Calculator")
screen.geometry("400x300")
screen.configure(bg="Light Blue")
l1=Label(screen, text="Weight (kgs)", fg="Black", bg="White", font=("Verdana", 20))
l1.grid(row=0, column=0)
def BMI():
    width=int(a.get())
    height=int(a2.get())
    total=width/height
    l1.config(text=total)
def Reset():
    a.delete(0, END)
    a2.delete(0, END)
a=Entry(screen, width=10, bg="White", font=("Verdana", 20))
a.grid(row=0, column=1)

l2=Label(screen, text="Height (in.)", fg="Black", bg="White", font=("Verdana", 20))
l2.grid(row=1, column=0)

a2=Entry(screen, width=10, bg="White", font=("Verdana", 20))
a2.grid(row=1, column=1)

l1=Label(screen, fg="Black", bg="White")
l1.grid(row=3, column=1)

b1=Button(screen, text="Calculate", fg="Black", bg="Light Gray", font=("Verdana", 20), command=BMI)
b1.grid(row=2, column=0)

b2=Button(screen, text="Reset", fg="Black", bg="Light Gray", font=("Verdana", 20), command=Reset)
b2.grid(row=2, column=1)
mainloop()