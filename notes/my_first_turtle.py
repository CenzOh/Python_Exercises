#works in the command line

#how to run the turtle lib in python in the terminal
#cd into the path
#cd ".spyder-py3/class_code"
#echo.> name.py to create the file
#py name.py to run it

#to test python code in termianl with the turtle library
#py
#import turtle
#t = turtle.Pen()


#import the lib
import turtle

#define the pencil
pencil = turtle.Pen()

"""""""""
#draw a square!!!

#draw a line. Side 1
pencil.forward(150)

#rotate the pencil/direction 
pencil.left(90)

#draw side 2
pencil.forward(150)

#rotate the pencil/direction 
pencil.left(90)

#draw side 3
pencil.forward(150)

#rotate the pencil/direction 
pencil.left(90)

#draw side 4
pencil.forward(150)

#makes our square!!
"""""""""

#draw two parrallel lines
pencil.forward(150)

#pen is not touching the paper
pencil.up()

#go back to where we started
pencil.backward(150)

#rotate
pencil.left(90)

#move forward
pencil.forward(50)

#put pencil back down
pencil.down()

#rotate
pencil.right(90)

#create the parrallel line
pencil.forward(150)

#FINISHED!!!



#keep window open until click
turtle.exitonclick()