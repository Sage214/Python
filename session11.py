#classes and objects
#objects:
#objects in coding are exactly same as the objects in real life, like we have so many objects all around us
#everyone having properties and functions
#simalarly, the diffrent objects in coding also have properties and functions
#The reason we use object is for defying those things which need both properties and functionality.\
#eg: player in a game, any reason in a game.
#to create these types of things in coding we need something that gives characterisistics which be often called as properties or attribbutes and functions.
#object is the only way to give both the details.

#---------------------------------------#Class--------------------------------------------------
#like the real life objects, before they are created, designing is done, and then an object is created.
#simmalarly, in coding as well, we first do the designing then the object is created
#desinging in coding is called as class.
#so we first create a class and the we create an object
#there is another definition of class, class is something where we can gruop all function or variables together.
#Eg:
#school-> grades-> students
#class-> functions-> code in every function

#------------------#benifites of creating class----------------------------------------
#1. It is very organnized.
#2. Reusing the same class again. If we want to use all the functions once again, we can use it by calling the class.
#------------------------syntax for creating class----------------:
#class classname:
#--------------------syntax for creating an object-----------------:
#objectname=classname:

#-----------------Syntax for calling the variables-----------------------
#objectname.thevariablename
#------------------------syntax to call function of class----------------------------
#objectname.function
#--------------------__init__ functions------------------------------
#this function is an inbuilt function which is always used inside class. it is used to give all properties
#/variables we give r create here. we use self keyword to crearte thse variables/properties/attributes

#--------------------------------------------------------------------------------
#Eg: Create a class student, with the diffrent properties/variables, like name, email, phonenumber. Create a function of the student marks Where we calculate the avarage marks.
#create another function, change name, where we take the input just new name and then change it with the previous name. Create an object called both the functions.

class student:
    def __init__(self, name,email, phone_number):
        self.name=name
        self.email=email
        self.phone_number=phone_number
    def marks(self):# all function swhoch are inside the class put/give self keyword
        math=int(input("Enter your math marks"))
        science=int(input("Enter your science marks"))
        average=math+science/2
        print(average)
    def changename(self):
        ask_new_name=input("Enter your new name")
        self.name=ask_new_name
        print("New name is", self.name)
student1=student("John", "a@gmail.com", 9789797879) # here we pass all actuall values for variables craeted in init. eg if we have variable name
#the we give name value here. we just created only variables in __init__ and did not gave any actual values there
#so we give here in while creatig object

#print allvalues (optional)
#syntax : objectname.variablename eg student1.name
print("Student name is ", student1.name)
print("Student email is ", student1.email)
print("Student Phone number is ", student1.phone_number)

#call functions
student1.marks()
student1.changename()

