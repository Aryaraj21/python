def Ls2():
    a=int(input("Enter a:"))
    b=int(input("Enter b:"))
    if a>b:
        print(a,">=",b)
    elif a<b:
        print(b,">=",a)
    else:
        print(a,"=",b)

Ls2()


    

def Ls3():
    a1=int(input("Enter a:"))
    b1=int(input("Enter b:"))
    c1=int(input("Enter c:"))
    largest=a1
    if b1>largest:
        largest=b1
    if c1>largest:
        largest=c1
    print(largest)

Ls3()



def Ls3():
    a2=int(input("Enter a:"))
    b2=int(input("Enter b:"))
    c2=int(input("Enter c:"))
    smallest=a2
    if b2<smallest:
        smallest=b2
    if c2<smallest:
        smallest=c2
    print(smallest)

Ls3()
if largest==smallest:
    print("All values are same")
else:
    print(largest,"Largest",smallest,"smallest")
    



