class employee:
    def __init__( self,Name, Age, ID_details, Salary, Position, Bonus, Timeings):
        self.Name=Name
        self.Age=Age
        self.ID_details=ID_details
        self.Salary=Salary
        self.Position=Position
        self.Bonus=Bonus
        self.Timeings=Timeings
    def Increase_Salary(self):
        self.Salary=self.Salary+3000
        print("New Salary", self.Salary)
    def Promote_to_Another_Position(self):
        changeposition=input("What Position do you want to change to?")
        self.Position=changeposition
        print("New position", self.Position)
    def In_Time(self):
        Time=int(input("Time to come"))
        if Time>9:
            print("Late")
        else:
            print("On Time")
Object1=employee("Jhon", 34, "Sales person", 400, "Sales person", 3000, 9)
Object1.Increase_Salary()
Object1.Promote_to_Another_Position()
Object1.In_Time()