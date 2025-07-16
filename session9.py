#------------------------For loop---------------------------------------------------
#For loop is used to get data from data structure or where we ahve lot of data  like strings, list, tuple, set, dictonaries.
#We already have index value for list, strings, tuple to get/fetch data and dictonaries ahve keys to fetch data.
#they allow us to fetch data one by one menas if we need to get all data from list we have to write index number of all of them.

# we have 300 data in list and we need to get all. if we use index number tehn itw oudl be time taking and make 
#code bigger so we use for loop to get all data quickly.

#index value/ keys are useful when w e want only few things from list and dictonary

#-------to get one or two data use index value/keys--------------
#but to get all data from list/dictonary etc.. use for loop it will be quick and make code shorter.

#-----------why it is called as loop----------------
#as for loop gets data from list one by one in rounds doing the same thing quickly this is why it is called as loop

#syntax to use for loop : for variablename in listname:
#variable goes inside the list and gets all data one by one by one

list1=["hello", 12, 13, 100, "this is good"]
for i in list1:
    print(i)# first it will go inside and bring hello, after bringing it prints hello on screen,
    # the again goes inside and brings 12 and prints so on....

#Example : craete a list with numbers, get all data  and check whcih one out of that is even or which one is odd
number=[12, 100 ,300, 400, 600, 12, 34, 78, 56, 23, 30]

for j in number:
    if j%2==0:
        print(j, "is even") # first brings 12, divide 12 by 2 to check, the brings 100, again check 
    else:
        print(j, "is odd")

#Example : create a tuple with nummbers in them. check if those numbers ae greater tahn 18 then print you will go to university else print you will not

number1=(13,6,25,4,78,96,15,35,2,46,9,7,2,6,5,4,25)

for g in number1:
    if g>18:
        print(g, "you will go to university")
    else:
        print(g, "you will not go to university")
#Example: Use for loop to get all the numbers and add them up.
sum=0
for g in number1:
    sum+=g
print(sum)
#Break and continue keywords can be used in for loop.
#Break is used to completly stop the loop so it won't get all the data.
#Continue will stop at one point, and it won't get that perticular data where it stops because it restarts again and will get all other datas.
list2=["Jhon", "emily", "Raz","Tara","loran"]
for f in list2:
    print(f)
    if f=="Tara":
        break
for f1 in list2:
    if f1=="emily":
        continue 
    print(f1)

#---------------------------------random library----------------------------------
#library are python files inside which  we have pre written functions by some one else whcih 
#whcih w ecan use it in our code to make things easier. thse function were not creared when python we created
#they were creaed later by different people so to use them w ehave to first connect with there python files or library using
#import keyword

#library or file name is random
import random

#randint() : to generate any random number between given range

a=random.randint(1, 300) # it can generate any number and store in a
print(a)

#---------------------------Assignment-----------------------------------------
#craete a variable and generate a random number between 1 to 6. check if number is equal to 6 then print
#you won the dice game else print you did not won the dice game.
#craete a list of  any random numbers(100, 200, 300, 400, 500, 600, 700, 800,900, 1000, 1100). apply for loop to add all numbers 
#skip 600 and 700 (use continue)

