# ISI 300   Vincenzo Mezzio     Assignment 6
# BubbleSort Assignment
# Exercise 1   Swap

#define sqp fcn to swap two elements inside a vector
def swap(vector, index1, index2): #selects which index to swap
    #NOTE: swap will occur in place
    tmp = vector[index1] #tmp has value of index1
    vector[index1] = vector[index2] #index 1 now equals index 2
    vector[index2] = tmp # idx 2 equals what idx 1 was originally, now storred in tmp


print('## START OF PORGRAM ##')
#provide two test cases
vector_one = [10, 5, 1, 40, 35] # test case with ints

vector_two = ['H', 'E', 'O', 'L', 'L'] # test case with char

idx = 1
idx2 = 3

print()
print('pre swap', vector_one)
print('indexes to swap', idx, 'and', idx2)
print('values to swap', vector_one[idx], 'and', vector_one[idx2])

swap(vector_one, idx, idx2) # swaps INDEX 1 (5) and 3 (40)

print()
print('post swap', vector_one)

idx = 2
idx2 = 4

print()
print('pre swap', vector_two)
print('indexes to swap', idx, 'and', idx2)
print('values to swap', vector_two[idx], 'and', vector_two[idx2])


swap(vector_two, idx, idx2)

print('post swap', vector_two)

print()
print('## END OF PORGRAM ##')