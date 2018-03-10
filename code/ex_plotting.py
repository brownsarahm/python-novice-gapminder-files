## Plotting Excercise 1

# Fill in the blanks below to plot the minimum GDP per capita over time for all
#  the countries in Europe.
data_europe = pandas.read_csv('data/gapminder_gdp_europe.csv', index_col='country')
data_europe.____.plot(label='min')
data_europe.____
plt.legend(loc='best')
plt.xticks(rotation=90)

# Modify it again to plot the maximum GDP per capita over time for Europe.


## Plotting Excercise 2
# add annotation for the new keywords introduced in this plot
data_all = pandas.read_csv('data/gapminder_all.csv', index_col='country')
data_all.plot(kind='scatter', x='gdpPercap_2007', y='lifeExp_2007',
              s=data_all['pop_2007']/1e6)
