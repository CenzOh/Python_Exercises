# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

i_my_zip_code_ = 10314
#setting the variable to value: 10314

i_new_variable = 4
#var to be deleted

#print the zip
print("print zip at CSI is")
print(i_my_zip_code_)

s_csi_address = "2800 Victory Blvd"
#store text with double quotes

#check for equality with ==
1==2
#prints false in terminal
print(2==2)
#prints true in the console!

del i_new_variable
#typing in print(i_new_variable) will result in error. However, will clean up auto when program terminates 


a = 3 #changing to not be hardcoded
#user input
t_reading_user_input = input("Please enter a number: ")

print("Number provided:", t_reading_user_input)

#copying the number into our variable a
#a = t_reading_user_input #does not work since this is type string comparing to int
a = int(t_reading_user_input) #whatever you're reading from, convert it into an integer!!

#note: python will remember the user input and updated a in the "variable explorer"

#test condition, USE colon rather than = !!
if(a>0):
    print("This is a positive number")
    print("I am in the positive case")
    print("I am leaving the positive case block")

#else if
elif(a<0):
    print("this is a negative number")

#otherwise, do this (if everything else failed)
else:
    print("Neither a pos/neg number") 
    #this would occur if a = 0 
    
print("finished")


#making a loop
s_values = [2021, 2, 1] #s for sequence

for a_single_value in s_values: #you see how python is "friendlier" than c++?
    print(a_single_value / 2) #will print decimals!!
    
    