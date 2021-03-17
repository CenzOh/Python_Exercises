# Vincenzo Mezzio ISI 300 #

#define a vector of integers with 5 elements
my_vector = [2,4,6,8,10]


def vector_swap(vector, i, l): #i and l are the two indexes
#given a vector and two indexes, return a vector where the values at the provided indexes are swapped
    temp_val = my_vector[i] #put i in a temp so when we change i's value, it will have already been saved in a temp
    my_vector[i] = my_vector[l]
    my_vector[l] = temp_val
    return vector #return the array to confirm changes
print(my_vector)
print("We will swap", my_vector[0], "with", my_vector[1])
print(vector_swap(my_vector,0,1)) #remember calling the swap fcn requires the two indexes as well as the array