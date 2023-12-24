from turtle import *
tim=Turtle()
screen=Screen()
def move_forward():
    tim.forward(10)
def move_backward():
    tim.backward(10)    
def turn_left():
    new_hed=tim.heading() +10
    tim.setheading(new_hed)
def turn_right():
    new_hed=tim.heading() - 10
    tim.setheading(new_hed)
def clear():
    tim.clear()
        
screen.listen()
screen.onkey(key="w",fun=move_forward)
screen.onkey(key="s",fun=move_backward)
screen.onkey(key="a",fun=turn_left)
screen.onkey(key="d",fun=turn_right)
screen.onkey(key="c",fun=clear)
screen.exitonclick()