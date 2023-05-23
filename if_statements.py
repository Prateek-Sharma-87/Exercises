######## Ignoring Case When Checking for Equality ########
car = 'Audi'
car == 'audi'
# output -> False

"""
But if case doesn't matter
and instead you just want to test the value of a variable, you can convert the
variable's value to lowercase before doing the comparison
"""
car = 'Audi'
car.lower() == 'audi'
# output -> True

"""
The lower() function doesn't change the value that was originally stored in car, 
so you can do this kind of comparison without affecting the original variable
"""

######## Using and to Check Multiple Conditions ########
age_0 = 22
age_1 = 18
age_0 >= 21 and age_1 >= 21
# output -> False

age_1 = 22
age_0 >= 21 and age_1 >= 21
# output -> True

"""
To improve readability, you can use parentheses around the individual
tests, but they are not required. If you use parentheses, your test would look
like this: (age_0 >= 21) and (age_1 >= 21)
"""

######## Checking Whether a Value Is in a List ########
requested_toppings = ['mushrooms', 'onions', 'pineapple']
'mushrooms' in requested_toppings
# output -> True
'pepperoni' in requested_toppings
# output -> False

######## Checking Whether a Value Is Not in a List ########
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")

######## Boolean Expressions ########
"""
A Boolean expression is just another name for a
conditional test. A Boolean value is either True or False. Boolean values 
are often used to keep track of certain conditions, such as whether a game 
is running or whether a user can edit certain content on a website etc.
"""
game_active = True
can_edit = False

######## Using Multiple elif Blocks ########
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
else:
    price = 20
print(f"Your admission cost is ${price}.")

######## Omitting the else Block ########
"""
Python does not require an else block at the end of an if-elif chain. Sometimes
an else block is useful; sometimes it is clearer to use an additional
elif statement that catches the specific condition of interest
"""
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
elif age >= 65:
    price = 20
print(f"Your admission cost is ${price}.")

"""
Note: The else block is a catchall statement. It matches any condition that
wasn't matched by a specific if or elif test, and that can sometimes include
invalid or even malicious data. If you have a specific final condition you are
testing for, consider using a final elif block and omit the else block. As a
result, you'll gain extra confidence that your code will run only under the
correct conditions.
"""

"""
In summary, if you want only one block of code to run, use an if-elif-else
chain. If more than one block of code needs to run, use a series of
independent if statements
"""

######## Checking That a List Is Not Empty ########
requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}.")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")








































