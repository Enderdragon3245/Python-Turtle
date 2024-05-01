from turtle import *
import colorsys

t = Turtle()
move = 1
t.speed(0)

for i in range(360):
    t.pendown()
    t.right(move)
    t.forward(100)
    t.right(30)
    t.forward(60)
    t.right(30)
    t.forward(30)
    t.penup()
    t.home()
    move = move+1


mainloop()
