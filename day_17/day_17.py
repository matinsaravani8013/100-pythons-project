import random
class Quiz():
    def __init__(self,text,answer):
        self.text=text
        self.answer=answer
    def show(self):
        print(f"your quiz is {self.text}")
q1=Quiz("2+2=5","false")   
q2=Quiz("3+4=7","true")   
q3=Quiz("10*10=100","true") 
my_list=[q1,q2,q3]
for i in my_list:
    pass
    
