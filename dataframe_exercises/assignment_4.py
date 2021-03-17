# ISI 300 Vincenzo Mezzio Assignment 4

import numpy as np
import pandas as pd

#references
#https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.loc.html
#https://numpy.org/doc/stable/reference/generated/numpy.mean.html

#load data from the csv file
stats = pd.read_csv('Euro_2012_stats_TEAM.csv')

#select only the goal column
print(stats[['Goals']]) #returns as dataframe
print()

#show the humber of teams in the database
print("Total number of teams:", len(stats["Team"])) #get the length of the list of teams
print()

#show only the columns Team, Yellow Cards and Red Cards
print(stats.loc[:,["Team","Red Cards","Yellow Cards"]])
print() #with loc we have a start : end.
# :, makes it so it lists out an enitre column, no condition for the rows

# sort the teams by red cards, then by yellow cards
#print(stats.sort_values(by=['Red Cards'])) #this one does sort but it shows every column
print(stats.loc[:,["Team", "Red Cards"]].sort_values(by=["Red Cards"])) #sorts and only shows the two columns
#sort_values is a built in fcn.
print()
#print(stats.sort_values(by=['Yellow Cards'])) #two different print statements to print one for red cards sorting and the other for yellow
print(stats.loc[:,["Team", "Yellow Cards"]].sort_values(by=["Yellow Cards"]))

#calculate the mean number of yellow cards in the tournament
print(stats.groupby('Team').agg({'Yellow Cards':[np.mean]}))
print() #group by filters the left column. We will do it by teams (default order)
#next we use aggregates. Aggregates can calc the mean and aggregates need grouped by to be used.

#find teams that scored more than 6 goals.
print(stats[(stats['Goals'] > 6)]) #repeat the name of the data frame so it d/n print out as true false list
print()

#select the teams whose name start with a G
#print(stats[(stats['Team']])
print(stats[(stats["Team"].str.startswith("G"))]) #displays the true false condition IF you do not write the name of the db twice!!
print()

#select the first 7 columns
print(stats.iloc[:, list(range(7))]) #we use iloc to select the first 7 columns (range 7)
print() #again the :, means we do not alter the rows

#select all columns except the last 3
print(stats.iloc[:, :-3]) #-3 shows what we want to exclude
print() # :-3 means we do not want to alter the beginning (left side) but we want to alter the condition of the end (right side)

#present only the shooting accuracy from england, italy, and russia
part1 = stats.loc[:,['Team','Shooting Accuracy']] #part 1 selects only the team names and shooting accuracy columns
print(part1.loc[[3,7,12],:]) #we display the two columns but on the left side (of :) we want to display only rows england index 3, italy index 7, and russia index 12
#print(stats[(stats['Team'] == "England") & stats.s ])
print()