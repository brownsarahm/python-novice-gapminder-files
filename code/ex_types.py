# ex0: split this into multiple cells and choose the either python or markdown for each

## Types Excercise 1
# What type of value is 3.4? How can you find out?

## Types Excercise 2
# What type of value is 3.25 + 4?

## Types Excercise 3
What type of value (integer, floating point number, or character string) would you use to represent each of the following? Try to come up with more than one good answer for each problem. For example, in # 1, when would counting days with a floating point variable make more sense than using an integer?

1. Number of days since the start of the year.
1. Time elapsed since the start of the year.
1. Serial number of a piece of lab equipment.
3. A lab specimen’s age.
1. Current population of a city.
1. Average population of a city over time.

Note: _see in markdown that those number display as incementing even though in
the plain source they're not in order!. This means you can make a list and then add
a new item in the middle of the list without having to change the numbers_

## Types Excercise 4

# Which of the following will have a value of 2.0?
# Note: there may be more than one right answer.

first = 1.0
second = "1"
third = "1.1"
a = first + float(second)
b = float(second) + float(third)
c = first + int(third)
d = first + int(float(third))
e= int(first) + int(float(third))
f = 2.0 * second

##  Types Excercise 5

Python provides complex numbers, which are written as 1.0+2.0j. If val is an imaginary number, its real and imaginary parts can be accessed using dot notation as val.real and val.imag.

1. Why do you think Python uses j instead of i for the imaginary part?
1. What do you expect 1+2j + 3 to produce?
1. What do you expect ‘4j’ to be? What about 4 j or `4 + j’?
