# ISI 300   Vincenzo Mezzio     Assignment 7
# MergeSort

#NOTE: DO NOT use built in functions. Meaning we can not use .append. Just do currlist = currlist + val2append
#QUICK NOTE: By tring to do currlist = currlist + val2append, it reads val2append as an INT not a LIST
# to fix this, just add [] arround it: currlist = currlist + [val2append] # val2append is now a LIST!!!

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
            merged = merged + [left[i]] # removed built in function .append
            i = i+1
        else:
            # if smallest is on the right side,
            # then add it to the merged list
            merged = merged + [right[j]] # removed built in function .append
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
        merged = merged + [left[k]] # removed built in function .append
        
    # are there elements left in the right list?
    # If so, add them to the end of merged list
    # .extend right 
    print("Left-overs in right list", right[j:])
    for k in range(j, len(right)):
        merged = merged + [right[k]] # removed built in function .append
    
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

list1 = [3,4,5]
list2 = [7,8,9]
# you can do list1=[11,13,15]; list2=[12,14,16]; # to get a better idea!
# create a new list that is the merge of the above
# [3,4,5] + [7,8,9]
#print("Simple merge on list:",list1,list2)
#m = merge(list1, list2)
#print("Merged", m)

print("let us try a sort")
list3 = [5,6,3,2,6,7,7,8]
print("random list:",list3)
sortedlist = mergesort(list3)
print(sortedlist)