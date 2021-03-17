import turtle

pencil = turtle.Pen()

counter = 0

while (counter < 10): 
    pencil.forward(50)
    pencil.up()
    pencil.backward(50)
    pencil.right(90)
    pencil.forward(10)
    pencil.left(90)
    pencil.down()
    counter += 1
    
#keep window open until click
turtle.exitonclick()
