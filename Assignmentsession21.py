from tkinter import *
from tkinter import messagebox
screen=Tk()
screen.title("Pizza Toppings")
screen.geometry("200x300")
screen.configure(bg="White")
def function1():
    if s.get()==1:
        messagebox.showinfo("Inf", "You ordered pepperoni pizza")
    elif s.get()==0:
        messagebox.showinfo("Inf", "You have ordered pizza with no pepperoni")

s=IntVar()
c1=Checkbutton(screen, text="Pepperoni", variable=s)
c1.grid(row=0, column=1)

b1=Button(screen, text="Order", command=function1)
b1.grid(row=2, column=3)
mainloop()