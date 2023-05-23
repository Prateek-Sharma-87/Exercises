"""
A docstring describes what the function does. Docstrings are enclosed in triple quotes, which Python looks for when it generates documentation for the functions in your programs.
"""

######## Basic function ########
def greet_user():
    """Display a simple greeting."""
    print("Hello!")

greet_user()

######## Passing Information to a Function ########
def greet_user(username):
    """Display a simple greeting."""
    print(f"Hello, {username.title()}!")

greet_user('jesse')

"""
Arguments and Parameters:
The variable username in the definition of greet_user() is an example of a parameter, a piece of information the function needs to do its job. The value 'jesse' in greet_user('jesse') is an example of an argument. An argument is a piece of information that's passed from a function call to a function. When we call the function, we place the value we want the function to work with in parentheses. In this case the argument 'jesse' was passed to the function greet_user(), and the value was assigned to the parameter username.

Please Note:
People sometimes speak of arguments and parameters interchangeably. Don't be surprised if you see the variables in a function definition referred to as arguments or the variables in a function call referred to as parameters.
"""

######## Positional Arguments ########
"""
When you call a function, Python must match each argument in the function call with a parameter in the function definition. The simplest way to do this is based on the order of the arguments provided. Values matched up this way are called positional arguments. Order Matters in Positional Arguments.
"""

def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster', 'harry')

######## Keyword Arguments ########
"""
A keyword argument is a name-value pair that you pass to a function. You directly associate the name and the value within the argument, so when you pass the argument to the function, there's no confusion. Keyword arguments free you from having to worry about correctly ordering your arguments in the function call, and they clarify the role of each value in the function call. The order of keyword arguments doesn't matter because Python knows where each value should go. When you use keyword arguments, be sure to use the exact names of the parameters in the function's definition.
"""

def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(pet_name='harry', animal_type='hamster')

""" 
Please Note: The function describe_pet() hasn't changed. Also, the above two function calls are equivalent. 
"""

######## Default Values ########
"""
Using default values can simplify your function calls and clarify the ways in which your functions are typically used. For example, if you notice that most of the calls to describe_pet() are being used to describe dogs, you can set the default value of animal_type to 'dog'. Now anyone calling describe_pet() for a dog can omit that information.
"""

def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(pet_name='willie')

# OR

describe_pet('willie')

"""
Note that the order of the parameters in the function definition had to be changed. Because the default value makes it unnecessary to specify a type of animal as an argument, the only argument left in the function call is the pet's name. Python still interprets this as a positional argument, so if the function is called with just a pet's name, that argument will match up with the first parameter listed in the function's definition. This is the reason the first parameter needs to be pet_name. Hence, the simplest way to use this function now is to provide just a dog's name in the function call (as shown in example above).

When you use default values, any parameter with a default value needs to be listed after all the parameters that don't have default values. This allows Python to continue interpreting positional arguments correctly.
"""

######## Equivalent Function Calls ########
"""
Because positional arguments, keyword arguments, and default values can all be used together, often you'll have several equivalent ways to call a function. It doesn't really matter which calling style you use. As long as your function calls produce the output you want, just use the style you find easiest to understand.
"""

#### A dog named Willie.
describe_pet('willie')
# OR
describe_pet(pet_name='willie')

#### A hamster named Harry.
describe_pet('harry', 'hamster')
# OR
describe_pet(pet_name='harry', animal_type='hamster')
# OR
describe_pet(animal_type='hamster', pet_name='harry')

######## Making an Argument Optional ########
def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)

######## Returning a Dictionary ########
def build_person(first_name, last_name, age=None):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    
    return person

musician = build_person('jimi', 'hendrix', age=27)
print(musician)

"""
Please Note: We added a new optional parameter age to the function definition and
assign the parameter the special value None, which is used when a variable
has no specific value assigned to it. You can think of None as a placeholder
value. In conditional tests, None evaluates to False.
"""

######## Modifying a List in a Function ########

#### Non-Function Format

# Start with some designs that need to be printed.
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

# Simulate printing each design, until none are left.
# Move each design to completed_models after printing.
while unprinted_designs:
    current_design = unprinted_designs.pop()

    print(f"Printing model: {current_design}")
    completed_models.append(current_design)

# Display all completed models.
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)

#### Function Format
def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design, until none are left.
    Move each design to completed_models after printing.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Show all the models that were printed."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

# Actual body of the program
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

"""
Please Note: This program has the same output as the version without functions, but the code is much more organized. The code that does most of the work has been moved to two separate functions, which makes the main part of the program easier to understand. Also, the descriptive function names allow others to read this code and understand it, even without comments.

This program is easier to extend and maintain than the version without functions. If we need to print more designs later on, we can simply call print_models() again. If we realize the printing code needs to be modified, we can change the code once, and our changes will take place everywhere the function is called. This technique is more efficient than having to update code separately in several places in the program. This example also demonstrates the idea that every function should have one specific job. If you're writing a function and notice the function is doing too many different tasks, try to split the code into two functions. Remember that you can always call a function from another function, which can be helpful when splitting a complex task into a series of steps.
"""

######## Preventing a Function from Modifying a List ########
""" You can send a copy of a list to a function. E.g. function_name(list_name[:]) """

print_models(unprinted_designs[:], completed_models)

"""
Even though you can preserve the contents of a list by passing a copy of it to your functions, you should pass the original list to functions unless you have a specific reason to pass a copy. It's more efficient for a function to work with an existing list to avoid using the time and memory needed to make a separate copy, especially when you're working with large lists.
"""

######## Passing an Arbitrary Number of Arguments ########
def make_pizza(*toppings):
    """Print the list of toppings that have been requested."""
    print(toppings)
make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

## Output:
## ('pepperoni',)
## ('mushrooms', 'green peppers', 'extra cheese')

"""
Note: The asterisk in the parameter name *toppings tells Python to make an empty tuple called toppings and pack whatever values it receives into this tuple. Also, note that Python packs the arguments into a tuple, even if the function receives only one value.
"""

#### Looping through list of toppings
def make_pizza(*toppings):
    """Summarize the pizza we are about to make."""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

######## Mixing Positional and Arbitrary Arguments ########
"""
If you want a function to accept several different kinds of arguments, the parameter that accepts an arbitrary number of arguments must be placed last in the function definition. Python matches positional and keyword arguments first and then collects any remaining arguments in the final parameter. You'll often see the generic parameter name *args, which collects arbitrary positional arguments like this.
"""

def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

######## Using Arbitrary Keyword Arguments ########
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')
print(user_profile)

"""
The double asterisks before the parameter **user_info cause Python to create an empty dictionary called user_info and pack whatever name-value pairs it receives into this dictionary. Within the function, you can access the key-value pairs in user_info just as you would for any dictionary. You can mix positional, keyword, and arbitrary values in many different ways when writing your own functions. You'll often see the parameter name **kwargs used to collect non-specific keyword arguments.
"""

######## Storing Your Functions in Modules ########
"""
One advantage of functions is the way they separate blocks of code from your main program. By using descriptive names for your functions, your main program will be much easier to follow. You can go a step further by storing your functions in a separate file called a module and then importing that module into your main program. To start importing functions, we first need to create a module. A module is a file ending in .py that contains the code you want to import into your program. In the below example, we'll make a separate file called making_pizzas.py in the same directory as pizza.py and import pizza.py in making_pizzas.py.
"""

#### Importing an Entire Module
import pizza

pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

"""
When Python reads this file, the line import pizza tells Python to open the file pizza.py and copy all the functions from it into this program. You don't actually see code being copied between files because Python copies the code behind the scenes just before the program runs. All you need to know is that any function defined in pizza.py will now be available in making_pizzas.py.
"""

#### Importing Specific Functions

""" E.g. from module_name import function_0, function_1, function_2 """

from pizza import make_pizza

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

#### Using as to Give a Function an Alias

"""
If the name of a function you're importing might conflict with an existing name in your program or if the function name is long, you can use a short, unique alias — an alternate name similar to a nickname for the function. You'll give the function this special nickname when you import the function. Here we give the function make_pizza() an alias, mp(), by importing make_pizza as mp. The as keyword renames a function using the alias you provide.
"""

from pizza import make_pizza as mp

mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')

#### Using as to Give a Module an Alias

import pizza as p

p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

#### Importing All Functions in a Module

from pizza import *

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

"""
The asterisk in the import statement tells Python to copy every function from the module pizza into this program file. Because every function is imported, you can call each function by name without using the dot notation. However, it's best not to use this approach when you're working with larger modules that you didn't write: if the module has a function name that matches an existing name in your project, you can get some unexpected results. Python may see several functions or variables with the same name, and instead of importing all the functions separately, it will overwrite the functions.
The best approach is to import the function or functions you want, or import the entire module and use the dot notation. This leads to clear code that's easy to read and understand.
"""

######## Styling Functions ########

"""
1. You need to keep a few details in mind when you're styling functions. Functions should have descriptive names, and these names should use lowercase letters and underscores. Descriptive names help you and others understand what your code is trying to do. Module names should use these conventions as well.
2. Every function should have a comment that explains concisely what the function does. This comment should appear immediately after the function definition and use the docstring format. In a well-documented function, other programmers can use the function by reading only the description in the docstring. They should be able to trust that the code works as described, and as long as they know the name of the function, the arguments it needs, and the kind of value it returns, they should be able to use it in their programs.
3. If you specify a default value for a parameter, no spaces should be used on either side of the equal sign: 
------
def function_name(parameter_0, parameter_1='default value').
----
The same convention should be used for keyword arguments in function calls:
----
function_name(value_0, parameter_1='value')
----
4. PEP 8 (https://www.python.org/dev/peps/pep-0008/) recommends that you limit lines of code to 79 characters so every line is visible in a reasonably sized editor window. If a set of parameters causes a function's definition to be longer than 79 characters, press enter after the opening parenthesis on the definition line. On the next line, press tab twice to separate the list of arguments from the body of the function, which will only be indented one level. Most editors automatically line up any additional lines of parameters to match the indentation you have established on the first line:
----
def function_name(
        parameter_0, parameter_1, parameter_2,
        parameter_3, parameter_4, parameter_5):
    function body...
----
5. If your program or module has more than one function, you can separate each by two blank lines to make it easier to see where one function ends and the next one begins. All import statements should be written at the beginning of a file. The only exception is if you use comments at the beginning of your file to describe the overall program.
6. Using functions makes your programs easier to read, and good function names summarize what each part of a program does. Reading a series of function calls gives you a much quicker sense of what a program does than reading a long series of code blocks. Functions also make your code easier to test and debug. When the bulk of your program's work is done by a set of functions, each of which has a specific job, it's much easier to test and maintain the code you've written. You can write a separate program that calls each function and tests whether each function works in all the situations it may encounter. When you do this, you can be confident that your functions will work properly each time you call them.
"""




