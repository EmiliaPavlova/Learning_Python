import turtle

my_turtle = turtle.Turtle()

# Change the shape of the turtle
my_turtle.shape('turtle')

for i in range(0, 4):
    # Draw an equilateral triangle
    my_turtle.left(30)
    my_turtle.forward(200)
    my_turtle.left(120)
    my_turtle.forward(200)
    my_turtle.left(120)
    my_turtle.forward(200)

    # Draw a line in the triangle
    my_turtle.left(-30)
    my_turtle.penup()
    my_turtle.backward(50)
    my_turtle.pendown()
    my_turtle.backward(100)
    my_turtle.penup()
    my_turtle.forward(150)
    my_turtle.pendown()
    my_turtle.left(30)

turtle.done
