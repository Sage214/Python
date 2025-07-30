while True:
    input1=input("Enter your digits or type 'over' to stop")
    if input1 == "over":
        print("Program stopped")
        break
    else:
        print(input1[::-1])
list1=[]
while True:
    input2=input("Enter the correct password")
    if input2 == "Computer":
        print("Program stopped")
        break
    else:
        list1.append(input2)
        print(list1)
        continue