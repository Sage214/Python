#Functions
#Function used to do some work. there are 2 type of functions in python.
#1. intel functions
#intel functions are those functions which are already there in python. like input(), print()
#We don't have to create them. they're already created by python we just need to call them.
#2. user defined functions
#This is when we want to create our own functions.
#creating your own function means grouping or storing the lines of code in a function.
#its just like variables. like in variables we are only storing one value.
#here we store lots of lines of code.
#Reason for storing the code or creating the function
#1. if there are ome lines of code which we want to use later, then rather than copy pasting, we can store that code in a function, give a name to it, and whenever you want to copy it or use it we can call the function.
#this means re-using the same code again.
#2. your code becomes more organized if we group it together.
#exm: if we have a game and it has 300 lines of code written, and we are searching for the game over code, then it might be time taking to search for it.
#but if we put all the code in diffrent functions. Like 1 function where you put game over code, 1 function where we put all the player code, etc... then searching becomes very easy.
#please note: there will be no change in the output before or after using the functions.
#syntax to creat a function:
#def functioname():
#   code

#syntax to call the function : 
#functioname()

#---------------------------------------Example-------------------------------------------------------
#1. create a function with the name of even inside that take the input from the user, check if the number given is an even number, then print it is an even number. else print its an odd number.
def even():
    a=int(input("Enter your number"))
    if a % 2==0:
        print("It's an even number")
    else:
        print("It's an odd number")
even()
even()
#2. create a function with the name hello, which will have list inside that, use for loop, and get the data and print it on screen.
def hello():
    a=[100,200,"hello", "jhon", 1,2,3,4,5,6,7,8,9]
    for b in a:
        print(b)
hello()
#Example 3: create a function with the name of hi, take the input from the user, a word, reverse the word, check if the given word is a palendrom then print its a palendrom, else print its not a palendrom.
def hi():
    b=input("Enter your word")
    r=b[::-1]
    if b==r:
        print("its a palendrom")
    else:
        print("its not a palendrom")
hi()
#find out the square root of a number, to find out the square root of a number, we have the SQRT function in math library.
# to find perfect square we do two things
# first square root of number and check number gotten is an integer
#so sue sqrt() from math librray and then use is_integer()
#import math
#a=math.sqrt(b)
#if a.is_integer: print
#else