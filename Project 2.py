import turtle

# Set up circle
def draw_circle(color):
    turtle.pencolor(color)
    turtle.circle(100)
    turtle.right(180)


def main():
    turtle.bgcolor('black') # Set bg colour 
    turtle.speed(0) # Set turtle speed 
    colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"] # List of colours

    # Loop for drawing the pattern
    for i in range(120):
        draw_circle(colors[i % len(colors)])
        draw_circle(colors[i % len(colors)])

        turtle.penup()
        turtle.forward(3)
        turtle.pendown()

        turtle.left(3)

    turtle.exitonclick()

if __name__ == "__main__":
    main()