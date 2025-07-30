from tkinter import *
from tkinter import messagebox
screen=Tk()
screen.title("message box and J slider")
screen.geometry("600x600")
screen.configure(bg="White")
#message box means showing the form of messages on the screen. Message box, class so it has to be imported separatly at the top.
#Steps to follow:
#1. first import message box at the top.
#2. Use diffrent , functions to diffrent a message on screen.
#For simple message:
messagebox.showinfo("information", "your file has been downloaded")
#For warning and error messages:
messagebox.showwarning("Download", "There was an error downloading the file")
messagebox.showerror("information", "There is an error by downloading the file")
#For asking questions:
messagebox.askokcancel("question", "do you want to download this file?")
messagebox.askretrycancel("question", "do you want to download this file?")
messagebox.askyesno("question", "Do you want to download this file?")
messagebox.askyesnocancel("question", "Do you want to download this file?")
#How to go from one screen to another:
def SecondScreen():
    #in order to creat a new screen we always use the Tk function
    screen1=Tk()
    screen1.title("Second Screen")
    screen1.geometry("600x600")
    screen1.configure(bg="Light Blue")
    l1=Label(screen1, text="Second Page")
    l1.grid(row=0, column=0)

b1=Button(screen, text="Go To The Second Screen", fg="Black", bg="White", font=("Roboto", 20), command=SecondScreen)
b1.grid(row=0, column=0)
#For closing the screen:
#command=screenname.destroy
mainloop()