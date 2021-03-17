# Vincenzo Mezzio ISI 300 #
# Assignment 3
# Bingo Like Lyrics Generator

dog_name = ['R','O','C','K','Y'];
dogs_name = "BINGO";

def bingo_lyrics(vector):
    
    song='There was a farmer who had a dog and bingo was his name-o: '
    
    if isinstance(vector, list): # checks if the vector is a list, i.e. character array 'r' 'o' 'w'
        vector = ''.join(vector) # makes the list into a string array: 'r' 'o' 'w' -> 'row'
        
    #print(song, vector) #initial NOTE: prints twice? First iteration prints without *
    for value in range(len(vector)): #len of vector gets the size of the vector. range gives us a list of numbers the size of the length of the vector
        first = "*"*(value) #prefix has certain num of * each iteration
        last = vector[value:] #slice the vector string ti use first set of *. value: means start at the first index
        combine = first + last #combine first and last in each iteration
        print(song, combine) #prints song as well as dog name with appropriate amount of *
    print(song, vector) #print the full dog name on final line

bingo_lyrics(dogs_name) #works as string arr
print()
bingo_lyrics(dog_name) #works as list
    