class Student:
    def __init__(self,name, School_information):
        self.name=name
        self.School_information=School_information
    def Average(self):
        Math_Grades=int(input("Enter your Math grades"))
        Science_Grades=int(input("Enter your Science grades"))
        English_Grades=int(input("Enter your English grades"))
        Average_Marks=Math_Grades+Science_Grades+English_Grades/3
        print(Average_Marks)
class workingstudent(Student):
    def __init__(self, salary, name, School_information):
        self.salary=salary
        Student.__init__(self,name,School_information)
    def Marks(self):
        Student.Average(self)
object1=workingstudent(100, "Jhon", "Millstone River School")
print(object1.name, object1.School_information)
object1.Marks()