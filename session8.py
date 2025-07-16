while True:

    q1=int(input("Enter your First number"))
    q2=input("Enter the sign you want to use")
    q3=int(input("Enter your second number"))
    if q2=="+":
        print(q1+q3)
    elif q2=="-":
        print(q1-q3)
    elif q2=="*":
        print(q1*q3)
    elif q2=="/":
        print(q1/q3)
    ask=input("Enter if you want to continue")
    if ask=="yes":
        continue
    else:
        print("Thank you for using the app")
        break