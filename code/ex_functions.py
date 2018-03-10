## Functions Excercise 1
1. Read the code below and try to identify what the errors are without running it.
1. Run the code and read the error message. Is it a SyntaxError or an IndentationError?
1. Fix the error.
1. Repeat steps 2 and 3 until you have fixed all the errors.

def another_function
  print("Syntax errors are annoying.")
   print("But at least python tells us about them!")
  print("So they are usually not too hard to fix.")

## Functions Excercise 2
# What does the following cell print? (try to guess before running it)
def report(pressure):
    print('pressure is', pressure)

print('calling', report, 22.5)


## Functions Excercise 3

# Fix this code so that it runs:
result = print_date(1871,3,19)

def print_date(year, month, day):
   joined = str(year) + '/' + str(month) + '/' + str(day)
   print(joined)

## Functions Excercise 4

# explain the output of the following code
result = print_date(1871, 3, 19)
print('result of call is:', result)

## Functions Excercise 5
# Fill in the blanks to create a function that takes a single filename as an
# argument, loads the data in the file named by the argument, and returns the
# minimum value in that data.

import pandas

def min_in_data(____):
    data = ____
    return ____

# Now, create a small data file to test your program above

test_data1 = []
df = pd.DataFrame(data= ___, columns=['val'])

## Functions Excercise 6


df = pandas.read_csv('gapminder_gdp_asia.csv', index_col=0)
japan = df.ix['Japan']

#Complete the statements below to obtain the average GDP for Japan across
# the years reported for the 1980s.
year = 1983
gdp_decade = 'gdpPercap_' + str(year // ____)
avg = (japan.ix[gdp_decade + ___] + japan.ix[gdp_decade + ___]) / 2

#Abstract the code above into a single function.
def avg_gdp_in_decade(country, continent, year):
    df = pd.read_csv('gapminder_gdp_'+___+'.csv',delimiter=',',index_col=0)
    ____
    ____
    ____
    return avg
#How would you generalize this function if you did not know beforehand which
# specific years occurred as columns in the data? For instance, what if we also
# had data from years ending in 1 and 9 for each decade? (Hint: use the columns
# to filter out the ones that correspond to the decade, instead of enumerating
# them in the code.)
