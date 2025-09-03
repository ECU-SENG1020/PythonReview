# list
# mutable collection of heterogenous data types
fruit_list = ['apple','banana', 'cherry']

# tuple
# immutable collection of heterogenous data types
fruit_tuple = ('apple','banana','cherry')

# dictionary
# collection of key:value pairs
fruit_dictionary = {'a':'apple','b':'banana'}

# set
# collection of unique values
fruit_set = {'apple','banana', 'cherry','cherry'}

# converting a tuple to a list using list constructor
fruits2 = list(fruit_tuple)

# iterating over collections

print("***** List *****")
for fruit in fruit_list:
    print(fruit)

print("***** tuple *****")
for fruit in fruit_tuple:
    print(fruit)

print("***** set *****")
for fruit in fruit_set:
    print(fruit)

print("***** dictionary *****")
for fruit in fruit_set:
    print(fruit)
