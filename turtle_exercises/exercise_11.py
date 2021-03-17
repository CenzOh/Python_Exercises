import turtle

pencil = turtle.Pen()

size = 5
pencil.left(90)

for x in range(50):
    pencil.forward(size) #conduct this once per loop not 3 times it messes up the spiral!
    pencil.right(90)
    size = size + size * 0.10 # increment segment size by 10% for each new segment. Cn also do size = size * 1.1. Same thing

#keep window open until click
turtle.exitonclick()