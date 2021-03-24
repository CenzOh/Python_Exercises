# ISI 300 Vincenzo Mezzio Assignment 5 Exercise 2

class Student: # no need to use the init_ or i_ for these variables you could if you want
    def __init__(self, init_name, init_address):
        self.__name = init_name
        self.__address = init_address
        self.__course_names = []#at initialization the list is empty
        self.__course_grades = []
        
    def setName(self, new_name): #set the variable, can set again after initial declaration
        self.__name = new_name #__name is private var
    def getName(self): #get the variable by returning it
        return self.__name
    
    def setAddress(self, address):
        self.__address = address
    def getAddress(self): 
        return self.__address
    
    def addExam(self, name, grade):
        self.__course_names.append(name) #appends exam name and grade
        self.__course_grades.append(grade)
        
    def getGrade(self, name): #retrieve grade for a given course
        for i in range(len(self.__course_names)):
            if (name == self.__course_names[i]):
                print(self.__course_grades[i])
                return #will not execute print statement if we found grade
        print("Unable to find that grade!")
        
    def listTests(self): #list all exams
        for i in range(len(self.__course_names)):
            print("Course", self.__course_names[i], "Grade", self.__course_grades[i])


giorgio = Student('Giorgio', '123 Street')
giorgio.addExam('ISI300', 'A')
giorgio.addExam('CSC315', 'B+')
giorgio.getGrade('CSC315')
giorgio.listTests()    