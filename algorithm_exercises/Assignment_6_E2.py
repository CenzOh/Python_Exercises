# ISI 300   Vincenzo Mezzio     Assignment 6
# BubbleSort Assignment
# Exercise 2    Bubble-Up

# define bubble up fcn. Bubble up element with highest value
# input a vector of ints and output a vector having the highest calue at last index

#using the swap fcn from pervious exercise
def swap(vector_to_swap, index1, index2): 
    tmp = vector_to_swap[index1] 
    vector_to_swap[index1] = vector_to_swap[index2]
    vector_to_swap[index2] = tmp


def bubble_up(vector):
    for i in range(len(vector)-1): #for loop through the vector, size is the length - 1 because we are counting indexes (start at 0)
        if(vector[i] > vector[i+1]): #check if current element is larger than the next element
            swap(vector, i, i+1) #if this is the case, swap the elements
    return vector
#if not, move on to the next element
#bubble sort must execute size - 1 times for all of the vlaues to be in order

print('## START OF PROGRAM ##')
#provide two test cases
vector_one = [10, 40, 1, 5, 35]

vector_two = [5, 4, 1, 3, 2]

print()
print('pre bubble-up', vector_one)

bubble_up(vector_one)

print()
print('post bubble-up, iterated once', vector_one) #40, the largest value, is in the correct index

print()
print('pre bubble-up', vector_two)

bubble_up(vector_two)

print()
print('post bubble-up, iterated once', vector_two) #5, the largest value, is in the correct index

print()
print('## END OF PROGRAM ##')
