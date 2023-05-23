#### Changing Case in a String with Methods ####

name = "ada lovelace"
print(name.title())

"""
The method title() appears after the variable in the print() call. A method is an action that Python can perform on a piece of data. The dot (.) after name in name.title() tells Python to make the title() method act on the variable name. Every method is followed by a set of parentheses, because methods often need additional information to do their work. That information is provided inside the parentheses. The title() function doesn't need any additional information, so its parentheses are empty.

The title() method changes each word to title case, where each word begins with a capital letter.
"""

#### Change a string to all uppercase or all lowercase letters ####

name = "Ada Lovelace"
print(name.upper())
print(name.lower())

#### Using Variables in Strings ####
"""
To insert a variable's value into a string, place the letter f immediately before the opening quotation mark. Put braces around the name or names of any variable you want to use inside the string. Python will replace each variable with its value when the string is displayed. These strings are called f-strings. The f is for format, because Python formats the string by replacing the name of any variable in braces with its value.
"""
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
message = f"Hello, {full_name.title()}!"
print(message)

#### Using format() instead of F-strings ####
"""
F-strings were first introduced in Python 3.6. If you're using Python 3.5 or earlier you'll need to use the format() method rather than this f syntax. To use format(), list the variables you want to use in the string inside the parentheses following format. Each variable is referred to by a set of braces; the braces will be filled by the values listed in parentheses in the order provided:
"""
full_name = "{} {}".format(first_name, last_name)

#### Adding Whitespace to Strings with Tabs or Newlines ####
"""
In programming, whitespace refers to any nonprinting character, such as spaces, tabs and end-of-line symbols. You can use whitespace to organize your output so it's easier for users to read.
"""
print("Python")
## Output -> Python

print("\tPython")
##Output ->     Python

print("Languages:\nPython\nC\nJavaScript")
## Output ->
# Languages:
# Python
# C
# JavaScript

#### Combining tabs and newlines in a single string ####
print("Languages:\n\tPython\n\tC\n\tJavaScript")
## Output ->
# Languages:
#     Python
#     C
#     JavaScript

#### Stripping Whitespace ####
"""
Extra whitespace can be confusing in your programs. To programmers 'python' and 'python ' look pretty much the same. But to a program, they are two different strings. Python detects the extra space in 'python ' and considers it significant unless you tell it otherwise.
"""

## Removing whitespace from the right end of a string
favorite_language = 'python '
favorite_language.rstrip()
# Output -> 'python'
favorite_language
# Output -> 'python '

## Removing whitespace from the right end of a string - Permanently
favorite_language = favorite_language.rstrip()
favorite_language
# Output -> 'python'

## Removing whitespace from the left end of a string
favorite_language = ' python'
favorite_language.lstrip()
# Output -> 'python'

## Removing whitespace from both ends of a string
favorite_language = ' python '
favorite_language.strip()
# Output -> 'python'

#### Integers and Floats ####
"""
When you divide any two numbers, even if they are integers that result in a whole number, you'll always get a float. Python defaults to a float in any operation that uses a float, even if the output is a whole number.
"""
x = 4/2
x
# Output -> 2.0

""" If you mix an integer and a float in any other operation, you'll get a float as well """

x = 1 + 2.0
x
# Output -> 3.0

x = 2 * 3.0
x
# Output -> 6.0

x = 3.0 ** 2
x
# Output -> 9.0

#### Integers and Floats ####
"""
When you're writing long numbers, you can group digits using underscores to make large numbers more readable. Python ignores the underscores when storing these kinds of values. Even if you don't group the digits in threes, the value will still be unaffected. To Python, 1000 is the same as 1_000, which is the same as 10_00. This feature works for integers and floats, but it's only available in Python 3.6
and later.
"""

universe_age = 14_000_000_000
print(universe_age)
# Output -> 14000000000

#### Multiple Assignment ####
"""
You can assign values to more than one variable using just a single line. This can help shorten your programs and make them easier to read; you'll use this technique most often when initializing a set of numbers. For example, here's how you can initialize the variables x, y, and z to zero.

You need to separate the variable names with commas, and do the same with the values, and Python will assign each value to its respectively positioned variable. As long as the number of values matches the number of variables, Python will match them up correctly.
"""

x, y, z = 0, 0, 0

#### Constants ####
"""
A constant is like a variable whose value stays the same throughout the life of a program. Python doesn't have built-in constant types, but Python programmers use all capital letters to indicate a variable should be treated as a constant and never be changed. When you want to treat a variable as a constant in your code, make the name of the variable all capital letters.
"""

MAX_CONNECTIONS = 5000

#### The Zen of Python ####

"""
The Python community's philosophy is contained in “The Zen of Python” by Tim Peters. You can access this brief set of principles for writing good Python code by entering import this into your interpreter.
"""

## The Zen of Python, by Tim Peters

# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.
# Flat is better than nested.
# Sparse is better than dense.
# Readability counts.
# Special cases aren't special enough to break the rules.
# Although practicality beats purity.
# Errors should never pass silently.
# Unless explicitly silenced.
# In the face of ambiguity, refuse the temptation to guess.
# There should be one-- and preferably only one --obvious way to do it.
# Although that way may not be obvious at first unless you're Dutch.
# Now is better than never.
# Although never is often better than *right* now.
# If the implementation is hard to explain, it's a bad idea.
# If the implementation is easy to explain, it may be a good idea.
# Namespaces are one honking great idea -- let's do more of those!















