# ISI 300   Vincenzo Mezzio     Assignment 6
# BubbleSort Assignment
# Exercise 4    FAST Bubble-Sort

# implement the bubble sort fcn, sort an array from lowest to highest value
# Optimize the bubble sort to ** immediately finish when array is sorted **

#input vector of ints, output the input vector with all elements sorted

#let's make this one fcn and not have to refer to swap or bubble up
def bubble_sort(vector):
    # stop iterating when we pass w/o swapping
    swapped = True # checking if we performed a swap
    iteration = 0 # this var counts the iterations
    while(swapped): # continue this until we do not swap (that means the rest of the vector is in place)
        swapped = False # first let us assume we will not swap
        for i in range(len(vector) - iteration - 1): # check if we are in range of the vector  
            if(vector[i] > vector[i+1]): # check if the next element is lrager than current
                #if so, swap here
                vector[i], vector[i+1] = vector[i+1], vector[i] # in-line way to swap the indexes
                swapped = True # we have swapped so declare variable as true
        iteration += 1 # increase the iteration outside the for loop
        print('iterated', iteration, 'time(s)!')
        
print('## START OF PROGRAM ##')
#provide two test cases

vector_one = [10, 11, 5, 35, 40]
#normally iterates size - 1 times, what if last two values are where they should be?
#then that means the bubble sort will execute only 3 times now!

vector_two = [1, 2, 3, 4, 6, 5]
#what if the first four elements are sorted? 
#First iteration should swap 5 and 6 

print()
print('pre bubble sort', vector_one)

print()
bubble_sort(vector_one) 

print()
print('post bubble sort', vector_one)

print()
print('pre bubble sort', vector_two)

print()
bubble_sort(vector_two)

print()
print('post bubble sort', vector_two)

print('## END OF PROGRAM ##')