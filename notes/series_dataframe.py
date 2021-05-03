# 3/1/21 class ISI 300 L05

import pandas as pd #importing the pandas library
import numpy as np

#   create a series

s = pd.Series([7, 'Paolo', 'ISI', 300]) #this guy comes from Pandas library, that's whay we type "pd."
print(s) #prints the series as a list
#this is also a good way to check if it is installed correctly!
#dtype listed at the bottom implies the data type, if the list has integers the dtype would be int64

#   named index
print()
t = pd.Series(
              [7, 'Paolo', 'ISI', 300]
              , index=['id','name','program','code'])
print(t) #refer to index "program" rather than index 2. Give me the value form "program" More convenient

print()
print("Print program by index:",t[2])# prints ISI

print("Print the program by named-index:",t['program'])
#end result is the same but would you rather rememner index number or index name?

print()
#create a series with city population data
s_population = pd.Series([1000,1300,900,1100,450,None]#NaN means Not A Number
                         ,index=['Chicago','New York','Portland'
                                 ,'San Francisco','Austin','Boston'])
print("Population\n", s_population) #NaN tells the series it is a float. Interesting...

print()
# printing a few cities
print("A few cities, by index-numb")
print(s_population[[0,2,3]]) #we NEED a DOUBLE BRACKET NOTATION

print()
# printing a few cities by the index-name
print("A few cities, by index-name")
print(s_population[['Chicago','Portland','San Francisco']])#double bracket
#basically, square brackets are used for the numeric values

print()
# loop+if condition. State the condition we want to go for. Condition applies to DATA NOT the INDEX
print("Large cities, that is population > 1000")
print(s_population[ s_population>1000 ])

print()
print("Condition... population > 1000")
print(s_population>1000) #boolean values / boolean condition
# ^^this statement takes the series and comapres against the series (while loop)

print()
print("Large cities using booleans")
print(s_population[ [False,True,False,True,False,False] ])
#true, show the value, false, do not show the value

print()
print("Old value for Chicago:", s_population['Chicago'])
s_population['Chicago'] = 1400 #updating the value of Chicago
print("New value for Chicago:", s_population['Chicago'])

# update in bulk: Conditional Value Update
print()
print("Old values:")
print(s_population)
s_population[s_population<1000] = 750 #if less than 1000 update to 750
print("New values:")
print(s_population)

print()
#       membership: checking value is present
#convenient way to avoid a loop
print('Seattle' in s_population) #keyword in, we have seen this in for loops
print('San Francisco' in s_population)

print()
#       math operations on series
# slash city popultion to 1/3
print("Old values:")
print(s_population)
s_population = s_population / 3
print("New values:")
print(s_population)
#this helps us avoid loops at the end of the day!!

print()
#           Conditional Bulk Update
# square city values if pop<300
print("Old values:")
print(s_population)
s_population[s_population < 300] = np.square( 
#       NP is from numpy!!!
    s_population[s_population < 300]
    )
print("New values (squares):")
print(s_population)

print()
#           Adding series
s_population_some_cities_part1 = s_population[['Chicago','New York','Portland']]
s_population_some_cities_part2 = s_population[['Austin','New York']]
print("Some cities and population, part 1")
print(s_population_some_cities_part1)
print("Some cities and population, part 2")
print(s_population_some_cities_part2)
#       We are working with two different databases

#           Add populations from series
s_population_all_cities = s_population_some_cities_part1 + s_population_some_cities_part2
print("Population all cities")
print(s_population_all_cities) #\ is supposed to tell python to continue onto the next line

print()
#           Concatenate series, attach the two series together
s_population_all_cities = \
pd.concat( [ \
s_population_some_cities_part1,
s_population_some_cities_part2
] ) #"\" shows to continue onto the next line!!
    #"concat" is the function to concatinate the series'
print("Population after concatenation")
print(s_population_all_cities)

print()
#           Checking for NaN/NULL values
print("City has NaN/NULL value?")
print(s_population.isnull()) ##s.pop == NULL | None | NaN ???
print()
print("Cities having NaN/NULL value")
print(s_population[s_population.isnull()]) 
print()
print("Cities not having NaN/NULL value")
print(s_population[s_population.notnull()])
#.isnull() gives us back true or false whether or not the condition is satisfied
#.notnull does the opposite

#       Applying an aggregate fcn
print("Mean value:", s_population.mean())
#no loop to write, no conditions


#           Lambda Function
# map on custom function
print("Custom function: y = 2*x - 2") #this is our custom fcn
print("Before applying function")
print(s_population)
print()
print("After applying function")
print(s_population.map(lambda value: 2*value - 2 ))
#       LAMBDA means i am defining a function on this lines
#       MAP is applying the funciton to every value inside cities
#   Value is the placeholder we can change it to X if we want
print()

#       Dataframe
# create a dataframe
data = {'year': [2010, 2011, 2012, 2011, 2012, 2010, 2011, 2012],
'team': ['Bears', 'Bears', 'Bears', 'Packers', 'Packers', 'Lions', 'Lions', 'Lions'],
'wins': [11, 8, 10, 15, 11, 6, 10, 4],
'losses': [5, 8, 6, 1, 5, 10, 6, 12]}
football = pd.DataFrame(data, columns=['year', 'team', 'wins', 'losses'])
print(football)
#pd.Dataframe is the way to create the data frame. Our input is data (what we define at the top). Specify that we have a bunch of columns
#It all adds up to be a table

print()
#       Saving as well as Loading dataframes
# saving to CSV file, no index
print("Save dataframe to CSV file")
#from_csv.to_csv('game_stats.csv', index=False)


print()
# loading from CSV file
print("Load dataframe from CSV file")
from_csv = pd.read_csv('game_stats.csv')#need a file with data in it before we can load it
print()
print("Print dataframe loaded from CSV")
print(from_csv)

print()
#       Slicing
print("Slicing 2:5")
print(from_csv[2:5])

print()
#       Selecting
print("Show columns 'year' and 'team'")
print( from_csv[ ['year','team'] ].head() )

print()
#       Filtering
print("Packers' data")
print( from_csv[ from_csv['team'] == 'Packers' ] )

print()
print("Packers' data for 2012")
print( from_csv[ (from_csv['team'] == 'Packers') &
(from_csv['year'] == 2012 ) ] )

print()
print("Packers' data for 2012, or about Lions")
print( from_csv[ (from_csv['team'] == 'Packers') &
(from_csv['year'] == 2012 ) | (from_csv['team'] == 'Lions' ) ] )
# | the "Or" symbol. & the "And" symbol