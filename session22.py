from tkinter import *
from reportlab.pdfgen import canvas
screen=Tk()
screen.title("Billing Managemant System")
screen.geometry("1000x700")
screen.configure(bg="White")
b1=Button(screen, text="Total", fg="Red", bg="Yellow", font=("Arial", 15))
b1.grid(row=2, column=0)

def Print():
    #we use canvas where we will put a text using draw string and then save as a pdf file
    c=canvas.Canvas("bill.pdf") # canvas is white plain file with name bill.pdf
    c.drawString(100, 750, "Billing Management") # drawSTring to giev text on it, x, y given in beginning
    c.drawString(100, 730, "Bread: " + e1.get()) 
    c.drawString(100, 710, "Water Bottle: " + e2.get())
    c.drawString(100, 690, "Milk: " + e3.get())
    c.drawString(100, 670, "Chips: " + e5.get())
    c.drawString(100, 650, "Total : "+ str(r))
    c.drawString(100, 630, str(r))
    c.save()



def Total():
    global r
    try:
        print(e1.get())
        a=int(e1.get())*2
        print(a)
        b=int(e2.get())*2
        c=int(e3.get())*2
        d=int(e5.get())*2
        r=a+b+c+d
        s1.set(a)
        s2.set(b)
        s3.set(c)
        s4.set(d)
        ll.config(text=r)
    except:
        print("Error")

def reset():
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e5.delete(0, END)
    e6.delete(0, END)
    e7.delete(0, END)
    e8.delete(0, END)
    e9.delete(0, END)
    ll.config(text="")
label=Label(screen)
label.grid(row=3, column=0)
def Quantity():
    r=int(e1.get())+int(e2.get())+int(e3.get())+int(e5.get())
    label.config(text=r)
def exit():
    screen.destroy()
b2=Button(screen, text="Print", fg="Red", bg="Yellow", font=("Arial", 15))
b2.grid(row=2, column=1)

b3=Button(screen, text="Reset", fg="Red", bg="Yellow", font=("Arial", 15))
b3.grid(row=2, column=2)

b4=Button(screen, text="Exit", fg="Red", bg="Yellow", font=("Arial", 15))
b4.grid(row=2, column=3)

l1=Label(screen, text="Billing Managemant System", fg="White" ,bg="Teal", font=("Verdana", 25))
l1.grid(row=0, column=0)

f=LabelFrame(screen,width=700, height=400, fg="White", font=("Arial", 30, "bold"),bg="Teal",relief="groove", labelanchor="n", text="product details")
f.grid(row=1, column=0, padx=50, pady=50, sticky="nsew" )

l2=Label(f, text="Bread", fg="White" ,bg="Teal", font=("Verdana", 15))
l2.grid(row=2, column=1)

e1=Entry(f, fg="Black", bg="White", font=("Arial", 15))
e1.grid(row=2, column=2)

l3=Label(f, text="Water Bottle", fg="White" ,bg="Teal", font=("Verdana", 15))
l3.grid(row=3, column=1)

e2=Entry(f, fg="Black", bg="White", font=("Arial", 15))
e2.grid(row=3, column=2)

l4=Label(f, text="Milk", fg="White", bg="Teal", font=("Arial", 15))
l4.grid(row=4, column=1)

e3=Entry(f, fg="Black", bg="White", font=("Arial", 15))
e3.grid(row=4, column=2)

l5=Label(f, text="Chips", fg="White", bg="Teal", font=("Arial", 15))
l5.grid(row=5, column=1)

l6=Label(f, text="Total", fg="White", bg="Teal", font=("Arial", 15))
l6.grid(row=6, column=1)

ll=Label(f)
ll.grid(row=6, column=2)

s=StringVar()
e5=Entry(f, fg="Black", bg="White", font=("Arial", 15), textvariable=s)
e5.grid(row=5, column=2)

b1=Button(screen, text="Total", fg="Red", bg="Yellow", font=("Arial", 15), command=Total)
b1.grid(row=2, column=0)

b2=Button(screen, text="Print", fg="Red", bg="Yellow", font=("Arial", 15), command=Print)
b2.grid(row=2, column=1)

b3=Button(screen, text="Reset", fg="Red", bg="Yellow", font=("Arial", 15), command=reset)
b3.grid(row=2, column=2)

b4=Button(screen, text="Exit", fg="Red", bg="Yellow", font=("Arial", 15), command=exit)
b4.grid(row=2, column=3)

s1=StringVar()
e6=Entry(f, fg="Black", bg="White", font=("Arial", 15), textvariable=s1)
e6.grid(row=2, column=3)

s2=StringVar()
e7=Entry(f, fg="Black", bg="White", font=("Arial", 15), textvariable=s2)
e7.grid(row=3, column=3)

s3=StringVar()
e8=Entry(f, fg="Black", bg="White", font=("Arial", 15), textvariable=s3)
e8.grid(row=4, column=3)

s4=StringVar()
e9=Entry(f, fg="Black", bg="White", font=("Arial", 15), textvariable=s4)
e9.grid(row=5, column=3)

l7=Label(f, text="Number of items", fg="Black", bg="Teal", font=("Arial", 20))
l7.grid(row=1, column=2)

l8=Label(f, text="Cost of items", fg="Black", bg="Teal", font=("Arial", 20))
l8.grid(row=1, column=3)

b5=Button(screen, text="Quantity", fg="Red", bg="Yellow", font=("Arial", 15), command=Quantity)
b5.grid(row=2, column=4)
mainloop()