from tkinter import *
from tkinter import messagebox
screen=Tk()
screen.title("Check boxes and dropdowns")
screen.geometry("800x700")
screen.configure(bg="White")
#-----------------------------checkbox--------------------------------
#checkbox means checkbutton where we can select multiple options.
#onvalue and offvalue. onvalue=1 menas checkbutton is selected and offvalue=0 means checkbutton is not selected.

#every checkbutton will have different tkinter variable beacuse whenever we select any checkbutton 1 will go to
#inside tkinter variable and if its not selected then 0 will go inside tkinter variable.

#we use if then else to check if we are getting 0 or 1 in s or s1
#get() to get value from these tkinter variable
def rf():
    if s.get()==0 and s1.get()==1:
        messagebox.showinfo("Inf", "C++ is selected")
    elif s.get()==1 and s1.get()==0:
        messagebox.showinfo("Inf", "Python is selected")
    elif s.get()==1 and s1.get()==1:
        messagebox.showinfo("Inf", "Both are selected")
    else:
        messagebox.showinfo("Inf", "Nothing has been selected")


s=IntVar()
c1=Checkbutton(screen, text="Python", variable=s)
c1.grid(row=0, column=0)

s1=IntVar()
c2=Checkbutton(screen, text="C++", variable=s1)
c2.grid(row=1, column=1)

b1=Button(screen, text="Submit", command=rf)
b1.grid(row=2, column=1)

#dropdown is a menubox, when we click on the arrows, a list opens
r=["apple", "mango", "blueberry"]
#
b=OptionMenu(screen, )
mainloop()