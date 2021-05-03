# ISI 300   3/8/21      Continuing L05
# create a dataframe

import numpy as np
import pandas as pd

#data = {'year': [2010, 2011, 2012, 2011, 2012, 2010, 2011, 2012],
#'team': ['Bears', 'Bears', 'Bears', 'Packers', 'Packers', 'Lions', 'Lions', 'Lions'],
#'wins': [11, 8, 10, 15, 11, 6, 10, 4],
#'losses': [5, 8, 6, 1, 5, 10, 6, 12]}

#df_football = pd.DataFrame(data, columns=['year', 'team', 'wins', 'losses']);
#print(df_football)


# saving to CSV file, no index
#print("Save dataframe to CSV file")
#df_football.to_csv('game_stats.csv', index=False) #i do not think I need to define the path, looks like it is in class_code by default

# loading from CSV file
print("Load dataframe from CSV file")
df_football = pd.read_csv('game_stats.csv') #variable to save the file we want to read
print("Print dataframe loaded from CSV")
print(df_football) #printing the var that stores the data.

# info about a dataframe
print()
print("Info about a dataframe:")
df_football.info()

# stats about dataframe 
print()
print("Stats about a dataframe")
print(df_football.describe())

# head and tail
print()
print("First 3 rows")
print(df_football.head(3)) #top three lines

print()
print("Last 2 rows")
print(df_football.tail(2)) #removing the 2 will give us 5 lines (by default)

# slicing, identical to series and lists. Pick on the rows
print()
print("Slicing 2:5")
print(df_football[2:5]) # we take a subset of the data to print out

# selecting, pick on some of the columns
print()
print("Show columns 'year' and 'team'")
print( df_football[ ['year','team'] ].head() )
#inner [] are the list of columns we want to see
#df_footbal[2:5] are rows and df_footbal['year', 'team'] are columns


# filtering, select data based on a condition!
print()
print("Packers' data")
print( df_football[ df_football['team'] == 'Packers' ] )
#prints out all ROWS where team = packers
#need to repeat the name of the data frame inside the []

print()
print("condition result on packers")
print(df_football['team'] == 'Packers')
#this is why we need to repeat the name of the data frame


#narrow down our search inside the data.
print()
print("Packers' data for 2012")
print( df_football[ (df_football['team'] == 'Packers') &
(df_football['year'] == 2012 ) ] ) #our only good result is index 5

print()
print("condition result on 2012")
print(df_football['year'] == 2012)
#you can look at the above's table as the following:
    # one table checks for condition result on team = packers
    # other table checks on result of year = 2012
    # essentially an AND statement, both conditions MUST be TRUE

# using the OR condition
print()
print("Packers' data for 2012, or about 'Lions'")

print( df_football[ 
    (df_football['team'] == 'Packers') #packers AND 2012
    & (df_football['year'] == 2012 ) #packers 2012 OR Lions
    | (df_football['team'] == 'Lions' ) 
    ] )

#we use single & and | in python!!
# if you want to be sure what you are writing you can wrap the text in ()
# for instance, you can write & ( or condition ) so it MUST be condition prior to &


# indexing
print()
print("Setting an index on year-team")
df_football.set_index( ['year','team'], inplace = True )
df_football.sort_index(inplace=True)
print(df_football)
# we can overwrite the data frame with a new index. No longer a num but a number
# and a name!
# inplace remain, force the name on tha same variable and continue.
# if this is false ^, python takes a copy
#   Our data is the same, just a different shape. Before everything was a row
#   The empty space where the year would be STILL has the year value, it is NOT NULL

#slicing revisited
print()
print("Show the first 2 rows")
print(df_football[0:3]) #0,1,2. 3 is excluded

print()
print("Show the first 2 rows, using iloc") #index numeric location (iloc)
print(df_football.iloc[0:3])
# you may have to use one or the other depending on the occassion

#slice with named index
print()
print("Show the rows for the index 2010")
print(df_football.loc[(2010)])

print()
print("Show the rows for the index 2010-Lions")
print(df_football.loc[(2010,'Lions')])
#professor is not a fan of referring to this syntax

print()
print("Show the rows for the index: from 2010-Lions to 2011")
print(df_football.loc[(2010,'Lions'):(2011)])
#statisticians love uusing this syntax


#Index can be reset to "standard" numbers
print()
print("Resetting the index")
df_football.reset_index(inplace = True)
print(df_football)
#back to the old index


#add a column to the dataframe
print()
print("Add a column")
df_football['country'] = "USA" #every row will be USA in country column
print(df_football)

#operations across columns one row at a time
print()
print("Add a column, from operation")
df_football['games'] = df_football['wins'] + df_football['losses']
print(df_football)
# we are calcualting total number of games which is caluclated by the sum of
# wins and loses!
#   we have to state which column we are working with. Games is a new column
#   This syntax creates a loop for each row. Also attach games to all the rows


# extending dataframe by row
#what is a row? a small dataframe consited of a ...
print()
data_more_games = {'year': [2015, 2016],
                   'team': ['Dolphins', 'Dolphins'],
                   'wins': [8, 10], 'losses': [8, 6],
                   'country': 'USA', 'games': [16, 16]} #two columns each

df_football_more_games = pd.DataFrame(
        data_more_games
        , columns=['year'
                   , 'team', 'wins', 'losses'
                   , 'country', 'games'
                   ]
        )

print("Additional data")
print(df_football_more_games) #same data structure
#stitch them together! use APPEND!
df_football_all_games = df_football.append(df_football_more_games)

# note: index duplicates
print()
print("All data")
print(df_football_all_games)

# reset index to remove duplicates
print()
df_football_all_games.reset_index(inplace=True)
print(df_football_all_games)
#simply use reset index key words


print()
print("Length")
print(len(df_football_all_games))
#prints length which is 10 rows
print(len(df_football_all_games)*['Zone-NA'])

#new column which has a sequence of values 
s_region = pd.Series(len(df_football_all_games)*['Zone-NA'])
#10 times array of one element
s_continent = pd.Series(len(df_football_all_games)*['America'])
#same strat, repeat america same amount of times as the length

print(s_region)
print(s_continent)

#let us attach it to the dataframe via concatination
#i am creating a new dataframe from two series
df_region = pd.concat([s_region,s_continent], axis=1) 
print()
print("The new dataframe")
print(df_region) # no name for columns yet

#giving a name to the columns
df_region.columns = ['region','continent']
print()
print("The new dataframe, now with column names")
print(df_region) # no name for columns yet


#extend dataframe with a set of given values
df_football_all_data = pd.concat([df_football_all_games,df_region], axis=1)
print("Games with region data",df_football_all_data)


#   Sorting

# just one column
print()
print("Sort by one column")
print(df_football.sort_values(by='team'))
#alphabetical order, bears is first.

# just multiple columns
print()
print("Sort by multiple columns")
print(df_football.sort_values(by=['team','wins'], ascending=False))
#sort by teams and wins descending (z to a)
#when the same value conflicts it will look at the next criteria, wins.

# applying functions, built-in
print()
print("Max of each column")
print(df_football.apply(max, axis=0)) #what is axis 0? by column
#0 goes vertically (columns) and 1 would go horizontally (rows)

print()
print("Minimum")
print(df_football.apply(np.min, axis=0)) 


# applying functions, custom, whole row
print()
def calculate_points(row): # function, ** requires a dataframe **
    points = 3*row['wins'] + 1*row['losses'] #takes two values, wins and losses
    return(points) # 3 points for a win and 1 point for a loss
    
#add a new column called score by win losses
df_football['score_by_wr'] = \
    df_football.apply(calculate_points, axis=1) # the \ means fcn continues on next line
print("Score by whole row")
print(df_football)


#another way to apply the fcn, lamba. It is a fcn that can be applied on the fly!
# applying functions, custom, arbitrary parameters
def calculate_points2 ( wins, losses ): #passing basic data types
    points = 3*wins + 1*losses
    return(points)
#same type of fcn but defining it a bit differently
#a bit more flexible because you d/n need a dataframe to make it work

df_football['score_by_ap'] = df_football.apply( \
    lambda row: calculate_points2( 
    row['wins']
    , row['losses'] ), axis=1)

print()
print("Score by arbitrare parameters")
print(df_football)


# Aggregates, calculates mean, max, min, count, etc.
#for each team, we want to know how many games they won (by count) and on avg how many
#they played

print()
# group-by and aggregates, we can only use aggregate by using group by
print( df_football.groupby('team').agg(
    { 'wins': [np.size, np.mean] } ) )
#count how many entries! Calculate the mean for the average!
#the three lines that have same team name become one group / one line
# specifically looking at wins ^^ as defined above

# we can load data from csv files and excel files. We can connect to a database and load
# data from a database. data is auto collected. we can filter values, remove null values
# we can transform data with built in fcns or custom fcns
# we have all the tools to work with data to draw analysis

# charts are an easy way to visualize all of the work we did

# charting
import matplotlib.pyplot as plt #library in python to draw a chart, this is one of them
# team avg wins over all years
df_football.groupby(
    ['team']).agg({'wins': [np.mean]}).plot(kind='bar')
# result of an aggregate.
#this is a bar chart we can make multiple kinds of charts


# team championships
df_football.groupby(['team']).agg({'year': [np.size]}).plot(kind='bar')

# team wins (count and average) by year
df_football.groupby(['team','year']).agg({'wins': [np.size,
np.mean]}).plot(kind='bar')

# team wins (count and average) by year, other chart type
df_football.groupby(['team','year']).agg({'wins': [np.size,
np.mean]}).plot(kind='hist')

# team wins as pie chart
df_football.groupby(['team']).agg({'wins': [np.sum]}).plot(kind='pie',
subplots=True)

# Merge
#merges two dataframes into one, similar to join operation in relational databses
# horizontal stiching of two dataframes on common columns

#left data frame
left = pd.DataFrame({
    'id':[1,2,3,4],
    'prof':['Paolo','Tom','Michele','Alessia'],
    'subject':['ISI300','MTK101','ISI374','MTK101']
    }
)

#right dataframe
right = pd.DataFrame({
    'id':[1,2,3],
    'subject':['ISI300','MTK101','ISI374'],
    'building':['3N','1C','2M']
    }
)

print()
print(left)
print()
print(right)
print()
#merge the dataframes
print(pd.merge(left,right,on='subject'))
print()
# Notice how MTK101 is listed twice with same building number and respective professor!