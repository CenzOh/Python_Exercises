from random import randint #import statement for the randint fcn

counter = 0 #using i in the for loop counts for iterations. Even when using break statements iteration will auto inc
#iterations = 0

for i in range(20): #twenty times
    print() #newline
    print("iteration: ", i) #print which iteration is being run
    ran = randint(0,10) #generate a positive num between 0 and 10, this is the increment value
    print("increment value: ", ran) #print the increment the value, do not increment the counter yet
    
    if(ran > 10):
        print("the increment is too large, ending the program") #alert message?
        break #end the program
    
    if(ran > 3):
        print("Don't like the increment; let's try this again")
       # iterations += 1 #iteration increment here BUT NOT counter
        continue #d/n increment counter, restart from the icrement generation
    if(counter >= 20 or i >= 20): #stop if counter is >= 20 or 20 iterations have run
        break


    counter += 1
    print("Current value of the counter: ", counter) #increment counter and print its value to screen
    #iterations +=1 #iterations will increment by one at all times
    
print("Counter final state: ", counter)