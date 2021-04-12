# ISI 300   Vincenzo Mezzio    Assignment 5   Exercise 4 
# Implement classes animal, elephant, eagle, parrot.
# animal is parent, use inheritance

from random import randint #we will use this random fcn later

class Animal:
    def __init__(self, name):
        self.__name = name # private var
    
    def get_name(self):
        return(self.__name)
    
# Elephant is an animal!
class Elephant(Animal): # takes type animal, extending the animal class
    def __init__(self, name, trunk_length): # next line refers to the parent class
        super().__init__(name) # keyword super is the python way to refer to a parent class. Reuses code from animal
        self.__trunk_length = trunk_length #super is similiar to how it works in java and cpp
        # specific to elephant ^^
        
    def trunk_length(self):
        return self.__trunk_length
    
    def speak(self):
        print('Sound: trumpet!') #what the example shows

        

class Eagle(Animal):
    def __init__(self, name):
        super().__init__(name)
        
    def speak(self):
        print('Sound: screech...')
        

class Parrot(Animal):
    def __init__(self, name): #user does not give vocabulary
        super().__init__(name)
        self.__vocabulary = ['one', 'two']
    
    def __get_word(self): #randomly chooses a word from parrots vocab
        return self.__vocabulary[randint(0, len(self.__vocabulary)-1)]
    
    def get_vocabulary(self):
        return self.__get_word()
    
    def add_word(self, word): # add a new word to parrots vocab
        self.__vocabulary.append(word)
        
    def speak(self):
        print('Sound:', self.get_vocabulary()) #selects a random word from vocab
    
    
    
print("### Start of Program ###")
print()

eagle = Eagle('Eddie') #display_info did not work for me
print('Animal:', eagle.get_name()) #display name of animal
eagle.speak() #display sound animal makes

print()

elephant = Elephant("Dumbo", "5")
print('Animal:', elephant.get_name())
print('Trunk is long:', elephant.trunk_length()) #display length of elephant trunk
elephant.speak()

print()

parrot = Parrot('Cocorito')
print('4 words parrot')
print('Animal:', parrot.get_name())
parrot.speak() #will randomly say a word in vocab
parrot.speak()
parrot.speak()
parrot.speak()

print()
print("Post expanding vocab:")
print()
parrot.add_word('three') # expand vocab
parrot.add_word('four')

parrot.speak()
parrot.speak()
parrot.speak()
parrot.speak()

print()
print("### End of Program ###")