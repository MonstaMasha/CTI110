import turtle
wn = turtle.Screen()
wn.bgcolor("azure")
wn.title("initials")

alex = turtle.Turtle()
alex.color("violet")
alex.pensize(5)

gina = turtle.Turtle()
gina.color("red")
gina.pensize(5)

alex.backward(150)
alex.forward(130)
alex.right(45)
alex.forward(50)
alex.backward(150)

alex.right(90)
alex.forward(150)

gina.circle(-80, -180)
gina.right(90)
gina.forward(50)
gina.right(90)
gina.backward(50)
