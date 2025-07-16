import math
def function():    
    a=int(input("Enter your number"))
    a=math.sqrt(a)
    if a.is_integer():
        print("True")
    else:
        print("False")
function()
def function2():
    empty1=[]
    list1=[1321, 13278, 3732, 237583, 1267, 37438, 2347382,6732, 7438, 27348, 16, 100]
    for i in list1:
        a=math.sqrt(i)
        if a.is_integer() and a%2==0:
            empty1.append(i)
            print("The list of both perect square and even are")
            print(empty1)
function2()
#We need to create 2 strings in a function and
#1. Replace all the occerences of the first character in the string of greater length with the first character of the smaller string
#2. Length of both the strings are same
#3. replace all the small letters with the capital letters.
def Alphabet():
    b = input("Enter your first string: ")
    c = input("Enter your second string: ")

    
    larger = b if len(b) >= len(c) else c
    smaller = c if len(b) >= len(c) else b


    first_smaller = smaller[0]
    first_larger = larger[0]

    replacelarger = larger.replace(first_larger, first_smaller)
    upper1 = b.upper()
    upper2 = c.upper()

    
    print("Modified Larger String:", replacelarger)
    print("String 1 in Uppercase:", upper1)
    print("String 2 in Uppercase:", upper2)


Alphabet()
