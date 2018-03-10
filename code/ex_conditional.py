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
