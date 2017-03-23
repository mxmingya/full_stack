import turtle

def draw_square(turtle):
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)

def draw_circle():
    window = turtle.Screen()
    window.bgcolor("white")

    jasmine = turtle.Turtle()
    jasmine.circle(50)
    jasmine.speed(0.1)
    jasmine.color("blue")
    jasmine.shape("arrow")

def draw_arts():
    window = turtle.Screen()
    window.bgcolor("white")
    jasmine = turtle.Turtle()
    jasmine.speed(20)
    jasmine.color("red")
    # for i in range(1,36):
    #     draw_square(jasmine)
    #     jasmine.right(10)
    draw_tria(jasmine)
    draw_tria(jasmine)

    window.exitonclick()

def draw_tria(turtle):
    for i in range(1,4):
        turtle.left(120)
        turtle.forward(180)
    for i in range(1,4):
        turtle.right(120)
        turtle.forward(180)


# brad = turtle.Turtle()
# brad.speed(50)
# draw_tria(brad)
draw_arts()

