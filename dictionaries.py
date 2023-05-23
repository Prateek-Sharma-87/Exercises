"""
A dictionary in Python is a collection of key-value pairs. Each key is connected
to a value, and you can use a key to access the value associated with that key.
A key's value can be a number, a string, a list, or even another dictionary.
In fact, you can use any object that you can create in Python as a value in a
dictionary.

A key-value pair is a set of values associated with each other. When you
provide a key, Python returns the value associated with that key. Every key
is connected to its value by a colon, and individual key-value pairs are separated
by commas. You can store as many key-value pairs as you want in a
dictionary.
"""

######## Adding New Key-Value Pairs ########
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

"""
As of Python 3.7, dictionaries retain the order in which they were defined. When you print a dictionary or loop through its elements, you will see the elements in the same order in which they were added to the dictionary
"""

######## Starting with an Empty Dictionary ########
alien_0 = {}

alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)

######## Modifying Values in a Dictionary ########
alien_0 = {'color': 'green'}
print(f"The alien is {alien_0['color']}.")

alien_0['color'] = 'yellow'
print(f"The alien is now {alien_0['color']}.")

######## Removing Key-Value Pairs ########
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

del alien_0['points']
print(alien_0)

""" Be aware that the deleted key-value pair is removed permanently """

######## Adding more than one line to define a dictionary ########

"""
When you know you'll need more than one line to
define a dictionary, press enter after the opening brace. Then indent the
next line one level (four spaces), and write the first key-value pair, followed
by a comma. From this point forward when you press enter, your text editor
should automatically indent all subsequent key-value pairs to match the
first key-value pair. It's good practice to include a comma after the
last key-value pair as well, so you're ready to add a new key-value pair on the
next line.
"""

favorite_languages = {
    'jen': 'python', 
    'sarah': 'c', 
    'edward': 'ruby', 
    'phil': 'python',
}

######## Using get() to Access Values ########
"""
The get() method requires a key as a first argument. As a second
optional argument, you can pass the value to be returned if the key doesn't
exist. If the key 'points' exists in the dictionary, you'll get the corresponding
value. If it doesn't, you get the default value. In this case, points doesn't
exist, and we get a clean message instead of an error. If there's a chance the key you're asking for might not exist, consider using the get() method instead of the square bracket notation.

If you leave out the second argument in the call to get() and the key doesn't exist, Python will return the value None. The special value None means “no value exists.” This is not an error: it's a special value meant to indicate the absence of a value.
"""

alien_0 = {'color': 'green', 'speed': 'slow'}

point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)

######## Looping Through a Dictionary ########

# Looping Through All Key-Value Pairs
user_0 = {
    'username': 'efermi', 
    'first': 'enrico', 
    'last': 'fermi',
}

""" The method items() returns a list of key-value pairs """

for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")

# Looping Through All the Keys in a Dictionary
favorite_languages = {
    'jen': 'python', 
    'sarah': 'c', 
    'edward': 'ruby', 
    'phil': 'python',
}

""" The keys() method is useful when you don't need to work with all of the values in a dictionary. Looping through the keys is actually the default behavior when looping
through a dictionary. You can choose to use the keys() method explicitly if it makes your code easier to read, or you can omit it if you wish. The keys() method isn't just for looping: it actually returns a list of all the keys. """

for name in favorite_languages.keys():
    print(name.title())

# OR

for name in favorite_languages:
    print(name.title())

# Looping Through All the Keys in a Dictionary and Accessing required values

favorite_languages = {
    'jen': 'python', 
    'sarah': 'c', 
    'edward': 'ruby', 
    'phil': 'python',
}

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())
    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")

if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")

# Looping Through a Dictionary’s Keys in a Particular Order
"""
Starting in Python 3.7, looping through a dictionary returns the items in
the same order they were inserted. Sometimes, though, you'll want to loop
through a dictionary in a different order. One way to do this is to sort the keys as they're returned in the for loop. You can use the sorted() function to get a copy of the keys in order.
"""

favorite_languages = {
    'jen': 'python', 
    'sarah': 'c', 'edward': 'ruby', 
    'phil': 'python',
}

for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")

# Looping Through All Values in a Dictionary
"""
The values() method returns a list of values without any keys. This approach pulls all the values from the dictionary without checking for repeats. To see each value without repetition, we can use a set. A set is a collection in which each item must be unique. When you wrap set() around a list that contains duplicate items, Python identifies the unique items in the list and builds a set from those items.
"""
favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}
print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())

######## Nesting - A List in a Dictionary ########
pizza = {
    'crust': 'thick', 
    'toppings': ['mushrooms', 'extra cheese'],
}

print(f"You ordered a {pizza['crust']}-crust pizza " 
      "with the following toppings:")

for topping in pizza['toppings']:
    print("\t" + topping)

favorite_languages = {
    'jen': ['python', 'ruby'], 
    'sarah': ['c'], 
    'edward': ['ruby', 'go'], 
    'phil': ['python', 'haskell'],
}
for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}")

"""
You should not nest lists and dictionaries too deeply. If you're nesting items much
deeper than what you see in the preceding examples or you're working with someone
else's code with significant levels of nesting, most likely a simpler way to solve the
problem exists.
"""

######## A Dictionary in a Dictionary ########
"""
You can nest a dictionary inside another dictionary, but your code can get complicated quickly when you do.
"""
users = {
    'aeinstein': {
        'first': 'albert', 
        'last': 'einstein', 
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}
for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']
    
    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")

"""
Notice that the structure of each user's dictionary is identical. Although not required by Python, this structure makes nested dictionaries easier to work with. If each user's dictionary had different keys, the code inside the for loop would be more complicated.
"""






