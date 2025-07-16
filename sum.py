def A():
    a=int(input("Enter your first number"))
    b=input("Enter wht operation you want to use for the 2 numbers")
    c=int(input("Enter your second number"))
    if b=="*":
        print(a*c)
    elif b=="-":
        print(a-c)
    elif b=="+":
        print(a+c)
    elif b=="/":
        print(a/c)
    else:
        print("No operation entered")
A()