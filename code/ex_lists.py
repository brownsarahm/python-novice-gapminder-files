## Lists Excercise 1

Complete the code below to generate the following output
```
first time: [1, 3, 5]
second time: [3, 5]
```

values = ____
values.____(1)
values.____(3)
values.____(5)
print('first time:', values)
values = values[____]
print('second time:', values)

## Lists Excercise 2

# run this code, then answer the questions below
print('string to list:', list('tin'))
print('list to string:', ''.join(['g', 'o', 'l', 'd']))


Explain in simple terms what list('some string') does.
What does '-'.join(['x', 'y']) generate?


## Lists Excercise 3

# use this code to answer the questions below
element = 'helium'
print(element[-1])

1. How does Python interpret a negative index?
1. If a list or string has N elements, what is the most negative index that can
safely be used with it, and what location does that index represent?
1. If values is a list, what does del values[-1] do?
How can you display all elements but the last one without changing values? (Hint: you will need to combine slicing and negative indexing.)
