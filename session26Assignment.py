import sqlite3

con=sqlite3.connect("Database.db")

csrs=con.cursor()

sql="""
create table if not exists tmp(
Student_Number integer,
f_name text,
l_name text,
grade integer,
gender text
)
"""

csrs.execute(sql)
con.commit()

def inset():
    a=e1.get()
    b=e2.get()
    c=e3.get()
    d=e4.get()
    e=e6.get()
    sql="""
insert into tmp(Student_Number, f_name, l_name, grade, gender) values(?, ?, ?, ?, ?)
"""
    csrs.execute(sql,(e,a, b,c,d))
    con.commit()

def getdetails():
    l=e5.get()
    csrs.execute("select * from tmp where Student_Number = ?",(l,))
    r=csrs.fetchall()
    f=""
    for i in r:
        f=str(i[0])+"\n"+(i[1])+"\n"+(i[2])+"\n"+str(i[3])+"\n"+(i[4])+"\n"
    l5.config(text=f)
def edit():
    a=e11.get()
    b=e22.get()
    c=e33.get()
    d=e44.get()
    e=e66.get()
    original=e5.get()
    csrs.execute("update tmp set Student_Number=?, f_name=?, l_name=?, grade=?, gender=? where Staff_Number=?", (a,b,c,d,e, original))
    con.commit()
def update():
    screen1=Tk()
    screen1.geometry("400x500")
    global e11, e22, e33, e44, e66
    l11=Label(screen1, text="First Name", bg="White", fg="Black", font=("Arial", 25))
    l11.grid(row=0, column=0)
    e11=Entry(screen1, bg="White", fg="Black", font=("Arial", 25))
    e11.grid(row=0, column=1)
    l22=Label(screen1, text="Last Name", fg="Black", bg="White", font=("Arial", 25))
    l22.grid(row=1, column=0)
    e22=Entry(screen1, bg="White", fg="Black", font=("Arial", 25))
    e22.grid(row=1, column=1)
    l33=Label(screen1, text="Grade", bg="White", fg="Black", font=("Arial", 25))
    l33.grid(row=2, column=0)
    e33=Entry(screen1, bg="White", fg="Black", font=("Arial", 25))
    e33.grid(row=2, column=1)
    l44=Label(screen1, text="Gender", bg="White", fg="black", font=("Arial", 25))
    l44.grid(row=3, column=0)
    e44=Entry(screen1, bg="White", fg="Black", font=('Arial', 25))
    e44.grid(row=3, column=1)
    b33=Button(screen1, text="Edit", bg="Gray", fg="White", font=("Arial", 25), command=edit)
    b33.grid(row=6, column=0)
    l66=Label(screen1, text="Student number", bg="White", fg="Black", font=("Arial", 25))
    l66.grid(row=5, column=0)
    e66=Entry(screen1, fg="Black", bg="White", font=("Arial", 25))
    e66.grid(row=5, column=1)
    l=e5.get()
    csrs.execute("select * from tmp where Student_Number = ?", (l,))
    r=csrs.fetchone()
    e66.insert(0,r[0])
    e11.insert(0,r[1])
    e22.insert(0,r[2])
    e33.insert(0,r[3])
    e44.insert(0,r[4])
def delete():
    a=e5.get()
    csrs.execute("delete from tmp where Student_Number=?", (a, ))
    con.commit()
from tkinter import *
screen=Tk()
screen.title("Student ID")
screen.geometry("700x800")
screen.configure(bg="White")
l1=Label(screen, text="First Name", bg="White", fg="Black", font=("Arial", 25))
l1.grid(row=0, column=0)
e1=Entry(screen, bg="White", fg="Black", font=("Arial", 25))
e1.grid(row=0, column=1)
l2=Label(screen, text="Last Name", fg="Black", bg="White", font=("Arial", 25))
l2.grid(row=1, column=0)
e2=Entry(screen, bg="White", fg="Black", font=("Arial", 25))
e2.grid(row=1, column=1)
l3=Label(screen, text="Grade", bg="White", fg="Black", font=("Arial", 25))
l3.grid(row=2, column=0)
e3=Entry(screen, bg="White", fg="Black", font=("Arial", 25))
e3.grid(row=2, column=1)
l4=Label(screen, text="Gender", bg="White", fg="black", font=("Arial", 25))
l4.grid(row=3, column=0)
e4=Entry(screen, bg="White", fg="Black", font=('Arial', 25))
e4.grid(row=3, column=1)
b1=Button(screen, text="Add Student ID", bg="Gray", fg="White", font=("Arial", 25), command=inset)
b1.grid(row=5, column=0)
b2=Button(screen, text="Search For Student ID", bg="Gray", fg="White", font=("Arial", 25), command=getdetails)
b2.grid(row=6, column=0)
b3=Button(screen, text="Update Student ID", bg="Gray", fg="White", font=("Arial", 25), command=update)
b3.grid(row=7, column=0)
b4=Button(screen, text="Delete Student ID", bg="Gray", fg="White", font=("Arial", 25), command=delete)
b4.grid(row=8, column=0)
l5=Label(screen)
l5.grid(row=9, column=0)
e5=Entry(screen, bg="White", fg="Black", font=("Arial", 25))
e5.grid(row=10, column=0)
l6=Label(screen, text="Student number", bg="White", fg="Black", font=("Arial", 25))
l6.grid(row=4, column=0)
e6=Entry(screen, fg="Black", bg="White", font=("Arial", 25))
e6.grid(row=4, column=1)
mainloop()