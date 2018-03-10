## Data Looping Excercise 1
# Modify this program so that it prints the number of records in the file that has the fewest records.

import pandas
fewest = ____
for filename in glob.glob('data/*.csv'):
    dataframe = pandas.____(filename)
    fewest = min(____, dataframe.shape[0])
print('smallest file has', fewest, 'records')

## Data Looping Excercise 2

Write a program that reads in the regional data sets and plots the average GDP
per capita for each region over time in a single chart.
