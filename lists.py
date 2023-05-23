
######## Appending Elements to the End of a List ########
motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

######## Inserting Elements into a List ########
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati')
print(motorcycles)

######## Removing an Item Using the del Statement ########
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
del motorcycles[0]
print(motorcycles)

######## Removing an Item Using the pop() Method ########
"""
The pop() method removes the last item in a list, but it lets you work
with that item after removing it
"""
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

######## Popping Items from any Position in a List ########
motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}.")

"""
If you're unsure whether to use the del statement or the pop() method,
here's a simple way to decide: when you want to delete an item from a list
and not use that item in any way, use the del statement; 
if you want to use an item as you remove it, use the pop() method
"""

######## Removing an Item by Value ########
"""
The remove() method deletes only the first occurrence of the value you 
specify. If there's a possibility the value appears more than once in 
the list, you'll need to use a loop to make sure all occurrences of the 
value are removed.
"""
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)

######## Sorting a List Permanently with the sort() Method ########
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)

######## Sorting a List Temporarily with the sorted() Function ########
"""
To maintain the original order of a list but present it in a sorted order, 
you can use the sorted() function. The sorted() function can also accept a 
reverse=True argument if you want to display a list in reverse alphabetical order.
"""
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))
print("\nHere is the original list again:")
print(cars)

"""
Sorting a list alphabetically is a bit more complicated when all the values are not in
lowercase.
"""

######## Printing a List in Reverse Order ########
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.reverse()
print(cars)

######## Finding the Length of a List ########
cars = ['bmw', 'audi', 'toyota', 'subaru']
len(cars)

######## Using the range() Function ########
for value in range(1, 5):
    print(value)

"""
The output of above code will be 1 2 3 4. To print first 5 numbers use range(1, 6). 
You can also pass range() only one argument, and it will start the sequence of numbers at 0. 
For example, range(6) would return the numbers from 0 through 5.
"""

######## Using range() to Make a List of Numbers ########
numbers = list(range(1, 6))
print(numbers)

######## Using the range() function to tell Python to skip numbers in a given range ########
even_numbers = list(range(2, 11, 2))
print(even_numbers)

######## Using range() function to make a list of the first 10 square numbers ########
squares = []
for value in range(1, 11):
    square = value ** 2    # In Python, two asterisks (**) represent exponents.
    squares.append(square)
    print(squares)

######## More concise version of above code ########
squares = []
for value in range(1,11):
    squares.append(value**2)
    print(squares)

######## Simple Statistics with a List of Numbers ########
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
min(digits)
max(digits)
sum(digits)

######## List Comprehensions ########
"""
A list comprehension combines the for loop and the creation of new elements into one line, 
and automatically appends each new element
"""
squares = [value**2 for value in range(1, 11)]
print(squares)

# Slicing a List
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])  # Will return first 3 items in the list

print(players[:4])    # Without a starting index, Python starts at the beginning of the list

print(players[2:])    # Without a ending index, Python ends at the end of the list

print(players[-3:])   # To get last 3 items in the list

"""
You can include a third value in the brackets indicating a slice. If a third value is
included, this tells Python how many items to skip between items in the specified range.
"""

######## Looping Through a Slice ########
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())

######## Copying a List ########
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]    # Omitting the first index and the second index ([:]) tells Python to make a slice that starts at the first item and ends with the last item

# This doesn't work:
# friend_foods = my_foods

"""
This syntax actually tells Python to associate the new variable friend_foods with the list that is 
already associated with my_foods, so now both variables point to the same list. As a result, when we
add 'cannoli' to my_foods, it will also appear in friend_foods. Likewise 'ice cream' will appear in 
both lists, even though it appears to be added only to friend_foods.
"""

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)
    
print("\nMy friend's favorite foods are:")
print(friend_foods)

"""
Note: If you're trying to work with a copy of a list and you see unexpected behavior, make sure you are 
copying the list using a slice, as we did in the first example
"""




























