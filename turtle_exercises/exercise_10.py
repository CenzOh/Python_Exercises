import turtle

pencil = turtle.Pen()

counter = 0

pencil.left(90)

while (counter < 10): #number of steps
    pencil.forward(10)
    pencil.right(90)
    pencil.up()
    pencil.forward(15)
    pencil.right(90)
    pencil.down()
    pencil.forward(10)
    pencil.backward(5)
    pencil.right(90)
    pencil.forward(15)
    pencil.right(90)
    pencil.forward(5)
    counter += 1


#keep window open until click
turtle.exitonclick()
