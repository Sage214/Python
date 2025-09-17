from tkinter import *
screen=Tk()
screen.title("List Box")
screen.geometry("700x800")
screen.configure(bg="White")
#delete, delete all, delete multiple, select, select multiple
#list box is a box inside which we put items and those items can be selected, deleted, and inserted,
l=Listbox(screen, width=30, selectmode=MULTIPLE)
l.grid()
l.insert(END,"Car")
l.insert(END,"apple")
l.insert(END,"Iphone")
l.insert(END,"laptop")

def Delete():
    #this first button deletes one item from the box at a time
    #ANCHOR means selected item
    l.delete(ANCHOR)
def Delete_All():
    #This means delete all the items from the box
    l.delete(0, END)
def Delete_Multiple():
    #this is to delete multiple items selected at one time
    #with the help of for we can get the items the person has selected and then delete. curse selection function
    for i in (l.curselection()):
        l.delete(i)
l1=Label(screen)
l1.grid(row=6, column=0)
def select():
    #this allows us to select one item, and display that as a label
    l1.config(text=l.get(ANCHOR))
def select_multiple():
    #multiple items selected will get and be displayed as a label
    r=""
    for i in (l.curselection()):
        r=r+str(l.get(i))+"\n"
    l1.config(text=r)
b1=Button(screen, text="delete", fg="Black", bg="Light Blue", font=("Verdana", 20), command=Delete)
b1.grid(row=1, column=0)

b2=Button(screen, text="delete all", fg="Black", bg="Light Blue", font=("Verdana", 20), command=Delete_All)
b2.grid(row=2, column=0)

b3=Button(screen, text="delete multiple items", fg="Black", bg="Light blue", font=("Verdana", 20), command=Delete_Multiple)
b3.grid(row=3, column=0)

b4=Button(screen, text="select", fg="Black", bg="Light blue", font=("Verdana", 20), command=select)
b4.grid(row=4, column=0)

b5=Button(screen, text="select multiple", fg="Black", bg="light blue", font=("Verdana", 20), command=select_multiple)
b5.grid(row=5, column=0)

l2=Label(screen, text='!this is a tester interface!', fg="Black", bg='white', font=("Verdana", 7))
l2.grid(row=6, column=6)
mainloop()