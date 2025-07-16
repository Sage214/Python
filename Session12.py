#--------------------------Inheritance----------------------------------------------------------------
#Inheritance means  in real life when children take something from parents.
#in coding inheritance has teh same meaning. so lets say we are creating a class
# The variables and functions inside that class  we want to create are already 
#created earlier in previous class. One way is we can create once again thoe functions, variables in new class.
#The second way is we can take from the previous class where w ealready created it as this will makecode
#shorter and save time.

#so if one class wants to take things(functions and variables) from other class then we have to
#connect these two classes first by establishing a relationship between them. like in real
#life preants and children have relationship that is why children takes from parents.
#so declare or tell the second class who wants to take things is child class and first class is parent class 
#now child class can take anything fro parent class(previous class).

#in simple words if one class wants to take things from  other class. the tell this is child class and 
#other class is parent class. after that second class can  take everything from first class

#Advantages of inheritance :
#1. saves time as we do not have to create same functions, variables again
#2. makes code shorter

#------------------------------connect two classes------------------------------------------
#class class1:

#class class2(class1):

#We only have to write name of class 1 in () of class 2

#------------------------Transfer all variables from first class to second class---------------------
#syntax to transfer variables on init function
#call init fuction in second class
#firstclassname.__init__(self, variables)

#synatx to transfer or call function
#firstclassname.functioname()

#--------------------------------------------------------------------

#Example : create  one teacher class which has attributes : name, age. create function marks to calculate average marks.
#create a student class (child class) here create attributes  : id, schoolinfo. 

class teacher: # parent class
    def __init__(self,name, age):
        self.name=name
        self.age=age

    def marks(self):
        math=int(input("Enter math marks"))
        science=int(input("Enter science marks"))
        english=int(input("Enter english marks"))
        average=math+science+english
        print("Marks : ", average)



class student(teacher): # child class
    def __init__(self, id, school, name, age):
        self.id=id
        self.school=school
        #transferring variables from init function by calling
        teacher.__init__(self, name, age)

    def average_marks(self):
        #transfer or call function from previosu class 
        teacher.marks(self)


#create object of child class
student1=student(1, "St marry", "Riya", 12)
print(student1.name, student1.id, student1.age, student1.school )
student1.average_marks()


#----------------------------Polymorphism---------------------------------------------------------
#sakshi.rampal@codevidhya.com