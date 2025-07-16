from tkinter import *
screen=Tk()
screen.title("Calculator")
screen.geometry("1000x750")
screen.configure(bg="Dark Blue")

#for spacing we use : ipadx, ipady  inside from left side and top. outside box padx and pady
#textbox :Entry
s=StringVar()
global expression
expression=""

#-------------------------------4 functions------------------------------------------
#one function  when we press any no/ sign it goes in entrybox 
def press(num):
    global expression
    # we put numbers/ sign in tkinter variable firts and from there it goes to entrybox
    #s.set(1) if w edo like this then w ehav eto create seperate function for all numbers and sign
    # that will be very big.
    # so w euse only one function for this  instead of writing any number or sign we use variable 
    # and later varoable is replaced by actual value
    expression += str(num)# here w e join new number pressed with previous number
    #expression is previous numberand num is new number
    s.set(expression) # w e put in tkinter variable s and it goes to entrybox



#second function when we press = then operation is performed
def equal():
    global expression # eval() inbuilt function wil perform all actions such a s+, -, *, /
    # so wegive no. sign to eval(). expression variable has it
    r=eval(expression)
    s.set(r) # give ans to s to goes to a entry
    expression=""



#third function when we press clear button evrything gets cleared from entrybox
def clea():
    global expression
    expression=""
    s.set(expression)#



#convert number + sign to -
def minusplus():
    global expression
    expression=expression*(-1)
    s.set(expression)






#------------------------------------call functions---------------------------------------
#Two ways to call function
#1. Function whcih has no variable in () : def functioname():
#command=functioname

#2. Function with variable in () : def functioname(variablename):
#command=lambda : functioname(valu)

#---------------------------------tkinter Variable----------------------------------------
#tkinter vraiable also store data but on which comes from tkinter widget such as text entered in entrybox
# whcih comes from tehre can be stored in tkinter variable. any input given through widget can be store in 
#these tkinter variable  if we have created. StringVar(), IntVar(), DoubleVar(), BoolVar().
#syntax for tkinter variable : varoablename=function
#eg : if text is coming we : s=StringVar().
#connect the tkinter vraiable with widget  textvariable or variable=varoablename

#Benefit of tkinter variable:
#anything we put in entrybox can automatically come here in tkinter vraiable and vice versa
#anything we put in tkinter variable it goes to entrybox

#--------------------------------------
#because although we enter no in Entrybox but we cannot write DoubleVra() or IntVar() because Entrybox
#always take data as text. so no are string

a=Entry(screen, width=80,bg="black" , textvariable=s)#no height, for height : ipady
a.grid(row=0, column=0, columnspan=4 , ipady=30)#this combines 4 columns in 1. 4 columns will be under entrybox
b1=Button(screen, text="AC", fg="White", bg="Gray",font=("SF Pro", 20), width=6, height=2, command=clea)
b1.grid(row=1, column=0)

b2=Button(screen, text="+/-", fg="White", bg="Gray", font=("SF Pro", 20), width=6, height=2, command=minusplus)
b2.grid(row=1, column=1)

b3=Button(screen, text="%", fg="White", bg="Gray", font=("SF Pro", 20), width=6, height=2, command=lambda: press("%"))
b3.grid(row=1, column=2)

b4=Button(screen, text="7", fg="White", bg="Black", font=("SF Pro", 20), width=6, height=2, command=lambda: press("7"))
b4.grid(row=2, column=0)

b5=Button(screen, text="8", fg="White", bg="Black", font=("SF Pro", 20), width=6, height=2, command=lambda: press("8"))
b5.grid(row=2, column=1)

b6=Button(screen, text="9", fg="White", bg="Black", font=("SF Pro", 20), width=6, height=2, command=lambda: press("9"))
b6.grid(row=2, column=2)

b7=Button(screen,text="4", fg="White", bg="Black", font=("SF Pro", 20), width=6, height=2,command=lambda:press("4"))
b7.grid(row=3, column=0)

b8=Button(screen, text="5", fg="White", bg="black", font=("SF Pro", 20), width=6, height=2, command=lambda:press("5"))
b8.grid(row=3, column=1)

b9=Button(screen, text="6", fg="White", bg="Black", font=("SF Pro", 20), width=6, height=2, command=lambda:press("6"))
b9.grid(row=3, column=2)

b10=Button(screen, text="1", fg="White", bg="Black", font=("SF Pro", 20), width=6, height=2, command=lambda:press("1"))
b10.grid(row=4, column=0)

b11=Button(screen, text="2", fg="White", bg="Black", font=("SF Pro", 20), width=6, height=2, command=lambda:press("2"))
b11.grid(row=4, column=1)

b12=Button(screen, text="3", fg="White", bg="Black", font=("SF Pro", 20), width=6, height=2, command=lambda:press("3"))
b12.grid(row=4, column=2)

b13=Button(screen, text="0", fg="White", bg="Black", font=("SF Pro", 20), width=13, height=2, command=lambda:press("0"))
b13.grid(row=5, column=0, columnspan=2)

b14=Button(screen, text=".", fg="White", bg="Black", font=("SF Pro", 20), width=6, height=2, command=lambda:press("."))
b14.grid(row=5, column=2)

b15=Button(screen, text="/", fg="White", bg="Orange", font=("SF Pro", 20), width=6, height=2, command=lambda:press("/"))
b15.grid(row=1, column=3)

b16=Button(screen, text="X", fg="white", bg="orange", font=("SF Pro", 20), width=6, height=2,command=lambda:press("*"))
b16.grid(row=2, column=3)

b17=Button(screen, text="-", fg="white", bg="orange", font=('SF Pro', 20), width=6, height=2, command=lambda:press("-"))
b17.grid(row=3, column=3)

b18=Button(screen, text="+", fg="white", bg="orange", font=("SF Pro", 20), width=6, height=2, command=lambda:press("+"))
b18.grid(row=4, column=3)

b19=Button(screen, text="=", fg="white", bg="orange", font=("SF Pro", 20), width=6, height=2,command=equal)
b19.grid(row=5, column=3)
mainloop()

#------------------------------------------Assignment----------------------------------------
#create a  login page  with username label and entrybox. password label and entrybox. signinbutton, email label, email box, confirm password label, and confirm password box
