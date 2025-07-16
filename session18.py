from tkinter import *
from PIL import ImageTk, Image
screen=Tk()
screen.title("Icon, images, trail")
screen.geometry("600x600")
screen.configure(bg="White")
#------------------------Putting Icon in screen--------------------------------
#Steps to follow:
#1. we have to first download an image, load an image in a variable, using photoimage function.load means store.
#2. use iconphoto() if .png image is there to display image on screen. use iconbitmap() if .ico image is there.
a=PhotoImage(file="Dog.png")
screen.iconphoto(False, a)

#-------------------------------Putting image on screen------------------------
#1. We have load or store our image in variabel using function called as ImageTk.PhotoImage(). But thi function is in library called as
#PIL (pillow) so we first import the library at top. 
#2. install PIL using command : pip install pillow in cmd
#3. use Image.open() to give image name
#4. To increase image size we use resize()
#5. use ImageTk.PhotoImage() to store image in variable
#6. use label to  display on screen. label is used to give text as well and label is used to giev image too.

a=Image.open("Dog.png")
a=a.resize((300, 300)) # width, height
a=ImageTk.PhotoImage(a)
l=Label(screen,image=a)
l.image=a
l.pack()

#-------------------------------------Frames-------------------------------------------
#frame is a box inside which we can put the widgets to make it a litle better.
#Example: in this vs code software, we have the terminal in a separate box, coding in a separate box, and files in a separate box, so like this is we want to divide the things we can use frame.
f=Frame(screen,bg="green", width=100, height=100)
f.pack_propagate=False
f.pack()
b1=Button(f, text="Click")
b1.pack()
mainloop()

#----------------------------Assignment---------------------------
#craete a prev and next button. craete two for both and call them on each button. Inside both functions do coding of image.
#in firts display a different image and in second different image.