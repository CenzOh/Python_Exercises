import turtle

pencil = turtle.Pen()

for i in range(30): #i will increase
    pencil.forward(i*10) 
    pencil.right(90)
#can also do forward(i + 5) constant increment


#keep window open until click
turtle.exitonclick()