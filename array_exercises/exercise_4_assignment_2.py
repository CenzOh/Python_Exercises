# Vincenzo Mezzio ISI 300 #

#define a vector of integers with 10 elements
my_vector = [0,1,2,3,4,5,6,7,8,9]
def print_odd_first(vector): #check for odd number by asking if x%2 = 1 then do this...
    index = 0 #define index
    loop_twice = False #I will loop through while loop again to do evens. Odd will execute once
    
    while (index < len(my_vector)): #iterate through whole loop
        if (loop_twice is False and vector[index] % 2 == 1): #if odd print first
            print(vector[index])
        elif (loop_twice and vector[index] % 2 == 0): #on second iteration of while loop, print even
            print(vector[index])
        if (index == len(my_vector)-1 and loop_twice == False):
            loop_twice = True #^^ elif did not work, made it into an if statement
            #print("Yes")
            index = 0
            continue #does not skip the first index
        index += 1 #increase index
        #print(index)

# not using more memory by allocating soace for extra arrrays, just looping through twice and printing

    
print_odd_first(my_vector)
       