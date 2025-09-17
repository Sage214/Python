from tkinter import *
from tkinter import filedialog
import os
screen=Tk()
screen.title("Notepad")
screen.geometry("700x600")
screen.configure(bg="White")
#we will create a menu bar.
#1. use add_command to give the items which will appear when we click on the menu bar
#2. use add_cascade is used to give the name inside the menu bar
#3. add_separater is used to give the line
#creating the big text area:
t=Text(screen, wrap="word", font=("Arial", 20))
s=Scrollbar(screen, command=t.yview)#we want the scroll bar vertically around the textbox
t.configure(yscrollcommand=s.set)
t.pack(side=RIGHT, fill=BOTH, expand=TRUE)
file=None
def Newfile():
    global file
    file=None
    screen.title("untitled-notepad")
    t.delete(1.0, END)
def Openfile():
    global file
    p=filedialog.askopenfilename(defaultextension=".txt", filetypes=(("Img File", "*.jpg"), ("Imag File", "*.png"), ("Imgg File", "*.jpeg"), ("Text File","*.txt"), ("Python File", "*.py")))
    if p:
        file=p
        with open(p,"r", encoding="utf-8")as f:
            t.delete(1.0, END)
            t.insert(END, f.read())
        screen.title(os.path.basename(p)+"-Notepad")
def Savefile():
    global file
    p=filedialog.asksaveasfilename(defaultextension=".txt", filetypes=(("Img File", "*.jpg"), ("Imag File", "*.png"), ("Imgg File", "*.jpeg"), ("Text File","*.txt"), ("Python File", "*.py")))
    if p:
        file=p
        with open(p,"w", encoding="utf-8")as f:
            f.write(t.get(1.0, END))
        screen.title(os.path.basename(p)+"-Notepad")
def Exitfile():
    screen.destroy()
def Cut():
    #there is an in-built function Event_generate which helps us to cut, copy, paste.
    t.event_generate("<<Cut>>")
def Copy():
    t.event_generate("<<Copy>>")
def Paste():
    t.event_generate("<<Paste>>")
menubar=Menu(screen)
filemenu=Menu(menubar, tearoff=0)
filemenu.add_command(label="new", command=Newfile)
filemenu.add_command(label="open", command=Openfile)
filemenu.add_command(label="save", command=Savefile)
filemenu.add_separator()
filemenu.add_command(label="exit", command=Exitfile)
menubar.add_cascade(label="file", menu=filemenu)
editmenu=Menu(menubar, tearoff=0)
editmenu.add_command(label="cut", command=Cut)
editmenu.add_command(label="copy", command=Copy)
editmenu.add_command(label="paste", command=Paste)
menubar.add_cascade(label="edit", menu=editmenu)
screen.config(menu=menubar)
mainloop()