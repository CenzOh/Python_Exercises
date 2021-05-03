# 3/15/21   ISI 300     3/15/21

# define a class
class Person:
    
    # constructor, __ is syntax for some hiddent fcns
    def __init__(self, init_firstname , init_lastname): ## <-- initial values coming from the outside (caller)
    # Variables to store first and last name of a person
        self.firstname = init_firstname #how we create one object out of a class person
        self.lastname = init_lastname
                  
    #a method to print info
    def displayInfo(self):
        print ("Firstname is: ", self.firstname , ", Lastname is: ", self.lastname)
        #self refers to firstname inside the person
        
#print("### START OF PROGRAM ###")
#creating an object from person.
#let's create paolo cappellari

paolo = Person('paolo', 'cappellari')
#paolo is an object with a specific first and last name     
#how to generat eoutput, use any built in method

#print("### END OF PROGRAM ###")   

#to interact with an object we should use the class' public methods
paolo.displayInfo()#self we do not need to pass anything it is inside paolo itself

print()       #exercises slide 24 on slide deck week 6

class Student: # no need to use the init_ or i_ for these variables you could if you want
    def __init__(self, init_name, init_address, init_completed_courses, init_completed_course_grades):
        self.__name = init_name
        self.address = init_address
        self.completed_courses = init_completed_courses
        self.completed_course_grades = init_completed_course_grades
        
    def displayInfo(self):
        print("Name is: ", self.__name #this is a list
              , ", Address is:", self.address
              , ", Courses are", self.completed_courses
              , ", Grades are", self.completed_course_grades)
    def setName(self, new_name): #set the variable, can set again after initial declaration
        #if(new_name in <list-of-good-names>):
        self.__name = new_name # states that this is a private field!!
        #else: ERROR
    def getName(self): #get the variable by returning it
        return self.__name
    
    def setAddress(self, address):
        self.address = address
    def getAddress(self): 
        return self.address
    
    def setCompletedCourses(self, completed_courses): 
        self.completed_courses = completed_courses
    def getCompletedCourses(self): 
        return self.completed_courses
    
    def setCompletedCoursesGrades(self, completed_course_grades): 
        self.completed_course_grades = completed_course_grades
    def getCompletedCoursesGrades(self): 
        return self.completed_course_grades
    
    
    #at the end of a semester I would like to add any new course along with the grade
    def add_a_course_with_grade(self, new_course, new_grade):
        #self.completed_courses += new_course
        #   *** Another way to do it below ***
        self.completed_courses.append(new_course) # another way to do this, we do not need the square brackets if we do it like this
        self.completed_course_grades.append(new_grade)
        
        
    #add courses with grades -- buld load
    def add_a_course_with_grades(self, new_courses, new_grades):
        self.completed_courses += new_courses
        self.completed_course_grades += new_grades
        
    
    #def estimate_my_gpa_at_graduation():
        # some complex logic that given the grades earned so far 
        # guesses the final GPA
        #
        #
        
george = Student('giorgio', '123 street', ['ISI 300', 'CSC 315'], ['A', 'B']) #Now we have a list!     
print(george.getName())    # returns the name
george.setName('mario') # sets the new name from john to max
print(george.getName())
print(george.getAddress())
print(george.getCompletedCourses())
print(george.getCompletedCoursesGrades())
#george.add_a_course_with_grade(["CSC 330"], ['C']) #adding the [] turns the input into a list 
george.add_a_course_with_grade('CSC 330', 'C') 
george.displayInfo() #we ADDED / CONCATINATED the new class and grade

print()
#one issue we have is we can put one course in our "list"
#define the list with [], python is dynamic for us to just add [] in our definition

#using the add a course with grades so we can add more than 1 course and grade at a time
george.add_a_course_with_grades(['MGT 110', 'CSC 126'], ['A', 'A'])
george.displayInfo() #we still have to use the [] but in the fcn def we have to use += (I think concat and append do not work?)

print()
print("Access internals")
#print(george.name) #writing underscore here will not work! name is now private
print(george.getName())
print()
print("Access internals: change name to Luca")
george.name = "Luca"
print(george.name)
george.__name = 'Mario' #will not get picked up by the class
print()
george.displayInfo()
        

#slide 30
class Person2:
    def __init__(self, i_name, i_hair_color, i_colors_liked):
        self.__name = i_name
        self.__hair_color = i_hair_color
        self.__colors_liked = i_colors_liked
        
    def displayInfo(self):
        print("Name: ", self.__name
              , ", color of hair: ", self.__hair_color
              , ", possible colors: ", self.__colors_liked
              )
    def __set_hair_color(self, new_color): #set is not visible now
        self.__hair_color = new_color
        
    def dye(self, new_color): #visible fcn
            #print("### IN DYE FCN")
            #before modifying the color, check if it is a good one
            #print("### condition evaluates to: ", self.__colors_liked == new_color)
            #print(self.__colors_liked)
        print(new_color) #is an array = to text? of course not
        if(new_color in self.__colors_liked):     # never forget the self!
               #that color checks out fine let us change it 
               #print("### running the check")
           self.__set_hair_color(new_color)
        else:
            print("U nuts?")
        
print()
laura = Person2('Laura', 'black', ['red', 'blonde'])
print("Initial person: Laura with black hairs")
laura.displayInfo()

print()
print("Dye hairs to blonde:") #directly affecting the variable
laura.__hair_color = 'blonde' #color of hair is STILL black! D/n work outside the fcn

#laura.dye('blonde')
laura.displayInfo()

print()
print("Dye hairs to blonde: Attempt 2") #using the set function
#laura.set_hair_color('pink') #can not do this or even use __, straight up can not invoke it
laura.dye('red') #pink will NOT work, red will
laura.displayInfo()

print()
print("Dye hairs to blonde: Attempt 3") #using the set function
#laura.set_hair_color('pink') #can not do this or even use __, straight up can not invoke it
laura.dye('green') #gree will not work
laura.displayInfo()
