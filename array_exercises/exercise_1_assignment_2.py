# Vincenzo Mezzio ISI 300 #

#define a vector of ints with 5 elements
my_vector=[1,2,3,4,5] #array od dimension 1

def vector_sum(vector) : #return sum of elements
    the_sum = 0 #start at 0
    for v in vector: #iterate through array
        the_sum += v #increment sum counter
    return (the_sum) #RETURN the sum DON'T PRINT
        
print("Sum of the vector:", vector_sum(my_vector)) #print the fcn

def vector_prod(vector): #given a vector return the product
    if len(vector) == 0: #if the array has no elements, the product = 0, not 1
        the_product = 0
    the_product = 1 #iterate through array and multiply by each element
    for v in vector: #^starting at vector (array) prints the whole array, no good
        the_product = the_product * v
    return(the_product)

print("Product of the vector:", vector_prod(my_vector))

def vector_max(vector) :
    max_val = vector[0] #explicitly defining max and min val as first element in arrray. If i define it as a number outside array it will not work
    for v in vector:
        if v > max_val:
            max_val = v
    return (max_val)
    
print("Max value:", vector_max(my_vector))

def vector_min(vector):
    min_val = vector[0] 
    for v in vector:
        if v < min_val:
            min_val = v
    return (min_val)

print("Min value:", vector_min(my_vector))
