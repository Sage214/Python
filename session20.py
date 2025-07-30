from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
screen=Tk()
screen.title("Download, upload file, J slider")
screen.geometry("600x600")
screen.configure(bg="White")
#--------------------------Download and upload the file-------------------------
#
def Upload():
    #upload means selecting a file from a system
    #steps to follow are:
    #1. import file dialuog at the top
    #2. use the function askopenfile
    #this function allows us to open a file and select a file from our system.
    #later if we want to put that file on screen we have to code.
    #here we will select an image file and put an image file on screen.
    #so we use PIL functions to put image on screen.
    a=filedialog.askopenfilename(initialdir="/", filetypes=(("PNG file", '*.png'), ("Jpg File", "*.jpg"), ("Htnl File", "*.html"),("Python File", "*.py"), ("Text", "*.txt")))
    #in a variable we will select that image which the person will select
    a=Image.open(a)
    a=a.resize((300, 300)) # width, height
    a=ImageTk.PhotoImage(a)
    l=Label(screen,image=a)
    l.image=a
    l.grid(row=1, column=0)
def Save():
    a=filedialog.asksaveasfile(initialdir="/", filetypes=(("PNG file", '*.png'), ("Jpg File", "*.jpg"), ("Htnl File", "*.html"),("Python File", "*.py"), ("Text", "*.txt")))
b1=Button(screen, text="Upload", fg="Black", bg="Light blue", font=("Verdana", 20), command=Upload)
b1.grid(row=0, column=2)
b2=Button(screen, text="Download", fg="black", bg='light blue', font=("Verdana", 20), command=Save)
b2.grid(row=0, column=4)
#--------------------------------J slider-------------------------------------------
#J slider means a scale where we can select any number so we get that number and display as label on screen.
def function():
    s1=s.get()
    label.config(text=s1)
s=Scale(screen, from_=1,to=100)
s.grid(row=2, column=0)
label=Label(screen)
label.grid(row=1, column=3)
b3=Button(screen, text="Click", fg="black", bg="light Blue", font=("Verdana", 20), command=function)
b3.grid(row=1, column=2)
mainloop()