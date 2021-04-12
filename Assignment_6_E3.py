# ISI 300   Vincenzo Mezzio     Assignment 6
# BubbleSort Assignment
# Exercise 3    Bubble-Sort

#implement bubble sort fcn. Sort an array from lowest to highest value
# NO OPTIMIZATION 
#input a vector of ints, output the input vector with all elements ordered


#using swap fcn from pervious two exercises
def swap(vector_to_swap, index1, index2): 
    tmp = vector_to_swap[index1] 
    vector_to_swap[index1] = vector_to_swap[index2] 
    vector_to_swap[index2] = tmp 
  

#using bubble up fcn from previous exercise
def bubble_up(vector): 
    for i in range(len(vector)-1): 
        if(vector[i] > vector[i+1]):
            swap(vector, i, i+1) 
    return vector


#our bubble sort fcn
def bubble_sort(vector):
    for i in range(len(vector)-1): #loop for the length of the vector
        bubble_up(vector) #calls the logic from the bubble up fcn since it only occurs once
        print("iterated:", i+1, "time(s)!") #just an extra thing i added so we can see how many iterations it took
    return vector


print('## START OF PROGRAM ##')
#provide two test cases

vector_one = [40, 10, 35, 1, 5]

vector_two = [1, 6, 2, 4, 3, 5]

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
