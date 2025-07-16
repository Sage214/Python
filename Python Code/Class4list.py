#-----------------------List-----------------------------------------------------------
#List allows variables to store lot of data all together infinite data. so firts w ecreate variable and then convert it to list
# in order to store lot of data in it. we give [] to convert it into list. we put data seperated by commas
# we can put any data over here in list strings, numbers, boolean value etc...
#syntax to create list : vraiablename/listname=[]

list1=[1, 2, 3, 4, "hello", True]
print(list1)

#----------------------Index value/position number----------------------
#every data has index value given which starts from zero, followed by 1, 2 and so on...

#Why do w eneed to index value
#if we want to get specific data from list
#syntax to get through index value : listname[indexvalue]
#get hello from list
print(list1[4])

#---------------------------Functions in list-------------------------
#1. append() : add data in list later without making chnages to above from right side
list1.append("good")
print(list1)

#2. pop() : deletes data from right side
list1.pop()
print(list1)

#3.sort
#used to solve the data alphabetically and in number order for sorting to be used either list should be all strings or all numbers
list2=[23, 100, 200, 120, 300, 400, 12, 13]
list2.sort()
print(list2)

list3=["ab", "hello", "yellow","qw", "tyu", "o"]
list3.sort()
print(list3)

#4. reverse() : used to reverse the list
list3.reverse()
print(list3)

#5. remove() : it deletes specific data
list3.remove("o")
print(list3)

#6. insert() : insets data at specific position
list3.insert(2, "orange")# and whatveer is at 2 index value will shift to next index value that is qw
print(list3)

#7. count() : counts the number of times specific data appears.
list4=["hi", "hello", "hi", "hi", "good"]
a=list4.count("hi")
print(a)

#8. index() : get index value of data we give
a=list4.index("hello")
print(a)

#9. copy() : copy the list
b=list4.copy()
print(b) # in b it has all list4 data

#10. max() and min() : . max means maximum. min means minimumbiggest number and smallest num. only work for number list
tp1=(10, 12, 557, 89, 90)
t=max(tp1)
print(t)
t1=min(tp1)
print(t1)

#11. sum() : find the sum of all numbers. only works number tuple/list
s=sum(tp1)
print(s)
#----------------------------Slicing in list------------------
#delete from left : totalnumberwant to delete:
#keep it from left side : : totalnumberwant tokeep

print(list4[1:])
print(list4[:2])

#delete from right side : -totalnumberwant todelete:
#keep from right side : : -totalnumber
print(list4[-2:])
print(list4[:-1])

#-----------------------------Nesting of List-------------------------
#Nesting means  when something  is inside something. here it is if there is list inside list
#combine the list
list5=[1,2 ,3, 4, 5,6]
list6=[12, 23, 14, 15, 70]
total=list5+list6
print(total)

#nesting of list Example
listt=[[1, 2, 3], [1, 2, 3,5]]
print(listt)

#get 4 from second list
# in two list we first give index value of outer one nad then index value of inner one
print(listt[1][3])
