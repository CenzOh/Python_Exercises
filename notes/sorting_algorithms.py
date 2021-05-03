# ISI 300       Sorting Algorithms
# we will discuss complexity time later in the semester
# Remember data strcutres class? CSC 326
# complexity time allows you to figure out how to make programs run easier on different machines!  


# first, swap two elements inside a vector
def swap(vector_to_swap, index1, index2): #selecting which indexes to swap
    #NOTE: swap occurs IN PLACE
    tmp = vector_to_swap[index1] #tmp = 1
    vector_to_swap[index1] = vector_to_swap[index2] #idx 1 = what idx 2 is, both are equal
    vector_to_swap[index2] = tmp #idx 2 equals tmp, which is what idx 1 was originally equal to
    
vector_one = [10,5,1,40,35]
print(vector_one)

swap(vector_one,1,3) #swap index one (5) and three (40)

print("Swap", vector_one)#last element is correct



print()
# Bubble Sort Part 1
def bubble_up(vector): #takes in a vector / list
    for i in range(len(vector)-1): #for loop through the vector, size is the length - 1 because we are counting indexes (start at 0)
        if(vector[i] > vector[i+1]): #check if current element is larger than the enxt element
            swap(vector, i, i+1) #if this is the case, swap the elements
    return vector
#if not, move on to the next element
#bubble sort for our example must execute 4 times for the values to be in order

bubble_up(vector_one)
print("Bubble Up once", vector_one) #last two elements are correct



#Bubble Sort Part 2
def bubble_sort(vector):
    for i in range(len(vector)-1): #loop for the length of the vector
        bubble_up(vector) #calls the logic from the bubble up fcn since it only occurs once
        print("iterated:", i+1, "time(s)!")
    return vector

print()
bubble_sort(vector_one) #fully sorted now
print("Bubble Sort", vector_one) #however, it iterated 4 times!



