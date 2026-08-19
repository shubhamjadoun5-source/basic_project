while True:
    n1=int(input("Enter a first Number: "))
    n2=int(input("Enter a second number: "))
    operation=input("Enter a Operation (+,-,*,/)")
    if operation == "+":
        sum=n1+n2
        print("Sum(+) :", sum)
    elif operation == "-":
        sub=n1-n2
        print("SUbract(-): ", sub)
    elif operation == "*":
        mul= n1*n2
        print("Multiple(*): ", mul)
    elif operation == "/":
        try: 
            div=n1/n2
            print("Division(/): ", div)
        except ZeroDivisionError:
            print("Cannot Divide by zero")
    else:
        print("Invalid Operation")


    choice=input("Do you want to continue?(yes/no): ")
    if choice=="no":
        break



  
