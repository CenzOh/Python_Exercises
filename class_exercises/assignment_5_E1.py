# ISI 300 Vincenzo Mezzio Assignment 5 Exercise 1

class Student: # no need to use the init_ or i_ for these variables you could if you want
    def __init__(self, init_name, init_address, init_completed_courses, init_completed_course_grades):
        self.name = init_name
        self.address = init_address
        self.completed_courses = init_completed_courses
        self.completed_course_grades = init_completed_course_grades
        
    def setName(self, new_name): #set the variable, can set again after initial declaration
        self.name = new_name 
    def getName(self): #get the variable by returning it
        return self.name
    
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
    
class Professor:
    def __init__(self, name, address, courses_taught): #won't use init for these vars  
        self.name = name
        self.address = address
        self.courses_taught = courses_taught
        
    def setName(self, name):
        self.name = name
    def getName(self):
        return self.name
    
    def setAddress(self, address):
        self.address = address
    def getAddress(self):
        return self.address
    
    def setCoursesTaught(self, courses_taught):
        self.courses_taught = courses_taught
    def getCoursesTaught(self):
        return self.courses_taught