import turtle
window = turtle.Screen() #Create window
window.setup(0.5, 0.75) #Set window size
window.bgcolor(0.5, 0.2, 0.7) #Set window color
#Title of the output window
window.title("controlling turtle")
# Create laser cannon
cannon = turtle.Turtle() #Pointer/pen
cannon.color(1, 1, 1) #Pointer/pen color
cannon.shape("turtle") #Pointer/pen shape
cannon.pensize(5)
cannon.fillcolor("blue")
cannon.forward(100) #move 100 units in current direction
cannon.left(90) #turn anticlockwise 90 degrees
cannon.forward(100)
cannon.right(90)
cannon.forward(100)
cannon.left(90)
cannon.forward(100)
cannon.right(90)
cannon.forward(100)

turtle.done() #render the screen