# Vincenzo Mezzio ISI 300 #

#I will define a vector of integers with 5 elements
my_vector = [1,3,5,7,9,1,3]
my_value = 3

def print_up_to_value(a_vector, a_value):
    index = 0
    while(index < len(a_vector)): #EXPLICITLY ASKED TO USE WHILE LOOPS
        print (a_vector[index])#print the values, not an array of the values?
        if(a_vector[index] == a_value): #if the indexed value equals the provided value, break from the loop
            break
        index += 1
    print("End of function")
print("My array:", my_vector)
print("Print up to", my_value)
print_up_to_value(my_vector, my_value) #adding print here results in a final output of "None"


