#-----------------------------operators--------------------------------------------------
#Operators means different signs we will be using it over here.
#1. Arthmetic operator: +, -, *, /(divide the numbers and give answer as quotient), %(modulus :divide two numbers and give answer as remiander)
#2. comparison operator : <, >, <=(less than or equal), >=, ==(to check if two things are equal as = sign is used by variable to store the value), 
#!=(not equal)
#3. Logical operator: or(either of the things should ), and(both should happen), not(nothing should happen)
#4. Assignment operator: +=, -=, *=, /=.
#we assign a vlaue to variable  by adding, sub, multiplying, dividing.

a=3
#add 6 to a
a+=6
print(a)
a*=6
print(a)

#Note : input() will be always converted to int when we use any mathematical sig n on it as input() takes input in text form
#it is string always. we have use either int() or float()
#-----------------------------Conditions-------------------------------------
#Conditions means if we do one thing then another thing happens and if that conditions does not happen then esle will happen
#syntax to use conditions:
#if condition:
#  next thing(give two tabs of space is indentation which is given always to make sure next thing is inside if)
#else: #no indentation means space as else is seperate part)
#  next thing

#syntax to use conditions in multiple condition
#if condition:
# next thing
#elif condition:
# next thing
#elif condition:
# next thing
#else:
#next thing


#Example 1:
#take input from user a number age. check if age is greater than 18 then print you can drive else print you cannot drive

age=int(input("Enter your age"))

if age>18:
    print("you can drive")
else:
    print("you cannot drive")

#Example 2:
#take input from user his favourite subject. check if subject is equal to math then print it is good genius
#else print not so good

Subject=input('Enter your favorite subject')
if Subject == 'Math':
    print("it's good")
else:
    print("it's not so good")

#Example3 : take input as score from user. check if score is between 90 to 100 then print excellent
#else if score is between 80 to 90 then print very good else if score is between 70 to 80 then print 
#good else print not bad

score=int(input("Enter your score"))
if score >=90 and score <=100:
    print("Excellent")
elif score>=80 and score <90:
    print("Very Good")
elif score>=70 and score <80:
    print("Good")
else:
    print("Not Bad")

#in and both condition should happen then next thing will happen.
#in or either of the condition should happen and next thing will happen.
if 5 > 10:
 print("fan")
elif 8 != 9:
 print("glass")
else: print("cream")