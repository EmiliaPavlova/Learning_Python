import turtle

my_turtle = turtle.Turtle()
my_turtle.shape('turtle')

for i in range(0, 3):
    side = 10
    for j in range(0, 7):
        for k in range(0, 3):
            my_turtle.forward(side)
            my_turtle.left(120)
            side += 10
    my_turtle.right(120)
    my_turtle.forward(50)

turtle.done
