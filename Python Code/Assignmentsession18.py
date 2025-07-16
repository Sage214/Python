from tkinter import *
from PIL import ImageTk, Image
screen=Tk()
screen.title("Picture Roll")
screen.geometry("500x650")
screen.configure(bg="White")
a=PhotoImage(file="Cyberwolf2.png")
screen.iconphoto(False, a)
def function():
    a=Image.open("Cyberwolf2.png")
    a=a.resize((200, 300))
    a=ImageTk.PhotoImage(a)
    l=Label(screen, image=a)
    l.image=a
    l.grid(row=2, column=3)
def function1():
    a=Image.open("Wolf.png")
    a=a.resize((200, 300))
    a=ImageTk.PhotoImage(a)
    l=Label(screen, image=a)
    l.image=a
    l.grid(row=2, column=3)

b1=Button(screen, text="Back", fg="Black", bg="Light gray", font=("Times New Roman", 20), command=function)
b1.grid(row=0, column=0)

b2=Button(screen, text="Exit", fg="Black", bg="light gray", font=("Times New Roman", 20), command=screen.destroy)
b2.grid(row=0, column=3)
#destroy is an inbuilt function used to close the screen
b3=Button(screen, text="Next", fg="Black", bg="Light Gray", font=("Times New Roman", 20), command=function1)
b3.grid(row=0, column=4)

mainloop()