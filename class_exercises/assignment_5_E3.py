# ISI 300 Vincenzo Mezzio Assignment 5 Exercise 3

class Professor:
    def __init__(self, name): #i think it's good practice for these vars to be private?
        self.__name = name
        self.__courses_allowed = []
        self.__semester_courses = []
        
    def setName(self, name): #getters and setters
        self.__name = name
    def getName(self):
        return self.__name
    
    def setCoursesAllowed(self, allowed):
        self.__courses_allowed = allowed
    def getCoursesAllowed(self):
        return self.__courses_allowed
    
    def setSemesterCourses(self, semester):
        self.__semester_courses = semester
    def getSemesterCourses(self):
        return self.__semester_courses
    
    def addAllowedCourse(self, name): #add a course
        self.__courses_allowed.append(name)
    def removeAllowedCourse(self, name): #remove a course
        if(name in self.__courses_allowed): #check if it is inside
            self.__courses_allowed.remove(name)
        else:
            print('Course not in the list!')
    
    def addCourse(self, semester, course): #add course to semester as a pair
        if(course in self.__courses_allowed): #check if professor can teach this course
            self.__semester_courses.append((semester, course))
        else:
            print('Professor can not teach the course', course)
    
    def removeCourse(self, semester, course): #remove the course for semester as a pair
        if ((semester, course) in self.__semester_courses): #check if the pair is in semester_courses
            self.__semester_courses.remove((semester, course)) 
        else:
            print('The pair of the course', course,'and the semester',semester,' were not found on the list!')
            
            
    def removeAllSemesterCourses(self, semester):
        temp = [] #temp stores courses that we d/n want to remove
        for i in self.__semester_courses: #looking for the course
            if(semester not in i): #removing all courses with semester
                temp.append(i) #put the courses we DO NOT want to remove in temp
        self.__semester_courses = [] #empty the original list of courses
        self.__semester_courses = temp #put the new list of courses in original list. New list d/n have courses we wanted to remove
        
    def removeAllCourseCourses(self, course): #remove all scheduled courses for a given course
        temp = [] 
        for i in self.__semester_courses: #looking for the course
            if(course not in i): #removing all courses with course
                temp.append(i)
        self.__semester_courses = []
        self.__semester_courses = temp
        
prof = Professor('Cappellari')
prof.addAllowedCourse('ISI300')
prof.addAllowedCourse('CSC315')
prof.addAllowedCourse('BUS215')

prof.addCourse('Spr 21', 'ISI300')
prof.addCourse('Fall 20', 'ISI300')
prof.addCourse('Spr 21', 'CSC315')
prof.addCourse('Fall 19', 'CSC315')
prof.addCourse('Fall 20', 'BUS215')
prof.addCourse('Fall 19', 'BUS215')
prof.addCourse('Spr 21', 'CSC330') #will not allow 

print()
print('Courses allowed for Professor: ', prof.getCoursesAllowed())
print()
print('Courses for Professor: ', prof.getSemesterCourses())
print()

prof.removeAllSemesterCourses('Fall 19')
print('Post removal of Fall 19 courses; courses for Professor:', prof.getSemesterCourses())
print() #Fall 19 is gone

prof.removeAllCourseCourses('ISI300')
print('Post removal of ISI courses; courses for Professor:', prof.getSemesterCourses())
print() #ISI courses are gone