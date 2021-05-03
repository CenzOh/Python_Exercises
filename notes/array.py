# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 20:09:42 2021

@author: Cenzo Oh
"""

#       ARRAYS
#let's define an array of integers
my_first_array = [ 11, 22, 56, -15 ] #do not need to specify the length, python is smart enough to understand

#let's print the array to screen
print(my_first_array) #no need for a loop to get all the values

#access a specific value in our array, let's access "box" number 3 (which is 56)
print("value in box #3 is: ", my_first_array[2]) #REMEMBER we start at index 0

#print value with loop
print()
print("print via loop:")
for value in my_first_array:
    print("value is: ", value)

#that was the python traditional way to do it

#this is the c way to do it
print()
print("print via loop... c style")
for index in range(len(my_first_array)):
    print("value is: ", my_first_array[index])
    
#what if we try to access box 5?  
#my_first_array[5] #out of range!!

#add elements to our array!!
print()
print("let us make the list longer! Add number 99 to it")
my_first_array.append(99)
print("extended array: ", my_first_array)

#can't do this in c or java unless you use data structures. python makes it easy by uisng dynamic resizing of the array


#   let's define a matrix, a bi-dimensional array
print()
m = [ [11,12], [21,22], [ 31, 32] ]
print("my matrix is: ", m)

print() #position 1 is what?
print("value at index 1 in my matrix is: ", m[1])

print() #grab a certain value. This is an array (within m[2]) so give me the value in the array [0]. Nesting
print("extract the value 31 from my matrix: ", m[2][0])


#define a list
my_first_list = [ "Paolo", 11, "Cappellari"]
print()
print("A list in python: ", my_first_list)

print("print the lsit via loop: ")
for value in my_first_list:
    print("value is: ", value)
    
    
#select some elements from an array
list2 = [0, 1, 2, 3, 4, 5, 6, 7 ];
print("Print from 2nd to 5th, that is list2[1:5]")
print(list2[1:5]) #index for SECOND element is 1


print()
#examples of some operations
list1 = [1,2,3]
list2 = [4,5,6]

print("plus: ", list1 + list2) #python creates this third list
print("product: ", list1*3) #list1, python creates a list with repition of list1 three times
value_to_find = 2
print("is this value", value_to_find, "in my array? ", value_to_find in list1, )
print("is this value", value_to_find , "in my array? ", value_to_find in list2, ) #python creates an if condition
#there is a whole logic workin under the hood!


print("start:stop:increment syntax doing? ", list1[:2])   #end @ index 2
print("start:stop:increment syntax doing? ", list1[1:])   #start @ index 1

list3 = list1*4
print("List3 is ", list3)
print("1::2 syntax doing? ", list3[1::2]) #start @ index 1 and run to the end (which is not visible) my increment is 2
#increment is a +2. after 2 [0] we do +2 to get 1 [2]


print()
list4 = [*range(15)]
print("List4 is ", list4)
print("1::2 syntax doing? ", list4[1::3]) #start @ index 1 and run to the end (which is not visible) my increment is 2
#start at box 1, skip the 0. Incrememnt by 3 so we go to 4, 7, ...


#NEGATIVE INDEXES, starts at the end and moves back
#-1 is the final element and moves back

print()
print("Last element: ", list4[-1])
print("Last N element: ", list4[-5])
#5 elements going backwards
print("1::3 syntax doing? ", list4[8::-3])
#start at 8, move back by 3
