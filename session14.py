#-------------------------------------Libraries-------------------------------------------------------
#Libraries means pre written code  in python file frm which has different functions in them.

#--------------------Datetime Library------------------------------------
#It has functions related to date and time.
import datetime

#now : gives current date and time
a=datetime.datetime.now() # datetime is libraryname, second datetime is classname
print(a)

#strftime() : helps extract the specific thing such as week day, day name, day number, month, month in number, eyar, 
#hour minute etc.. to extract all thse things from current time whcih is in a
#we have abbreviations for everythng : eg if we want ti know only yer just write Y and we get year

print(a.strftime("%Y"))
print(a.strftime("%B"))
print(a.strftime("%A"))
print(a.strftime("%H"))
print(a.strftime("%M"))
print(a.strftime("%S"))
print(a.strftime("%y"))
print(a.strftime("%W")) #weeek number
print(a.strftime("%w"))#day in number 4 day of the week
print(a.strftime("%m")) # month in number


#----------------------------collections--------------------------------------------
#collections librray has different  functions whch are sed to collect data.
import collections

#Counter : Count the no of times anything is coming in list, tuple, string
list1=[12, 12, 13, 100, 100, 100, 200, 300, 1000]
print(collections.Counter(list1))

#--------------------------math  library-------------------------------------
#math library has functions related to math
import math

#sqrt() : finds squareroot of number
print(math.sqrt(100))

#factorial : factorial of a number
print(math.factorial(5)) #5x4x3x2x1 =120

#exp : exponent of number
print(math.exp(3))

#pow() : power of number
print(math.pow(2, 3)) # 8

#ceil() : used to get smallest integer rouns off
print(math.ceil(2.33))

#degrees() : angle in radian and ned to convert to degree
print(math.degrees(12))

#radian() : angel in degree and need to conevrt to radians
print(math.radians(100))

#-------------------------------------time-----------------------------------
#It has time functions
#sleep() : it is used to make code wait

#print numbers 1 to 6 with a  wait of 3seconds

import time
a=1
while a<=6:
    print(a)
    a+=1
    time.sleep(3)
#----------------------------------calender------------------------------------------
#it has functions that shows the calender.
import calendar
#month is used to get the calender of a specific month.
print(calendar.month(2027, 8))

#calendar() : for whole year
print(calendar.calendar(2027))
print(calendar.isleap(2030))#returns true if its a leap year else false
print(calendar.weekday(2025, 6, 5))