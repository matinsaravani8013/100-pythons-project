import random
print("welcome to day 12")
print("do you like play?")
user=input("enter (yes) for play and (no) for exit: ")

def Number():
    print("welcome to number choose play")
    print("I chose a number in my mind, can you guess it? ")
    computer_number=random.randint(1,100)
    print(computer_number)
    at=5
    while at>0:
        print(f"your attempts({at})")
        user_number=int(input("enter your number: "))
        if computer_number==user_number:
            print("very good")
            return    
        else:
            print("you lose") 
            at-=1   
if user=="yes":
    Number()
else:
    print("good bye")    