# ISI 300   4/5/21  
# Sorting    Merge Sort

# Divide and conquer, idea is to cut the problem in half and 
# use the results from each half. We keep cutting in halves
# until the problem is trivial, we solve for both halves,
# and we combine the solutions.

# Example of what we want:
# index 0  1  2  3  4   5
# value 77 42 35 12 101 5

# into

# index 0 1  2  3  4  5
# value 5 12 35 42 77 101


# MergeSort:
    
# 98 23 45 14 6 67 33 42
# Split in half

# 98 23 45 14       6 67 33 42
# Call MergeSort on the left sdie (split the left side in half)

# 98 23      45 14      6 67 33 42
#Split again so we have two lists with one number in each

# 98    23      45 14       6 67 33 42
# Compare 98 and 23, apply the merge. 23 goes before 98
# Split 45 and 14

# 23 98     45  14      6 67 33 42
# 14 goes before 45

# 23 98      14 45       6 67 33 42
# 23 98 and 14 45 are independently sorted
# lowest number is always to the left, we need to build a merge
# of the two lists. Compare the first element of each list. 14
# is lower...

# 14 23 45 98 ("sorted")    6 67 33 42
# Same thing applies to the second half, after the second one is
# sorted this is what we have:

# 14 23 45 98       6 33 42 67
# now, compare the two lists, start with the left most element:
# 14 vs 6, 6 is lowest, add 6 first and move onto next element:
# 14 vs 33, 14 is lower, add it, rinse and repeat.

#final sorted list:
# 6 14 23 33 42 45 67 98



# Professor's answer:


def merge(left, right): #input lists are already sorted (independently)
    merged = [] # new list to add sorted elements to
    i = 0; j = 0;
    
    print(left) # inside the fcn, printing to see the lists
    print(right)
    
    while (i < len(left) and j < len(right)): #remember from loops, do not go out of bounds
    # compare the left most elements from both lists    
        print("Comparison: left", left[i], "Vs right",right[j])    
        if left[i] < right[j]: #ex, is 3 < 7? Yes, add 3 to the merge, move on index from left list D/N move on in the right list
            # if smallest is on left list,
            # then add it to the merged list
            merged.append(left[i])
            i = i+1
        else:
            # if smallest is on the right side,
            # then add it to the merged list
            merged.append(right[j])
            j=j+1
        print("part merged list:", merged)
            
    print("part merged list (2nd):", merged)
    print("index i is:", i)
    print("index j is:", j)
    
    # are there elements left in the left list?
    # If so, add them to the end of merged list
    # .extend left
    print("Left-overs in left list", left[i:]) # show where we stopped (i)
    for k in range(i, len(left)):
        merged.append(left[k])
        
    # are there elements left in the right list?
    # If so, add them to the end of merged list
    # .extend right 
    print("Left-overs in right list", right[j:])
    for k in range(j, len(right)):
        merged.append(right[k])
    
    return(merged)



def mergesort(vector):
    # split problem if too complex
    sortedlist = []
    if (len(vector) > 1):
        mid = len(vector)//2
        
        #define the two sub problems
        left = vector[:mid]
        right = vector[mid:]
        print("Left list:",left)
        print("Right list:",right)
        
        #recursive call
        #problem of same nature, but smaller/easier: apply same idea
        print("calling mergesort on left list",left)
        sortedleft = mergesort(left)
        print("calling mergesort on right list",right)
        sortedright = mergesort(right)
        
        print("Finished with splitting, let us merge")
        sortedlist = merge(sortedleft, sortedright)
        return(sortedlist)
    
    print("List is of length one, just return it")
    print("this list is:",vector)
    return(vector)  # outside if statement, we have a list with length of one

    

# Driver code

list1 = [3,4,5]
list2 = [7,8,9]
# you can do list1=[11,13,15]; list2=[12,14,16]; # to get a better idea!
# create a new list that is the merge of the above
# [3,4,5] + [7,8,9]
#print("Simple merge on list:",list1,list2)
#m = merge(list1, list2)
#print("Merged", m)

#print("let us try a sort")
list3 = [5,6,3,2,6,7,7,8]
#print("random list:",list3)
#sortedlist = mergesort(list3)
#print(sortedlist)

# I should write as many print outs as I need to understand what is going on!


# Second example with dataframes

import pandas as pd
#left dataframe
prof_course = pd.DataFrame({
    'prof': ['Paolo', 'Tom', 'Michele', 'Alessia', 'Mark'],
    'subject':['ISI300','MKT101','ISI374','MKT101','ISI300']
    })

# right dataframe
course_building = pd.DataFrame({
    'subject':['ISI300','MKT101','ISI374'],
    'building':['3N','1C','2M']})

print("prof-course")
print(prof_course)
print()

print("course-building")
print(course_building)

# merge the dataframes, in essence a concatination
df_merged = pd.merge(prof_course,course_building,on='subject')

print()
print("Merged dataset")
print(df_merged)