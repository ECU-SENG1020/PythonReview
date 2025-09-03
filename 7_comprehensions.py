

# List comprehensions
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
numbers = [x for x in range(10)]
print('List of numbers:')
print(numbers)

# even_numbers = [x for x in numbers if x % 2 == 0]
# print('Even numbers:')
# print(even_numbers) 

# odd_numbers = [x for x in numbers if x % 2 != 0]
# print('Odd numbers:')
# print(odd_numbers)

# squared_numbers = [x**2 for x in numbers]
# print('Squared numbers:')
# print(squared_numbers)

# numbers_set = {x for x in numbers}
# print('Set of numbers:')
# print(numbers_set)

# dictionary_squared_numbers = {x: x**2 for x in numbers}
# print('Dictionary of squared numbers:')
# print(dictionary_squared_numbers)

# There is no tuple comprehension.  
# The reason is that the syntax for tuple comprehension would be 
# the same as for generator expressions, which use parentheses instead 
# of square brackets.