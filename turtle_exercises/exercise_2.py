# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 21:30:18 2021

@author: Cenzo Oh
"""

operation = 0

def add(num1, num2): return num1 + num2

def sub(num1, num2): return num1 - num2

def multiply(num1, num2): return num1 * num2

def divide(num1, num2): return num1 / num2

while (operation != 5): #inside a loop so you can make another or redo calculation
                        #also inside loop i can use break case for number 5
    print()
    print("Choose your operation: ")
    print("1. Add")
    print("2. Sub")
    print("3. Multiply")
    print("4. Divide")
    print("5. Quit")
    
    operation = int(input("Please enter an operation from 1-5: ")) #taking user input. Putting int in front of input turns the input into an int
    if operation == 5: #check to quit first before making user input
        break
        print("Quitting...")
        
    num1 = int(input("First number: "))
    num2 = int(input("Second number: "))
    
    if operation == 1:
        print(num1, "+", num2, "=", add(num1, num2))
    elif operation == 2:
        print(num1, "-", num2, "=", sub(num1, num2))
    elif operation == 3:
        print(num1, "*", num2, "=", multiply(num1, num2))
    elif operation == 4:
        print(num1, "/", num2, "=", divide(num1, num2))
    
    else: #incase the user writes incorrectly
        print("Invalid input")