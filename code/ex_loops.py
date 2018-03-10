
## Loop Excercise
use the markdown table template below to trace the output of the cell below. add
lines to the table as needed

| Line no | Variables            |
|---------|----------------------|
|    1    |                      |
|         |                      |
|         |                      |
|         |                      |

_hint: in command mode of a notebook, you can turn on line numbers of a code
cell by pressing l_

total = 0
for char in "tin":
    total = total + 1

# fill in the blanks to  complete each of the following
## Loop Excercise 2 -

# reverse the string and print nit
original = "tin"
result = ____
for char in original:
    result = ____
print(result)

# Total length of the strings in the list: ["red", "green", "blue"] => 12
total = 0
for word in ["red", "green", "blue"]:
    ____ = ____ + len(word)
print(total)

#  List of word lengths: ["red", "green", "blue"] => [3, 5, 4]
lengths = ____
for word in ["red", "green", "blue"]:
    lengths.____(____)
print(lengths)

# Concatenate all words: ["red", "green", "blue"] => "redgreenblue"
words = ["red", "green", "blue"]
result = ____
for ____ in ____:
    ____
print(result)

# Create acronym: ["red", "green", "blue"] => "RGB"
# write the whole thing

## ist Excercise 3
1. Read the code below and try to identify what the errors are without running it.
1. Run the code, and read the error message. What type of error is it?
1. Fix the error.
seasons = ['Spring', 'Summer', 'Fall', 'Winter']
print('My favorite season is ', seasons[4])
