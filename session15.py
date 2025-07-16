#Today we'll be learning about the file handeling libraries
#These are those libraries which have functions Which helps us to perform diffrent functions like creating a file, delete a file
#copying things from one file to another.
#we usually do all these things manually, now we'll do with the help of the functions.
import os
import shutil
#1. opening a file and reading what is there inside the file using function
#file=open("demo.txt","r")#open function opens the file and r is read which gets the data from the file
#print(file.read())
#2. opening a file making changes inside the file for using fuction
#file=open("demo.txt", "a")#open will open a file, and a means append, it will add the data into the file.
#file.write("I am 15 years old and am in a champions league")
#3. copy is used to copy the data from one file to another.
#shutil.copy("demo.txt", "demo1.txt")
#4. move funtion moves everything from one file to another and deletes the previous file
#shutil.move("demo.txt", "demo1.txt")
#5. use remove to delete
#os.remove("demo1.txt")
#--------------------------------------------exceptional handeling--------------------------------------------------
#this means handeling exceptional errors. Syntax errors can be solved but sometimes, the program or the app does not work
#due to some other diffrent errors or something went wrong on the user site, these errors are not syntax errors.
#What things might happen: user is searching for a fil, but that file is not there,/0 dividion error
#internet issue, memory full, system issue, etc...
#These things MIGHT happen to the users site, and program might not work.
#we can not stop these errors, but we can make sure that instead of displaying the big error message, we just print a simple message
#if anything goes wrong a big error sign will come on the users site, and user might get scared.
#So, we can display a simple message, instead of this, using try and accept.
#syntax for try and accept:
#try:
#   code
#except:
#   message
#In the try, we put that code which we think might create an issue. If there is no issue, try again gets executed
#and is the error comes, except will get executed
try:
    a=3
    b=0
    print(a/b)
except:
    print("please try again without 0")