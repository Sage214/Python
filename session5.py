#--------------------------Tuple-------------------------------------------
#Tuple is used to store data  like list. it can also store infinite data. Every data has index value over here whic starts from 0.
#Tuple we cannot add or delete data later. it is fixed once it is created.
#unlike list where w ecan add or delete the data. () is used

#syntax to create tuple : variablename/tuplename=(data1, data2....)
tp=(1, 2, 3, 4, 5, 6,"hello", True)
#Indexaing is there
print(tp[2])

#-----------------------Different Tuple functions are -----------------------
#1. count() : count no of times  data is repeating
tp=(1,2,1, 1, 1, "hello")
a=tp.count(1)
print(a)

#2. index() : gets index value of data
r=tp.index("hello")
print(r)

#3. max() and min() : . max means maximum. min means minimumbiggest number and smallest num. only work for number list
tp1=(10, 12, 557, 89, 90)
t=max(tp1)
print(t)
t1=min(tp1)
print(t1)

#4. sum() : find the sum of all numbers. only works number tuple/list
s=sum(tp1)
print(s)

#----------------------------Dictonary----------------------------------
#Dictonary is also used to store data but main difference is it stores two things data and keys(meaning of data we are storing).
#its like real life dictonarys we have words  and meanings of those words. similary here also we have 
#data and meaning of that data(called as keys)
#{} is used
#syntax  for dictonary : dictonaryname={}
#keyname: data1,
#keyname:data2,
#-----
#List
John_info=["John", 12, 100, "New York"]

#Dictonary
john_info2={
'name':"John",
  "Age" :12,
    "marks":100,
    "city" :"New york"
}

print(john_info2)

#-----------------------use keyname to get specific data----------------------------
#syntax to get specific data through keyname : dictonaryname["keyname"]
#get New York
print(john_info2["city"])

#----------------------Functions in dictonary-----------------------
#1. keys() : gets all keys
print(john_info2.keys())

#2. values() : get all values
print(john_info2.values())

#3. add new data
john_info2["country"]="USA"
print(john_info2)

#4. replcae to chnage any information/data
john_info2["name"]="riya"
print(john_info2)

#5. pop() to delete specific data
john_info2.pop("Age")
print(john_info2)

#6. get() : used to get specific data
r1=john_info2.get("name")
print(r1)

#7. copy() : copy dictonary
r2=john_info2.copy()
print(r2)

#-------------------------Nesting of list, tuple, dictonary------------------------
a=[1,2 ,3 , "hello", {"name":"riya", "marks":(100, 200, 300, 1000)}]
#get 1000
#we have solve every bracket one by one. whatever bracket comes we have to write index value or keyname
#remember new barcket means new index value
print(a[4]["marks"][3])

b={"name":"John", 'marks':[100, 200, {"english":[12, 13, 30]}]}
#print 30 
print(b['marks'][2]["english"][2])

c=[1, 2, 3, "hello", ['marks', [100,200]]]
#print 100
print(c[4][1][0])