#daiter is used to create GUI(graphicaluserinterface)
#that mean we can create desktop apps with a screen, button, labels, images, on top of it.
#steps to use daiter:
#1. import daiter library.
#2. create a screen using Tk()
#3. create title using title()
#4. geometry/ size to screen using geometry("widthxheight")
#5. bgcolor(optional) using configure(bg="colorname")
#6. mainloop() at the end always to make sure screen continues to display and update. infinite loop.

#---------------------------Three way to set position of widgets on screen--------------------
#1. pack() : it places them one after other in different 
#2. grid() : if we want thing in horizontal and vertical. give row and columns
#eg:grid(row=0, column=0)
#3. place() : anywhere on screen. Use x, y
#eg : place(x=100, y=100)
#------------------------------------------------------------------
#for left : decrease x
#for right : increase x
#for bottom : incraese y
#for top : decrease y

#-----------------------------Style properties----------------------------------
#1. fg : textcolor
#2. bg : backgroundcolor
#3.font : font family and font size
#4. width and height : for size of button, entrybox. anything in box shape.

#-----------------------------------------------------------
#Note : in one program if we have used pack() for one we have to use same for all widgets in that program.
#vice versa ifwe are grid() we have to use grid, place() then place for all of them.


from tkinter import *
screen=Tk()
screen.title("My First app")
screen.geometry("600x300")
screen.configure(bg="green")

#---------craete text uisng Label---------------------
#syntax : variablename=Label(screename, text="")
#l1=Label(screen, text="My first app", fg="white", bg="green", font=("Times New Roman", 30))
#l1.pack() # to set position

#-----------button---------------------
#in one line give same row different column. different line give different row

b1=Button(screen,text="Click here", fg="Red", bg="blue", font=("Bitcount Grid Double",64))
b1.grid(row=0, column=0)

b2=Button(screen,text="Click here", fg="Red", bg="blue", font=("Bitcount Grid Double",64))
b2.grid(row=0, column=1)

b3=Button(screen,text="Click here", fg="Red", bg="blue", font=("Bitcount Grid Double",64))
b3.grid(row=1, column=0)

b4=Button(screen,text="Click here", fg="Red", bg="blue", font=("Bitcount Grid Double",64))
b4.grid(row=1, column=1)

screen.mainloop()