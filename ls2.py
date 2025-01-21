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
    

def even():
    a=int(input("enter your number:"))
    if a%2==0:
        print("it is even")
    else:
        print("it is oddd")

even()

age=int(input("Enter the age of a person:"))
if age<18:
    print("the person is minor")
else:
    print("the person is major")


