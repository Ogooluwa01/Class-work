import turtle

window = turtle.getscreen() #Create window
window.setup(0.5, 0.75) #Set window size
window.bgcolor(1, 1, 0) #Set window colour
#Title of the output window
window.title("Activity Program")
# Create laser cannon
cannon = turtle.Turtle() #Pointer/pen
cannon.color(1, 1, 1) #Pointer/pen color
cannon.shape("turtle") #Pointer/pen shape
cannon.goto(100,100) #Pointer movement

turtle.done