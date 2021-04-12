# ISI 300   Vincenzo Mezzio     Assignment 6
# Bubblesort Assignment
# Exercise 5    Fast Bubble-Sort with Info

# Same idea as last exercise except,
# number of swaps should be printed to screen, not a return
# and the number of bubble up executed should be printed to screen

# Use test cases in a single R program ? 
#bubble sort ssame idea as previous exmaple, ill write it differently however

def bubble_sort(vector):
    length = len(vector)
    changed = True
    swap = 0
    while (changed):
        changed = False
        for i in range(length - 1):
            if (vector[i] > vector[i+1]):
                swap = swap + 1
                vector[i], vector[i+1] = vector[i+1], vector[i]
                changed = True
        length = length - 1
    print(vector)
    print("Number of swaps:",swap)
        
print('## Start of Program ##')

vector_one = [1,3,2,4,5] # should swap once

vector_two = [10,6,9,8,7] # should swap 7 times
            #[6,9,8,7,10] 4 times, moved 10 to back
            #[6,8,7,9,10] 2 times, moved 9 to second to last
            #[6,7,8,9,10] 1 time, moved 7 to second to first
            #4 + 2 + 1 = 7 times swapped

print()
print('pre bubble sort', vector_one)
print()
bubble_sort(vector_one)

print()
print('pre bubble sort', vector_two)
print()
bubble_sort(vector_two)

print('## End of Program ##')