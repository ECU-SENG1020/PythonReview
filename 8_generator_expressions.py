
# List of numbers 0 through 9
numbers = [x for x in range(10)]

# Generator function using yield
def generator_function(nums):
    for x in nums:
        yield x**2

gen_func = generator_function(numbers)

print('Print using generator function and next()')
# next prints the next item returned by the generator
print(next(gen_func))
print(next(gen_func))
print(next(gen_func))

print('Print using generator function in for loop')
# Using a loop to get remaining values
for item in gen_func:
    print(item)

# Generator expression
gen_exp = (x**2 for x in numbers)

print('Print using generator expression and next()')
# next prints the next item returned by the generator expression
print(next(gen_exp))
print(next(gen_exp))
print(next(gen_exp))

print('Print using generator expression in for loop')
# Using a loop to get remaining values
for item in gen_exp:
    print(item)