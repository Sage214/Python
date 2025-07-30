#--------------------------Strings-----------------------------
#Strings are the data type which has all chrcaters like text, numbers and special characters.
#" " or ' 'to write
a="hello"
print(a)
b="World"
#+ sign is to join two strings
print(a+b)

#Note : if we put + sign between a string and a number error comes.
c=3
c=str(c)
print(b+c)

#-----------------------Index value--------------------------
#Index value means position number given to every alpahbet in string. when string is created it is by default given.
#index value or position number count starts from 0, 1, 2,....
#so alpahbet which comes first is at 0 position, and alpabet comes next at 1 and so on....
#if there is space in sentence in string then it is also counted a son index value

#Reason for indexing : we can get specific alpahbets with index value if we do not want whole string
#syntax to use : variablename[indexvalue]

print(a[2])
#get o

print(a[4])

#------------------String functions----------------------------
#1.capitalize() : it make sthe first letter of string capital only
a="this is good"
b=a.capitalize()
print(b)
#2. lower() : converts all alphabets to small letters
d="THIS IS gooD"
e=d.lower()
print(e)

#3. upper() :converts all to capital
f=e.upper()
print(f)

#4. replace() : used to replace word in sentence
r="I love coding"
f=r.replace("coding", "maths")
print(f)

#5. index() : it tell the position or index value number via alphabet
r1="Python is object-oriented programming language with lot of libraries in that"
r2=r1.index("r")
print(r2)

#6. split() :split() seperates words in sentence and form a list
r3="hello reyansh you are doing good"
r4=r3.split()
print(r4)

#7. reverse a string :  ::-1
print(r3[::-1])
#8. isnumeric() : check if chrcaters are numerals. if they are ir returns answer True else False
ss="67868"
s2=ss.isnumeric()
print(s2)

#9. endsWith() : check if string ends with given alphebets or not. returns True else False
s3="Hello world"
s4=s3.endswith("ldd")#False
s4=s3.endswith("ld")#True
print(s4)

#10. startswith : checks if string starts with guven alphabet returns True else False
s5=s3.startswith("He") #True
print(s5)

#11. find() : if we seraching for any word or alphebet. it returns position or index number
s6="this is nice dress"
s7=s6.find("nice")#returns n index position value
print(s7)


#----------------------------Slicing-----------------------------------
#Slicing means deleting some apahbets from left side or right side or from middle
#from left side : variablename[no of alpahbets need to be deleted :]
s="World"
#delete 3 alphebets from left side
print(s[3:])

#from right side : variablename[ : no of alphbets wants to keep from left side]
#delete 3 alpahabets from right side 
print(s[:2])

#Negative slicing
#if we put negative number before : it gives the alpahbet from right side according to number
#2 means : 2 alpahbets from right side
print(s[-2:])

#if we negative number after : it deletes the alpahebt from right side 
#below deletes 1 alphabet from right side
print(s[:-1])
