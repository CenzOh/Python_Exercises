
import turtle

pencil = turtle.Pen()

counter = 0

while(counter < 20):
    if(counter % 2 == 0): #odd, solid
        pencil.forward(150)    
    
    if(counter % 2 == 1): #even, dashed
        for x in range(10): #making use of the foor loop
            pencil.forward(10) #solid segment
            pencil.up()
            pencil.forward(5) #non-visible segment
            pencil.down()
    pencil.up()
    pencil.backward(150)
    pencil.right(90)
    pencil.forward(10)
    pencil.left(90)
    pencil.down()
    counter += 1

#keep window open until click
turtle.exitonclick()