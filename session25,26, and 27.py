#sqlite is a database which is in-built in python, it is used to store data which is coming from the user permenantly. All though sqlite is small in size, used only to store small amounts of data
#But, its in-Built so we dont have to install it, no connection issue, we have external databases as well, like, mysql, oracle. all though they are bigger in size, but, we need to install them and connect with python by us
#Steps\Querys which we need to use in sqlite
#1. import sqlite library at top
#2. use .connect function to connect the database
#3. using cursor we creat one cursor which we later use to execute the query
#4. data here is always stored in the form of table so we create a table using create table query
#5. we insert data into the table using insert query
#6. we need to get the data from the database using selectquery and fetch all function
#7. if you want to update the data use update query
#8. if we need to delete the data then we need to use delete query

import sqlite3

con=sqlite3.connect("Database.db")#.db function is used for database

csrs=con.cursor()

#table name is always related to what data we storing and we create column
# also what adta is coming come interface. in our tkinter we hav e5 entrybox
#staff no, f name, lname, gender, DOJ.  data we enter in the entrybox is stored in database.
#so w ecreate 5 columns. for all five columns we give data type
#data type  in db : integer, text, varchar(100) number limit.
#if data has number, special character, alphabets : varchar
sql="""
create table if not exists emp(
staff_number integer,
f_name text,
l_name text,
DOJ varchar(100),
gender text
)
"""
#the above query will not create a table unless we do not do the next step that exceutimg using cursor.
#cusror is like to put final attempt on it.

csrs.execute(sql)
#after writing every query use this to save. commit is used to save all changes done permantely
con.commit()

def inset1():
    #here we put data from entryboxe to table
    #first we get the data from entry in a variable
    #then we use insert query to insert the data in table
    #the data we got in a variable we give to insert to put it in a table. we cant directly put the data so we use ? as a temporary value for the data and later on we combine it with a variable
    a=e1.get()
    b=e2.get()
    c=e3.get()
    d=e4.get()
    e=e5.get()
    sql="""
insert into emp(staff_number,f_name,l_name,DOJ,gender) values(?, ?, ?, ?, ?)
"""
    csrs.execute(sql,(a,b,c,d,e))
    #after writing every query use execute and commit
    con.commit()

def Get_Details():
    #first we get the ID of the employee whos details we need to search from the entrybox, e6 is the inside which we'll enter the ID of who's details we need to search.
    l=e6.get()
    #then we use a select Query to select the detail of only that person whos ID has been entered in the entrybox and then use fetch all function to get all the details
    #and then using label diplay on screen
    csrs.execute("select * from emp where staff_number = ?",(l,))
    r=csrs.fetchall()
    #r is a list so we use for loop to get the data and label to display on screen.
    f=""
    for i in r:
        f=str(i[0])+"\n"+i[1]+"\n"+i[2]+"\n"+i[3]+"\n"+i[4]+"\n"
        #\n is used for a new line
    l6.config(text=f)
def Edit():
    #write tabelname, set word, column names. ? is temporray value
    #we get all entry data in variable and pass variable below
    a=e12.get()
    b=e23.get()
    c=e33.get()
    d=e44.get()
    e=e56.get()
    original=e6.get()
    csrs.execute("update emp set staff_number=?, f_name=?, l_name=?, DOJ=?, gender=? where staff_number=?", (a, b, c, d, e, original))
    con.commit()
    
def Update():
    #here we create second screen with five labels and 5 entryboxes as first screen and then by using the fetchall we get the details and put it in these entryboxes
    screen2=Tk()
    global e12,e23,e33,e44,e56
    l12=Label(screen2, text="Staff Number", font=("Arial", 25))
    l12.grid(row=0, column=0)
    e12=Entry(screen2, bg="White", fg="Black", font=("Arial", 25))
    e12.grid(row=0, column=1)
    l23=Label(screen2, text="First Name", font=("Arial", 25))
    l23.grid(row=1, column=0)
    e23=Entry(screen2, bg="White", fg="Black", font=("Arial", 25))
    e23.grid(row=1, column=1)
    l34=Label(screen2, text="Last Name", font=("Arial", 25))
    l34.grid(row=2, column=0)
    e33=Entry(screen2, bg="White", fg="Black", font=("Arial", 25))
    e33.grid(row=2, column=1)
    l44=Label(screen2, text="Gender",font=("Arial", 25))
    l44.grid(row=3, column=0)
    e44=Entry(screen2, bg="White", fg="Black", font=("Arial", 25))
    e44.grid(row=3, column=1)
    l55=Label(screen2, text="date of joining", font=("Arial", 25))
    l55.grid(row=4, column=0)
    e56=Entry(screen2, bg="White", fg="Black", font=("Arial", 25))
    e56.grid(row=4, column=1)
    button=Button(screen2, text="Update", fg="Black", bg="White", font=("Arial", 25), command=Edit)
    button.grid(row=5, column=0)
    l=e6.get()
    csrs.execute("select * from emp where staff_number = ?",(l,))
    r=csrs.fetchone()
    
        #insert is a function which is used to insert and delete is a function to delete the data from the entryboxes
    e12.insert(0,r[0])
    e23.insert(0,r[1])
    e33.insert(0,r[2])
    e44.insert(0,r[3])
    e56.insert(0,r[4])


def delete():
    #enter Staff_number in e6 the one whose data we want to delete
    #write tablename, tehn write columname which detail we added in e6
    a=e6.get()
    csrs.execute("delete from emp where staff_number=?", (a, ))
    con.commit()


from tkinter import *
screen=Tk()
screen.title("Employee software")
screen.geometry("700x800")
screen.configure(bg="White")
l1=Label(screen, text="Staff Number", font=("Arial", 25))
l1.grid(row=0, column=0)
e1=Entry(screen, bg="White", fg="Black", font=("Arial", 25))
e1.grid(row=0, column=1)
l2=Label(screen, text="First Name", font=("Arial", 25))
l2.grid(row=1, column=0)
e2=Entry(screen, bg="White", fg="Black", font=("Arial", 25))
e2.grid(row=1, column=1)
l3=Label(screen, text="Last Name", font=("Arial", 25))
l3.grid(row=2, column=0)
e3=Entry(screen, bg="White", fg="Black", font=("Arial", 25))
e3.grid(row=2, column=1)
l4=Label(screen, text="Gender",font=("Arial", 25))
l4.grid(row=3, column=0)
e4=Entry(screen, bg="White", fg="Black", font=("Arial", 25))
e4.grid(row=3, column=1)
l5=Label(screen, text="date of joining", font=("Arial", 25))
l5.grid(row=4, column=0)
e5=Entry(screen, bg="White", fg="Black", font=("Arial", 25))
e5.grid(row=4, column=1)
b1=Button(screen, text="Add Record To Database", font=("Arial", 25), command=inset1)
b1.grid(row=5, column=0)
b2=Button(screen, text="Query The Database", font=("Arial", 25), command=Get_Details)
b2.grid(row=6, column=0)
b3=Button(screen, text="Update Database", font=("Arial", 25), command=Update)
b3.grid(row=7, column=0)
b4=Button(screen, text="Delete Database", font=("Arial", 25), command=delete)
b4.grid(row=8, column=0)
e6=Entry(screen, bg="White", fg="Black", font=("Arial", 25))
e6.grid(row=9, column=0)
l6=Label(screen)
l6.grid(row=10, column=0)
mainloop()


#create student app id, name, marks, phone number, age. labels and entry of all. 4 buttons add, update, search, delete.
#connect with database. create table. add function to insert data, get details function,update function, delete function.



