
## DataFrames Excercise 1
# Write an expression to find the Per Capita GDP of Serbia in 2007.

## DataFrames Excercise 2: DataFrame slicing
1. Do the two statements below produce the same output?
1. Based on this, what rule governs what is included (or not) in numerical slices and named slices in Pandas?

print(data.iloc[0:2, 0:2])
print(data.loc['Albania':'Belgium', 'gdpPercap_1952':'gdpPercap_1962'])


## DataFrames Excercise 3
# Improve the following code with comments and better variable names

first = pandas.read_csv('data/gapminder_all.csv', index_col='country')
second = first[first['continent'] == 'Americas']
third = second.drop('Puerto Rico')
fourth = third.drop('continent', axis = 1)
fourth.to_csv('result.csv')

# bonus: is your current working directory the best place to save processed data?


## DataFrames Excercise 4
# Add documentation to the following excerpt and make yourself some notes about
# what `idxmin` and `idxmax` and where you would use them
data = pandas.read_csv('data/gapminder_gdp_europe.csv', index_col='country')
print(data.idxmin())
print(data.idxmax())

## DataFrames Excercise 5

#Generate the following stats as

# GDP per capita for all countries in 1982.
# GDP per capita for Denmark for all years.
# GDP per capita for all countries for years after 1985.
# GDP per capita for each country in 2007 as a multiple of GDP per capita for
#   that country in 1952.
