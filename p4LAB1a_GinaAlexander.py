import turtle           
wn = turtle.Screen()
wn.bgcolor("Blanched Almond")
wn.title("Glorb & Shmorlb House")

glorb = turtle.Turtle()
glorb.color("red")
glorb.pensize(5)

shmorlb = turtle.Turtle()
shmorlb.color("yellow")
shmorlb.pensize(4)

glorb.forward(90)          
glorb.left(135)             
glorb.forward(90)
glorb.left(110)
glorb.forward(70)
glorb.left(135)

shmorlb.left(270)
shmorlb.forward(100)
shmorlb.left(90)
shmorlb.forward(100)
shmorlb.left(90)
shmorlb.forward(100)
shmorlb.left(90)
shmorlb.forward(100)
shmorlb.left(90)


wn.mainloop()
