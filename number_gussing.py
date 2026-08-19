import random

number= random.randint(1,100)
attempts=0
while True:

    user=int(input("Enter a Number: "))
    attempts+=1

    if number ==  user: 
        print("Correct! Attempts:",attempts)
        
        
        break
        
    elif user < number  :
        print("TOO High")
       

    else:
        print("Too Low")
        

    
