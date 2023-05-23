"""
Lists work well for storing collections of items that can change throughout
the life of a program. However, sometimes you'll want to create a list of items that cannot
change. Tuples allow you to do just that. Python refers to values that cannot
change as immutable, and an immutable list is called a tuple.
"""

######## Defining a Tuple ########
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# This will throw an error
# dimensions[0] = 250

"""
Tuples are technically defined by the presence of a comma; the parentheses make them
look neater and more readable. If you want to define a tuple with one element, you
need to include a trailing comma, e.g. my_t = (3,). Although it doesn't often make sense 
to build a tuple with one element, but this can happen when tuples are generated automatically.
"""

######## Looping Through All Values in a Tuple ########
dimensions = (200, 50)
for dimension in dimensions:
    print(dimension)

######## Writing over a Tuple ########
"""
Although you can't modify a tuple, you can assign a new value to a variable that represents a tuple
"""
dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)

"""
When compared with lists, tuples are simple data structures. Use them
when you want to store a set of values that should not be changed throughout
the life of a program.
"""

