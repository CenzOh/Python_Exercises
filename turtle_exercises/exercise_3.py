import turtle

pencil = turtle.Pen()

counter = 0

while (counter < 4): #needed to add the fourth so it can make the full square
    pencil.forward(10)
    pencil.right(90)
    counter += 1
    
#keep window open until click
turtle.exitonclick()