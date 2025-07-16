#-----------------------------While loop------------------------------------------
#while loop helps to repeat the same code over and over. if we manually repeat the or type the same code.then it might take some time and make the  code
#bigger
#while loop saves times and make code shorter.
#4 imp things which we need to give in while loop
#1. start point : when loop begins : create variable and store start value in that.
#2. ending point : here we mention number how many times loop will repeat. sometimes there can be infinite loop as well.
#3. code to repeat we have to tell once what is the code we need to repeat.
#4. inccreament. increasing the variable value so that it can reach to end. its like a counting

#eg : if a user needs to do a task again n again then there will be 4 things which user needs to know.
#1. what is the task
#2. when to start
#3. when to end.
#4. counting


#syntax for while loop:
#variable=startvalue
#while variable<=valuetostop:
#  code to repeat
#  increament
#there above 4 things which we do in real life are same as 4 things which are used in while loop.

#Example : print all even numbers between 2 to 100

#start point
a=2
while a<=100:# means our while loop will repeat till the time a is less than equal to 100, when condition becomes false means when a>100 the loop stops.
#till the time condition is true  or happens loop goes on
#code to repeat
   print(a)
   #increament
   a+=2

#Example 2 :print square of numbers from 2 to 30
b=2
while b<=30:
   print(b*b)
   b+=1

#Example 3 :find the factorial of 9
c=1
fact=1
while c<=9:
   fact*=c
   c+=1
print(fact)
#break and continue
#Break is used to completly stop the infinite loop.
#Continue is stop the loop but then again it restarts.


#Example 4 : infinite loop is done with the help of True we do not give any ending point so it never
#print hello infinite times

d=1
while True:
    print("hello")
    d+=1
    if d==13:
        break

#Example 5 : continue stops at condition given but again restarts after that.
#print all numbers from 1 to 10 except 3 and 8

e=0
while e<=9:
    e+=1
    if e==3 or e==8:
        continue
    print(e)

#---------------------------fibnocci series----------------------------
#0 1 1 2 3 5 8  13 21 34..
#fibnonci series means when we total two number and its answer is added to previous number and we keep on doing