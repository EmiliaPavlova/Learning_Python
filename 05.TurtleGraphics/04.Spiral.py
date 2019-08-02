import turtle

my_turtle = turtle.Turtle()
my_turtle.shape('turtle')
side = 10

for i in range(0, 20):
    my_turtle.forward(side)
    my_turtle.right(60)
    side += 10

turtle.done
