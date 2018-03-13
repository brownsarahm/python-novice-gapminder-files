## Conditionnal Excercise 1

# fill in the blanks to make result have 0 where original has negative values
# and 1 where original has positive values

original = [-1.5, 0.2, 0.4, 0.0, -1.3, 0.4]
result = ____
for value in original:
    if ____:
        result.append(0)
    else:
        ____
print(result)

## Conditionnal Excercise 2
#Modify this program so that it only processes files with fewer than 50 records.

import glob
import pandas
for filename in glob.glob('data/*.csv'):
    contents = pandas.read_csv(filename)
    ____:
        print(filename, len(contents))

## Conditionnal Excercise 3
# Functions will often contain conditionals. Here is a short example that will
# indicate which quartile the argument is in based on hand-coded values for
#  the quartile cut points.
def calculate_life_quartile(exp):
    if exp < 58.41:
        # This observation is in the first quartile
        return 1
    elif exp >= 58.41 and exp < 67.05:
        # This observation is in the second quartile
       return 2
    elif exp >= 67.05 and exp < 71.70:
        # This observation is in the third quartile
       return 3
    elif exp >= 71.70:
        # This observation is in the fourth quartile
       return 4
    else:
        # This observation has bad data
       return None

calculate_life_quartile(62.5)


# That function would typically be used within a for loop, but Pandas has a
# different, more efficient way of doing the same thing, and that is by applying
# a function to a dataframe or a portion of a dataframe. Here is an example,
# using the definition above.
data = pd.read_csv('data/gapminder_gdp_americas.csv')
data['life_qrtl'] = data['lifeExp'].apply(calculate_life_quartile)

# Apply this to a second data set and plot them to compare

# Create a function that calculates the life quartiles for a dataset

# Modify your funtion to take two parameters, so that it can use the life
# expectancy that you computed
