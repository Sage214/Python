a=0
b=1
c=1
while c<=10:
    print(a)
    t=b # we store value of b in  t (previous value) 
    b=a+b # here b update to sum of two variables (new value)
    a=t # we store give t to a (previous value given to a)
    c+=1