#----------------------------Data types---------------------------
#dfferent data which w ecan store or assign in variable
#1. Number : Integer/decimal(float)
#2. Strings : " " or ''. all alphabets like text, special characters, numbers
a=3# integer
a="3" # string
#3. Boolean Values : True/False
#First three are single data type : w ecan store only one at one time
#4. List/Tuple/set/dictonaries : they allow variable to store lot of data all together.

#---------------------------Variables--------------
#Variables are used to store datas like strings, numbers, booleans, list etc...
#Rules to create variable or give variable names :
#1. variable name always begin with text . Never start with number
#2. variable name  can never have space. _ can be used between two words for variable 
#eg : 
first_name="John"
#3. no other special character can be used to give name except _
#4. in one variable we can store only one value
#5. give valid or variable name according to value you are storing
#6. variables names are never written in " "


#value is on right side nad variable nam eis on left side.
#syntax to create variable : variiablename=value
#Example 1: create two variables and store 2values in that, calculate average and print answer
num1=6
num2=4
average=(num1+num2)/2
print(average)

#--------------------------------input()------------------------------------------
#input() is used to take input from or ask a question from user and based on that answer something happend.
#input(0 will take answer) from user and we store that answer in name variable

#---------------------------take string input from user------------------------------
#input() always takes answer in text form. so if we want number then convert it into int/float#
f_name=input("Enter your name")
print(f_name)

#-----------------------Concatenation---------------------
#+ sigh between two numbers adds 
# + sign between two strings join them
#" " will give empty space
l_name=input("Enter your last name ")
print(f_name+" "+l_name)
print("f_name")

#-----------------------add two numbers  and calculate average using input()-----------
#convert into int/float only when mathemtical thing needs to be done
n1=int(input("Enter first number"))
n2=int(input("Enter your second number"))
n3=(n1+n2)/2
print(n3)

#-------------------------conevrting data types to each other-----------
#String : str()
#Integer : int()
#Float : float()
#boolean " bool()

#----------------------function to check data type---------------
#type()

#convert int value to string
d=3
print(type(d))
d1=str(d)
print(type(d1))

#convert float to string
e=0.68
f=str(e)
print(type(f))