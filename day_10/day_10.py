print("welcome to day 10")
print("this project is a calculator")
def calculator():
     num_1=int(input("enter your first number: "))
     print(num_1)
     op=input("enter your operator:(*,/,+,-) ")
     print(op)
     num_2=int(input("enter your second number: "))
     print(num_2)
     if op =="*" :
          print(f"{num_1} {op} {num_2} = {num_2 * num_1}")
     elif  op =="+" :
          print(f"{num_1} {op} {num_2} = {num_2 + num_1}")
     elif op =="/" :
          print(f"{num_1} {op} {num_2} = {num_2 / num_1}")
     elif op =="-" :
          print(f"{num_1} {op} {num_2} = {num_2 - num_1}")
     else:
          print("invalid")            
    