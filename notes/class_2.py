# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#       Second class!

#       Loops

#       for loops

#printing values in a for loop
my_seq_of_values = [2019,1,28, 2021, 2, 8]

#counter
i = 0
print("### Start of my for loop program ###")
print()

#checking the length of the array
l = len(my_seq_of_values)
print("The length of my sequence is: ", l)
print()


#print all values in the sequence

#my_values is var decalred in for loop
for my_value in my_seq_of_values:
    #take the first or next sequence of my values and do something with it
    split_the_value = my_value / 2
    print("Current index/position is: ", i)
    print("The value for the current iteration is: ", my_value)
    #grabs index i in the array
    print("Value at position (via index) is: ", my_seq_of_values[i])
    print("the split value: ", split_the_value )
    print() #creates space
    i = i + 1
    
    
#syntax for c: for(i=0;i<l;i++)
for index in range(len(my_seq_of_values)): #no need to specify the starting point 0 since it starts there by default
    #range generates 3 values, for each value it runs the usual code
    #give the range if you know how many times you want to run through the loop
    
    #NOTE hardcoding 3 is bad practice. If the sequence is longer we won't print out the whole array.
    print("POS -- other loop with range! curr value is: ", index) 
    print("POS -- val @ curr pos: ", my_seq_of_values[index])
    print()
    
print("### End of my for loop program ###")


#       while loop

counter = 0

l = len(my_seq_of_values)

while(counter < l) : # - - > is 0 < 5 ?? --> YES
    print("Index is: ", counter, " and value is: ", my_seq_of_values[counter])
    counter += 1 # counter = 0 + 1 --> counter = 1
    
#if you don't understand what is going on you can try to debug with print statements
#reverse order counting while loop

#NOTE: in python when you put a - in front of a number it will start at the end and count backwards
counter = len(my_seq_of_values) - 1 #length of sequence will give a number one higher than the index, so sub by one
while(counter >= 0): #add the equal sign (greater than or EQUAL TO) because we want to include index 0
    print()
    print("DEBUG: value forn counter is: ", counter)
    print("Index is: ", counter, " and value is: ", my_seq_of_values[counter])
    counter = counter - 1
    
    
#       break statement

for my_value in my_seq_of_values :
    print()
    print("Value is: ", my_value)
    #if I found my value of the day, let's skip the rest of the seq and go about my (rest) of program
    if(my_value == 2021) : #2 and 8 WILL NOT print
        break ## <-- this line will kick you out of the loop. Anything after will not execute. Used to OPTIMIZE logic not FIX it!
    
print("Done with the loop")

#       continue statement

for my_value in my_seq_of_values :
    print()
    
    print("The number is (before if): ", my_value)
    
    if(my_value % 2 == 0): 
        print("Found an even number: ", my_value)
        continue #continue skips the print the number is: it goes back to top of loop and onto next iteration
            
    print("The number is (after if): ", my_value)
    print("You will not see me if we found an even number")
    
    
#       functions examples
    
my_seq1 = [2019, 1, 28]
my_seq2 = [2021, 2, 8, 60]

# a program to print two sequences

"""""""""

#this is a comment block

#print the first sequence
print()
print("First sequence")
for v in my_seq1:
    print("Value is: ", v)
    
#print the second sequence
print()
print("Second sequence")
for v in my_seq2:
    print("The value is: ", v)
    
#do not do something like this!!
"""""""""

def print_my_sequence(input_sequence) : #define the fcn before. Python only knows what is has seen (reads top to bottom) Python is an interpretated language no compiling!
    for v in input_sequence :
        print("The value in your sequence is: ", v)
        
        
print()
print("First sequence")
print_my_sequence(my_seq1)

print()
print("Second sequence")
print_my_sequence(my_seq2)


#       turtle library, included in core python by default
"""""
import turtle

#defines a pencil to draw on a canvas
pencil = turtle.Pen()

#draws a line of length 50
pencil.forwards(50)



#close window on click
turtle.exitonclick()
""""""
