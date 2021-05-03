# ISI 300       Inheritance 

#this is the common class
class Person:
    def __init__(self, name, address):
        self.__name = name
        self.__address = address
        
    def getName (self):
        return(self.__name)
    
    def getAddress(self):
        return(self.__address)
    
    def display_info (self):
        print ("My name is", self.getName()
               , ", and I live in", self.getAddress())


#Professor is a Person!!!
class Professor(Person): #takes type person, extending the person class
    def __init__(self, name, address, courses): #next line refers to the parent class
        super().__init__(name, address) #keyword super is the python way to refer to the parent class. Reuses code from person
        self.courses = courses #super is similiar to how it works in java and cpp
        #plus. specific info about professor ^^
        
    # overloading the print info method
    def display_info(self):
        print("Printing info about a Professor")
        #reusing print info from parent class
        super().display_info() #calls the display info fcn from the Person class
        print("Courses taught:", "".join([str(c)+"," for c in self.courses]))


class Student(Person):
    def __init__(self, name, address, grades):
        super().__init__(name, address)
        self.__grades = grades
        
    def display_info(self):
        print("Info about the Student")
        super().display_info()
        print("Grades:", self.__grades)
        
        

print('### START ###')
print()

paolo = Person("Paolo", "2800 Victory Blvd")
paolo.display_info()

print()
tom = Professor("Tom", "Time Sq", ["MKT101", "BUS215"])
print("Info about Tom as a Professor:")
print()
tom.display_info() #we can call this fcn even if it is not defined. It is in Person (parent) class though!!
print()
print("Tom's address:", tom.getAddress()) #example of calling a fcn from the parent class

print()
susan = Student("Susan", "New York City", ["A", "B", "A"])
print("Info about Susan as a Student:")
print()
susan.display_info()
#what if we want to modify the fcns? DO you have to modify each individual class (stduent, professor, ...)
#just update person and see the effects where data is reused




print()
print('### END ###')